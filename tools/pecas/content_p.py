# Semana do preconceito — quarta 18/11 a domingo 22/11/2026
from content import S, P, CR, SAGE, TEAL_D, OCRE, ROSE, MIST, BEGE, LILAS, AMAR, CORAL, MENTA, CEU
C = "/home/claude/kncasadeintegracao.github.io/fotos/"

ITEMS = ["Psicoterapia de crianças, adolescentes e adultos", "Orientação a pais", "Avaliação psicológica e neuropsicológica", "Escuta sem julgamento"]
pieces = []

# QUARTA (Reels 19h30)
REELS_SCENES = [
 (0, 4.2, "photo", P+"4672710.jpg", "<div class='k' style='color:#D9B86E'>Semana do preconceito</div><div class='t' style='font-size:104px'>Quase ninguém se acha <i>preconceituoso.</i></div>"),
 (4.2, 8.4, "seda", None, "<div class='t' style='font-size:90px'>O preconceito costuma chegar <i>disfarçado.</i></div><div class='s' style='font-size:40px;color:#D7E6E3'>De piada, de conselho, de “é só uma opinião”.</div>"),
 (8.4, 12.8, "photo", P+"6150432.jpg", "<div class='k' style='color:#D9B86E'>Onde ele aparece</div><div class='lst'><div>Na piada sobre o sotaque</div><div>No comentário sobre o corpo</div><div>Na desconfiança pela cor da pele</div><div>No “isso não é coisa de menino”</div></div>"),
 (12.8, 17.2, "photo", P+"7216021.jpg", "<div class='k' style='color:#D9B86E'>O que fica em quem ouve</div><div class='lst'><div>Vergonha</div><div>Vontade de se esconder</div><div>Cansaço de se explicar</div><div>A sensação de não pertencer</div></div>"),
 (17.2, 20.4, "seda", None, "<div class='t' style='font-size:92px'>Preconceito se aprende. <i>E o que se aprende pode ser revisto.</i></div>"),
 (20.4, 23.5, "end", C+"casa-6.jpg", "<div class='t' style='font-size:80px'>Um lugar de escuta <i>sem julgamento</i></div><div style=\"width:100%;height:520px;border-radius:30px;background:url('file://__PH__') 50% 50%/cover;box-shadow:0 30px 60px rgba(0,0,0,.3)\"></div><div class='s' style='font-size:36px;color:#D7E6E3'>KN Casa de Integração® · Mooca/SP e online<br><b style='color:#D9B86E'>Leia a reflexão no site · link na bio</b></div>"),
]
pieces += [
 dict(id="qua_reels_capa", size="story", tpl="fullphoto", pal=TEAL_D, photo=P+"4672710.jpg", pos="50% 45%", seal=True,
      k="Semana do preconceito", t="Quase ninguém se acha <i>preconceituoso.</i>", s="Assista até o fim."),
 dict(id="qua_reels", size="story", tpl="anim_reels", pal=TEAL_D, dur=23.5),
 dict(id="qua_story", size="story", tpl="storypost", pal=MIST, photo=P+"4672710.jpg",
      k="Reels novo", t="Preconceito: <i>o que a gente aprende sem perceber</i>", cta="Assistir"),
]
# QUINTA (carrossel 12h30)
pieces += [
 dict(id="qui_c01", size="feed", tpl="framed", pal=ROSE, photo=P+"5318962.jpg", pos="50% 50%", page="1/7",
      k="Preconceito no dia a dia", t="Frases que parecem <i>inofensivas</i>",
      s="5 falas comuns que carregam preconceito, e o que elas fazem com quem ouve.", cta="Arraste →"),
 dict(id="qui_c02", size="feed", tpl="text", pal=BEGE, page="2/7", num="1",
      k="“Você nem parece…”", t="Parece elogio. <i>Não é.</i>",
      s="A frase supõe que o grupo daquela pessoa é inferior e que ela seria uma exceção."),
 dict(id="qui_c03", size="feed", tpl="anim_seda", pal=MIST, dur=6, page="3/7", num="2",
      k="“Isso é coisa de menina”", t="O limite chega antes da escolha.",
      s="Brincadeiras, cores e sentimentos ficam proibidos antes de a criança descobrir do que gosta."),
 dict(id="qui_c04", size="feed", tpl="framed", pal=SAGE, photo=P+"8433480.jpg", pos="50% 40%", page="4/7", num="3",
      k="“Você seria tão bonita se emagrecesse”", t="O corpo vira condição para o afeto.",
      s="E a pessoa aprende a se olhar no espelho com desconfiança."),
 dict(id="qui_c05", size="feed", tpl="text", pal=OCRE, page="5/7", num="4",
      k="“Na sua idade, não dá mais”", t="Ninguém tem prazo <i>para recomeçar.</i>",
      s="O preconceito contra a idade tira das pessoas o direito de aprender, mudar e desejar."),
 dict(id="qui_c06", size="feed", tpl="text", pal=ROSE, page="6/7", num="5",
      k="“Foi só uma brincadeira”", t="Quando só um lado ri, <i>não é brincadeira.</i>",
      s="Quem ouve sente. E, muitas vezes, guarda por anos."),
 dict(id="qui_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-8.jpg", page="7/7",
      t="A KN Casa de Integração® acolhe todas as pessoas, com escuta e respeito", items=ITEMS,
      s="Presencialmente na Mooca/SP e online."),
 dict(id="qui_story", size="story", tpl="storypost", pal=ROSE, photo=P+"5318962.jpg",
      k="Post novo no feed", t="Frases que parecem <i>inofensivas</i>", cta="Ver o post"),
]
# SEXTA 20/11 (Dia Nacional de Zumbi e da Consciência Negra)
pieces += [
 dict(id="sex_post", size="feed", tpl="framed", pal=TEAL_D, photo=P+"12906205.jpg", pos="50% 30%",
      k="20 de novembro · Consciência Negra", t="O racismo <i>também adoece.</i>",
      s="O sofrimento causado pelo racismo é real e merece escuta qualificada, com respeito à história de cada pessoa.",
      cta="Leia o texto no site →"),
 dict(id="sex_story", size="story", tpl="storypost", pal=TEAL_D, photo=P+"12906205.jpg",
      k="Dia Nacional de Zumbi e da Consciência Negra", t="O racismo <i>também adoece</i>", cta="Ler no site"),
]
# SÁBADO (só stories)
pieces += [
 dict(id="sab_story1", size="story", tpl="ask", pal=SAGE, photo=P+"8380089.jpg",
      k="Caixinha de perguntas", t="Que frase você gostaria que <i>as pessoas parassem de dizer?</i>",
      s="Responda aqui. Algumas respostas podem aparecer, sem nomes, nos próximos stories."),
 dict(id="sab_story2", size="story", tpl="anim_seda", pal=MIST, dur=6,
      k="Enquete", t="Você já percebeu <i>um preconceito seu?</i>",
      s="Responda na enquete abaixo. Perceber já é um começo.<br><br><br><br>"),
 dict(id="sab_story3", size="story", tpl="storypost", pal=BEGE, photo=P+"19924416.jpg",
      k="Reflexão da semana", t="O que a gente aprende <i>sem perceber</i>", cta="Ler no site"),
]
# DOMINGO (19h30)
pieces += [
 dict(id="dom_post", size="feed", tpl="framed", pal=BEGE, photo=P+"19924416.jpg", pos="50% 35%",
      k="Reflexão da semana", t="Ninguém nasce <i>com preconceito.</i>",
      s="A gente aprende em casa, na escola, nas piadas. E o que se aprende também pode ser revisto.",
      cta="Leia mais no site →"),
 dict(id="dom_story", size="story", tpl="storypost", pal=BEGE, photo=P+"19924416.jpg",
      k="Post novo no feed", t="Um convite para este domingo", cta="Ver o post"),
]
