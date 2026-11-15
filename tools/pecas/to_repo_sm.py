"""Semana 16–22/11/2026 (Saúde mental do homem): grava mídias, posts/*/post.json e o index_novo.
Rodar só depois do "pode publicar". DEST=<pasta> grava numa cópia (teste); sem DEST grava no repositório."""
import json, os, shutil, sys, re
S = os.environ.get("KN_WORK", "/tmp/kn_work")
R = "/home/claude/kncasadeintegracao.github.io"
DEST = os.environ.get("DEST", R)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import assemble_sm as A

caps = {d["chip"].split()[0]: d.get("cap", "") for d in A.days}
MD = "midia/2026-11-saude-do-homem"
os.makedirs(f"{DEST}/{MD}", exist_ok=True)
for f in os.listdir(S + "/out_sm"):
    if f.endswith("_frame.jpg"): continue
    shutil.copy(f"{S}/out_sm/{f}", f"{DEST}/{MD}/{f}")
m = lambda f: f"{MD}/{f}"

posts = []
def P(folder, **kw):
    kw.setdefault("status", "aprovado"); posts.append((folder, kw))
car = lambda p: [m(f"{p}_c0{i}.{'mp4' if (p, i) in (('ter', 3), ('qui', 5)) else 'jpg'}") for i in range(1, 8)]

P("2026-11-16-1229-site-semana", tipo="site", agendar_para="2026-11-16T12:29:00-03:00", acao="trocar_index", arquivo="index_novo.html")
P("2026-11-16-1230-post-abertura", tipo="imagem", agendar_para="2026-11-16T12:30:00-03:00", imagem=m("seg_post.jpg"), legenda=caps["Segunda"], site_marcador="smh-seg-post")
P("2026-11-16-1235-story", tipo="story", agendar_para="2026-11-16T12:35:00-03:00", midia=m("seg_story.jpg"))
P("2026-11-17-1230-carrossel-sinais", tipo="carrossel", agendar_para="2026-11-17T12:30:00-03:00", imagens=car("ter"), legenda=caps["Terça"], site_marcador="smh-ter-carrossel")
P("2026-11-17-1235-story", tipo="story", agendar_para="2026-11-17T12:35:00-03:00", midia=m("ter_story.jpg"))
P("2026-11-18-1929-site-texto", tipo="site", agendar_para="2026-11-18T19:29:00-03:00", acao="revelar", marcador="texto-homem")
P("2026-11-18-1930-reels-limite", tipo="reels", agendar_para="2026-11-18T19:30:00-03:00", video=m("qua_reels.mp4"), capa=m("qua_reels_capa.jpg"), legenda=caps["Quarta"], site_marcador="smh-qua-reels")
P("2026-11-18-1935-story", tipo="story", agendar_para="2026-11-18T19:35:00-03:00", midia=m("qua_story.jpg"))
P("2026-11-19-1230-carrossel-frases", tipo="carrossel", agendar_para="2026-11-19T12:30:00-03:00", imagens=car("qui"), legenda=caps["Quinta"], site_marcador="smh-qui-carrossel")
P("2026-11-19-1235-story", tipo="story", agendar_para="2026-11-19T12:35:00-03:00", midia=m("qui_story.jpg"))
P("2026-11-20-1230-post-terapia", tipo="imagem", agendar_para="2026-11-20T12:30:00-03:00", imagem=m("sex_post.jpg"), legenda=caps["Sexta"], site_marcador="smh-sex-post")
P("2026-11-20-1235-story", tipo="story", agendar_para="2026-11-20T12:35:00-03:00", midia=m("sex_story.jpg"))
P("2026-11-21-1800-story-reflexao", tipo="story", agendar_para="2026-11-21T18:00:00-03:00", midia=m("sab_story3.jpg"))
P("2026-11-22-1930-post-domingo", tipo="imagem", agendar_para="2026-11-22T19:30:00-03:00", imagem=m("dom_post.jpg"), legenda=caps["Domingo"], site_marcador="smh-dom-post")
P("2026-11-22-1935-story", tipo="story", agendar_para="2026-11-22T19:35:00-03:00", midia=m("dom_story.jpg"))

for folder, post in posts:
    os.makedirs(f"{DEST}/posts/{folder}", exist_ok=True)
    json.dump(post, open(f"{DEST}/posts/{folder}/post.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- novo index (troca às 12h29 de segunda) ----------
html = open(f"{R}/index.html", encoding="utf-8").read()
def bloco(start, end):
    i = html.index(start); j = html.index(end, i) + len(end); return i, j

i4, j4 = bloco('<article class="card reflexao destaque" id="rf-4">', "</article>")
ia, ja = bloco('<div class="card reflexao" data-agendado="serie-aniv-1ano">', "</p>\n    </div>")
ic, jc = bloco('<article class="card reflexao" id="rf-corpo"', "</article>")
assert i4 < ia < ic

def limpar_refs(b):
    """tira do corpo do texto as referências que já estão no rodapé (sobra da montagem anterior)"""
    refline = re.search(r'<p class="rf-ref">Referências: (.*?)</p>', b).group(1)
    for r in refline.split(" · "):
        b = b.replace(f"        <p>{r}</p>\n", "")
    return b

rf4 = limpar_refs(html[i4:j4])
rf4 = (rf4.replace('<article class="card reflexao destaque" id="rf-4">', '<article class="card reflexao" id="rf-4">')
          .replace('      <p class="rf-selo">Reflexão da semana</p>\n', '', 1)
          .replace('        <p class="rf-teaser" id="rf-teaser"></p>\n', '')
          .replace('<li hidden data-agendado=', '<li data-agendado='))
aniv = html[ia:ja]
rfc = limpar_refs(html[ic:jc]).replace(' data-agendado="texto-corpo"', '').replace('      <p class="rf-selo">Texto da semana</p>\n', '', 1)
assert 'id="rf-teaser"' not in rf4 and "rf-selo\">Reflexão" not in rf4

def site_article(art, aid, selo, extra_attr, ig_marker, data_ext, serie=""):
    t = re.search(r"<h2>(.*?)</h2>", art).group(1)
    by = re.search(r'<div class="by">(.*?)</div>', art).group(1)
    corpo = art[:art.index('<div class="refs">')]
    paras = re.findall(r"\n      <p>(.*?)</p>", corpo, re.S)
    refs = re.findall(r"<p>(.*?)</p>", art[art.index('class="refs"'):art.index('class="sign"')], re.S)
    it = lambda s: s.replace("<em>", "<i>").replace("</em>", "</i>")
    return f'''<article class="card reflexao{' destaque' if selo == 'Reflexão da semana' else ''}" id="{aid}"{extra_attr}>
      <p class="rf-selo">{selo}</p>
      <h3>{t}</h3>
      <p class="rf-data">{by}</p>
      <div class="rf-texto">
''' + "".join(f"        <p>{it(p)}</p>\n" for p in paras) + f'''      </div>
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
      <p class="rf-ref">Referências: {" · ".join(it(r) for r in refs)}</p>
      <p class="rf-ref">© 2026 KN Casa de Integração®. Todos os direitos reservados.</p>
    </article>'''

arts = A.ARTS.split("<article>")[1:]
SERIE = [("smh-seg-post", "16/11 · Saúde mental do homem", "Abertura da semana: força também é conseguir dizer “não estou bem”."),
         ("smh-ter-carrossel", "17/11 · Nem todo sofrimento parece tristeza", "Cinco sinais que muitos homens não reconhecem como pedido de ajuda: irritação constante, trabalho sem fim, sintomas no corpo, mais álcool e menos conversa, isolamento."),
         ("smh-qua-reels", "18/11 · Por que tantos homens só pedem ajuda no limite?", "Quando sentir foi ensinado como fraqueza, o sofrimento aparece de outro jeito. Para ir mais fundo, leia o texto “O que muitos homens não aprenderam a dizer”, publicado nesta semana."),
         ("smh-qui-carrossel", "19/11 · Frases que já podem se aposentar", "“Homem não chora”, “engole o choro”, “seja homem”, “isso é frescura” e “aguenta firme”, e o que dizer no lugar de cada uma."),
         ("smh-sex-post", "20/11 · Terapia também é lugar de homem", "Psicoterapia de adultos na KN Casa de Integração®: um espaço sigiloso para pensar o trabalho, as relações, a paternidade e o que anda pesando."),
         ("smh-dom-post", "22/11 · Calar não é o mesmo que estar bem", "Ninguém precisa morar no meio do rio. Há outras margens possíveis, e a escuta pode ser uma delas.")]
serie_html = ('      <div class="rf-serie">\n        <p class="eyebrow">Série Saúde Mental do Homem</p>\n'
              '        <p class="rf-cred">A cada dia desta semana, um novo conteúdo no Instagram e aqui, com o contexto completo.</p>\n        <ul>'
              + "".join(f'<li hidden data-agendado="serie-{k}"><b>{t}</b><br>{d} <!--IG:{k}--></li>' for k, t, d in SERIE)
              + '</ul>\n        <p class="rf-teaser" id="rf-teaser"></p>\n      </div>\n')
nova = site_article(arts[0], "rf-5", "Reflexão da semana", "", "smh-seg-post", "16 de novembro de 2026", serie_html)
texto2 = site_article(arts[1], "rf-homem", "Texto da semana", ' hidden data-agendado="texto-homem"', "smh-qua-reels", "18 de novembro de 2026")

ant = ('      <details>\n        <summary>Boletim não é retrato <span class="small">(nov/26)</span></summary>\n        ' + rf4 + '\n      </details>\n'
       '      <details>\n        <summary>Quando o corpo fala antes das palavras <span class="small">(nov/26)</span></summary>\n        ' + rfc + '\n      </details>\n'
       '      <details>\n        <summary>Um ano no nosso novo espaço <span class="small">(nov/26)</span></summary>\n        ' + aniv + '\n      </details>\n')
novo = html[:i4] + nova + "\n\n    " + texto2 + html[jc:]
k = novo.index('<p class="small">As reflexões ficam guardadas aqui, da mais recente para a mais antiga.</p>\n')
k = novo.index("\n", k) + 1
novo = novo[:k] + ant + novo[k:]

oldcard = re.search(r'(<button class="card rf-home" data-go="reflexoes">\s*<p class="rf-selo">Reflexão da semana</p>\s*)<b>.*?</b>\s*<span>.*?</span>', novo, re.S)
novo = novo.replace(oldcard.group(0), oldcard.group(1) + '<b>A terceira margem do silêncio</b>\n        <span>Sobre a saúde mental do homem: o que muitos aprenderam a calar, os sinais que passam despercebidos e o lugar da escuta.</span>')
assert novo.count('id="rf-teaser"') == 1 and novo.count('id="rf-4"') == 1 and novo.count('id="rf-corpo"') == 1
open(f"{DEST}/posts/2026-11-16-1229-site-semana/index_novo.html", "w", encoding="utf-8").write(novo)
print("posts:", len(posts), "index_novo:", len(novo))
