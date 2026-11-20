# Semana "Comprar para preencher" — segunda 23/11 a domingo 29/11/2026
from content import S, P, CR, SAGE, TEAL_D, OCRE, ROSE, MIST, BEGE
C = "/home/claude/kncasadeintegracao.github.io/fotos/"

ITEMS = ["Psicoterapia de crianças, adolescentes e adultos", "Orientação a pais", "Avaliação psicológica e neuropsicológica", "Escuta sem julgamento"]
pieces = []

# SEGUNDA 23/11 (carrossel 12h30 + story 12h35)
pieces += [
 dict(id="seg_c01", size="feed", tpl="framed", pal=SAGE, photo=P+"6214128.jpg", pos="50% 45%", page="1/6",
      k="Tema da semana", t="Comprar para <i>preencher</i>",
      s="Quando a compra tenta acalmar algo que não está em nenhuma vitrine.", cta="Arraste →"),
 dict(id="seg_c02", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="2/6",
      t="A compra traz alívio. <i>Por alguns minutos.</i>",
      s="Depois o vazio volta, muitas vezes acompanhado de culpa."),
 dict(id="seg_c03", size="feed", tpl="text", pal=OCRE, page="3/6", num="1",
      k="O que pode estar por trás", t="Cansaço, solidão, tédio ou uma tristeza que ainda não tem nome.",
      s="Comprar vira um jeito rápido de sentir outra coisa."),
 dict(id="seg_c04", size="feed", tpl="framed", pal=ROSE, photo=P+"7278919.jpg", pos="50% 40%", page="4/6",
      k="Uma pergunta honesta", t="O que eu queria sentir <i>quando cliquei em comprar?</i>",
      s="A resposta costuma dizer mais sobre você do que o produto."),
 dict(id="seg_c05", size="feed", tpl="text", pal=BEGE, page="5/6",
      k="Sem culpa", t="Gostar de comprar <i>faz parte da vida.</i>",
      s="O sinal de alerta aparece quando a compra vira o único jeito de lidar com o que dói."),
 dict(id="seg_c06", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-3.jpg", page="6/6",
      t="Escuta com ciência e afeto", items=ITEMS, s="Presencialmente na Mooca/SP e online."),
 dict(id="seg_story", size="story", tpl="storypost", pal=SAGE, photo=P+"6214128.jpg",
      k="Tema da semana", t="Comprar para <i>preencher</i>", cta="Ver o post"),
]
# TERÇA 24/11 (carrossel 12h30 + story 12h35)
pieces += [
 dict(id="ter_c01", size="feed", tpl="framed", pal=OCRE, photo=P+"8938731.jpg", pos="50% 45%", page="1/7",
      k="Consumo e emoção", t="5 sinais de que a compra <i>ocupa o lugar de outra coisa</i>",
      s="Para ler, salvar e mandar para quem precisa.", cta="Arraste →"),
 dict(id="ter_c02", size="feed", tpl="text", pal=BEGE, page="2/7", num="1",
      k="Sinal 1", t="Você compra para aliviar um dia ruim.", s="E o alívio dura menos do que a entrega."),
 dict(id="ter_c03", size="feed", tpl="text", pal=SAGE, page="3/7", num="2",
      k="Sinal 2", t="Esconde as compras <i>ou o valor delas.</i>", s="O segredo costuma vir junto com a vergonha."),
 dict(id="ter_c04", size="feed", tpl="framed", pal=ROSE, photo=P+"6382484.jpg", pos="50% 35%", page="4/7", num="3",
      k="Sinal 3", t="Sente culpa logo depois.", s="Promete que não vai repetir e, poucos dias depois, repete."),
 dict(id="ter_c05", size="feed", tpl="text", pal=OCRE, page="5/7", num="4",
      k="Sinal 4", t="As parcelas já pesam <i>no fim do mês.</i>", s="E, mesmo assim, parar parece difícil."),
 dict(id="ter_c06", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="6/7", num="5",
      k="Sinal 5", t="Os pacotes chegam <i>e ficam fechados.</i>", s="O desejo terminou no clique."),
 dict(id="ter_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-8.jpg", page="7/7",
      t="Se você se reconheceu, dá para cuidar disso", items=ITEMS, s="Presencialmente na Mooca/SP e online."),
 dict(id="ter_story", size="story", tpl="storypost", pal=OCRE, photo=P+"8938731.jpg",
      k="Post novo no feed", t="5 sinais para <i>prestar atenção</i>", cta="Ver o post"),
]
# QUARTA 25/11 (Reels 18h00 + story 18h05; reflexão no site 17h59)
REELS_SCENES = [
 (0, 4.2, "photo", P+"8939519.jpg", "<div class='k' style='color:#D9B86E'>A Black Friday está chegando</div><div class='t' style='font-size:104px'>Comprei, e dez minutos depois <i>o vazio voltou.</i></div>"),
 (4.2, 8.4, "seda", None, "<div class='t' style='font-size:92px'>A compra acalma por um instante.</div><div class='t' style='font-size:92px;color:#D9B86E'><i>O que doía continua lá.</i></div>"),
 (8.4, 12.8, "photo", P+"6567383.jpg", "<div class='k' style='color:#D9B86E'>Antes de comprar, pergunte</div><div class='lst'><div>Eu preciso disso?</div><div>Eu já queria isso ontem?</div><div>O que estou sentindo agora?</div></div>"),
 (12.8, 17.2, "photo", P+"7278919.jpg", "<div class='k' style='color:#D9B86E'>Às vezes, o que falta é</div><div class='lst'><div>Descanso</div><div>Companhia</div><div>Uma conversa sem pressa</div><div>Um sentido para os dias</div></div>"),
 (17.2, 20.4, "seda", None, "<div class='t' style='font-size:96px'>Nenhum carrinho <i>dá conta disso.</i></div>"),
 (20.4, 23.5, "end", C+"casa-6.jpg", "<div class='t' style='font-size:80px'>Um lugar para falar <i>do que falta</i></div><div style=\"width:100%;height:520px;border-radius:30px;background:url('file://__PH__') 50% 50%/cover;box-shadow:0 30px 60px rgba(0,0,0,.3)\"></div><div class='s' style='font-size:36px;color:#D7E6E3'>KN Casa de Integração® · Mooca/SP e online<br><b style='color:#D9B86E'>Para agendar, link na bio</b></div>"),
]
pieces += [
 dict(id="qua_reels_capa", size="story", tpl="fullphoto", pal=TEAL_D, photo=P+"8939519.jpg", pos="50% 40%",
      k="A Black Friday está chegando", t="Comprei, e dez minutos depois <i>o vazio voltou.</i>", s="Assista até o fim."),
 dict(id="qua_reels", size="story", tpl="anim_reels", pal=TEAL_D, dur=23.5),
 dict(id="qua_story", size="story", tpl="storypost", pal=MIST, photo=P+"8939519.jpg",
      k="Reels novo", t="O que a gente tenta <i>comprar</i> quando compra demais", cta="Assistir"),
]
# QUINTA 26/11 (vídeo da Dra. Katheryne 12h30 + story 12h35) — marcador; o vídeo chega na quarta
pieces += [
 dict(id="qui_video_lugar", size="story", tpl="text", pal=TEAL_D,
      k="Quinta, 12h30 · Reels", t="Aqui entra <i>o seu vídeo</i>",
      s="Você grava na quarta e me manda. Eu coloco legendas, título e marca d'água e devolvo para você aprovar no mesmo dia."),
]
# SEXTA 27/11 — Black Friday (carrossel 12h30 + story 12h35; texto curto no site 12h29)
pieces += [
 dict(id="sex_c01", size="feed", tpl="framed", pal=SAGE, photo=P+"4127629.jpg", pos="50% 40%", page="1/6",
      k="Hoje é Black Friday", t="4 perguntas <i>antes de comprar</i>",
      s="Para aproveitar o desconto sem cair na armadilha do impulso.", cta="Arraste →"),
 dict(id="sex_c02", size="feed", tpl="text", pal=BEGE, page="2/6", num="1",
      k="Pergunta 1", t="Eu já queria isso <i>antes da promoção?</i>", s="Se o desejo nasceu agora, espere 24 horas."),
 dict(id="sex_c03", size="feed", tpl="text", pal=OCRE, page="3/6", num="2",
      k="Pergunta 2", t="Cabe no meu mês, <i>com folga?</i>", s="Desconto que vira dívida deixa de ser desconto."),
 dict(id="sex_c04", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="4/6", num="3",
      k="Pergunta 3", t="O que eu estou sentindo <i>agora?</i>", s="Cansaço, ansiedade e tédio enchem o carrinho mais depressa."),
 dict(id="sex_c05", size="feed", tpl="text", pal=ROSE, page="5/6", num="4",
      k="Pergunta 4", t="Daqui a um mês, <i>eu vou usar?</i>", s="Imagine o objeto na sua casa, num dia comum, sem a etiqueta vermelha."),
 dict(id="sex_c06", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-8.jpg", page="6/6",
      t="Cuidar do que a gente sente também é economia", items=ITEMS, s="Presencialmente na Mooca/SP e online."),
 dict(id="sex_story", size="story", tpl="storypost", pal=SAGE, photo=P+"4127629.jpg",
      k="Black Friday", t="4 perguntas <i>antes de comprar</i>", cta="Ver o post"),
]
# SÁBADO 28/11 (só stories, pelo robô)
pieces += [
 dict(id="sab_story1", size="story", tpl="ask", pal=SAGE, photo=P+"6382484.jpg",
      k="Pergunta da semana", t="O que você <i>comprou e não precisava?</i>",
      s="Responda por mensagem. Eu leio todas, com carinho e sem julgamento."),
 dict(id="sab_story2", size="story", tpl="storypost", pal=TEAL_D, photo=C+"casa-6.jpg",
      k="KN Casa de Integração®", t="Para agendar, <i>fale com a KN</i>", cta="Link na bio"),
]
# DOMINGO 29/11 (carrossel 19h30 + story 19h35). Reserva: trechos da reflexão.
# Quando o vídeo dela chegar, este carrossel passa a trazer frases do vídeo.
pieces += [
 dict(id="dom_c01", size="feed", tpl="fullphoto", pal=TEAL_D, photo=P+"7279060.jpg", pos="50% 30%", page="1/5",
      k="Reflexão da semana", t="Ou isto <i>ou aquilo</i>",
      s="O que a gente perde quando quer tudo ao mesmo tempo."),
 dict(id="dom_c02", size="feed", tpl="text", pal=BEGE, page="2/5",
      t="Desejar faz parte de <i>estar vivo.</i>",
      s="A dificuldade começa quando tentamos preencher com objetos um espaço que pede outra coisa."),
 dict(id="dom_c03", size="feed", tpl="text", pal=SAGE, page="3/5",
      k="Melanie Klein", t="Chamou de voracidade <i>a fome que nada sacia.</i>",
      s="Um querer que vai além do que precisamos e do que o outro pode oferecer."),
 dict(id="dom_c04", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="4/5",
      t="Escolher também é <i>abrir mão.</i>", s="E é nesse abrir mão que o desejo ganha forma."),
 dict(id="dom_c05", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-3.jpg", page="5/5",
      t="Um lugar para falar do que falta", items=ITEMS, s="Presencialmente na Mooca/SP e online."),
 dict(id="dom_story", size="story", tpl="storypost", pal=BEGE, photo=P+"7279060.jpg",
      k="Post novo no feed", t="Ou isto <i>ou aquilo</i>", cta="Ver o post"),
]
