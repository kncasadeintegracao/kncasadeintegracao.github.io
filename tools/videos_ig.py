"""Baixa vídeos já publicados no Instagram da KN (só leitura), para avaliação.
IDs em posts/videos_pedido.txt (um por linha). Saída em /tmp/videos/."""
import json, os, urllib.request, urllib.parse
TOKEN = os.environ["IG_TOKEN"]; API = "https://graph.facebook.com/v21.0"
os.makedirs("/tmp/videos", exist_ok=True)
for linha in open("posts/videos_pedido.txt"):
    mid = linha.strip()
    if not mid or not mid.isdigit(): continue
    q = urllib.parse.urlencode({"fields": "media_url,timestamp", "access_token": TOKEN})
    with urllib.request.urlopen(f"{API}/{mid}?{q}", timeout=60) as r:
        m = json.load(r)
    url = m.get("media_url")
    if url:
        urllib.request.urlretrieve(url, f"/tmp/videos/{m['timestamp'][:10]}_{mid}.mp4")
        print("ok", mid)
