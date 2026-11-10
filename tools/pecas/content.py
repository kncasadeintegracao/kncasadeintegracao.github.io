import os
# Conteúdo da semana 9 a 15/11/2026 — "Fechar o ano sem se fechar"
S = os.environ.get("KN_WORK", "/tmp/kn_work")
P = S + "/fotos/"
C = "/home/claude/kncasadeintegracao/kncasadeintegracao.github.io/fotos/"

# Paletas (fundo, texto, destaque)
SAGE   = dict(bg="#E6EFEA", fg="#1F5558", ac="#B8924A", sub="#3F5F5C")
TEAL_D = dict(bg="#1F5558", fg="#FFFFFF", ac="#D9B86E", sub="#D7E6E3")
OCRE   = dict(bg="#F3E4C7", fg="#4E2D0C", ac="#1F5558", sub="#6B4A2A")
ROSE   = dict(bg="#F4E2DB", fg="#1F5558", ac="#C0756A", sub="#5B4A47")
MIST   = dict(bg="#DDEBEC", fg="#1F5558", ac="#518E91", sub="#3F5F5C")
BEGE   = dict(bg="#EAD8C4", fg="#1F5558", ac="#4E2D0C", sub="#5B4632")
# jovens (adolescência)
LILAS  = dict(bg="#C9B8F0", fg="#2A1F5C", ac="#F06C5B", sub="#3B2F72", box="#2E2466")
AMAR   = dict(bg="#F7C548", fg="#3A2A06", ac="#2E2466", sub="#4A3A12")
CORAL  = dict(bg="#F59E8B", fg="#3A1410", ac="#2E2466", sub="#4A221C")
MENTA  = dict(bg="#BFE8D8", fg="#14463F", ac="#F06C5B", sub="#24564E")
CEU    = dict(bg="#BFDDF5", fg="#1B3A5C", ac="#F06C5B", sub="#2B4A6C")

CR = "© 2026 KN Casa de Integração®. Todos os direitos reservados."

pieces = []  # cada item: dict(id, size, tpl, pal, ...)

# ---------- SEGUNDA ----------
pieces += [
 dict(id="seg_post", size="feed", tpl="framed", pal=SAGE, photo=P+"6263016.jpg", pos="50% 62%",
      k="Tema da semana", t="Fechar o ano <i>sem se fechar</i>",
      s="Novembro chegou e, com ele, a vontade de dar conta de tudo antes de dezembro.",
      cta="Leia a reflexão no site →"),
 dict(id="seg_story", size="story", tpl="anim_anel", pal=TEAL_D, dur=7,
      k="Hoje, às 19h", t="Começa o grupo <i>Final de ano:</i> o que fizemos e o que faremos",
      s="Segundas e quartas · Mooca/SP<br>Venha em dupla", cta="Toque no link"),
]
# ---------- TERÇA (carrossel) ----------
pieces += [
 dict(id="ter_c01", size="feed", tpl="framed", pal=OCRE, photo=P+"7319189.jpg", pos="50% 50%",
      k="Fim de ano", t="Balanço de fim de ano <i>não é tribunal</i>",
      s="Como olhar para 2026 sem se condenar.", cta="Arraste →", page="1/7"),
 dict(id="ter_c02", size="feed", tpl="anim_seda", pal=SAGE, dur=6, page="2/7",
      t="Quem escreveu suas metas em janeiro <i>não sabia</i> o que o ano traria.",
      s="Toda lista nasce num momento da vida. O ano muda a gente no caminho."),
 dict(id="ter_c03", size="feed", tpl="text", pal=OCRE, page="3/7", num="1",
      k="Cuidado com o julgamento", t="Você não tinha, em janeiro, as informações que tem hoje.",
      s="Cobrar-se pelo que não aconteceu, sem olhar para o que aconteceu no caminho, é julgar o passado com olhos do presente."),
 dict(id="ter_c04", size="feed", tpl="fullphoto", pal=TEAL_D, photo=P+"19697889.jpg", pos="50% 35%", page="4/7",
      k="Troque as perguntas", t="O que eu sustentei este ano?<br>O que eu atravessei?<br>O que aprendi sobre mim?"),
 dict(id="ter_c05", size="feed", tpl="text", pal=ROSE, page="5/7", num="2",
      k="Quando a cobrança passa do ponto", t="Cansaço constante, irritação e a sensação de nunca ser suficiente pedem atenção.",
      s="Nesses casos, vale buscar escuta profissional."),
 dict(id="ter_c06", size="feed", tpl="text", pal=MIST, page="6/7",
      k="Um balanço gentil", t="Ele também enxerga o que precisa mudar.",
      s="Só lembra que quem vai mudar é uma pessoa, e não uma planilha."),
 dict(id="ter_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-3.jpg", page="7/7",
      t="Escuta com ciência e afeto",
      items=["Psicoterapia para crianças, adolescentes e adultos","Avaliação psicológica e neuropsicológica","Grupo de fim de ano · segundas e quartas, 19h"],
      s="Presencialmente na Mooca/SP e online."),
 dict(id="ter_story", size="story", tpl="storypost", pal=OCRE, photo=P+"7319189.jpg",
      k="Post novo no feed", t="Balanço de fim de ano <i>não é tribunal</i>", cta="Ver o post"),
]
# ---------- QUARTA (Reels) ----------
pieces += [
 dict(id="qua_reels_capa", size="story", tpl="fullphoto", pal=TEAL_D, photo=P+"8534054.jpg", pos="45% 50%", seal=True,
      t="Se você já acorda cansado em novembro, <i>este vídeo é para você.</i>", s="Assista até o fim."),
 dict(id="qua_reels", size="story", tpl="anim_reels", pal=TEAL_D, dur=22),
 dict(id="qua_story", size="story", tpl="storypost", pal=MIST, photo=P+"8534054.jpg",
      k="Reels novo", t="O cansaço de novembro <i>tem nome</i>", cta="Assistir"),
]
# ---------- QUINTA (carrossel festas de fim de ano) ----------
NOITE = dict(bg="#22474B", fg="#FFFFFF", ac="#D9B86E", sub="#D7E6E3")
pieces += [
 dict(id="qui_c01", size="feed", tpl="framed", pal=NOITE, photo=P+"19421460.jpg", pos="50% 45%", page="1/7",
      k="Dezembro está chegando", t="Nem todo mundo está <i>em clima de festa</i>",
      s="5 cuidados para atravessar as festas de fim de ano do seu jeito.", cta="Arraste →"),
 dict(id="qui_c02", size="feed", tpl="text", pal=ROSE, page="2/7", num="1",
      k="Saudade também senta à mesa", t="A ausência de quem se foi pesa mais nesta época.",
      s="Abrir espaço para a lembrança costuma aliviar mais do que fingir que está tudo bem."),
 dict(id="qui_c03", size="feed", tpl="text", pal=OCRE, page="3/7", num="2",
      k="Escolha seus encontros", t="Você não precisa ir a tudo.",
      s="Escolher os encontros que fazem sentido para você é cuidado, e não desfeita."),
 dict(id="qui_c04", size="feed", tpl="framed", pal=BEGE, photo=P+"5778898.jpg", pos="50% 40%", page="4/7", num="3",
      k="Conversas difíceis", t="A ceia raramente é o melhor momento.",
      s="Assuntos delicados de família rendem melhor com tempo e calma, longe do calor da festa."),
 dict(id="qui_c05", size="feed", tpl="anim_seda", pal=SAGE, dur=6, page="5/7", num="4",
      k="Ajuste as expectativas", t="A festa perfeita das propagandas quase nunca existe.",
      s="A sua pode ser simples e, ainda assim, boa."),
 dict(id="qui_c06", size="feed", tpl="text", pal=MIST, page="6/7", num="5",
      k="Olhe ao redor", t="Alguém perto de você pode estar sozinho.",
      s="Uma mensagem, um convite ou uma ligação fazem diferença. E, se a tristeza pesar demais, procure ajuda profissional."),
 dict(id="qui_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-6.jpg", page="7/7",
      t="A KN Casa de Integração® cuida de você também nas festas",
      items=["Psicoterapia para crianças, adolescentes e adultos","Grupo de fim de ano · segundas e quartas, 19h","Avaliação psicológica e neuropsicológica"],
      s="Presencialmente na Mooca/SP e online."),
 dict(id="qui_story", size="story", tpl="storypost", pal=ROSE, photo=P+"4383361.jpg",
      k="Post novo no feed", t="Nem todo mundo está <i>em clima de festa</i>", cta="Ver o post"),
]
# ---------- SEXTA ----------
pieces += [
 dict(id="sex_post", size="feed", tpl="framed", pal=BEGE, photo=P+"373970.jpg", pos="50% 60%",
      k="Venha em dupla", t="Final de ano: <i>o que fizemos e o que faremos</i>",
      s="Segundas e quartas · 19h · Mooca/SP<br>Encontros presenciais para adultos, até meados de dezembro.",
      cta="Inscrições pelo link da bio"),
 dict(id="sex_story", size="story", tpl="storypost", pal=BEGE, photo=P+"373970.jpg",
      k="Ainda dá tempo", t="Grupo de fim de ano: <i>venha em dupla</i>", cta="Quero saber mais"),
]
# ---------- SÁBADO ----------
pieces += [
 dict(id="sab_story1", size="story", tpl="ask", pal=SAGE, photo=P+"796602.jpg",
      k="Caixinha de perguntas", t="O que você quer <i>deixar</i> em 2026?",
      s="Responda aqui. Algumas respostas podem aparecer, sem nomes, nos próximos stories."),
 dict(id="sab_story2", size="story", tpl="anim_anel", pal=OCRE, dur=6, poll=True,
      k="Enquete", t="Seu fim de ano está mais para…", s=""),
 dict(id="sab_story3", size="story", tpl="storypost", pal=MIST, photo=P+"8353689.jpg",
      k="Reflexão da semana", t="Fechar o ano <i>sem se fechar</i>", cta="Ler no site"),
]
# ---------- DOMINGO ----------
pieces += [
 dict(id="dom_post", size="feed", tpl="fullphoto", pal=TEAL_D, photo=P+"8353689.jpg", pos="50% 50%", seal=True, quote=True,
      k="Reflexão da semana",
      t="Não precisamos sair de dezembro <i>como outra pessoa.</i>",
      s="Precisamos sair reconhecendo quem atravessou este ano, com o que conseguiu e com o que não conseguiu.",
      cta="Leia mais no site →"),
 dict(id="dom_story", size="story", tpl="storypost", pal=TEAL_D, photo=P+"8353689.jpg",
      k="Post novo no feed", t="Um convite para este domingo", cta="Ver o post"),
]
