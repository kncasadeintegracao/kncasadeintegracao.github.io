import json, os, shutil, sys, re
S = os.environ.get("KN_WORK", "/tmp/kn_work")
R = "/home/claude/kncasadeintegracao.github.io"
sys.path.insert(0, S + "/build")
import assemble_b as A  # traz days (legendas) e ARTS (textos do site)

caps = {d["chip"].split()[0]: d.get("cap", "") for d in A.days}
FOOT = ("Katheryne Solange Muniz Nazer – RT · Psicóloga · CRP 06/117.713\n"
        "KN Casa de Integração® · Mooca/SP e online\n"
        "Cuidar de pessoas. Formar profissionais. Transformar realidades.\n"
        "© 2026 KN Casa de Integração®. Todos os direitos reservados.")
def leg(dia):
    c = caps[dia]; i = c.rindex("\n\n#")
    return c[:i] + "\n\n" + FOOT + c[i:]

MD = "midia/2026-11-fim-ano-letivo"
os.makedirs(f"{R}/{MD}", exist_ok=True)
for f in os.listdir(S + "/out_b"):
    if f.endswith("_frame.jpg"): continue
    shutil.copy(f"{S}/out_b/{f}", f"{R}/{MD}/{f}")
m = lambda f: f"{MD}/{f}"

posts = []
def P(folder, **kw):
    kw.setdefault("status", "aprovado"); posts.append((folder, kw))

P("2026-11-09-1229-site-semana", tipo="site", agendar_para="2026-11-09T12:29:00-03:00", acao="trocar_index", arquivo="index_novo.html")
P("2026-11-09-1230-post-abertura", tipo="imagem", agendar_para="2026-11-09T12:30:00-03:00", imagem=m("seg_post.jpg"), legenda=leg("Segunda"), site_marcador="fal-seg-post")
P("2026-11-09-1235-story", tipo="story", agendar_para="2026-11-09T12:35:00-03:00", midia=m("seg_story.jpg"))
P("2026-11-09-1700-story-grupo", tipo="story", agendar_para="2026-11-09T17:00:00-03:00", midia=m("seg_story_grupo.mp4"))
P("2026-11-10-1230-carrossel-provas", tipo="carrossel", agendar_para="2026-11-10T12:30:00-03:00",
  imagens=[m(x) for x in ["ter_c01.jpg","ter_c02.jpg","ter_c03.mp4","ter_c04.jpg","ter_c05.jpg","ter_c06.jpg","ter_c07.jpg"]], legenda=leg("Terça"), site_marcador="fal-ter-carrossel")
P("2026-11-10-1235-story", tipo="story", agendar_para="2026-11-10T12:35:00-03:00", midia=m("ter_story.jpg"))
P("2026-11-11-1929-site-texto", tipo="site", agendar_para="2026-11-11T19:29:00-03:00", acao="revelar", marcador="texto-corpo")
P("2026-11-11-1930-reels-sinais", tipo="reels", agendar_para="2026-11-11T19:30:00-03:00", video=m("qua_reels.mp4"), capa=m("qua_reels_capa.jpg"), legenda=leg("Quarta"), site_marcador="fal-qua-reels")
P("2026-11-11-1935-story", tipo="story", agendar_para="2026-11-11T19:35:00-03:00", midia=m("qua_story.jpg"))
P("2026-11-12-1230-carrossel-frustracao", tipo="carrossel", agendar_para="2026-11-12T12:30:00-03:00",
  imagens=[m(x) for x in ["qui_c01.jpg","qui_c02.jpg","qui_c03.jpg","qui_c04.jpg","qui_c05.mp4","qui_c06.jpg","qui_c07.jpg"]], legenda=leg("Quinta"), site_marcador="fal-qui-carrossel")
P("2026-11-12-1235-story", tipo="story", agendar_para="2026-11-12T12:35:00-03:00", midia=m("qui_story.jpg"))
P("2026-11-13-1230-post-orientacao", tipo="imagem", agendar_para="2026-11-13T12:30:00-03:00", imagem=m("sex_post.jpg"), legenda=leg("Sexta"), site_marcador="fal-sex-post")
P("2026-11-13-1235-story", tipo="story", agendar_para="2026-11-13T12:35:00-03:00", midia=m("sex_story.jpg"))
P("2026-11-14-1800-story-reflexao", tipo="story", agendar_para="2026-11-14T18:00:00-03:00", midia=m("sab_story3.jpg"))
P("2026-11-15-1930-post-domingo", tipo="imagem", agendar_para="2026-11-15T19:30:00-03:00", imagem=m("dom_post.jpg"), legenda=leg("Domingo"), site_marcador="fal-dom-post")
P("2026-11-15-1935-story", tipo="story", agendar_para="2026-11-15T19:35:00-03:00", midia=m("dom_story.jpg"))

for folder, post in posts:
    os.makedirs(f"{R}/posts/{folder}", exist_ok=True)
    json.dump(post, open(f"{R}/posts/{folder}/post.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)

# ---------- novo index (troca às 12h29 de segunda) ----------
html = open(f"{R}/index.html", encoding="utf-8").read()

def bloco(start):
    i = html.index(start); j = html.index("</article>", i) + len("</article>")
    return i, j

# 1) Reflexão de 3/11 e texto de 5/11 viram "anteriores"
i3, j3 = bloco('<article class="card reflexao destaque" id="rf-3">')
rf3 = html[i3:j3]
ia, ja = bloco('<article class="card reflexao" id="rf-adolescentes" data-agendado="texto-adolescentes">')
rfa = html[ia:ja]
rf3_old = (rf3.replace('<article class="card reflexao destaque" id="rf-3">', '<article class="card reflexao" id="rf-3">')
              .replace('      <p class="rf-selo">Reflexão da semana</p>\n', '', 1)
              .replace('        <p class="rf-teaser" id="rf-teaser"></p>\n', ''))
assert 'id="rf-teaser"' not in rf3_old
rfa_old = rfa.replace('<p class="rf-selo">Texto da semana</p>\n', '', 1)

ARTS = A.ARTS  # html do quadro (artigos) — converto para o padrão do site
def site_article(art, aid, selo, extra_attr, ig_marker, data_ext, serie=""):
    t = re.search(r"<h2>(.*?)</h2>", art).group(1)
    by = re.search(r'<div class="by">(.*?)</div>', art).group(1)
    paras = re.findall(r"      <p>(.*?)</p>", art, re.S)
    refs = re.findall(r"        <p>(.*?)</p>", art[art.index('class="refs"'):art.index('class="sign"')], re.S)
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

arts = ARTS.split("<article>")[1:]
SERIE = [("fal-seg-post", "09/11 · O fim do ano letivo também mexe com eles", "Abertura da semana: provas, recuperação, despedidas e férias chegando, e como acompanhar crianças e adolescentes nesta reta final."),
         ("fal-ter-carrossel", "10/11 · Provas, recuperação e cansaço: 5 atitudes que ajudam", "Olhar para o processo, ajudar a organizar sem assumir o lugar do filho, escutar antes de aconselhar, ver a recuperação como nova chance e cuidar do descanso."),
         ("fal-qua-reels", "11/11 · Sinais de sobrecarga no fim do ano letivo", "O que o corpo e o comportamento das crianças e dos adolescentes podem estar dizendo, e quando procurar ajuda. Para ir mais fundo, leia o texto “Quando o corpo fala antes das palavras”, publicado nesta semana."),
         ("fal-qui-carrossel", "12/11 · Quando o resultado não veio", "Cinco formas de ajudar seu filho diante da frustração: acolher primeiro, separar a pessoa da nota, olhar para a frente juntos, evitar comparações e mostrar que errar faz parte."),
         ("fal-sex-post", "13/11 · Orientação profissional: o próximo passo", "Para quem termina o 9º ano ou o ensino médio, e também para adultos em transição de carreira: de 8 a 12 encontros, com devolutiva presencial."),
         ("fal-dom-post", "15/11 · Boletim não é retrato", "Uma nota fala de um momento. Quem seu filho é cabe em muito mais do que isso.")]
serie_html = ('      <div class="rf-serie">\n        <p class="eyebrow">Série Fim do Ano Letivo</p>\n'
              '        <p class="rf-cred">A cada dia desta semana, um novo conteúdo no Instagram e aqui, com o contexto completo.</p>\n        <ul>'
              + "".join(f'<li hidden data-agendado="serie-{k}"><b>{t}</b><br>{d} <!--IG:{k}--></li>' for k, t, d in SERIE)
              + '</ul>\n        <p class="rf-teaser" id="rf-teaser"></p>\n      </div>\n')
nova = site_article(arts[0], "rf-4", "Reflexão da semana", "", "fal-seg-post", "9 de novembro de 2026", serie_html)
texto2 = site_article(arts[1], "rf-corpo", "Texto da semana", ' hidden data-agendado="texto-corpo"', "fal-qua-reels", "11 de novembro de 2026")
assert ' hidden data-agendado="texto-corpo"' in texto2

ant = '''      <details>
        <summary>O mundo digital veio para facilitar a nossa vida. E o que a gente faz com isso? <span class="small">(nov/26)</span></summary>
        ''' + rf3_old + '''
      </details>
      <details>
        <summary>Adolescentes e telas: menos guerra, mais presença <span class="small">(nov/26)</span></summary>
        ''' + rfa_old + '''
      </details>
'''
# monta: tira os dois blocos antigos, põe os novos no lugar, e os antigos no topo das anteriores
novo = html[:i3] + nova + "\n\n    " + texto2 + html[j3:ia] + html[ja:]
k = novo.index('<p class="small">As reflexões ficam guardadas aqui, da mais recente para a mais antiga.</p>\n')
k = novo.index("\n", k) + 1
novo = novo[:k] + ant + novo[k:]

# 2) cartão da Reflexão da semana na página inicial
oldcard = re.search(r'(<button class="card rf-home" data-go="reflexoes">\s*<p class="rf-selo">Reflexão da semana</p>\s*)<b>.*?</b>\s*<span>.*?</span>', novo, re.S)
novo = novo.replace(oldcard.group(0), oldcard.group(1) + '<b>Boletim não é retrato</b>\n        <span>Sobre o fim do ano letivo de crianças e adolescentes: provas, recuperação, frustração e o que nenhuma nota consegue medir.</span>')

# o novo index não pode levar links da semana passada como marcadores pendentes
open(f"{R}/posts/2026-11-09-1229-site-semana/index_novo.html", "w", encoding="utf-8").write(novo)
print("posts:", len(posts), "index_novo:", len(novo))
