# Opção B — semana 9 a 15/11/2026: "O fim do ano letivo também mexe com eles"
from content import S, P, C, CR, SAGE, TEAL_D, OCRE, ROSE, MIST, BEGE, LILAS, AMAR, CORAL, MENTA, CEU

ITEMS_KN = ["Psicoterapia de crianças e adolescentes", "Orientação a pais", "Avaliação psicológica e neuropsicológica", "Orientação profissional"]
pieces = []
# SEGUNDA
pieces += [
 dict(id="seg_post", size="feed", tpl="framed", pal=MENTA, photo=P+"30595755.jpg", pos="25% 78%",
      k="Tema da semana", t="O fim do ano letivo <i>também mexe com eles</i>",
      s="Provas, recuperação, despedidas e férias chegando: como acompanhar crianças e adolescentes nesta reta final.",
      cta="Leia a reflexão no site →"),
 dict(id="seg_story", size="story", tpl="storypost", pal=MENTA, photo=P+"30595755.jpg",
      k="Post novo no feed", t="O fim do ano letivo <i>também mexe com eles</i>", cta="Ver o post"),
]
# TERÇA
pieces += [
 dict(id="ter_c01", size="feed", tpl="framed", pal=LILAS, photo=P+"6958551.jpg", pos="50% 40%", page="1/7", dark_box=True,
      k="Reta final", t="Provas, recuperação e cansaço",
      s="5 atitudes que ajudam crianças e adolescentes a fechar o ano", cta="Arraste →"),
 dict(id="ter_c02", size="feed", tpl="text", pal=AMAR, page="2/7", num="1",
      k="Olhe para o processo", t="A nota é só uma parte da história.",
      s="Pergunte como foi o ano, o que foi difícil e do que ele se orgulha."),
 dict(id="ter_c03", size="feed", tpl="anim_seda", pal=CORAL, dur=6, page="3/7", num="2",
      k="Ajude a organizar", t="Apoie sem assumir o lugar dele.",
      s="Um calendário das provas à vista e pausas combinadas ajudam mais do que a cobrança diária."),
 dict(id="ter_c04", size="feed", tpl="framed", pal=MENTA, photo=P+"6957233.jpg", pos="50% 40%", page="4/7", num="3",
      k="Escute antes de aconselhar", t="Às vezes, ele só precisa contar o que sente.",
      s="Conselho dado cedo demais costuma fechar a conversa."),
 dict(id="ter_c05", size="feed", tpl="text", pal=LILAS, page="5/7", num="4",
      k="Recuperação", t="É uma nova chance de aprender.",
      s="O tom da família pesa muito em como a criança ou o adolescente vai viver esse momento."),
 dict(id="ter_c06", size="feed", tpl="text", pal=CEU, page="6/7", num="5",
      k="Cuide do descanso", t="Sono e pausa também fazem parte do estudo.",
      s="Cansaço demais atrapalha a memória e a concentração. Dormir bem na semana de provas ajuda mais do que virar a noite."),
 dict(id="ter_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-6.jpg", page="7/7",
      t="A KN Casa de Integração® acolhe crianças, adolescentes e famílias", items=ITEMS_KN,
      s="Presencialmente na Mooca/SP e online."),
 dict(id="ter_story", size="story", tpl="storypost", pal=LILAS, photo=P+"6958551.jpg",
      k="Post novo no feed", t="Provas, recuperação e cansaço: <i>5 atitudes que ajudam</i>", cta="Ver o post"),
]
# QUARTA (Reels)
REELS_SCENES = [
 (0, 4.2, "photo", P+"7929443.jpg", "<div class='k' style='color:#D9B86E'>Reta final do ano</div><div class='t' style='font-size:104px'>Seu filho anda diferente <i>nestes últimos dias de aula?</i></div>"),
 (4.2, 8.4, "seda", None, "<div class='t' style='font-size:92px'>Nem sempre eles dizem que estão <i>sobrecarregados.</i></div><div class='s' style='font-size:40px;color:#D7E6E3'>Muitas vezes, o corpo e o comportamento falam antes.</div>"),
 (8.4, 12.8, "photo", P+"6002434.jpg", "<div class='k' style='color:#D9B86E'>Nas crianças</div><div class='lst'><div>Dor de barriga ou de cabeça antes da aula</div><div>Choro e birras mais frequentes</div><div>Sono agitado</div><div>Voltar a hábitos de quando era menor</div></div>"),
 (12.8, 17.2, "photo", P+"5430075.jpg", "<div class='k' style='color:#D9B86E'>Nos adolescentes</div><div class='lst'><div>Isolamento no quarto</div><div>Irritação intensa</div><div>Sono desregulado</div><div>Um “tanto faz” para tudo</div></div>"),
 (17.2, 20.4, "seda", None, "<div class='t' style='font-size:92px'>Converse, observe e, se os sinais persistirem, <i>procure ajuda.</i></div>"),
 (20.4, 23.5, "end", C+"casa-6.jpg", "<div class='t' style='font-size:80px'>Avaliação e psicoterapia <i>para crianças e adolescentes</i></div><div style=\"width:100%;height:520px;border-radius:30px;background:url('file://__PH__') 50% 50%/cover;box-shadow:0 30px 60px rgba(0,0,0,.3)\"></div><div class='s' style='font-size:36px;color:#D7E6E3'>KN Casa de Integração® · Mooca/SP e online<br><b style='color:#D9B86E'>Leia mais no site · link na bio</b></div>"),
]
pieces += [
 dict(id="qua_reels_capa", size="story", tpl="fullphoto", pal=TEAL_D, photo=P+"7929443.jpg", pos="78% 50%", seal=True,
      t="Seu filho anda diferente <i>nestes últimos dias de aula?</i>", s="Assista até o fim."),
 dict(id="qua_reels", size="story", tpl="anim_reels", pal=TEAL_D, dur=23.5),
 dict(id="qua_story", size="story", tpl="storypost", pal=CEU, photo=P+"7929443.jpg",
      k="Reels novo", t="Sinais de sobrecarga <i>no fim do ano letivo</i>", cta="Assistir"),
]
# QUINTA (carrossel)
pieces += [
 dict(id="qui_c01", size="feed", tpl="framed", pal=CORAL, photo=P+"8841353.jpg", pos="50% 40%", page="1/7",
      k="Frustração", t="Quando o resultado <i>não veio</i>",
      s="Como ajudar seu filho diante da recuperação, da reprovação ou do resultado que ele esperava.", cta="Arraste →"),
 dict(id="qui_c02", size="feed", tpl="text", pal=ROSE, page="2/7", num="1",
      k="Acolha primeiro", t="Antes de explicar, acolha.",
      s="Uma frase como “eu sei que você queria muito” abre mais espaço do que um sermão."),
 dict(id="qui_c03", size="feed", tpl="text", pal=MENTA, page="3/7", num="2",
      k="Separe a pessoa do resultado", t="Ele não é a nota que tirou.",
      s="Um resultado ruim fala de um momento, e não de quem seu filho é."),
 dict(id="qui_c04", size="feed", tpl="framed", pal=CEU, photo=P+"4260094.jpg", pos="50% 40%", page="4/7", num="3",
      k="Olhem para a frente juntos", t="O que dá para fazer diferente?",
      s="Montar um plano junto devolve a ele a sensação de que pode agir."),
 dict(id="qui_c05", size="feed", tpl="anim_seda", pal=LILAS, dur=6, page="5/7", num="4",
      k="Cuidado com comparações", t="Cada criança tem o seu tempo.",
      s="Comparar com irmãos, primos ou colegas costuma aumentar a vergonha, e não o empenho."),
 dict(id="qui_c06", size="feed", tpl="text", pal=AMAR, page="6/7", num="5",
      k="Errar faz parte", t="Conte de uma vez em que você também não conseguiu.",
      s="Ver um adulto lidar com a frustração ensina mais do que qualquer conselho."),
 dict(id="qui_c07", size="feed", tpl="closing", pal=TEAL_D, photo=C+"casa-8.jpg", page="7/7",
      t="A KN Casa de Integração® acolhe crianças, adolescentes e famílias", items=ITEMS_KN,
      s="Presencialmente na Mooca/SP e online."),
 dict(id="qui_story", size="story", tpl="storypost", pal=CORAL, photo=P+"4260094.jpg",
      k="Post novo no feed", t="Quando o resultado <i>não veio</i>", cta="Ver o post"),
]
# SEXTA (orientação profissional)
pieces += [
 dict(id="sex_post", size="feed", tpl="framed", pal=SAGE, photo=P+"6958563.jpg", pos="50% 35%",
      k="Orientação profissional", t="Terminando o 9º ano <i>ou o ensino médio?</i>",
      s="Escolher o próximo passo pede escuta. Na KN, são de 8 a 12 encontros, com os instrumentos certos para cada caso e devolutiva presencial.",
      cta="Saiba mais pelo link da bio"),
 dict(id="sex_story", size="story", tpl="storypost", pal=SAGE, photo=P+"6958563.jpg",
      k="Orientação profissional", t="O próximo passo <i>com mais clareza</i>", cta="Quero saber mais"),
]
# SÁBADO
pieces += [
 dict(id="sab_story1", size="story", tpl="ask", pal=SAGE, photo=P+"796602.jpg",
      k="Caixinha de perguntas", t="Como foi o ano letivo <i>aí na sua casa?</i>",
      s="Responda aqui. Algumas respostas podem aparecer, sem nomes, nos próximos stories."),
 dict(id="sab_story2", size="story", tpl="anim_anel", pal=OCRE, dur=6, poll=True, opts=("Cansado", "Tranquilo"),
      k="Enquete", t="Seu filho está terminando o ano…", s=""),
 dict(id="sab_story3", size="story", tpl="storypost", pal=MIST, photo=P+"8813566.jpg",
      k="Reflexão da semana", t="Boletim <i>não é retrato</i>", cta="Ler no site"),
]
# DOMINGO
pieces += [
 dict(id="dom_post", size="feed", tpl="framed", pal=AMAR, photo=P+"8813566.jpg", pos="50% 40%",
      k="Reflexão da semana", t="Boletim <i>não é retrato.</i>",
      s="Uma nota fala de um momento. Quem seu filho é cabe em muito mais do que isso.",
      cta="Leia mais no site →"),
 dict(id="dom_story", size="story", tpl="storypost", pal=AMAR, photo=P+"8813566.jpg",
      k="Post novo no feed", t="Um convite para este domingo", cta="Ver o post"),
]
