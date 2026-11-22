# Semana "Comprar para preencher" — segunda 23/11 a domingo 29/11/2026
from content import S, P, CR, SAGE, TEAL_D, OCRE, ROSE, MIST, BEGE
C = "/home/claude/kncasadeintegracao.github.io/fotos/"

ITEMS = ["Psicoterapia de crianças, adolescentes e adultos", "Orientação a pais", "Avaliação psicológica e neuropsicológica", "Escuta sem julgamento"]
SHARE = "<b style='color:#D9B86E'>Mande para quem precisa ler isso hoje.</b>"
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
      t="Escuta com ciência e afeto", items=ITEMS, s="Presencialmente na Mooca/SP e online.", share=SHARE),
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
      t="Se você se reconheceu, dá para cuidar disso", items=ITEMS, s="Presencialmente na Mooca/SP e online.", share=SHARE),
]
# QUARTA 25/11 (reflexão no site 19h29; Reels 19h30 + story 19h35)
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
# QUINTA 26/11 (carrossel 12h30; VÍDEO 2 da Dra. Katheryne 19h30 + story 19h35; reserva pronta)
pieces += [
 dict(id="qui_c01", size="feed", tpl="framed", pal=SAGE, photo=P+"6643421.jpg", pos="50% 45%", page="1/7",
      k="Para quem convive", t="Quando alguém que você ama <i>compra para preencher</i>",
      s="O que costuma ajudar na conversa, e o que costuma afastar.", cta="Arraste →"),
 dict(id="qui_c02", size="feed", tpl="text", pal=ROSE, page="2/7", num="1",
      k="Evite", t="Contar as caixas <i>e jogar a fatura na mesa.</i>",
      s="A vergonha empurra a compra para o escondido, e o ciclo fica mais forte."),
 dict(id="qui_c03", size="feed", tpl="text", pal=BEGE, page="3/7", num="2",
      k="Comece pela pessoa", t="“Tenho te visto cansada. <i>Como você está?</i>”",
      s="Pergunte pelo dia antes de perguntar pelo extrato."),
 dict(id="qui_c04", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="4/7", num="3",
      k="Escute com curiosidade", t="O que a compra <i>resolveu naquele dia?</i>",
      s="A resposta costuma abrir caminho para falar do que dói."),
 dict(id="qui_c05", size="feed", tpl="framed", pal=OCRE, photo=P+"6963891.jpg", pos="50% 40%", page="5/7", num="4",
      k="Combinem juntos", t="Um limite para o mês, <i>decidido a dois.</i>",
      s="Um combinado feito com a pessoa, e não contra ela."),
 dict(id="qui_c06", size="feed", tpl="text", pal=SAGE, page="6/7", num="5",
      k="Quando procurar ajuda", t="Dívidas, segredo e culpa que se repete <i>pedem cuidado profissional.</i>",
      s="A psicoterapia e a orientação à família ajudam a sair do ciclo."),
 dict(id="qui_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-1.jpg", page="7/7",
      t="Cuidar de quem a gente ama também é escutar", items=["Psicoterapia de crianças, adolescentes e adultos", "Atendimento a famílias e orientação a pais", "Avaliação psicológica e neuropsicológica"],
      s="Presencialmente na Mooca/SP e online.", share=SHARE),
 dict(id="qui_video_lugar", size="story", tpl="text", pal=TEAL_D,
      k="Quinta, 19h30 · Reels", t="Vídeo da <i>Dra. Katheryne</i>",
      s="Comprar para preencher. Gravado na terça, 24/11, no consultório. Entra aqui com legendas na tela, título no primeiro quadro e marca d'água."),
 # reserva da quinta 19h30 (sai só se o vídeo não chegar)
 dict(id="res_c01", size="feed", tpl="fullphoto", pal=TEAL_D, photo=P+"7279060.jpg", pos="50% 30%", page="1/5",
      k="Reflexão da semana", t="Ou isto <i>ou aquilo</i>",
      s="O que a gente perde quando quer tudo ao mesmo tempo."),
 dict(id="res_c02", size="feed", tpl="text", pal=BEGE, page="2/5",
      t="Desejar faz parte de <i>estar vivo.</i>",
      s="A dificuldade começa quando tentamos preencher com objetos um espaço que pede outra coisa."),
 dict(id="res_c03", size="feed", tpl="text", pal=SAGE, page="3/5",
      k="Melanie Klein", t="Chamou de voracidade <i>a fome que nada sacia.</i>",
      s="Um querer que vai além do que precisamos e do que o outro pode oferecer."),
 dict(id="res_c04", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="4/5",
      t="Escolher também é <i>abrir mão.</i>", s="E é nesse abrir mão que o desejo ganha forma."),
 dict(id="res_c05", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-3.jpg", page="5/5",
      t="Um lugar para falar do que falta", items=ITEMS, s="Presencialmente na Mooca/SP e online.", share=SHARE),
 dict(id="res_story", size="story", tpl="storypost", pal=BEGE, photo=P+"7279060.jpg",
      k="Post novo no feed", t="Ou isto <i>ou aquilo</i>", cta="Ver o post"),
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
      t="Cuidar do que a gente sente também é economia", items=ITEMS, s="Presencialmente na Mooca/SP e online.", share=SHARE),
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
# DOMINGO 29/11 (carrossel com frases do vídeo 19h30 + story com trecho 19h35)
pieces += [
 dict(id="dom_c01", size="feed", tpl="fullphoto", pal=TEAL_D, photo=P+"6214128.jpg", pos="50% 45%", page="1/5",
      k="Comprar para preencher", t="O que a Dra. Katheryne <i>disse nesta semana</i>",
      s="Três frases para guardar."),
 dict(id="dom_c02", size="feed", tpl="text", pal=BEGE, page="2/5",
      k="Dra. Katheryne", t="“Sabe aquela compra que, no dia seguinte, <i>você nem lembra por que fez?</i>”"),
 dict(id="dom_c03", size="feed", tpl="text", pal=SAGE, page="3/5",
      k="Dra. Katheryne", t="“O alívio dura pouco, porque o que estava doendo <i>não estava na loja.</i>”"),
 dict(id="dom_c04", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="4/5",
      k="Dra. Katheryne", t="“Antes de comprar, pare e pergunte: <i>o que eu estou sentindo agora?</i>”"),
 dict(id="dom_c05", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-6.jpg", page="5/5",
      t="Um lugar para falar do que falta", items=ITEMS, s="Presencialmente na Mooca/SP e online.", share=SHARE),
 dict(id="dom_story", size="story", tpl="storypost", pal=SAGE, photo=P+"6214128.jpg",
      k="Post novo no feed", t="O que eu disse <i>nesta semana</i>", cta="Ver o post"),
]
# QUARTA 25/11 À NOITE (fotos dela; montado na conversa quando as fotos chegarem)
pieces += [
 dict(id="noite_lugar", size="feed", tpl="text", pal=ROSE, k="Quarta, 25/11 · 18h50 e 21h30",
      t="Fotos da noite <i>de 25/11</i>",
      s="Story antes da peça e carrossel depois: capa com as quatro, um cartão para cada uma com a apresentação completa e o cartão final da KN."),
 dict(id="noite_final", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-6.jpg",
      t="Gente querida por perto", items=ITEMS, s="Presencialmente na Mooca/SP e online.",
      share="<b style='color:#D9B86E'>E você, com quem quer fechar este ano?</b>"),
]
