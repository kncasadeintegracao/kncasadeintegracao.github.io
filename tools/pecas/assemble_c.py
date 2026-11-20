import os, json
S = os.environ.get("KN_WORK", "/tmp/kn_work")
OUT = S + "/out_c"

FOOT = ("Katheryne Solange Muniz Nazer – RT · Psicóloga · CRP 06/117.713\n"
        "KN Casa de Integração® · Mooca/SP e online\n"
        "Cuidar de pessoas. Formar profissionais. Transformar realidades.\n"
        "© 2026 KN Casa de Integração®. Todos os direitos reservados.")
AG = "Para agendar, fale com a KN pelo link da bio."
def cap(body, tags): return body + "\n\n" + AG + "\n\n" + FOOT + "\n\n" + tags

SIGN = lambda dia: f"""<div class="sign">
        <div><b>Katheryne Solange Muniz Nazer (KN)</b> · Psicóloga · CRP 06/117.713 · Responsável Técnica · KN Casa de Integração®</div>
        <div>Mooca/SP, {dia} de novembro de 2026</div>
        <div class="slogan">Cuidar de pessoas. Formar profissionais. Transformar realidades.</div>
        <div class="copyr">© 2026 KN Casa de Integração®. Todos os direitos reservados.</div>
      </div>"""

ARTS = f"""
    <article>
      <div class="eyebrow">Reflexão da semana · entra na quarta, 25/11, às 17h59, ligada ao Reels</div>
      <h2>Ou isto ou aquilo: o que a gente compra quando compra demais</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Na sexta-feira, dia 27, chega a Black Friday, e com ela uma avalanche de anúncios, contagens regressivas e descontos que parecem imperdíveis. Nesta semana, quero conversar sobre um lado da compra que quase nunca aparece nas vitrines. No consultório, escuto com frequência frases como "comprei e no dia seguinte nem lembrava por quê" ou "a caixa ainda está fechada no armário". Quando a gente olha com calma, quase sempre havia alguma coisa acontecendo antes do clique: um dia difícil, uma solidão que apertou à noite, um cansaço que pedia descanso e recebeu um pacote.</p>
      <p>O sociólogo Zygmunt Bauman, em <em>Vida para consumo</em>, observou que a sociedade de consumo depende de uma promessa que nunca se cumpre por inteiro. Se um objeto satisfizesse de verdade, a próxima compra perderia o sentido. Por isso, o desejo precisa ser renovado o tempo todo, e cada novidade já chega com prazo de validade. Por isso, o alívio de comprar costuma durar tão pouco.</p>
      <p>A psicanálise ajuda a entender o que acontece do nosso lado dessa equação. Melanie Klein, em <em>Inveja e gratidão</em>, de 1957, descreveu a voracidade como um desejo impetuoso e insaciável, que vai além do que a pessoa precisa e do que o outro é capaz de oferecer. Klein falava das primeiras relações do bebê com quem cuida dele, mas a ideia ajuda a pensar a vida adulta: quando o vazio é de dentro, nenhum objeto de fora consegue preenchê-lo. A pessoa compra, sente um alívio rápido e, logo depois, a mesma fome volta.</p>
      <p>Cecília Meireles tem um poema para crianças que leio de vez em quando para os adultos: "Ou isto ou aquilo", do livro de mesmo nome, publicado em 1964. Com uma delicadeza enorme, ela mostra uma criança diante de situações em que não dá para ter as duas coisas ao mesmo tempo, e que passa o dia escolhendo, sem saber ainda qual opção é melhor. O poema ensina algo que o consumo tenta nos fazer esquecer: escolher é também abrir mão. E é justamente nesse abrir mão que o desejo ganha contorno e deixa de ser uma fome sem fim.</p>
      <p>Gostar de comprar faz parte da vida, e ninguém precisa sentir culpa por aproveitar uma promoção. O sinal de alerta aparece quando a compra vira o principal jeito de lidar com o que dói, quando as compras passam a ser escondidas, quando as parcelas pesam no mês ou quando a culpa chega todas as vezes. Nesses casos, vale parar e perguntar, com honestidade: o que eu queria sentir quando cliquei em comprar?</p>
      <p>Na KN Casa de Integração®, essa pergunta tem espaço para ser feita com calma, sem julgamento. Se você percebeu que tem comprado para preencher algo, a terapia pode ajudar a dar nome ao que falta, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Bauman, Z. (2008). <em>Vida para consumo: a transformação das pessoas em mercadoria</em> (C. A. Medeiros, Trad.). Rio de Janeiro: Zahar. (Obra original de 2007)</p>
        <p>Klein, M. (1991). Inveja e gratidão. In <em>Inveja e gratidão e outros trabalhos (1946-1963)</em> (Obras completas de Melanie Klein, Vol. 3). Rio de Janeiro: Imago. (Obra original de 1957)</p>
        <p>Meireles, C. (1964). <em>Ou isto ou aquilo</em>. São Paulo: Giroflê.</p>
      </div>
      {SIGN(25)}
    </article>

    <article>
      <div class="eyebrow">Texto autoral · entra na sexta, 27/11, às 12h29, ligado ao carrossel da Black Friday</div>
      <h2>Black Friday com calma</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Hoje é Black Friday, e quase tudo ao nosso redor foi pensado para que a gente decida rápido: o relógio que corre na tela, o aviso de que restam poucas unidades, o desconto que vale só até a meia-noite. A pressa é parte do negócio. Por isso, a melhor proteção é recuperar o tempo de pensar.</p>
      <p>Uma prática simples ajuda muito: antes de fechar o carrinho, faça quatro perguntas. Eu já queria isso antes da promoção? Cabe no meu mês, com folga? O que eu estou sentindo agora? Daqui a um mês, eu vou usar? Se a resposta da primeira for "não", espere vinte e quatro horas. Muitas vezes, o desejo passa junto com a ansiedade que o trouxe.</p>
      <p>A terceira pergunta é a que mais me interessa como psicóloga. Cansaço, tédio, tristeza e ansiedade enchem o carrinho mais depressa. Perceber o que se sente antes de comprar preserva o prazer da compra e evita que ela seja usada para algo que não resolve.</p>
      <p>Se você tem notado que as compras viraram uma forma de aliviar o que dói, procure ajuda. A KN Casa de Integração® atende presencialmente na Mooca/SP e online.</p>
      {SIGN(27)}
    </article>"""

PX = lambda id, autor: f'<a href="https://www.pexels.com/photo/{id}/" target="_blank" rel="noopener">Pexels nº {id}</a>, foto de {autor}'

days = [
 dict(chip="Segunda 23/11 · 12h30", h="Carrossel de abertura: comprar para preencher",
  kind="Carrossel com 6 cartões + story às 12h35. Tudo automático.",
  items=[dict(f="seg_c01.jpg", c="1 · foto Pexels"), dict(f="seg_c02.mp4", c="2 · animação criada por mim"), dict(f="seg_c03.jpg", c="3 · cartão criado por mim"),
         dict(f="seg_c04.jpg", c="4 · foto Pexels"), dict(f="seg_c05.jpg", c="5 · cartão criado por mim"), dict(f="seg_c06.jpg", c="6 · foto da sala da KN"), dict(f="seg_story.jpg", st=1, c="Story 12h35")],
  cap=cap("Comprar para preencher. 🛍️\n👉 Arraste para ver.\n\nA compra traz alívio, mas, muitas vezes, por poucos minutos. Depois o vazio volta, às vezes acompanhado de culpa. Nesta semana da Black Friday, quero conversar sobre o que pode estar por trás do clique: cansaço, solidão, tédio ou uma tristeza que ainda não tem nome.\n\nGostar de comprar faz parte da vida. O sinal de alerta aparece quando a compra vira o único jeito de lidar com o que dói.\n\nE você: o que costuma sentir logo antes de comprar algo que não estava nos planos? Conte nos comentários.",
          "#consumo #blackfriday #ansiedade #saudemental #psicologia #kncasadeintegracao"), nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(6214128, "Nataliya Vaitkevich") + "; cartão 4: " + PX(7278919, "MART PRODUCTION") + "; cartões 2, 3 e 5 criados por mim; cartão 6: foto da própria KN (sala)."),
 dict(chip="Terça 24/11 · 12h30", h="Carrossel: 5 sinais de que a compra ocupa o lugar de outra coisa",
  kind="Carrossel com 7 cartões, feito para salvar e encaminhar, + story às 12h35",
  items=[dict(f="ter_c01.jpg", c="1 · foto Pexels"), dict(f="ter_c02.jpg", c="2"), dict(f="ter_c03.jpg", c="3"), dict(f="ter_c04.jpg", c="4 · foto Pexels"),
         dict(f="ter_c05.jpg", c="5"), dict(f="ter_c06.mp4", c="6 · animação criada por mim"), dict(f="ter_c07.jpg", c="7 · sala da KN"), dict(f="ter_story.jpg", st=1, c="Story 12h35")],
  cap=cap("5 sinais de que a compra está ocupando o lugar de outra coisa. 💭\n👉 Arraste e veja.\n\n1. Você compra para aliviar um dia ruim.\n2. Esconde as compras ou o valor delas.\n3. Sente culpa logo depois e promete que não vai repetir.\n4. As parcelas já pesam no fim do mês.\n5. Os pacotes chegam e ficam fechados.\n\nSe você se reconheceu em algum deles, olhe para isso com carinho e sem vergonha. Vale prestar atenção ao que você está sentindo.\n\n📌 Salve este post e mande para quem precisa ler isto hoje.",
          "#consumo #comprascompulsivas #ansiedade #saudemental #autocuidado #kncasadeintegracao"), nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(8938731, "Leeloo The First") + "; cartão 4: " + PX(6382484, "Liza Summer") + "; cartões 2, 3, 5 e 6 criados por mim; cartão 7: foto da própria KN."),
 dict(chip="Quarta 25/11 · 18h00", h="Reels: comprei, e dez minutos depois o vazio voltou",
  kind="Reels de 23 segundos + story às 18h05. A reflexão da semana entra no site às 17h59.",
  items=[dict(f="qua_reels_capa.jpg", st=1, c="Capa do Reels"), dict(f="qua_reels.mp4", st=1, c="Reels: fotos Pexels com movimento e telas criadas por mim; final com a sala da KN"), dict(f="qua_story.jpg", st=1, c="Story 18h05")],
  cap=cap("Comprei, e dez minutos depois o vazio voltou. 🤍\n\nA compra acalma por um instante, mas o que doía continua lá. Às vezes o que falta é descanso, companhia, uma conversa sem pressa ou um sentido para os dias. E nenhum carrinho dá conta disso.\n\nAntes de comprar, vale perguntar: eu preciso disso? Eu já queria isso ontem? O que estou sentindo agora?\n\n📖 A reflexão da semana, \"Ou isto ou aquilo\", com Bauman, Melanie Klein e Cecília Meireles, está no site (link na bio).\n\nQual dessas perguntas é a mais difícil para você? Responda aqui embaixo.",
          "#blackfriday #consumo #vazio #psicanalise #saudemental #kncasadeintegracao"), nocr=True,
  notes="<b>Origem das imagens:</b> capa, cena 1 e story: " + PX(8939519, "Nataliya Vaitkevich") + "; cena 3: " + PX(6567383, "Tim Douglas") + "; cena 4: " + PX(7278919, "MART PRODUCTION") + "; cenas 2 e 5 (linhas fluidas) criadas por mim; cena final: foto da própria KN. <b>Áudio:</b> instrumental calmo da biblioteca do Instagram."),
 dict(chip="Quinta 26/11 · 12h30", h="Seu vídeo da semana (Reels)",
  kind="Você grava na quarta e me manda. Eu coloco legendas, título e marca d'água e te devolvo no mesmo dia para aprovar. Sai na quinta às 12h30 como Reels, com trecho nos stories às 12h35.",
  items=[dict(f="qui_video_lugar.jpg", st=1, c="Lugar do seu vídeo")],
  notes="<b>Roteiro sugerido (45 a 75 segundos):</b><br>Abertura: \"Sabe aquela compra que, no dia seguinte, você nem lembra por que fez?\"<br>1) A compra pode virar um jeito rápido de aliviar cansaço, solidão ou ansiedade.<br>2) O alívio dura pouco, porque o que estava doendo não estava na loja.<br>3) Antes de comprar, pare e pergunte: o que eu estou sentindo agora?<br>Fechamento: \"E você, já percebeu isso em si? Me conte nos comentários. Se isso faz sentido para você, a KN pode ajudar. Agende pelo link da bio.\"<br><b>Legenda:</b> eu escrevo a partir do que você falar no vídeo e coloco aqui para você aprovar junto."),
 dict(chip="Sexta 27/11 · 12h30 · Black Friday", h="Carrossel: 4 perguntas antes de comprar",
  kind="Carrossel com 6 cartões + story às 12h35. O texto \"Black Friday com calma\" entra no site às 12h29.",
  items=[dict(f="sex_c01.jpg", c="1 · foto Pexels"), dict(f="sex_c02.jpg", c="2"), dict(f="sex_c03.jpg", c="3"), dict(f="sex_c04.mp4", c="4 · animação criada por mim"),
         dict(f="sex_c05.jpg", c="5"), dict(f="sex_c06.jpg", c="6 · sala da KN"), dict(f="sex_story.jpg", st=1, c="Story 12h35")],
  cap=cap("Hoje é Black Friday. 🏷️\n👉 Arraste e veja 4 perguntas para fazer antes de comprar.\n\n1. Eu já queria isso antes da promoção?\n2. Cabe no meu mês, com folga?\n3. O que eu estou sentindo agora?\n4. Daqui a um mês, eu vou usar?\n\nAproveitar um desconto é ótimo. Comprar no impulso para aliviar um dia difícil costuma sair caro, no bolso e no coração.\n\n📖 No site, o texto \"Black Friday com calma\" (link na bio).\n📌 Salve e mande para quem vai às compras hoje.",
          "#blackfriday #consumoconsciente #ansiedade #saudemental #psicologia #kncasadeintegracao"), nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(4127629, "Gustavo Fring") + "; cartões 2 a 5 criados por mim; cartão 6: foto da própria KN."),
 dict(chip="Sábado 28/11", h="Só stories, publicados pelo robô",
  kind="Dois stories automáticos. Sem caixinha e sem enquete: a pessoa responde por mensagem.",
  items=[dict(f="sab_story1.jpg", st=1, c="10h30 · pergunta da semana"), dict(f="sab_story2.jpg", st=1, c="17h00 · lembrete para agendar")],
  notes="<b>Origem das imagens:</b> story das 10h30: " + PX(6382484, "Liza Summer") + "; story das 17h00: foto da própria KN (recepção)."),
 dict(chip="Domingo 29/11 · 19h30", h="Carrossel: ou isto ou aquilo",
  kind="Carrossel com 5 cartões + story às 19h35. Quando o seu vídeo chegar, troco os cartões 2 e 4 por frases ditas por você.",
  items=[dict(f="dom_c01.jpg", c="1 · foto Pexels"), dict(f="dom_c02.jpg", c="2"), dict(f="dom_c03.jpg", c="3"), dict(f="dom_c04.mp4", c="4 · animação criada por mim"),
         dict(f="dom_c05.jpg", c="5 · sala da KN"), dict(f="dom_story.jpg", st=1, c="Story 19h35")],
  cap=cap("Ou isto ou aquilo. 🌿\n\nCecília Meireles escreveu, para crianças, um poema sobre não poder ter tudo ao mesmo tempo. Melanie Klein chamou de voracidade a fome que nada sacia: um querer que vai além do que precisamos e do que o outro pode oferecer.\n\nDesejar faz parte de estar vivo. Escolher também é abrir mão, e é nesse abrir mão que o desejo ganha forma.\n\nNesta semana, conversamos sobre comprar para preencher. A reflexão completa está no site (link na bio).\n\nO que você escolheu deixar de lado esta semana para cuidar de si? Conte para mim.\n\nBom domingo para você e para os seus.",
          "#reflexao #psicanalise #ceciliameireles #desejo #saudemental #kncasadeintegracao"), nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(7279060, "MART PRODUCTION") + "; cartões 2, 3 e 4 criados por mim; cartão 5: foto da própria KN."),
]

HEADER = """<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>
    <h1>Comprar para preencher: consumo, ansiedade e vazio</h1>
    <p>Semana de segunda, 23, a domingo, 29 de novembro de 2026, a semana da Black Friday (sexta, 27). Tudo abaixo sai automaticamente pelo robô depois da sua aprovação. A única tarefa sua é gravar o vídeo na quarta. Os vídeos tocam aqui mesmo na página; arraste cada faixa para o lado para ver o carrossel inteiro.</p>
    <dl class="agenda">
      <dt>Seg 23/11 · 12h30</dt><dd>Carrossel de abertura: comprar para preencher + story 12h35 · automático</dd>
      <dt>Ter 24/11 · 12h30</dt><dd>Carrossel: 5 sinais de que a compra ocupa o lugar de outra coisa + story · automático</dd>
      <dt>Qua 25/11 · 9h55</dt><dd>Você recebe o lembrete e grava o vídeo · <b>sua parte</b></dd>
      <dt>Qua 25/11 · 17h59</dt><dd>Reflexão da semana no site · automático</dd>
      <dt>Qua 25/11 · 18h00</dt><dd>Reels: comprei, e dez minutos depois o vazio voltou + story 18h05 · automático</dd>
      <dt>Qui 26/11 · 12h30</dt><dd>Seu vídeo como Reels + trecho no story 12h35 · automático, depois do seu ok</dd>
      <dt>Sex 27/11 · 12h29</dt><dd>Texto "Black Friday com calma" no site · automático</dd>
      <dt>Sex 27/11 · 12h30</dt><dd>Carrossel: 4 perguntas antes de comprar + story · automático</dd>
      <dt>Sáb 28/11 · 10h30</dt><dd>Story: pergunta da semana, respondida por mensagem · automático</dd>
      <dt>Sáb 28/11 · 17h00</dt><dd>Story: lembrete para agendar · automático</dd>
      <dt>Dom 29/11 · 19h30</dt><dd>Carrossel: ou isto ou aquilo + story 19h35 · automático</dd>
      <dt>Seg 30/11 · 8h37</dt><dd>Relatório da semana chega para você</dd>
    </dl>
  </header>

  <div class="rule-box"><b>O que mudou:</b> seu vídeo passou para <b>quinta às 12h30</b>. Nos dados do perfil, os posts publicados por volta do meio-dia alcançaram em média cerca de 130 contas, e os das 19h, cerca de 45. Pelo mesmo motivo, o Reels de quarta saiu das 19h30 para as 18h, horário que também foi bem nas poucas vezes em que foi usado. O relatório de segunda vai confirmar ou corrigir essas escolhas. Toda legenda termina com uma pergunta para comentar e com o convite para agendar. Não há mais caixinha nem enquete: a interação vai para os comentários e para as mensagens.</div>
  <div class="rule-box"><b>Autores da semana:</b> Zygmunt Bauman e Melanie Klein na reflexão, com Cecília Meireles na literatura. Nenhum deles apareceu nas reflexões anteriores do site. O texto de sexta é só meu, prático, sem citações.</div>"""

src = open(os.path.join(os.path.dirname(__file__), "page_src.html")).read()
src = src.replace("<title>Semana Fechar o Ano</title>", "<title>KN – Semana de 23 a 29/11: comprar para preencher</title>")
i = src.index('<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>')
j = src.index('<div id="days" class="wrap"></div>')
src = src[:i] + HEADER + "\n\n  " + src[j:]
src = src.replace("A reflexão entra hoje, ligada ao post de abertura. O segundo texto entra na quarta, ligado ao Reels. Cada um aparece no site só depois que o post correspondente for ao ar.",
                  "A reflexão entra na quarta, às 17h59, ligada ao Reels. O texto curto entra na sexta, às 12h29, ligado ao carrossel da Black Friday. Cada um aparece no site só depois que o post correspondente for ao ar.")
old_cred = src[src.index('<p class="credits">'):src.index('</p>', src.index('<p class="credits">')) + 4]
src = src.replace(old_cred, '<p class="credits">Fotos: Pexels (licença gratuita, uso livre sem atribuição obrigatória), sem marcas nem personagens; autores e links indicados em cada dia. Fotos da própria KN Casa de Integração® só nos cartões finais. Cartões, telas animadas e linhas fluidas criados por Claude. Estas anotações de origem aparecem só neste quadro, nunca nas publicações.</p>')
media = {}
for d in days:
    for it in d["items"]: media[it["f"]] = "midia/" + it["f"]
src = src.replace("__ARTICLES__", ARTS).replace("__MEDIA__", json.dumps(media)).replace("__DAYS__", json.dumps(days, ensure_ascii=False))
os.makedirs(S + "/site_c", exist_ok=True)
open(S + "/site_c/index.html", "w").write(src)
print("ok", len(src))
