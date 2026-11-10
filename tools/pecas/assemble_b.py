import os
import json, base64
S = os.environ.get("KN_WORK", "/tmp/kn_work")

SIGN = lambda dia: f"""<div class="sign">
        <div><b>Katheryne Solange Muniz Nazer (KN)</b> · Psicóloga · CRP 06/117.713 · Responsável Técnica · KN Casa de Integração®</div>
        <div>Mooca/SP, {dia} de novembro de 2026</div>
        <div class="slogan">Cuidar de pessoas. Formar profissionais. Transformar realidades.</div>
        <div class="copyr">© 2026 KN Casa de Integração®. Todos os direitos reservados.</div>
      </div>"""

ARTS = f"""
    <article>
      <div class="eyebrow">Reflexão da semana</div>
      <h2>Boletim não é retrato</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Novembro chega e, com ele, a reta final do ano letivo. Dentro de casa, o assunto muda: provas, notas, recuperação e a ansiedade de saber se o filho "passou de ano". No consultório, recebo crianças e adolescentes que chegam a dezembro cansados, e pais que chegam aflitos, querendo entender o que fazer.</p>
      <p>Françoise Dolto comparou o adolescente a uma lagosta no período em que troca de carapaça: a antiga já não serve, a nova ainda não endureceu, e ele fica exposto, mais sensível a tudo o que vem de fora. Penso muito nessa imagem quando um boletim chega. Para quem atravessa essa fase de mudança, uma nota baixa pode soar como sentença sobre quem ele é, e não como informação sobre um bimestre.</p>
      <p>Com as crianças, a delicadeza é a mesma. Winnicott dizia que é no brincar que a criança pode ser criativa e usar a personalidade inteira, e que é sendo criativa que ela encontra a si mesma. Aprender também depende disso: de algum espaço livre, de curiosidade e de prazer. Quando a escola vira só cobrança, esse espaço encolhe, e o aprender perde a graça.</p>
      <p>Drummond tem um poema de que eu gosto muito, "Infância", do livro <em>Alguma poesia</em>. Nele, o menino lê sozinho a história de Robinson Crusoé enquanto a vida da casa segue em volta, sem pressa. Ninguém cobra nada dele naquele momento: é só o encanto de uma história. É o desejo de saber em estado puro, e nenhum boletim mede isso. Talvez a pergunta mais importante deste fim de ano não seja "qual foi a sua nota?", e sim "o que você gostou de aprender?".</p>
      <p>Isso não significa ignorar as dificuldades. Uma recuperação, uma reprovação ou uma queda de rendimento merecem atenção e, às vezes, uma investigação cuidadosa: pode haver cansaço, sofrimento emocional ou uma dificuldade de aprendizagem que ninguém percebeu ainda. Mas o primeiro gesto da família pode ser outro: olhar para o filho inteiro antes de olhar para o número.</p>
      <p>Boletim não é retrato. É o registro de um momento, num ano que pediu muito de todos. Quem seu filho é cabe em muito mais do que isso.</p>
      <p>Se você percebe que seu filho ou sua filha precisa de um cuidado a mais nesta reta final, a KN Casa de Integração® está de portas abertas, com psicoterapia de crianças e adolescentes, orientação a pais, avaliação psicológica e neuropsicológica e orientação profissional, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Andrade, C. D. de (1930). Infância. In <em>Alguma poesia</em>. Belo Horizonte: Pindorama.</p>
        <p>Dolto, F. (1988/2022). <em>La causa de los adolescentes</em>. Barcelona: Paidós.</p>
        
        <p>Winnicott, D. W. (1971/1975). <em>O brincar e a realidade</em>. Rio de Janeiro: Imago.</p>
      </div>
      {SIGN(9)}
    </article>

    <article>
      <div class="eyebrow">Texto autoral · ligado ao Reels de quarta</div>
      <h2>Quando o corpo fala antes das palavras</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Muitas crianças não dizem "estou sobrecarregada". Dizem que estão com dor de barriga na segunda de manhã, choram por coisas pequenas, voltam a pedir para dormir com os pais ou a molhar a cama depois de muito tempo. Muitos adolescentes também não dizem "não estou dando conta". Fecham a porta do quarto, respondem com irritação, trocam o dia pela noite e passam a achar que tudo tanto faz.</p>
      <p>Freud nos ensinou a escutar o sintoma como uma forma de expressão: algo que não encontrou palavras procura outro caminho para aparecer. Na infância e na adolescência, esse caminho costuma passar pelo corpo e pelo comportamento. Por isso, antes de corrigir, vale perguntar o que aquilo está tentando dizer.</p>
      <p>Winnicott, por sua vez, insistiu na importância de um ambiente suficientemente bom, capaz de sustentar a criança enquanto ela amadurece. Em época de provas, esse ambiente pode ser uma rotina mais previsível, um adulto disponível para conversar e um pouco menos de pressão dentro de casa.</p>
      <p>Manoel de Barros, nas suas <em>Memórias inventadas</em>, revisita a infância como lugar de invenção e encantamento. Gosto de lembrar dele porque a infância precisa desse espaço, mesmo em novembro, mesmo com a semana cheia de provas.</p>
      <p>Quando os sinais aparecem por alguns dias e passam com o fim das provas, costuma ser um cansaço que a própria família consegue acolher. Quando persistem, aumentam ou vêm acompanhados de muita tristeza, falas de desesperança ou isolamento, é hora de buscar avaliação profissional.</p>
      <p>Na KN Casa de Integração®, crianças, adolescentes e famílias encontram escuta com ciência e afeto, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Barros, M. de (2003). <em>Memórias inventadas: a infância</em>. São Paulo: Planeta.</p>
        <p>Freud, S. (1926/2014). Inibição, sintoma e angústia. In <em>Obras completas</em> (Vol. 17). São Paulo: Companhia das Letras.</p>
        <p>Winnicott, D. W. (1965/1983). <em>O ambiente e os processos de maturação</em>. Porto Alegre: Artes Médicas.</p>
      </div>
      {SIGN(11)}
    </article>"""

days = [
 dict(chip="Segunda 9/11 · 12h30", h="Post de abertura", kind="Post único no feed às 12h30, story às 12h35 e lembrete do grupo de adultos às 17h",
  items=[dict(f="seg_post.jpg", c="Foto Pexels · cartão KN"), dict(f="seg_story.jpg", st=1, c="Story 12h35"), dict(f="seg_story_grupo.mp4", st=1, c="Story 17h · lembrete animado do grupo de hoje, 19h")],
  cap="Novembro chegou e, com ele, a reta final do ano letivo. 📚\n\nProvas, recuperação, despedidas dos colegas e férias chegando: tudo isso mexe com crianças e adolescentes, mesmo quando eles não falam sobre isso.\n\nNesta semana, a KN Casa de Integração® vai conversar com você, mãe, pai ou responsável, sobre como acompanhar seu filho nesta fase com mais escuta e menos cobrança.\n\n📖 A reflexão completa, \"Boletim não é retrato\", já está no site: kncasadeintegracao.com (link na bio).\n\n#psicologiainfantil #adolescencia #fimdeanoletivo #paisefilhos #saudemental #mooca #kncasadeintegracao",
  notes="<b>Site:</b> entra a reflexão \"Boletim não é retrato\", com o link deste post."),
 dict(chip="Terça 10/11 · 12h30", h="Carrossel: provas, recuperação e cansaço", kind="Carrossel com 7 cartões + story às 12h35",
  items=[dict(f="ter_c01.jpg", c="1 · foto Pexels"), dict(f="ter_c02.jpg", c="2"), dict(f="ter_c03.mp4", c="3 · animado, criado por mim"), dict(f="ter_c04.jpg", c="4 · foto Pexels"), dict(f="ter_c05.jpg", c="5"), dict(f="ter_c06.jpg", c="6"), dict(f="ter_c07.jpg", c="7 · sala da KN"), dict(f="ter_story.jpg", st=1, c="Story 12h35")],
  cap="Provas, recuperação e cansaço. 📚✏️\n👉 Arraste e veja 5 atitudes que ajudam crianças e adolescentes a fechar o ano letivo.\n\nNesta reta final, o jeito como a família recebe a nota pesa tanto quanto a própria nota. Escuta, organização e descanso fazem diferença.\n\n💚 A KN Casa de Integração® acolhe crianças, adolescentes e famílias, presencialmente na Mooca/SP e online.\n📌 Salve e envie para quem tem filho em semana de provas.\n\n#fimdeanoletivo #provas #recuperacao #adolescencia #psicologiainfantil #kncasadeintegracao"),
 dict(chip="Quarta 11/11 · 19h30", h="Reels: sinais de sobrecarga", kind="Reels de 23 segundos (capa + vídeo) + story às 19h35",
  items=[dict(f="qua_reels_capa.jpg", st=1, c="Capa do Reels"), dict(f="qua_reels.mp4", st=1, c="Reels: fotos Pexels com movimento e telas criadas por mim; final com a sala da KN"), dict(f="qua_story.jpg", st=1, c="Story 19h35")],
  cap="Seu filho anda diferente nestes últimos dias de aula? 👀\n\nCrianças e adolescentes nem sempre dizem que estão sobrecarregados. Muitas vezes, o corpo e o comportamento falam antes: dor de barriga antes da aula, choro, irritação, isolamento.\n\nConverse, observe e, se os sinais persistirem, procure ajuda profissional.\n\n📖 Leia mais no site: \"Quando o corpo fala antes das palavras\" (link na bio).\n💚 KN Casa de Integração® · Mooca/SP e online.\n\n#saudementalinfantil #adolescencia #fimdeanoletivo #paisefilhos #psicologia #kncasadeintegracao",
  notes="<b>Áudio:</b> instrumental calmo da biblioteca do Instagram, escolhido na hora de publicar. <b>Site:</b> entra o texto \"Quando o corpo fala antes das palavras\", com o link do Reels."),
 dict(chip="Quinta 12/11 · 12h30", h="Carrossel: quando o resultado não veio", kind="Carrossel com 7 cartões + story às 12h35. Seu vídeo, se vier, entra nos stories à tarde.",
  items=[dict(f="qui_c01.jpg", c="1 · foto Pexels"), dict(f="qui_c02.jpg", c="2"), dict(f="qui_c03.jpg", c="3"), dict(f="qui_c04.jpg", c="4 · foto Pexels"), dict(f="qui_c05.mp4", c="5 · animado, criado por mim"), dict(f="qui_c06.jpg", c="6"), dict(f="qui_c07.jpg", c="7 · sala da KN"), dict(f="qui_story.jpg", st=1, c="Story 12h35")],
  cap="Quando o resultado não veio. 💛\n👉 Arraste e veja 5 formas de ajudar seu filho diante da recuperação, da reprovação ou do resultado que ele tanto esperava.\n\nA frustração faz parte da vida, e aprender a atravessá-la com apoio é uma das coisas mais importantes que a infância e a adolescência podem oferecer.\n\n💚 Se seu filho está sofrendo mais do que o esperado, a KN Casa de Integração® pode ajudar, presencialmente na Mooca/SP e online.\n📌 Salve para lembrar quando o boletim chegar.\n\n#frustracao #fimdeanoletivo #adolescencia #psicologiainfantil #paisefilhos #kncasadeintegracao",
  notes="<b>Seu vídeo da semana (opcional):</b> tema sugerido \"Como falar com seu filho quando o boletim chega\". Grave na quarta e me mande; eu coloco marca d'água, legendas e título."),
 dict(chip="Sexta 13/11 · 12h30", h="Orientação profissional", kind="Post único no feed + story às 12h35",
  items=[dict(f="sex_post.jpg", c="Foto Pexels"), dict(f="sex_story.jpg", st=1, c="Story 12h35")],
  cap="Terminando o 9º ano ou o ensino médio? 🧭\n\nO fim do ano letivo costuma trazer uma pergunta grande: e agora, qual é o próximo passo? Escolher curso, escola ou profissão pede escuta, autoconhecimento e informação.\n\nNa KN Casa de Integração®, a orientação profissional é conduzida pela Dra. Katheryne, em cerca de 8 a 12 encontros, com os instrumentos adequados a cada caso e devolutiva presencial. É para adolescentes, jovens no vestibular e também adultos em transição de carreira.\n\n📍 Mooca/SP\n👉 Saiba mais e agende pelo link da bio.\n\n#orientacaoprofissional #vestibular #ensinomedio #escolhaprofissional #adolescencia #kncasadeintegracao",
  notes="Este post também ajuda a encher a agenda: fecha a semana escolar apresentando um serviço que só você oferece na casa."),
 dict(chip="Sábado 14/11", h="Só stories", kind="Três stories, sem post no feed (sugestão: 10h, 14h e 18h)",
  items=[dict(f="sab_story1.jpg", st=1, c="10h · caixinha de perguntas"), dict(f="sab_story2.mp4", st=1, c="14h · enquete animada, criada por mim"), dict(f="sab_story3.jpg", st=1, c="18h · lembrete da reflexão")]),
 dict(chip="Domingo 15/11 · 19h30", h="Trecho da reflexão", kind="Post único no feed + story às 19h35",
  items=[dict(f="dom_post.jpg", c="Foto Pexels"), dict(f="dom_story.jpg", st=1, c="Story 19h35")],
  cap="Boletim não é retrato. 💛\n\nUma nota fala de um momento, num ano que pediu muito de todos. Quem seu filho é cabe em muito mais do que isso.\n\nNesta semana, conversamos sobre o fim do ano letivo de crianças e adolescentes. A reflexão completa, com Dolto, Winnicott e Drummond, está no site da KN Casa de Integração® (link na bio).\n\nBom domingo para você e para os seus. 🌿\n\n#reflexao #psicanalise #infancia #adolescencia #fimdeanoletivo #kncasadeintegracao"),
]

media = {}
for d in days:
    for it in d["items"]:
        f = it["f"]; mime = "video/mp4" if f.endswith(".mp4") else "image/jpeg"
        media[f] = f"data:{mime};base64," + base64.b64encode(open(f"{S}/rev_b/{f}", "rb").read()).decode()

src = open(S + "/build/page_src.html").read()
rep = [
 ("<title>Semana Fechar o Ano</title>", "<title>Semana Fim do Ano Letivo</title>"),
 ("<div class=\"eyebrow\">KN Casa de Integração® · Programação para aprovação</div>", "<div class=\"eyebrow\">KN Casa de Integração® · Opção de tema para aprovação</div>"),
 ("<h1>Fechar o ano sem se fechar</h1>", "<h1>O fim do ano letivo também mexe com eles</h1>"),
 ("<dd>Post de abertura + story animado do grupo (hoje, 19h)</dd>", "<dd>Post de abertura + lembrete do grupo de adultos (hoje, 19h)</dd>"),
 ("<dd>Carrossel: balanço de fim de ano sem tribunal</dd>", "<dd>Carrossel: provas, recuperação e cansaço</dd>"),
 ("<dd>Reels: o cansaço de novembro + texto no site</dd>", "<dd>Reels: sinais de sobrecarga + texto no site</dd>"),
 ("<dd>Carrossel: nem todo mundo está em clima de festa</dd>", "<dd>Carrossel: quando o resultado não veio</dd>"),
 ("<dd>Convite do grupo: venha em dupla</dd>", "<dd>Orientação profissional: o próximo passo</dd>"),
 ("<dd>Só stories: caixinha, enquete e lembrete</dd>", "<dd>Só stories: caixinha, enquete e lembrete</dd>"),
 ("<dd>Trecho da reflexão, com \"leia mais no site\"</dd>", "<dd>Trecho da reflexão, com \"leia mais no site\"</dd>"),
 ("Fotos: Pexels (licença gratuita) e fotos da própria KN Casa de Integração® nos cartões finais. Imagens animadas (anel do ano e linhas fluidas) criadas por Claude.",
  "Fotos: Pexels (licença gratuita), sem personagens nem marcas, e fotos da própria KN Casa de Integração® nos cartões finais. Imagens animadas (anel do ano e linhas fluidas) criadas por Claude."),
]
for a, b in rep:
    assert a in src, a
    src = src.replace(a, b)
src = src.replace("__ARTICLES__", ARTS).replace("__MEDIA__", json.dumps(media)).replace("__DAYS__", json.dumps(days, ensure_ascii=False))
open(S + "/semana-fim-ano-letivo.html", "w").write(src)
print(len(src) / 1e6, "MB")
