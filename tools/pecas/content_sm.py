# Semana 16 a 22/11/2026 — "Saúde mental do homem"
from content import S, P, CR, SAGE, TEAL_D, OCRE, ROSE, MIST, BEGE
C = "/home/claude/kncasadeintegracao.github.io/fotos/"

# paletas extras da semana: verdes claros com destaque escuro, azul-ardósia e areia
VERDE_CL = dict(bg="#D8EBE3", fg="#1F5558", ac="#2E7D74", sub="#3F5F5C")
ARDOSIA  = dict(bg="#DCE4EA", fg="#23384A", ac="#518E91", sub="#3E5163")
AREIA    = dict(bg="#EFE6D8", fg="#1F5558", ac="#9A7432", sub="#5B4632")
VERDE_M  = dict(bg="#B9D8CB", fg="#163F42", ac="#1F5558", sub="#24564E")

ITEMS = ["Psicoterapia de adultos", "Avaliação psicológica e neuropsicológica", "Orientação profissional e transição de carreira", "Grupos presenciais e online"]
pieces = []
# SEGUNDA 16/11
pieces += [
 dict(id="seg_post", size="feed", tpl="framed", pal=VERDE_CL, photo=P+"4100670.jpg", pos="50% 45%",
      k="Tema da semana", t="Saúde mental <i>do homem</i>",
      s="Força também é conseguir dizer “não estou bem”. Nesta semana, vamos falar do que muitos homens aprenderam a calar.",
      cta="Leia a reflexão no site →"),
 dict(id="seg_story", size="story", tpl="storypost", pal=VERDE_CL, photo=P+"4100670.jpg",
      k="Post novo no feed", t="Saúde mental <i>do homem</i>", cta="Ver o post"),
]
# TERÇA 17/11
pieces += [
 dict(id="ter_c01", size="feed", tpl="framed", pal=ARDOSIA, photo=P+"3771115.jpg", pos="50% 40%", page="1/7",
      k="Saúde mental do homem", t="Nem todo sofrimento <i>parece tristeza</i>",
      s="5 sinais que muitos homens não reconhecem como pedido de ajuda.", cta="Arraste →"),
 dict(id="ter_c02", size="feed", tpl="text", pal=VERDE_CL, page="2/7", num="1",
      k="Irritação constante", t="Pavio curto também pode ser cansaço emocional.",
      s="Explosões por pouco, impaciência com quem está perto e dificuldade de relaxar costumam esconder algo que ainda não encontrou palavras."),
 dict(id="ter_c03", size="feed", tpl="anim_seda", pal=TEAL_D, dur=6, page="3/7", num="2",
      k="Trabalho sem fim", t="Ocupar o tempo todo para não pensar.",
      s="Quando o trabalho vira o único lugar seguro, vale perguntar do que ele está protegendo."),
 dict(id="ter_c04", size="feed", tpl="framed", pal=AREIA, photo=P+"5699431.jpg", pos="50% 45%", page="4/7", num="3",
      k="O corpo avisa", t="Insônia, dor de cabeça, aperto no peito.",
      s="Sintomas físicos sem explicação médica também merecem escuta. Muitas vezes, o corpo fala primeiro."),
 dict(id="ter_c05", size="feed", tpl="text", pal=ARDOSIA, page="5/7", num="4",
      k="Mais álcool, menos conversa", t="Quando a bebida vira a única pausa.",
      s="Beber para dormir, para relaxar ou para conseguir falar é sinal de que algo precisa de cuidado."),
 dict(id="ter_c06", size="feed", tpl="text", pal=VERDE_M, page="6/7", num="5",
      k="Isolamento", t="Sumir dos amigos e das conversas.",
      s="Recusar convites, responder com monossílabos e querer ficar sozinho por muito tempo pode ser mais do que cansaço."),
 dict(id="ter_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-7.jpg", page="7/7",
      t="A KN Casa de Integração® cuida de homens em todas as fases da vida", items=ITEMS,
      s="Presencialmente na Mooca/SP e online."),
 dict(id="ter_story", size="story", tpl="storypost", pal=ARDOSIA, photo=P+"3771115.jpg",
      k="Post novo no feed", t="Nem todo sofrimento <i>parece tristeza</i>", cta="Ver o post"),
]
# QUARTA 18/11 (Reels)
REELS_SCENES = [
 (0, 4.2, "photo", P+"3483965r.jpg", "<div class='k' style='color:#D9B86E'>Saúde mental do homem</div><div class='t' style='font-size:100px'>Por que tantos homens só pedem ajuda <i>quando já não aguentam mais?</i></div>"),
 (4.2, 8.4, "seda", None, "<div class='t' style='font-size:92px'>Muitos aprenderam cedo que sentir era <i>sinal de fraqueza.</i></div><div class='s' style='font-size:40px;color:#D7E6E3'>E cresceram resolvendo tudo sozinhos.</div>"),
 (8.4, 12.8, "photo", P+"6963019.jpg", "<div class='k' style='color:#D9B86E'>Então o sofrimento aparece de outro jeito</div><div class='lst'><div>Irritação por pouco</div><div>Trabalho sem pausa</div><div>Álcool para relaxar</div><div>Silêncio e isolamento</div></div>"),
 (12.8, 17.2, "seda", None, "<div class='t' style='font-size:92px'>Pedir ajuda não é desistir.</div><div class='t' style='font-size:92px;color:#D9B86E'><i>É começar a cuidar.</i></div>"),
 (17.2, 20.4, "photo", P+"5699479r.jpg", "<div class='k' style='color:#D9B86E'>A terapia é um lugar para</div><div class='lst'><div>Pensar sem pressa</div><div>Dar nome ao que pesa</div><div>Ser escutado sem julgamento</div></div>"),
 (20.4, 23.5, "end", C+"casa-3.jpg", "<div class='t' style='font-size:80px'>Psicoterapia de adultos <i>com escuta, ciência e afeto</i></div><div style=\"width:100%;height:520px;border-radius:30px;background:url('file://__PH__') 50% 50%/cover;box-shadow:0 30px 60px rgba(0,0,0,.3)\"></div><div class='s' style='font-size:36px;color:#D7E6E3'>KN Casa de Integração® · Mooca/SP e online<br><b style='color:#D9B86E'>Leia mais no site · link na bio</b></div>"),
]
pieces += [
 dict(id="qua_reels_capa", size="story", tpl="fullphoto", pal=TEAL_D, photo=P+"3483965r.jpg", pos="50% 50%",
      t="Por que tantos homens só pedem ajuda <i>quando já não aguentam mais?</i>", s="Assista até o fim."),
 dict(id="qua_reels", size="story", tpl="anim_reels", pal=TEAL_D, dur=23.5),
 dict(id="qua_story", size="story", tpl="storypost", pal=MIST, photo=P+"3483965.jpg",
      k="Reels novo", t="Quando o homem <i>só pede ajuda no limite</i>", cta="Assistir"),
]
# QUINTA 19/11 (carrossel fixo de quinta)
pieces += [
 dict(id="qui_c01", size="feed", tpl="framed", pal=AREIA, photo=P+"5700155c.jpg", pos="40% 40%", page="1/7",
      k="Frases que pesam", t="O que <i>já pode se aposentar</i>",
      s="Frases que muitos homens ouviram desde a infância, e o que dizer no lugar delas.", cta="Arraste →"),
 dict(id="qui_c02", size="feed", tpl="text", pal=VERDE_CL, page="2/7", num="1",
      k="Em vez de “homem não chora”", t="Pode chorar. Eu fico aqui com você.",
      s="Chorar não diminui ninguém. É uma das formas que o corpo encontra de dar passagem ao que dói."),
 dict(id="qui_c03", size="feed", tpl="text", pal=BEGE, page="3/7", num="2",
      k="Em vez de “engole o choro”", t="O que aconteceu?",
      s="Uma pergunta simples abre a conversa que a ordem fecha."),
 dict(id="qui_c04", size="feed", tpl="framed", pal=MIST, photo=P+"5711240.jpg", pos="50% 50%", page="4/7", num="3",
      k="Em vez de “seja homem”", t="Seja você, do seu jeito.",
      s="Há muitas maneiras de ser homem, e nenhuma delas exige silêncio sobre o que se sente."),
 dict(id="qui_c05", size="feed", tpl="anim_seda", pal=TEAL_D, dur=6, page="5/7", num="4",
      k="Em vez de “isso é frescura”", t="Parece que está pesado para você.",
      s="Nomear o que o outro sente, sem julgamento, mostra que ele foi visto."),
 dict(id="qui_c06", size="feed", tpl="text", pal=VERDE_M, page="6/7", num="5",
      k="Em vez de “aguenta firme”", t="Você não precisa dar conta sozinho.",
      s="Pedir ajuda é um gesto de responsabilidade consigo e com quem ele ama."),
 dict(id="qui_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-4.jpg", page="7/7",
      t="A KN Casa de Integração® cuida de homens em todas as fases da vida", items=ITEMS,
      s="Presencialmente na Mooca/SP e online."),
 dict(id="qui_story", size="story", tpl="storypost", pal=AREIA, photo=P+"5711240.jpg",
      k="Post novo no feed", t="Frases que <i>já podem se aposentar</i>", cta="Ver o post"),
]
# SEXTA 20/11
pieces += [
 dict(id="sex_post", size="feed", tpl="framed", pal=SAGE, photo=P+"4101143.jpg", pos="70% 45%",
      k="Psicoterapia de adultos", t="Terapia também <i>é lugar de homem</i>",
      s="Um espaço sigiloso para pensar o trabalho, as relações, a paternidade e o que anda pesando. Presencial na Mooca/SP e online.",
      cta="Agende pelo link da bio"),
 dict(id="sex_story", size="story", tpl="storypost", pal=SAGE, photo=P+"4101143.jpg",
      k="Psicoterapia de adultos", t="Um lugar para <i>pensar sem pressa</i>", cta="Quero agendar"),
]
# SÁBADO 21/11 (só stories)
pieces += [
 dict(id="sab_story1", size="story", tpl="ask", pal=SAGE, photo=P+"9065292.jpg",
      k="Caixinha de perguntas", t="O que mais dificulta <i>um homem pedir ajuda?</i>",
      s="Responda aqui. Algumas respostas podem aparecer, sem nomes, nos próximos stories."),
 dict(id="sab_story2", size="story", tpl="anim_seda", pal=TEAL_D, dur=6,
      k="Enquete", t="Os homens da sua vida falam sobre o que sentem?",
      s="Vote aqui embaixo ↓<div style='height:430px'></div>"),
 dict(id="sab_story3", size="story", tpl="storypost", pal=VERDE_CL, photo=P+"30172425.jpg",
      k="Reflexão da semana", t="A terceira margem <i>do silêncio</i>", cta="Ler no site"),
]
# DOMINGO 22/11
pieces += [
 dict(id="dom_post", size="feed", tpl="framed", pal=MIST, photo=P+"30172425.jpg", pos="50% 50%",
      k="Reflexão da semana", t="Calar <i>não é o mesmo que estar bem.</i>",
      s="Ninguém precisa morar no meio do rio. Há outras margens possíveis, e a escuta pode ser uma delas.",
      cta="Leia mais no site →"),
 dict(id="dom_story", size="story", tpl="storypost", pal=MIST, photo=P+"30172425.jpg",
      k="Post novo no feed", t="Um convite <i>para este domingo</i>", cta="Ver o post"),
]
