import json, os, shutil, sys, re
S = os.environ.get("KN_WORK", "/tmp/kn_work")
R = "/home/claude/kncasadeintegracao.github.io"
sys.path.insert(0, os.path.dirname(__file__))
import assemble_p as A

caps = {d["chip"].split()[0]: d.get("cap", "") for d in A.days}
FOOT = ("Katheryne Solange Muniz Nazer – RT · Psicóloga · CRP 06/117.713\n"
        "KN Casa de Integração® · Mooca/SP e online\n"
        "Cuidar de pessoas. Formar profissionais. Transformar realidades.\n"
        "© 2026 KN Casa de Integração®. Todos os direitos reservados.")
def leg(dia):
    c = caps[dia]; i = c.rindex("\n\n#")
    return c[:i] + "\n\n" + FOOT + c[i:]

MD = "midia/2026-11-preconceito"
os.makedirs(f"{R}/{MD}", exist_ok=True)
for f in os.listdir(S + "/out_p"):
    if f.endswith("_frame.jpg"): continue
    shutil.copy(f"{S}/out_p/{f}", f"{R}/{MD}/{f}")
m = lambda f: f"{MD}/{f}"

posts = []
def P(folder, **kw):
    kw.setdefault("status", "aprovado"); posts.append((folder, kw))

P("2026-11-18-1929-site-semana", tipo="site", agendar_para="2026-11-18T19:29:00-03:00", acao="trocar_index", arquivo="index_novo.html")
P("2026-11-18-1930-reels-preconceito", tipo="reels", agendar_para="2026-11-18T19:30:00-03:00", video=m("qua_reels.mp4"), capa=m("qua_reels_capa.jpg"), legenda=leg("Quarta"), site_marcador="pre-qua-reels")
P("2026-11-18-1935-story", tipo="story", agendar_para="2026-11-18T19:35:00-03:00", midia=m("qua_story.jpg"))
P("2026-11-19-1230-carrossel-frases", tipo="carrossel", agendar_para="2026-11-19T12:30:00-03:00",
  imagens=[m(x) for x in ["qui_c01.jpg","qui_c02.jpg","qui_c03.mp4","qui_c04.jpg","qui_c05.jpg","qui_c06.jpg","qui_c07.jpg"]], legenda=leg("Quinta"), site_marcador="pre-qui-carrossel")
P("2026-11-19-1235-story", tipo="story", agendar_para="2026-11-19T12:35:00-03:00", midia=m("qui_story.jpg"))
P("2026-11-20-1229-site-texto", tipo="site", agendar_para="2026-11-20T12:29:00-03:00", acao="revelar", marcador="texto-racismo")
P("2026-11-20-1230-post-consciencia", tipo="imagem", agendar_para="2026-11-20T12:30:00-03:00", imagem=m("sex_post.jpg"), legenda=leg("Sexta"), site_marcador="pre-sex-post")
P("2026-11-20-1235-story", tipo="story", agendar_para="2026-11-20T12:35:00-03:00", midia=m("sex_story.jpg"))
P("2026-11-21-1800-story-reflexao", tipo="story", agendar_para="2026-11-21T18:00:00-03:00", midia=m("sab_story3.jpg"))
P("2026-11-22-1930-post-domingo", tipo="imagem", agendar_para="2026-11-22T19:30:00-03:00", imagem=m("dom_post.jpg"), legenda=leg("Domingo"), site_marcador="pre-dom-post")
P("2026-11-22-1935-story", tipo="story", agendar_para="2026-11-22T19:35:00-03:00", midia=m("dom_story.jpg"))

for folder, post in posts:
    os.makedirs(f"{R}/posts/{folder}", exist_ok=True)
    json.dump(post, open(f"{R}/posts/{folder}/post.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- novo index (troca às 19h29 de quarta) ----------
html = open(f"{R}/index.html", encoding="utf-8").read()
def bloco(start, end="</article>"):
    i = html.index(start); j = html.index(end, i) + len(end); return i, j

def limpa_refs(card):
    # tira do corpo do texto as linhas de referência que entraram por engano
    refs = re.findall(r'<p class="rf-ref">Referências: (.*?)</p>', card, re.S)
    if not refs: return card
    for r in refs[0].split(" · "):
        card = card.replace(f"        <p>{r.strip()}</p>\n", "")
    return card

i4, j4 = bloco('<article class="card reflexao destaque" id="rf-4">')
rf4 = limpa_refs(html[i4:j4])
rf4_old = (rf4.replace('<article class="card reflexao destaque" id="rf-4">', '<article class="card reflexao" id="rf-4">')
              .replace('      <p class="rf-selo">Reflexão da semana</p>\n', '', 1)
              .replace('        <p class="rf-teaser" id="rf-teaser"></p>\n', ''))
assert 'id="rf-teaser"' not in rf4_old
ia, ja = bloco('<div class="card reflexao" data-agendado="serie-aniv-1ano">', "</div>\n\n    <article")
ja -= len("\n\n    <article")
aniv = html[ia:ja]
ic, jc = bloco('<article class="card reflexao" id="rf-corpo" data-agendado="texto-corpo">')
rfc_old = limpa_refs(html[ic:jc]).replace('      <p class="rf-selo">Texto da semana</p>\n', '', 1)

arts = A.ARTS.split("<article>")[1:]
def site_article(art, aid, selo, extra_attr, ig_marker, data_ext, serie=""):
    t = re.search(r"<h2>(.*?)</h2>", art).group(1)
    by = re.search(r'<div class="by">(.*?)</div>', art).group(1)
    corpo = art[:art.index('<div class="refs">')]
    paras = re.findall(r"\n      <p>(.*?)</p>", corpo, re.S)
    refs = re.findall(r"\n        <p>(.*?)</p>", art[art.index('class="refs"'):art.index('class="sign"')], re.S)
    paras = [p.replace("<em>", "<i>").replace("</em>", "</i>") for p in paras]
    refs = [r.replace("<em>", "<i>").replace("</em>", "</i>") for r in refs]
    return f'''<article class="card reflexao{' destaque' if selo=='Reflexão da semana' else ''}" id="{aid}"{extra_attr}>
      <p class="rf-selo">{selo}</p>
      <h3>{t}</h3>
      <p class="rf-data">{by}</p>
      <div class="rf-texto">
''' + "".join(f"        <p>{p}</p>\n" for p in paras) + f'''      </div>
      <div class="rf-acoes">
        <a class="btn" href="https://wa.me/5511949772000?text=Ol%C3%A1%21%20Li%20o%20texto%20do%20site%20e%20gostaria%20de%20agendar%20um%20atendimento." target="_blank" rel="noopener">Marcar um atendimento</a>
        <button class="btn ghost" type="button" onclick="window.kikaOpen&&window.kikaOpen()">Conversar com a Kika</button>
        <!--IG:{ig_marker}-->
      </div>
{serie}      <div class="rf-assina">
        <p class="rf-autora">Katheryne Solange Muniz Nazer</p>
        <p class="rf-cred">Responsável Técnica · KN Casa de Integração®<br>Psicóloga · Neuropsicóloga · CRP 06/117.713</p>
        <p class="rf-cred">São Paulo, {data_ext}</p>
        <p class="rf-lema">Cuidar de pessoas. Formar profissionais. Transformar realidades.</p>
      </div>
      <p class="rf-ref">Referências: {" · ".join(refs)}</p>
      <p class="rf-ref">© 2026 KN Casa de Integração®. Todos os direitos reservados.</p>
    </article>'''

SERIE = [("pre-qua-reels", "18/11 · Quase ninguém se acha preconceituoso", "O preconceito costuma chegar disfarçado de piada, de conselho ou de “é só uma opinião”, e deixa marcas em quem ouve. O que se aprende também pode ser revisto."),
         ("pre-qui-carrossel", "19/11 · Frases que parecem inofensivas", "Cinco falas do dia a dia que carregam preconceito, sobre origem, gênero, corpo e idade, e o que elas fazem com quem ouve."),
         ("pre-sex-post", "20/11 · Consciência Negra: o racismo também adoece", "No Dia Nacional de Zumbi e da Consciência Negra, um texto sobre o sofrimento psíquico causado pelo racismo. Leia “O racismo também adoece”, publicado nesta semana."),
         ("pre-dom-post", "22/11 · Ninguém nasce com preconceito", "A gente aprende em casa, na escola, nas piadas. E o que se aprende também pode ser revisto.")]
serie_html = ('      <div class="rf-serie">\n        <p class="eyebrow">Série Preconceito</p>\n'
              '        <p class="rf-cred">A cada dia desta semana, um novo conteúdo no Instagram e aqui, com o contexto completo.</p>\n        <ul>'
              + "".join(f'<li hidden data-agendado="serie-{k}"><b>{t}</b><br>{d} <!--IG:{k}--></li>' for k, t, d in SERIE)
              + '</ul>\n        <p class="rf-teaser" id="rf-teaser"></p>\n      </div>\n')
nova = site_article(arts[0], "rf-5", "Reflexão da semana", "", "pre-qua-reels", "18 de novembro de 2026", serie_html)
texto2 = site_article(arts[1], "rf-racismo", "Texto da semana", ' hidden data-agendado="texto-racismo"', "pre-sex-post", "20 de novembro de 2026")

ant = f'''      <details>
        <summary>Boletim não é retrato <span class="small">(nov/26)</span></summary>
        {rf4_old}
      </details>
      <details>
        <summary>Quando o corpo fala antes das palavras <span class="small">(nov/26)</span></summary>
        {rfc_old}
      </details>
      <details>
        <summary>Um ano no nosso novo espaço <span class="small">(nov/26)</span></summary>
        {aniv}
      </details>
'''
novo = html[:i4] + nova + "\n\n    " + texto2 + html[jc:]
k = novo.index('<p class="small">As reflexões ficam guardadas aqui, da mais recente para a mais antiga.</p>\n')
k = novo.index("\n", k) + 1
novo = novo[:k] + ant + novo[k:]

oldcard = re.search(r'(<button class="card rf-home" data-go="reflexoes">\s*<p class="rf-selo">Reflexão da semana</p>\s*)<b>.*?</b>\s*<span>.*?</span>', novo, re.S)
novo = novo.replace(oldcard.group(0), oldcard.group(1) + '<b>O que a gente aprende sem perceber</b>\n        <span>Sobre preconceito: como ele se aprende, o que deixa em quem ouve e por que também pode ser revisto.</span>')

assert novo.count('id="rf-teaser"') == 1 and 'Boletim não é retrato</h3>' in novo and 'id="rf-5"' in novo
open(f"{R}/posts/2026-11-18-1929-site-semana/index_novo.html", "w", encoding="utf-8").write(novo)
print("posts:", len(posts), "index_novo:", len(novo), "antes:", len(html))
