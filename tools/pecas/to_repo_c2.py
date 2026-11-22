# Semana 23 a 29/11/2026 (comprar para preencher): grava mídias, posts e o index da semana.
# Uso: STATUS=aprovado python3 to_repo_c2.py   (rodar só depois do "pode publicar")
import json, os, shutil, sys, re
S = os.environ.get("KN_WORK", "/tmp/kn_work")
R = os.environ.get("REPO", "/home/claude/kncasadeintegracao.github.io")
STATUS = os.environ.get("STATUS", "aguardando_aprovacao")
VIDEO = os.environ.get("VIDEO_QUI")          # midia/... do vídeo editado, quando chegar
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assemble_c2 as A

MD = "midia/2026-11-comprar"
os.makedirs(f"{R}/{MD}", exist_ok=True)
for f in os.listdir(S + "/site_c2/midia"):            # arquivos já sem metadados
    shutil.copy(f"{S}/site_c2/midia/{f}", f"{R}/{MD}/{f}")
m = lambda f: f"{MD}/{f}"
car = lambda pre, n: [m(f"{pre}_c{i:02d}.{'mp4' if (pre, i) in MP4 else 'jpg'}") for i in range(1, n + 1)]
MP4 = {("seg", 2), ("ter", 6), ("qui", 4), ("sex", 4), ("dom", 4), ("res", 4)}

posts = []
def P(folder, st=None, **kw):
    kw["status"] = st or STATUS; posts.append((folder, kw))

P("2026-11-23-1230-carrossel-comprar", tipo="carrossel", agendar_para="2026-11-23T12:30:00-03:00", imagens=car("seg", 6), legenda=A.CAP_SEG, site_marcador="cpp-seg")
P("2026-11-23-1235-story", tipo="story", agendar_para="2026-11-23T12:35:00-03:00", midia=m("seg_story.jpg"))
P("2026-11-24-1230-carrossel-sinais", tipo="carrossel", agendar_para="2026-11-24T12:30:00-03:00", imagens=car("ter", 7), legenda=A.CAP_TER, site_marcador="cpp-ter")
P("2026-11-25-1929-site-semana", tipo="site", agendar_para="2026-11-25T19:29:00-03:00", acao="trocar_index", arquivo="index_novo.html")
P("2026-11-25-1930-reels-vazio", tipo="reels", agendar_para="2026-11-25T19:30:00-03:00", video=m("qua_reels.mp4"), capa=m("qua_reels_capa.jpg"), legenda=A.CAP_QUA, site_marcador="cpp-qua")
P("2026-11-25-1935-story", tipo="story", agendar_para="2026-11-25T19:35:00-03:00", midia=m("qua_story.jpg"))
P("2026-11-26-1230-carrossel-familia", tipo="carrossel", agendar_para="2026-11-26T12:30:00-03:00", imagens=car("qui", 7), legenda=A.CAP_QUI, site_marcador="cpp-qui")
if VIDEO:
    P("2026-11-26-1930-video-katheryne", tipo="reels", agendar_para="2026-11-26T19:30:00-03:00", video=VIDEO, legenda=A.CAP_VID, site_marcador="cpp-qui-video")
else:   # reserva: sai só se o vídeo não chegar
    P("2026-11-26-1930-carrossel-reserva", tipo="carrossel", agendar_para="2026-11-26T19:30:00-03:00", imagens=car("res", 5), legenda=A.CAP_RES, site_marcador="cpp-qui-video")
    P("2026-11-26-1935-story", tipo="story", agendar_para="2026-11-26T19:35:00-03:00", midia=m("res_story.jpg"))
P("2026-11-27-1229-site-texto", tipo="site", agendar_para="2026-11-27T12:29:00-03:00", acao="revelar", marcador="texto-blackfriday")
P("2026-11-27-1230-carrossel-blackfriday", tipo="carrossel", agendar_para="2026-11-27T12:30:00-03:00", imagens=car("sex", 6), legenda=A.CAP_SEX, site_marcador="cpp-sex")
P("2026-11-27-1235-story", tipo="story", agendar_para="2026-11-27T12:35:00-03:00", midia=m("sex_story.jpg"))
P("2026-11-28-1030-story-pergunta", tipo="story", agendar_para="2026-11-28T10:30:00-03:00", midia=m("sab_story1.jpg"))
P("2026-11-28-1700-story-agendar", tipo="story", agendar_para="2026-11-28T17:00:00-03:00", midia=m("sab_story2.jpg"))
P("2026-11-29-1930-carrossel-frases", tipo="carrossel", agendar_para="2026-11-29T19:30:00-03:00", imagens=car("dom", 5), legenda=A.CAP_DOM, site_marcador="cpp-dom")
P("2026-11-29-1935-story", tipo="story", agendar_para="2026-11-29T19:35:00-03:00", midia=m("dom_story.jpg"))

for folder, post in posts:
    os.makedirs(f"{R}/posts/{folder}", exist_ok=True)
    json.dump(post, open(f"{R}/posts/{folder}/post.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- marcadores escondidos no index atual (segunda e terça saem antes da troca) ----------
html = open(f"{R}/index.html", encoding="utf-8").read()
if "<!--IG:cpp-seg-->" not in html and "<!--IGL:cpp-seg-->" not in html:
    k = html.index('<div class="rf-anteriores">')
    html = html[:k] + '<span hidden><!--IG:cpp-seg--><!--IG:cpp-ter--></span>\n\n    ' + html[k:]
    open(f"{R}/index.html", "w", encoding="utf-8").write(html)

# ---------- novo index (troca às 19h29 de quarta) ----------
def bloco(h, start, end="</article>"):
    i = h.index(start); j = h.index(end, i) + len(end); return i, j
i5, j5 = bloco(html, '<article class="card reflexao destaque" id="rf-5">')
rf5_old = (html[i5:j5].replace('<article class="card reflexao destaque" id="rf-5">', '<article class="card reflexao" id="rf-5">')
           .replace('      <p class="rf-selo">Reflexão da semana</p>\n', '', 1)
           .replace('        <p class="rf-teaser" id="rf-teaser"></p>\n', '')
           .replace(' hidden data-agendado="serie-pre-dom-post"', ' data-agendado="serie-pre-dom-post"'))
ir, jr = bloco(html, '<article class="card reflexao" id="rf-racismo"')
rfr_old = html[ir:jr].replace('      <p class="rf-selo">Texto da semana</p>\n', '', 1)
oculto = re.search(r'<span hidden><!--IG[L]?:cpp-seg-->.*?</span>\n\n    ', html, re.S)

exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "to_repo_p.py")).read().split("arts = A.ARTS")[1].split("SERIE = [")[0].join(["arts = A.ARTS", ""]))
SERIE = [("cpp-seg", "23/11 · Comprar para preencher", "Quando a compra tenta acalmar algo que não está em nenhuma vitrine: cansaço, solidão, tédio ou uma tristeza que ainda não tem nome.", False),
         ("cpp-ter", "24/11 · 5 sinais de que a compra ocupa o lugar de outra coisa", "Comprar para aliviar um dia ruim, esconder o valor, sentir culpa logo depois, parcelas que pesam e pacotes que ficam fechados.", False),
         ("cpp-qua", "25/11 · Comprei, e dez minutos depois o vazio voltou", "A compra acalma por um instante, mas o que doía continua lá. Três perguntas para fazer antes do clique.", True),
         ("cpp-qui", "26/11 · Quando alguém que você ama compra para preencher", "O que costuma ajudar na conversa em casa, e o que costuma afastar.", True),
         ("cpp-qui-video", "26/11 · Vídeo: comprar para preencher", "A Dra. Katheryne fala sobre a compra que tenta acalmar um dia difícil, e por que o alívio dura tão pouco.", True),
         ("cpp-sex", "27/11 · Black Friday: 4 perguntas antes de comprar", "Para aproveitar o desconto sem cair na armadilha do impulso. Leia também “Black Friday com calma”.", True),
         ("cpp-dom", "29/11 · O que a Dra. Katheryne disse nesta semana", "Três frases do vídeo sobre comprar para preencher.", True)]
serie_html = ('      <div class="rf-serie">\n        <p class="eyebrow">Série Comprar para preencher</p>\n'
              '        <p class="rf-cred">A cada dia desta semana, um novo conteúdo no Instagram e aqui, com o contexto completo.</p>\n        <ul>'
              + "".join(f'<li{" hidden" if h else ""} data-agendado="serie-{k}"><b>{t}</b><br>{d} <!--IG:{k}--></li>' for k, t, d, h in SERIE)
              + '</ul>\n        <p class="rf-teaser" id="rf-teaser"></p>\n      </div>\n')
nova = site_article(arts[0], "rf-6", "Reflexão da semana", "", "cpp-qua", "25 de novembro de 2026", serie_html)
arts[1] = arts[1].replace('      <div class="sign">', '      <div class="refs"></div>\n      <div class="sign">', 1) if '<div class="refs">' not in arts[1] else arts[1]
texto2 = site_article(arts[1], "rf-blackfriday", "Texto da semana", ' hidden data-agendado="texto-blackfriday"', "cpp-sex", "27 de novembro de 2026").replace('      <p class="rf-ref">Referências: </p>\n', '')

ant = f'''      <details>
        <summary>O que a gente aprende sem perceber <span class="small">(nov/26)</span></summary>
        {rf5_old}
      </details>
      <details>
        <summary>O racismo também adoece <span class="small">(nov/26)</span></summary>
        {rfr_old}
      </details>
'''
novo = html[:i5] + nova + "\n\n    " + texto2 + html[jr:]
if oculto: novo = novo.replace(oculto.group(0), "")
k = novo.index('<p class="small">As reflexões ficam guardadas aqui, da mais recente para a mais antiga.</p>\n')
k = novo.index("\n", k) + 1
novo = novo[:k] + ant + novo[k:]
oldcard = re.search(r'(<button class="card rf-home" data-go="reflexoes">\s*<p class="rf-selo">Reflexão da semana</p>\s*)<b>.*?</b>\s*<span>.*?</span>', novo, re.S)
novo = novo.replace(oldcard.group(0), oldcard.group(1) + '<b>Ou isto ou aquilo: o que a gente compra quando compra demais</b>\n        <span>Sobre consumo, ansiedade e vazio: por que o alívio de comprar dura tão pouco, com Melanie Klein, Bauman e Cecília Meireles.</span>')
assert novo.count('id="rf-teaser"') == 1 and 'id="rf-6"' in novo and 'O que a gente aprende sem perceber</h3>' in novo and 'id="rf-racismo"' in novo
open(f"{R}/posts/2026-11-25-1929-site-semana/index_novo.html", "w", encoding="utf-8").write(novo)
print("posts:", len(posts), "status:", STATUS, "index_novo:", len(novo), "antes:", len(html))
