"""Robô de publicação da KN Casa de Integração®.

Lê posts/*/post.json e publica no Instagram (ou atualiza o site) os itens com
"status": "aprovado" cujo horário "agendar_para" já chegou.
Roda no GitHub Actions; a chave fica no segredo IG_TOKEN (nunca no código).

Tipos aceitos:
  reels      -> "video", "capa" (opcional), "legenda"
  carrossel  -> "imagens" (lista; arquivos .mp4 entram como vídeo), "legenda"
  imagem     -> "imagem", "legenda"
  story      -> "midia" (imagem .jpg/.png ou vídeo .mp4)
  site       -> "acao": "trocar_index" ("arquivo") ou "revelar" ("marcador")

Depois de publicar, se o post tiver "site_marcador", o link do Instagram é
colocado no site no lugar de <!--IG:marcador-->.
"""
import json, os, sys, time, glob, shutil, urllib.request, urllib.parse
from datetime import datetime, timezone

TOKEN = os.environ.get("IG_TOKEN", "")
IG = os.environ.get("IG_USER_ID", "17841473570396419")
API = "https://graph.facebook.com/v21.0"
SITE = "https://kncasadeintegracao.com"
INDEX = "index.html"


class ErroAPI(Exception):
    pass


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
        raise ErroAPI(f"{path}: {e.read().decode()[:400]}")


def wait_url(url, tries=40):
    for _ in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method="HEAD"), timeout=30) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(15)
    raise ErroAPI(f"Arquivo não ficou disponível no site: {url}")


def wait_ready(cid, tries=90):
    for _ in range(tries):
        st = call("GET", cid, fields="status_code,status")
        if st.get("status_code") == "FINISHED":
            return
        if st.get("status_code") == "ERROR":
            raise ErroAPI(f"Instagram recusou a mídia: {st}")
        time.sleep(10)
    raise ErroAPI("Tempo esgotado processando a mídia")


def url(p):
    return p if p.startswith("http") else f"{SITE}/{p.lstrip('/')}"


def is_video(p):
    return p.lower().endswith((".mp4", ".mov"))


def criar_container(post):
    kind = post["tipo"]
    if kind == "reels":
        v = url(post["video"]); wait_url(v)
        params = dict(media_type="REELS", video_url=v, caption=post["legenda"], share_to_feed="true")
        if post.get("capa"):
            c = url(post["capa"]); wait_url(c); params["cover_url"] = c
        return call("POST", f"{IG}/media", **params)["id"]
    if kind == "carrossel":
        kids = []
        for m in post["imagens"]:
            u = url(m); wait_url(u)
            if is_video(m):
                kids.append(call("POST", f"{IG}/media", media_type="VIDEO", video_url=u, is_carousel_item="true")["id"])
            else:
                kids.append(call("POST", f"{IG}/media", image_url=u, is_carousel_item="true")["id"])
        for k in kids:
            wait_ready(k)
        return call("POST", f"{IG}/media", media_type="CAROUSEL", children=",".join(kids), caption=post["legenda"])["id"]
    if kind == "imagem":
        u = url(post["imagem"]); wait_url(u)
        return call("POST", f"{IG}/media", image_url=u, caption=post["legenda"])["id"]
    if kind == "story":
        u = url(post["midia"]); wait_url(u)
        key = "video_url" if is_video(post["midia"]) else "image_url"
        return call("POST", f"{IG}/media", media_type="STORIES", **{key: u})["id"]
    raise ErroAPI(f"tipo desconhecido: {kind}")


def publicar_instagram(post, f):
    cid = criar_container(post)
    wait_ready(cid)
    mid = call("POST", f"{IG}/media_publish", creation_id=cid)["id"]
    # salva já, para nunca publicar duas vezes
    post.update(status="publicado", media_id=mid, publicado_em=agora_sp())
    salvar(post, f)
    try:
        link = call("GET", mid, fields="permalink").get("permalink")
    except ErroAPI:
        link = None
    if link:
        post["permalink"] = link
        salvar(post, f)
    return link


def site_acao(post, pasta):
    html = open(INDEX, encoding="utf-8").read()
    if post["acao"] == "trocar_index":
        novo = open(os.path.join(pasta, post["arquivo"]), encoding="utf-8").read()
        # leva para a nova página os links que já tinham sido colocados
        for linha in html.split("<!--IGL:")[1:]:
            mk = linha.split("-->")[0]
            bloco = "<!--IGL:" + linha.split("<!--/IGL-->")[0] + "<!--/IGL-->"
            novo = novo.replace(f"<!--IG:{mk}-->", bloco)
        html = novo
    elif post["acao"] == "revelar":
        html = html.replace(f' hidden data-agendado="{post["marcador"]}"', f' data-agendado="{post["marcador"]}"')
    open(INDEX, "w", encoding="utf-8").write(html)


def colocar_link_no_site(marcador, link, rotulo="Ver no Instagram"):
    if not (marcador and link and os.path.exists(INDEX)):
        return
    html = open(INDEX, encoding="utf-8").read()
    botao = (f'<!--IGL:{marcador}--><a class="btn ghost" href="{link}" target="_blank" rel="noopener">'
             f'{rotulo}</a><!--/IGL-->')
    if f"<!--IG:{marcador}-->" in html:
        html = html.replace(f"<!--IG:{marcador}-->", botao)
        open(INDEX, "w", encoding="utf-8").write(html)


def agora_sp():
    return datetime.now(timezone.utc).astimezone().strftime("%Y-%m-%d %H:%M")


def salvar(post, f):
    json.dump(post, open(f, "w", encoding="utf-8"), ensure_ascii=False, indent=2)


def chegou_a_hora(post):
    quando = post.get("agendar_para")
    if not quando:
        return True
    return datetime.fromisoformat(quando) <= datetime.now(timezone.utc)


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "teste":
        info = call("GET", IG, fields="id,username,followers_count,media_count")
        info["conferido_em"] = agora_sp()
        json.dump(info, open("posts/_conexao.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
        print("Conexão OK:", info)
        return
    fila = []
    for f in glob.glob("posts/*/post.json"):
        post = json.load(open(f, encoding="utf-8"))
        if post.get("status") == "aprovado" and chegou_a_hora(post):
            fila.append((post.get("agendar_para", ""), f, post))
    fila.sort(key=lambda x: x[0])
    if not fila:
        print("Nada para publicar agora.")
        return
    for _, f, post in fila:
        print("Publicando", f)
        try:
            if post["tipo"] == "site":
                site_acao(post, os.path.dirname(f))
                post.update(status="publicado", publicado_em=agora_sp())
                salvar(post, f)
                print("Site atualizado.")
                continue
            link = publicar_instagram(post, f)
            colocar_link_no_site(post.get("site_marcador"), link, post.get("rotulo_site", "Ver no Instagram"))
            print("Publicado:", link)
        except (ErroAPI, KeyError, OSError) as e:
            post["tentativas"] = post.get("tentativas", 0) + 1
            post["ultimo_erro"] = str(e)[:400]
            if post["tentativas"] >= 3:
                post["status"] = "erro"
            salvar(post, f)
            print("ERRO em", f, "->", e)


if __name__ == "__main__":
    main()
