"""Publica no Instagram da KN os posts aprovados em posts/*/post.json.
Roda no GitHub Actions; a chave fica no segredo IG_TOKEN (nunca no código)."""
import json, os, sys, time, glob, urllib.request, urllib.parse, subprocess

TOKEN = os.environ["IG_TOKEN"]
IG = None
API = "https://graph.facebook.com/v21.0"
SITE = "https://kncasadeintegracao.com"

def call(method, path, **params):
    params["access_token"] = TOKEN
    data = urllib.parse.urlencode(params).encode()
    if method == "GET":
        req = urllib.request.Request(f"{API}/{path}?{data.decode()}")
    else:
        req = urllib.request.Request(f"{API}/{path}", data=data, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise SystemExit(f"Erro da API ({path}): {e.read().decode()}")

def wait_url(url, tries=40):
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
                if r.status == 200: return
        except Exception: pass
        time.sleep(15)
    raise SystemExit(f"Arquivo não ficou disponível no site: {url}")

def wait_ready(cid, tries=60):
    for _ in range(tries):
        st = call("GET", cid, fields="status_code,status")
        if st.get("status_code") == "FINISHED": return
        if st.get("status_code") == "ERROR": raise SystemExit(f"Instagram recusou a mídia: {st}")
        time.sleep(10)
    raise SystemExit("Tempo esgotado processando a mídia")

def url(p): return p if p.startswith("http") else f"{SITE}/{p.lstrip('/')}"

def publish(post):
    kind = post["tipo"]; cap = post["legenda"]
    if kind == "reels":
        v = url(post["video"]); wait_url(v)
        params = dict(media_type="REELS", video_url=v, caption=cap, share_to_feed="true")
        if post.get("capa"): c = url(post["capa"]); wait_url(c); params["cover_url"] = c
        cid = call("POST", f"{IG}/media", **params)["id"]
    elif kind == "carrossel":
        kids = []
        for img in post["imagens"]:
            u = url(img); wait_url(u)
            kids.append(call("POST", f"{IG}/media", image_url=u, is_carousel_item="true")["id"])
        for k in kids: wait_ready(k)
        cid = call("POST", f"{IG}/media", media_type="CAROUSEL", children=",".join(kids), caption=cap)["id"]
    elif kind == "imagem":
        u = url(post["imagem"]); wait_url(u)
        cid = call("POST", f"{IG}/media", image_url=u, caption=cap)["id"]
    else:
        raise SystemExit(f"tipo desconhecido: {kind}")
    wait_ready(cid)
    mid = call("POST", f"{IG}/media_publish", creation_id=cid)["id"]
    link = call("GET", mid, fields="permalink")["permalink"]
    return mid, link

def find_ig():
    """Descobre o ID da conta do Instagram a partir da própria chave."""
    tried = {}
    try:
        dbg = call("GET", "debug_token", input_token=TOKEN)["data"]
        for g in dbg.get("granular_scopes", []):
            if g.get("scope", "").startswith("instagram") and g.get("target_ids"):
                return g["target_ids"][0], {"via": "debug_token", "scopes": [x.get("scope") for x in dbg.get("granular_scopes", [])]}
        tried["debug_token"] = dbg.get("scopes")
    except SystemExit as e: tried["debug_token"] = str(e)[:300]
    for path, params in [("me/accounts", {"fields": "name,instagram_business_account"}),
                         ("me", {"fields": "id,name"})]:
        try:
            r = call("GET", path, **params); tried[path] = r
            for pg in r.get("data", []):
                if pg.get("instagram_business_account"):
                    return pg["instagram_business_account"]["id"], {"via": path}
        except SystemExit as e: tried[path] = str(e)[:300]
    raise SystemExit("Não encontrei a conta do Instagram. Tentativas: " + json.dumps(tried, ensure_ascii=False))

def main():
    global IG
    IG, how = find_ig()
    print("Conta do Instagram encontrada:", IG, how)
    info = call("GET", IG, fields="id,username,followers_count,media_count")
    info["conferido_em"] = time.strftime("%Y-%m-%d %H:%M")
    json.dump(info, open("posts/_conexao.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    print("Conexão OK:", info)
    if len(sys.argv) > 1 and sys.argv[1] == "teste": return
    changed = False
    for f in sorted(glob.glob("posts/*/post.json")):
        post = json.load(open(f, encoding="utf-8"))
        if post.get("status") != "aprovado": continue
        print("Publicando", f)
        mid, link = publish(post)
        post.update(status="publicado", media_id=mid, permalink=link,
                    publicado_em=time.strftime("%Y-%m-%d %H:%M"))
        json.dump(post, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("Publicado:", link); changed = True
    if not changed: print("Nenhum post aprovado para publicar.")

if __name__ == "__main__":
    main()
