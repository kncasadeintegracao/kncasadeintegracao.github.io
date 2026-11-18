import os, re, json, base64
S = os.environ.get("KN_WORK", "/tmp/kn_work")
OUT = S + "/out_p"

SIGN = lambda dia: f"""<div class="sign">
        <div><b>Katheryne Solange Muniz Nazer (KN)</b> · Psicóloga · CRP 06/117.713 · Responsável Técnica · KN Casa de Integração®</div>
        <div>Mooca/SP, {dia} de novembro de 2026</div>
        <div class="slogan">Cuidar de pessoas. Formar profissionais. Transformar realidades.</div>
        <div class="copyr">© 2026 KN Casa de Integração®. Todos os direitos reservados.</div>
      </div>"""

ARTS = f"""
    <article>
      <div class="eyebrow">Reflexão da semana · entra hoje, quarta, às 19h29, ligada ao Reels</div>
      <h2>O que a gente aprende sem perceber</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Nesta semana, quero conversar sobre preconceito. Quase ninguém se reconhece preconceituoso: o preconceito costuma ser sempre do outro, do vizinho, do parente mais velho, de quem pensa diferente. No consultório, porém, escuto com frequência o outro lado dessa história. A criança que deixou de brincar do que gostava porque riram dela. O adolescente que esconde o sotaque. A mulher que não vai à praia há anos por causa de um comentário sobre o corpo. O homem de sessenta anos que desistiu de um curso porque ouviu que, "nessa idade", não dava mais.</p>
      <p>Gordon Allport, psicólogo social norte-americano, publicou em 1954 um dos estudos clássicos sobre o tema. A definição mais curta que ele propôs é também a mais certeira: preconceito é pensar mal dos outros sem fundamento suficiente. Allport mostrou que a mente humana precisa de categorias para organizar o mundo, e que o problema começa quando essas categorias endurecem e deixam de ser revistas diante da pessoa real que está à nossa frente. A generalização vira sentença, e a pessoa desaparece atrás do rótulo.</p>
      <p>Machado de Assis tem um conto que me ajuda a pensar nisso: "O espelho", de 1882. Jacobina, o protagonista, tinha vinte e cinco anos quando foi nomeado alferes da Guarda Nacional. A família e os conhecidos passaram a tratá-lo só pelo posto, e ele mesmo passou a se reconhecer apenas na farda, até o ponto em que, nas palavras do conto, "o alferes eliminou o homem". Sozinho no sítio de uma tia, sem ninguém para olhá-lo, ele vê no espelho uma imagem vaga, desfeita, que só volta a ficar nítida quando ele veste a farda outra vez. Machado escreveu sobre vaidade e papéis sociais, mas o conto também mostra o quanto o olhar dos outros participa da construção de quem somos.</p>
      <p>Se o olhar do outro tem esse poder, o preconceito também tem. Neusa Santos Souza, psiquiatra e psicanalista negra, mostrou em <em>Tornar-se negro</em>, de 1983, o custo psíquico de crescer numa sociedade que oferece um ideal branco como medida de valor: muitas pessoas negras passam a se cobrar por um modelo que nunca foi feito para elas. Para a autora, ser negro é tornar-se negro, e esse caminho passa por construir um discurso próprio sobre si, em vez de aceitar o retrato pronto que o racismo oferece.</p>
      <p>Ninguém nasce com preconceito. A criança aprende com o que escuta em casa, na escola, nas piadas da família e nos silêncios diante de uma injustiça. Por isso mesmo, o que se aprende também pode ser revisto. Isso começa quando percebemos as nossas frases automáticas, quando perguntamos antes de concluir e quando deixamos a pessoa real aparecer por trás da categoria. E, quando somos nós que sofremos o preconceito, começa quando reconhecemos que aquele retrato não diz quem somos.</p>
      <p>Na KN Casa de Integração®, cada pessoa é recebida com escuta e respeito pela sua história, sem julgamento. Se você carrega marcas de preconceito, ou se percebeu em si algo que gostaria de rever, a terapia pode ser um lugar para isso, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Allport, G. W. (1954). <em>The nature of prejudice</em>. Cambridge, MA: Addison-Wesley.</p>
        <p>Assis, M. de (1882). O espelho: esboço de uma nova teoria da alma humana. In <em>Papéis avulsos</em>. Rio de Janeiro: Lombaerts. (Publicado originalmente na <em>Gazeta de Notícias</em>, 8 set. 1882)</p>
        <p>Souza, N. S. (2021). <em>Tornar-se negro: ou as vicissitudes da identidade do negro brasileiro em ascensão social</em>. Rio de Janeiro: Zahar. (Obra original de 1983)</p>
      </div>
      {SIGN(18)}
    </article>

    <article>
      <div class="eyebrow">Texto autoral · entra na sexta, 20/11, às 12h29, ligado ao post da Consciência Negra</div>
      <h2>O racismo também adoece</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Hoje, 20 de novembro, é o Dia Nacional de Zumbi e da Consciência Negra, feriado nacional desde a Lei nº 14.759, de 2023. A data lembra a morte de Zumbi dos Palmares, em 1695, e convida o país a olhar para a história e para o presente da população negra. Quero aproveitar o dia para falar de algo que também chega ao consultório: o racismo produz sofrimento psíquico.</p>
      <p>Frantz Fanon, psiquiatra nascido na Martinica, descreveu em <em>Pele negra, máscaras brancas</em>, de 1952, uma cena que nunca esqueci. Na rua, uma criança aponta para ele e o nomeia pela cor, diante da mãe. Naquele instante, Fanon sente que deixou de ser visto como pessoa e passou a ser apenas um corpo fixado pelo olhar do outro. Ele mostrou que essa experiência, repetida ao longo da vida, deixa marcas profundas no modo como alguém se percebe.</p>
      <p>No Brasil, a psicanalista Isildinha Baptista Nogueira retomou essa questão em <em>A cor do inconsciente: significações do corpo negro</em>. Ela mostra que o corpo é atravessado pelos sentidos que a sociedade lhe atribui, e que essas marcas se inscrevem no psiquismo. Na clínica, isso pode aparecer como vergonha do próprio corpo, ansiedade nos lugares em que a pessoa é a única negra, cansaço de precisar provar o tempo todo a própria competência, ou uma tristeza que ainda não encontrou nome.</p>
      <p>Conceição Evaristo chama de escrevivência a escrita que nasce da vida e da memória coletiva do povo negro. No conto que dá título a <em>Olhos d'água</em>, a narradora percebe, um dia, que não se lembra da cor dos olhos da mãe, e volta para casa para reencontrar esse olhar. Gosto dessa imagem porque ela fala de algo essencial em qualquer cuidado: ser olhado de verdade, com atenção à própria história, e não pelo estereótipo.</p>
      <p>Escutar uma pessoa negra no consultório pede esse mesmo cuidado. Não cabe ao terapeuta duvidar da experiência de racismo relatada, nem reduzi-la a uma questão só individual. Cabe acolher o que dói, reconhecer o peso das violências cotidianas e ajudar a pessoa a construir, com as próprias palavras, um lugar mais livre para existir.</p>
      <p>Na KN Casa de Integração®, cada pessoa é recebida com respeito à sua história, com ciência e afeto, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Brasil. (2023). <em>Lei nº 14.759, de 21 de dezembro de 2023</em>. Declara feriado nacional o Dia Nacional de Zumbi e da Consciência Negra. Diário Oficial da União, 22 dez. 2023.</p>
        <p>Evaristo, C. (2014). <em>Olhos d'água</em>. Rio de Janeiro: Pallas; Fundação Biblioteca Nacional.</p>
        <p>Fanon, F. (2020). <em>Pele negra, máscaras brancas</em> (S. Nascimento, Trad., com colaboração de R. Camargo). São Paulo: Ubu. (Obra original de 1952)</p>
        <p>Nogueira, I. B. (2021). <em>A cor do inconsciente: significações do corpo negro</em>. São Paulo: Perspectiva. (Tese original de 1998)</p>
      </div>
      {SIGN(20)}
    </article>"""

days = [
 dict(chip="Quarta 18/11 · 19h30 · hoje", h="Reels: quase ninguém se acha preconceituoso", kind="Reels de 23 segundos (capa + vídeo) + story às 19h35. A reflexão da semana entra no site às 19h29.",
  items=[dict(f="qua_reels_capa.jpg", st=1, c="Capa do Reels"), dict(f="qua_reels.mp4", st=1, c="Reels: fotos Pexels com movimento e telas criadas por mim; final com a sala da KN"), dict(f="qua_story.jpg", st=1, c="Story 19h35")],
  cap="Quase ninguém se acha preconceituoso. 🤍\n\nMas o preconceito costuma chegar disfarçado: de piada, de conselho, de “é só uma opinião”. E quem ouve sente: vergonha, vontade de se esconder, cansaço de se explicar.\n\nPreconceito se aprende. E o que se aprende também pode ser revisto.\n\n📖 A reflexão da semana, \"O que a gente aprende sem perceber\", já está no site (link na bio).\n💚 KN Casa de Integração® · Mooca/SP e online.\n\n#preconceito #saudemental #psicologia #respeito #diversidade #kncasadeintegracao",
  notes="<b>Áudio:</b> instrumental calmo da biblioteca do Instagram, escolhido na hora de publicar."),
 dict(chip="Quinta 19/11 · 12h30", h="Carrossel: frases que parecem inofensivas", kind="Carrossel com 7 cartões + story às 12h35. Seu vídeo, se vier, entra nos stories à tarde.",
  items=[dict(f="qui_c01.jpg", c="1 · foto Pexels"), dict(f="qui_c02.jpg", c="2"), dict(f="qui_c03.mp4", c="3 · animado, criado por mim"), dict(f="qui_c04.jpg", c="4 · foto Pexels"), dict(f="qui_c05.jpg", c="5"), dict(f="qui_c06.jpg", c="6"), dict(f="qui_c07.jpg", c="7 · sala da KN"), dict(f="qui_story.jpg", st=1, c="Story 12h35")],
  cap="Frases que parecem inofensivas. 💬\n👉 Arraste e veja 5 falas do dia a dia que carregam preconceito, e o que elas fazem com quem ouve.\n\nMuitas vezes, quem fala nem percebe. Quem ouve sente e, às vezes, carrega por anos. Perceber as próprias frases automáticas já é uma forma de cuidado.\n\n💚 A KN Casa de Integração® acolhe todas as pessoas, com escuta e respeito, presencialmente na Mooca/SP e online.\n📌 Salve e envie para alguém que precisa ler isto.\n\n#preconceito #etarismo #infancia #autoestima #saudemental #kncasadeintegracao",
  notes="<b>Seu vídeo da semana (opcional):</b> como o lembrete de hoje cedo saiu com o tema do homem, aqui vai o tema novo: \"Uma frase que machuca mais do que parece\". Três tópicos para 60 a 90 segundos: 1) por que a piada e o \"é só brincadeira\" ferem; 2) o que isso provoca em quem ouve, sobretudo crianças e adolescentes; 3) como rever as próprias frases sem culpa paralisante."),
 dict(chip="Sexta 20/11 · 12h30 · feriado", h="Dia Nacional de Zumbi e da Consciência Negra", kind="Post único no feed + story às 12h35. O texto \"O racismo também adoece\" entra no site às 12h29.",
  items=[dict(f="sex_post.jpg", c="Foto Pexels · cartão KN"), dict(f="sex_story.jpg", st=1, c="Story 12h35")],
  cap="Hoje é 20 de novembro, Dia Nacional de Zumbi e da Consciência Negra. ✊🏾\n\nO racismo não fere só no momento em que acontece. Repetido ao longo da vida, ele pode aparecer como vergonha do próprio corpo, ansiedade e cansaço de provar o próprio valor o tempo todo. Esse sofrimento é real e merece escuta qualificada, com respeito à história de cada pessoa.\n\n📖 No site, o texto \"O racismo também adoece\", com Fanon, Isildinha Baptista Nogueira e Conceição Evaristo (link na bio).\n💚 KN Casa de Integração® · Mooca/SP e online.\n\n#consciencianegra #20denovembro #racismo #saudemental #psicologia #kncasadeintegracao"),
 dict(chip="Sábado 21/11", h="Só stories", kind="Três stories, sem post no feed (sugestão: 10h, 14h e 18h)",
  items=[dict(f="sab_story1.jpg", st=1, c="10h · caixinha de perguntas"), dict(f="sab_story2.mp4", st=1, c="14h · enquete animada, criada por mim (o adesivo da enquete entra no espaço de baixo)"), dict(f="sab_story3.jpg", st=1, c="18h · lembrete da reflexão")]),
 dict(chip="Domingo 22/11 · 19h30", h="Trecho da reflexão", kind="Post único no feed + story às 19h35",
  items=[dict(f="dom_post.jpg", c="Foto Pexels"), dict(f="dom_story.jpg", st=1, c="Story 19h35")],
  cap="Ninguém nasce com preconceito. 🤍\n\nA gente aprende em casa, na escola, nas piadas, nos silêncios diante de uma injustiça. E o que se aprende também pode ser revisto: perguntar antes de concluir, deixar a pessoa real aparecer por trás do rótulo.\n\nNesta semana, conversamos sobre preconceito. A reflexão completa, com Allport, Neusa Santos Souza e Machado de Assis, está no site da KN Casa de Integração® (link na bio).\n\nBom domingo para você e para os seus. 🌿\n\n#reflexao #psicanalise #preconceito #respeito #machadodeassis #kncasadeintegracao"),
]

HEADER = """<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>
    <h1>Preconceito: o que a gente aprende sem perceber</h1>
    <p>Semana que começa hoje, quarta, 18 de novembro, e vai até domingo, 22. As peças estão prontas: fotos de bancos gratuitos intercaladas com imagens criadas por mim, algumas com movimento. Os vídeos tocam aqui mesmo na página. Arraste cada faixa para o lado para ver o carrossel inteiro.</p>
    <dl class="agenda">
      <dt>Qua 18/11 · 19h30</dt><dd>Reels: quase ninguém se acha preconceituoso + reflexão no site</dd>
      <dt>Qui 19/11 · 12h30</dt><dd>Carrossel: frases que parecem inofensivas</dd>
      <dt>Sex 20/11 · 12h30</dt><dd>Consciência Negra: o racismo também adoece + texto no site</dd>
      <dt>Sáb 21/11</dt><dd>Só stories: caixinha, enquete e lembrete</dd>
      <dt>Dom 22/11 · 19h30</dt><dd>Trecho da reflexão, com "leia mais no site"</dd>
    </dl>
  </header>

  <div class="rule-box"><b>Autores da semana:</b> Allport, Neusa Santos Souza e Machado de Assis na reflexão; Fanon, Isildinha Baptista Nogueira e Conceição Evaristo no texto de sexta. Nenhum deles foi usado nas reflexões anteriores do site nem na semana do homem, que fica guardada. <b>Sexta é feriado:</b> o post da Consciência Negra entra no horário fixo, 12h30.</div>

  <section class="day">
    <div class="dayhead"><span class="chip">Calendário</span><h2>Como ficam as próximas semanas</h2></div>
    <p class="note">Sem mexer em 9–15/11 (já publicada) nem nas semanas de Natal e Ano-Novo. Escolha uma das duas opções.</p>
    <div class="caption"><div class="eyebrow" style="margin-bottom:8px">Opção 1 · recomendada · pular a semana do homem</div>
      <dl class="agenda" style="margin-top:0">
        <dt>18–22/11</dt><dd>Preconceito (esta semana)</dd>
        <dt>23–29/11</dt><dd>Comprar para preencher: consumo, ansiedade e vazio (Black Friday, 27/11)</dd>
        <dt>30/11–6/12</dt><dd>Fechar o ano sem se fechar (já pronta)</dd>
        <dt>7–13/12</dt><dd>Festas de fim de ano, saudade e conflitos de família</dd>
        <dt>14–20/12</dt><dd>Férias das crianças: brincar, tédio e telas</dd>
        <dt>21–27/12</dt><dd>Natal, solidão e presença (sem mudança)</dd>
        <dt>28/12–3/1</dt><dd>Ano-novo sem promessas impossíveis (sem mudança)</dd>
        <dt>Janeiro</dt><dd>Saúde mental do homem (já pronta, guardada)</dd>
      </dl>
      <p class="note" style="margin-top:10px">Mantém o tema do consumo colado na Black Friday, que é quando ele faz mais sentido.</p></div>
    <div class="caption"><div class="eyebrow" style="margin-bottom:8px">Opção 2 · adiar a semana do homem para a próxima</div>
      <dl class="agenda" style="margin-top:0">
        <dt>18–22/11</dt><dd>Preconceito (esta semana)</dd>
        <dt>23–29/11</dt><dd>Saúde mental do homem (já pronta; só ajusto as datas)</dd>
        <dt>30/11–6/12</dt><dd>Fechar o ano sem se fechar (já pronta)</dd>
        <dt>7–13/12</dt><dd>Comprar para preencher (voltado às compras de presentes)</dd>
        <dt>14–20/12</dt><dd>Festas de fim de ano, saudade e conflitos de família</dd>
        <dt>21–27/12</dt><dd>Natal, solidão e presença (sem mudança)</dd>
        <dt>28/12–3/1</dt><dd>Ano-novo sem promessas impossíveis (sem mudança)</dd>
        <dt>4–10/1</dt><dd>Férias das crianças: brincar, tédio e telas</dd>
      </dl></div>
  </section>"""

media = {}
for d in days:
    for it in d["items"]:
        f = it["f"]; mime = "video/mp4" if f.endswith(".mp4") else "image/jpeg"
        media[f] = f"data:{mime};base64," + base64.b64encode(open(f"{OUT}/{f}", "rb").read()).decode()

src = open(os.path.join(os.path.dirname(__file__), "page_src.html")).read()
src = src.replace("<title>Semana Fechar o Ano</title>", "<title>Semana do Preconceito</title>")
i = src.index('<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>')
j = src.index('<div id="days" class="wrap"></div>')
src = src[:i] + HEADER + "\n\n  " + src[j:]
src = src.replace("A reflexão entra hoje, ligada ao post de abertura. O segundo texto entra na quarta, ligado ao Reels. Cada um aparece no site só depois que o post correspondente for ao ar.",
                  "A reflexão entra hoje, às 19h29, ligada ao Reels. O segundo texto entra na sexta, às 12h29, ligado ao post da Consciência Negra. Cada um aparece no site só depois que o post correspondente for ao ar.")
old_cred = src[src.index('<p class="credits">'):src.index('</p>', src.index('<p class="credits">')) + 4]
src = src.replace(old_cred, '<p class="credits">Fotos: Pexels (licença gratuita), sem marcas nem personagens, e fotos da própria KN Casa de Integração® só nos cartões finais. Telas animadas (linhas fluidas) criadas por Claude.</p>')
src = src.replace("__ARTICLES__", ARTS).replace("__MEDIA__", json.dumps(media)).replace("__DAYS__", json.dumps(days, ensure_ascii=False))
open(S + "/semana-preconceito.html", "w").write(src)
print(len(src) / 1e6, "MB")
