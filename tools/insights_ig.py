"""Busca estatísticas de público do Instagram da KN (horários ativos, cidades, idade/gênero,
alcance dos posts recentes). Só leitura. O resultado sai criptografado (tools/insights_pub.pem),
para não expor dados do público no repositório."""
import json, os, urllib.request, urllib.parse, datetime
TOKEN = os.environ["IG_TOKEN"]; IG = os.environ.get("IG_USER_ID", "17841473570396419")
API = "https://graph.facebook.com/v21.0"
def call(path, **p):
    p["access_token"] = TOKEN
    try:
        with urllib.request.urlopen(f"{API}/{path}?{urllib.parse.urlencode(p)}", timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"erro": e.read().decode()[:400]}
out = {"gerado_em": datetime.datetime.utcnow().isoformat() + "Z"}
out["conta"] = call(IG, fields="username,followers_count,media_count")
out["online_followers"] = call(f"{IG}/insights", metric="online_followers", period="lifetime")
for b in ("city", "age", "gender"):
    out[f"seguidores_{b}"] = call(f"{IG}/insights", metric="follower_demographics", period="lifetime",
                                  metric_type="total_value", breakdown=b, timeframe="this_month")
    out[f"engajados_{b}"] = call(f"{IG}/insights", metric="engaged_audience_demographics", period="lifetime",
                                 metric_type="total_value", breakdown=b, timeframe="this_month")
media = call(f"{IG}/media", fields="id,timestamp,media_type,media_product_type,like_count,comments_count,permalink,caption", limit=100)
out["conta_insights_30d"] = call(f"{IG}/insights", metric="profile_links_taps,website_clicks,profile_views,follows_and_unfollows,reach,views",
                                 period="day", metric_type="total_value",
                                 since=int((datetime.datetime.utcnow() - datetime.timedelta(days=28)).timestamp()),
                                 until=int(datetime.datetime.utcnow().timestamp()))
out["conta_toques_link_30d"] = call(f"{IG}/insights", metric="profile_links_taps", period="day", metric_type="total_value",
                                    breakdown="contact_button_type",
                                    since=int((datetime.datetime.utcnow() - datetime.timedelta(days=28)).timestamp()),
                                    until=int(datetime.datetime.utcnow().timestamp()))
def janela(d0, d1):
    agora = datetime.datetime.utcnow()
    return call(f"{IG}/insights", metric="profile_links_taps,website_clicks,profile_views,reach,views",
                period="day", metric_type="total_value",
                since=int((agora - datetime.timedelta(days=d0)).timestamp()),
                until=int((agora - datetime.timedelta(days=d1)).timestamp()))
out["conta_ultimos_7d"] = janela(7, 0)
out["conta_7d_anteriores"] = janela(14, 7)
posts = []
for m in media.get("data", []):
    m["caption"] = (m.get("caption") or "")[:300]
    ins = call(f"{m['id']}/insights", metric="reach,saved,shares,total_interactions,views,profile_visits,follows")
    if "erro" in ins:
        ins = call(f"{m['id']}/insights", metric="reach,saved,shares,total_interactions,views")
    if "erro" in ins:
        ins = call(f"{m['id']}/insights", metric="reach,saved,shares,total_interactions")
    m["insights"] = {d["name"]: d.get("values", [{}])[0].get("value", d.get("total_value", {}).get("value"))
                     for d in ins.get("data", [])} if "data" in ins else ins
    posts.append(m)
out["posts"] = posts if posts else media
def limpa(o):
    if isinstance(o, dict): return {k: limpa(v) for k, v in o.items() if k != "paging"}
    if isinstance(o, list): return [limpa(v) for v in o]
    return o
out = limpa(out)
open("/tmp/insights.json", "w").write(json.dumps(out, ensure_ascii=False))
