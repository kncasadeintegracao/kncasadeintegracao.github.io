# Quadro de aprovação — semana 23 a 29/11/2026 (comprar para preencher), na grade de 20/11/2026
import os, json, html as H
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "assemble_c2_top.py")).read())

PX = lambda id, autor: f'Pexels, foto de {autor}, <a href="https://www.pexels.com/photo/{id}/" target="_blank" rel="noopener">pexels.com/photo/{id}</a>'
EU = lambda o_que: f"criada pelo Claude ({o_que})"
KN = lambda o_que: f"foto da própria KN ({o_que})"

TAG_SEM = "#consumo #ansiedade #saudemental #psicologia #kncasadeintegracao"

CAP_SEG = cap("Comprar para preencher. Arraste para ver.\n\nA compra traz alívio, mas, muitas vezes, por poucos minutos. Depois o vazio volta, às vezes acompanhado de culpa. Nesta semana da Black Friday, quero conversar sobre o que pode estar por trás do clique: cansaço, solidão, tédio ou uma tristeza que ainda não tem nome.\n\nGostar de comprar faz parte da vida. O sinal de alerta aparece quando a compra vira o único jeito de lidar com o que dói.\n\nE você: o que costuma sentir logo antes de comprar algo que não estava nos planos? Conte nos comentários.",
              "#consumo #blackfriday #ansiedade #saudemental #psicologia #kncasadeintegracao")
CAP_TER = cap("5 sinais de que a compra está ocupando o lugar de outra coisa. Arraste e veja.\n\n1. Você compra para aliviar um dia ruim.\n2. Esconde as compras ou o valor delas.\n3. Sente culpa logo depois e promete que não vai repetir.\n4. As parcelas já pesam no fim do mês.\n5. Os pacotes chegam e ficam fechados.\n\nSe você se reconheceu em algum deles, olhe para isso com carinho e sem vergonha. Vale prestar atenção ao que você está sentindo.\n\nSalve este post e mande para quem precisa ler isso hoje.",
              "#consumo #comprascompulsivas #ansiedade #saudemental #autocuidado #kncasadeintegracao")
CAP_QUA = cap("Comprei, e dez minutos depois o vazio voltou.\n\nA compra acalma por um instante, mas o que doía continua lá. Às vezes o que falta é descanso, companhia, uma conversa sem pressa ou um sentido para os dias. E nenhum carrinho dá conta disso.\n\nAntes de comprar, vale perguntar: eu preciso disso? Eu já queria isso ontem? O que estou sentindo agora?\n\nA reflexão da semana, \"Ou isto ou aquilo\", com Bauman, Melanie Klein e Cecília Meireles, está no site (link na bio).\n\nQual dessas perguntas é a mais difícil para você? Responda aqui embaixo.",
              "#blackfriday #consumo #vazio #psicanalise #saudemental #kncasadeintegracao")
CAP_QUI = cap("Quando alguém que você ama compra para preencher, a primeira vontade é abrir a fatura na mesa e cobrar. Quase sempre isso afasta.\n\nO que costuma ajudar:\n1. Não contar as caixas nem expor a fatura.\n2. Começar pela pessoa: \"Tenho te visto cansada. Como você está?\"\n3. Escutar com curiosidade: o que a compra resolveu naquele dia?\n4. Combinar juntos um limite para o mês.\n5. Quando há dívidas, segredo e culpa que se repete, procurar ajuda profissional.\n\nNa KN, além da psicoterapia para crianças, adolescentes e adultos, atendemos famílias e fazemos orientação a pais.\n\nMande este post para quem convive com alguém assim. E conte: qual dessas atitudes é a mais difícil na sua casa?",
              "#consumo #familia #ansiedade #saudemental #psicologia #kncasadeintegracao")
CAP_VID = cap("Se você já abriu a fatura e não reconheceu metade das compras, este vídeo é para você.\n\nNa semana da Black Friday, quero falar de um tipo de compra que tem pouco a ver com o produto: a compra que tenta acalmar um dia difícil, uma solidão, um cansaço. O alívio vem rápido e vai embora mais rápido ainda, porque o que estava doendo não estava na loja.\n\nNa KN Casa de Integração®, a psicoterapia ajuda a dar nome ao que falta, com escuta e sem julgamento, presencialmente na Mooca/SP ou online.\n\nMande este vídeo para alguém que precisa ouvir isso hoje.",
              "#consumo #blackfriday #ansiedade #psicoterapia #saudemental #kncasadeintegracao")
CAP_RES = cap("Ou isto ou aquilo.\n\nCecília Meireles escreveu, para crianças, um poema sobre não poder ter tudo ao mesmo tempo. Melanie Klein chamou de voracidade a fome que nada sacia: um querer que vai além do que precisamos e do que o outro pode oferecer.\n\nDesejar faz parte de estar vivo. Escolher também é abrir mão, e é nesse abrir mão que o desejo ganha forma. A reflexão completa está no site (link na bio).\n\nO que você escolheu deixar de lado nesta semana para cuidar de si? Conte para mim.",
              "#reflexao #psicanalise #ceciliameireles #desejo #saudemental #kncasadeintegracao")
CAP_SEX = cap("Hoje é Black Friday. Arraste e veja 4 perguntas para fazer antes de comprar.\n\n1. Eu já queria isso antes da promoção?\n2. Cabe no meu mês, com folga?\n3. O que eu estou sentindo agora?\n4. Daqui a um mês, eu vou usar?\n\nAproveitar um desconto é ótimo. Comprar no impulso para aliviar um dia difícil costuma sair caro, no bolso e no coração. No site, o texto \"Black Friday com calma\" (link na bio).\n\nSalve e mande para quem vai às compras hoje.",
              "#blackfriday #consumoconsciente #ansiedade #saudemental #psicologia #kncasadeintegracao")
CAP_DOM = cap("O que eu disse nesta semana, no vídeo sobre comprar para preencher:\n\n\"Sabe aquela compra que, no dia seguinte, você nem lembra por que fez?\"\n\n\"O alívio dura pouco, porque o que estava doendo não estava na loja.\"\n\n\"Antes de comprar, pare e pergunte: o que eu estou sentindo agora?\"\n\nO vídeo completo está no perfil, e a reflexão da semana, com Melanie Klein e Cecília Meireles, está no site.\n\nQual dessas frases você precisava ouvir? Mande para alguém que também precisa.",
              "#consumo #psicologia #saudemental #autocuidado #reflexao #kncasadeintegracao")

LEG_NOITE = ("Hoje fechei o ano rindo ao lado de mulheres que me inspiram. No fim, é isso que preenche de verdade: gente querida por perto. Apresento quem estava comigo: / Katheryne Solange Muniz Nazer (Kathy, Kat, Kit, Kit Kat ou Kate): advogada (PUC/SP), especialista em Direitos Humanos (USP), exerceu o Direito por 20 anos e encontrou na Psicologia o seu lugar. Psicóloga, neuropsicóloga, psicanalista e supervisora clínica, mestranda em Psicologia Clínica e da Saúde (Universidad Europea del Atlántico) e RT da KN Casa de Integração®. Mãe da Kitty, cão de AAA da KN (adestrada pelo @bangsolucaoparacaes), e dos gatos Pichuquinha e Tuffy, que enfrenta a FeLV com coragem. / Maria da Conceição Muniz Lessi, minha mãe e minha inspiração: educadora física (USP), foi catedrática de voleibol na USP, diretora de escola particular e professora/coordenadora em escolas públicas. Mais de 60 anos dedicados à educação. Mãe excelente (eu que o diga!), avó apaixonada pelas netas Giulia e Helena e pelos netos de quatro patas. Faz um pudim que é patrimônio da família, e o feijão, a lentilha e a farofa dela não têm igual (já estou com fome!). / Rita Sassmannshausen Moretto: médica clínica geral e dermatologista (USP) e parte da equipe da KN Casa de Integração®. Antes de tudo, um olhar clínico atento à saúde: cuida da pessoa inteira, e não só da pele. Foi esse olhar que percebeu, ainda no começo, o câncer de pele do meu pai. Apaixonada pela medicina, pelos filhos Lucas e Paulo e pelos pais. Vegetariana que cozinha como uma carnívora, chama todo mundo para a casa dela: a Rita é uma pessoa de acolher. / Alexsandra Sousa Garcia: psicóloga por vocação, dedicada à psicanálise e aos estudos do desenvolvimento, com Vygotsky entre suas referências. Trabalhou por muitos anos nos CAPS de São Paulo e do ABC e transita com segurança entre a saúde pública e a privada. Hoje é psicóloga escolar em escolas públicas da cidade e atende na KN Casa de Integração®. Ama a família (especialmente o maridão e os sobrinhos) e faz um patê de atum maravilhoso. / E você, com quem quer fechar este ano? Para agendar, fale com a KN pelo link da bio. / © 2026 KN Casa de Integração®. Todos os direitos reservados.").replace(" / ", "\n\n")

APRES = [
 ("Katheryne Solange Muniz Nazer", "Também atende por Kathy, Kat, Kit, Kit Kat e Kate. Advogada (PUC/SP), especialista em Direitos Humanos (USP), exerceu o Direito, sua primeira profissão, por 20 anos e encontrou na Psicologia o seu lugar: é psicóloga, neuropsicóloga, psicanalista e supervisora clínica, especialista em saúde mental, em neuropsicofarmacologia e em riscos psicossociais do trabalho, e mestranda em Psicologia Clínica e da Saúde pela Universidad Europea del Atlántico, na Espanha. Responsável técnica da KN Casa de Integração®. Mãe da Kitty, cão de Atividade Assistida por Animais (AAA) da KN, adestrada e cuidada pelo Bang (@bangsolucaoparacaes) e \"deseducada\" pela mãe bichológica dela. Mãe também dos gatos Pichuquinha, de 14 anos, e Tuffy, de 4, que neste momento enfrenta a FeLV com muita coragem. Ama os seres viventes, gente, bicho e planta, e tem amor por todos."),
 ("Maria da Conceição Muniz Lessi", "Minha mãe e minha inspiração. Educadora física por formação (USP), foi catedrática de voleibol na USP, diretora de escola particular e professora/coordenadora em escolas públicas. Dedicou a vida (mais de 60 anos) à educação e segue apaixonada por gente, especialmente por crianças e adolescentes. Mãe excelente (eu que o diga!), avó apaixonada pelas netas Giulia e Helena e pelos netos de quatro patas, e faz um pudim que é patrimônio da família (ela acha que não cozinha bem, mas os preparos da mamãe não têm igual, sobretudo o feijão, o arroz soltinho, a lentilha, a farofa, as saladas incrementadas, os molhos para as pastas etc. Já estou com fome!)."),
 ("Rita Sassmannshausen Moretto", "Médica clínica geral e dermatologista, formada pela USP, e parte da equipe da KN Casa de Integração®. Tem, antes de tudo, um olhar clínico atento à saúde, que se soma ao cuidado da dermatologia estética: cuida da pessoa inteira, e não só da pele. Foi esse olhar que percebeu, ainda no começo, o câncer de pele do meu pai. Já acompanhou grupos de adolescentes em excursões aos Estados Unidos como médica da equipe. Apaixonada pela medicina, pelos filhos Lucas e Paulo e pelos pais, e ainda cozinha muito bem (vegetariana, cozinha como uma carnívora: tudo o que faz fica perfeito, das massas e dos molhos à carne assada). Não tem preguiça nenhuma de chamar todo mundo para a casa dela: a Rita é uma pessoa de acolher, e a cozinha faz parte do acolher."),
 ("Alexsandra Sousa Garcia", "Psicóloga por vocação, dedicada à psicanálise e aos estudos do desenvolvimento e da construção do conhecimento, com Vygotsky entre suas referências. Antes da Psicologia, foi técnica em farmácia e trabalhou por muitos anos nos CAPS de São Paulo e do ABC, onde depois atuou também como psicóloga. Tem ampla experiência na condução de casos de saúde mental e transita com segurança entre a saúde pública e a privada. Atualmente é psicóloga escolar em várias escolas públicas da cidade, dedicada às crianças no seu mister, e também atende na KN Casa de Integração®. Estuda com gosto, ama a família (especialmente o maridão e os sobrinhos) e o que faz, e é, acima de tudo, dedicada ao humano. (E faz um patê de atum que só ela sabe fazer, que é maravilhoso.)"),
]
NOITE_NOTES = ("<b>Como fica a noite:</b> <b>18h50</b>, story com a foto das quatro e/ou do ingresso (se for o ingresso, cubro totalmente QR code, código de barras e número do pedido). "
  "<b>21h30</b>, carrossel: capa com as quatro, um cartão para cada uma com a foto e a apresentação completa (mesmo destaque para as quatro, na ordem Katheryne, Maria da Conceição, Rita e Alê) e o cartão final da KN, já pronto acima. "
  "O teatro e o espetáculo aparecem só como o lugar aonde vocês foram: sem foto de palco, sem marcar e sem cara de parceria. Monto e publico na nossa conversa assim que as fotos chegarem. Os horários de quinta e sexta seguem a grade normal.<br><br><b>Apresentações completas (cartões 2 a 5):</b>"
  + "".join(f"<br><br><b>{H.escape(n)}</b> — {H.escape(t)}" for n, t in APRES)
  + "<br><br><b>Origem:</b> fotos de vocês; cartão final: " + KN("sala de atendimento") + "; espaço marcado: " + EU("cartão de aviso, não vai ao ar"))

days = [
 dict(chip="Segunda 23/11 · 12h30", h="Carrossel de abertura: comprar para preencher",
  kind="Carrossel com 6 cartões + story às 12h35 · automático. Nesta semana, excepcionalmente, a segunda não tem vídeo.",
  items=[dict(f="seg_c01.jpg", c="1 · foto Pexels"), dict(f="seg_c02.mp4", c="2 · animação"), dict(f="seg_c03.jpg", c="3"),
         dict(f="seg_c04.jpg", c="4 · foto Pexels"), dict(f="seg_c05.jpg", c="5"), dict(f="seg_c06.jpg", c="6 · sala da KN"), dict(f="seg_story.jpg", st=1, c="Story 12h35")],
  cap=CAP_SEG, nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(6214128, "Nataliya Vaitkevich") + "; cartão 4: " + PX(7278919, "MART PRODUCTION") + "; cartão 2: " + EU("linhas fluidas em movimento com o texto") + "; cartões 3 e 5: " + EU("cartões de texto nas cores da KN") + "; cartão 6: " + KN("sala de atendimento") + "."),
 dict(chip="Terça 24/11 · 12h30", h="Carrossel: 5 sinais de que a compra ocupa o lugar de outra coisa",
  kind="Carrossel com 7 cartões, feito para salvar e encaminhar · automático. Neste dia você grava o vídeo de quinta no consultório.",
  items=[dict(f="ter_c01.jpg", c="1 · foto Pexels"), dict(f="ter_c02.jpg", c="2"), dict(f="ter_c03.jpg", c="3"), dict(f="ter_c04.jpg", c="4 · foto Pexels"),
         dict(f="ter_c05.jpg", c="5"), dict(f="ter_c06.mp4", c="6 · animação"), dict(f="ter_c07.jpg", c="7 · sala da KN")],
  cap=CAP_TER, nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1: " + PX(8938731, "Leeloo The First") + "; cartão 4: " + PX(6382484, "Liza Summer") + "; cartões 2, 3 e 5: " + EU("cartões de texto numerados") + "; cartão 6: " + EU("linhas fluidas em movimento") + "; cartão 7: " + KN("recepção") + "."),
 dict(chip="Quarta 25/11 · 19h30", h="Reels: comprei, e dez minutos depois o vazio voltou",
  kind="Reels de 23 segundos + story às 19h35 · automático. A reflexão da semana entra no site às 19h29.",
  items=[dict(f="qua_reels_capa.jpg", st=1, c="Capa do Reels"), dict(f="qua_reels.mp4", st=1, c="Reels"), dict(f="qua_story.jpg", st=1, c="Story 19h35")],
  cap=CAP_QUA, nocr=True,
  notes="<b>Gancho humano:</b> abre com uma situação em primeira pessoa. <b>Origem das imagens:</b> capa, cena 1 e story: " + PX(8939519, "Nataliya Vaitkevich") + "; cena 3: " + PX(6567383, "Tim Douglas") + "; cena 4: " + PX(7278919, "MART PRODUCTION") + "; cenas 2 e 5: " + EU("linhas fluidas em movimento com o texto") + "; cena final: " + KN("recepção") + ". <b>Áudio:</b> instrumental calmo da biblioteca do Instagram."),
 dict(chip="Quarta 25/11 · 18h50 e 21h30", h="Fotos da noite de 25/11 (Alunos em Modo Avião, Teatro Caritas)",
  kind="Story antes da peça e carrossel depois. É a única parte da semana que depende das suas fotos; o resto já está pronto.",
  items=[dict(f="noite_lugar.jpg", c="Espaço marcado: fotos da noite de 25/11"), dict(f="noite_final.jpg", c="Cartão final da KN (pronto)")],
  cap=LEG_NOITE, nocr=True, capt="Legenda aprovada por você (2.174 caracteres)", notes=NOITE_NOTES),
 dict(chip="Quinta 26/11 · 12h30", h="Carrossel: quando alguém que você ama compra para preencher",
  kind="Carrossel com 7 cartões, prático, para salvar e encaminhar · automático",
  items=[dict(f="qui_c01.jpg", c="1 · foto Pexels"), dict(f="qui_c02.jpg", c="2"), dict(f="qui_c03.jpg", c="3"), dict(f="qui_c04.mp4", c="4 · animação"),
         dict(f="qui_c05.jpg", c="5 · foto Pexels"), dict(f="qui_c06.jpg", c="6"), dict(f="qui_c07.jpg", c="7 · fachada da KN")],
  cap=CAP_QUI, nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1: " + PX(6643421, "Alena Darmel") + "; cartão 5: " + PX(6963891, "Mikhail Nilov") + "; cartões 2, 3 e 6: " + EU("cartões de texto numerados") + "; cartão 4: " + EU("linhas fluidas em movimento") + "; cartão 7: " + KN("fachada") + "."),
 dict(chip="Quinta 26/11 · 19h30", h="Vídeo 2 da Dra. Katheryne: comprar para preencher",
  kind="Você grava na terça, 24/11, no consultório, com o roteiro que já está com você. Eu coloco legendas na tela, título no primeiro quadro e marca d'água, corto erros e pausas longas, e sai às 19h30 como Reels, com trecho no story das 19h35 · automático. Se o vídeo não chegar, sai no mesmo horário o carrossel reserva abaixo.",
  items=[dict(f="qui_video_lugar.jpg", st=1, c="Espaço marcado: vídeo da Dra. Katheryne"),
         dict(f="res_c01.jpg", c="Reserva 1 · foto Pexels"), dict(f="res_c02.jpg", c="Reserva 2"), dict(f="res_c03.jpg", c="Reserva 3"), dict(f="res_c04.mp4", c="Reserva 4 · animação"), dict(f="res_c05.jpg", c="Reserva 5 · sala da KN"), dict(f="res_story.jpg", st=1, c="Story reserva 19h35")],
  cap=CAP_VID, nocr=True, capt="Legenda do seu vídeo",
  notes="<b>Legenda do carrossel reserva (só se o vídeo não chegar):</b><br>" + H.escape(CAP_RES).replace("\n", "<br>")
        + "<br><br><b>Origem das imagens da reserva:</b> cartão 1 e story: " + PX(7279060, "MART PRODUCTION") + "; cartões 2 e 3: " + EU("cartões de texto") + "; cartão 4: " + EU("linhas fluidas em movimento") + "; cartão 5: " + KN("sala de atendimento") + "."),
 dict(chip="Sexta 27/11 · 12h30 · Black Friday", h="Carrossel: 4 perguntas antes de comprar",
  kind="Carrossel com 6 cartões + story às 12h35 · automático. O texto \"Black Friday com calma\" entra no site às 12h29.",
  items=[dict(f="sex_c01.jpg", c="1 · foto Pexels"), dict(f="sex_c02.jpg", c="2"), dict(f="sex_c03.jpg", c="3"), dict(f="sex_c04.mp4", c="4 · animação"),
         dict(f="sex_c05.jpg", c="5"), dict(f="sex_c06.jpg", c="6 · recepção da KN"), dict(f="sex_story.jpg", st=1, c="Story 12h35")],
  cap=CAP_SEX, nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story: " + PX(4127629, "Gustavo Fring") + "; cartões 2, 3 e 5: " + EU("cartões de texto numerados") + "; cartão 4: " + EU("linhas fluidas em movimento") + "; cartão 6: " + KN("recepção") + "."),
 dict(chip="Sábado 28/11", h="Dois stories, publicados pelo robô",
  kind="10h30, pergunta da semana em arte; 17h00, lembrete para agendar · automático. Sem caixinha e sem enquete: a pessoa responde por mensagem.",
  items=[dict(f="sab_story1.jpg", st=1, c="10h30 · pergunta da semana"), dict(f="sab_story2.jpg", st=1, c="17h00 · lembrete")],
  notes="<b>Origem das imagens:</b> 10h30: " + PX(6382484, "Liza Summer") + "; 17h00: " + KN("recepção") + "."),
 dict(chip="Domingo 29/11 · 19h30", h="Carrossel: o que a Dra. Katheryne disse nesta semana",
  kind="Carrossel com 5 cartões + story às 19h35 com um trecho de cerca de 20 segundos do seu vídeo · automático. Os cartões 2 a 4 trazem frases do roteiro do vídeo; na quinta, quando o vídeo chegar, troco pelas suas palavras exatas e recorto o trecho do story. Sem vídeo, sai o story reserva mostrado aqui.",
  items=[dict(f="dom_c01.jpg", c="1 · foto Pexels"), dict(f="dom_c02.jpg", c="2"), dict(f="dom_c03.jpg", c="3"), dict(f="dom_c04.mp4", c="4 · animação"),
         dict(f="dom_c05.jpg", c="5 · recepção da KN"), dict(f="dom_story.jpg", st=1, c="Story reserva 19h35")],
  cap=CAP_DOM, nocr=True,
  notes="<b>Origem das imagens:</b> cartão 1 e story reserva: " + PX(6214128, "Nataliya Vaitkevich") + "; cartões 2 e 3: " + EU("cartões com as frases") + "; cartão 4: " + EU("linhas fluidas em movimento") + "; cartão 5: " + KN("recepção") + "."),
]
for d in days:
    if d["chip"].startswith("Quarta 25/11 · 18h50"): continue
    assert len(d.get("cap", "")) <= 2200, (d["chip"], len(d["cap"]))
assert len(LEG_NOITE) <= 2200, len(LEG_NOITE)

A = lambda dt, dd: f"<dt>{dt}</dt><dd>{dd}</dd>"
HEADER = """<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>
    <h1>Comprar para preencher: consumo, ansiedade e vazio</h1>
    <p>Semana de segunda, 23, a domingo, 29 de novembro de 2026, a semana da Black Friday (sexta, 27) e da Cyber Monday (segunda, 30). Tudo sai automaticamente pelo robô depois do seu \"pode publicar\". As suas partes são só duas: gravar o vídeo na terça e mandar as fotos da noite de quarta. Os vídeos tocam aqui na página; arraste cada faixa para o lado para ver o carrossel inteiro.</p>
    <dl class="agenda">""" + "".join([
  A("Seg 23/11 · 12h30", "Carrossel de abertura: comprar para preencher · automático"),
  A("Seg 23/11 · 12h35", "Story do carrossel · automático"),
  A("Seg 23/11 · noite", "Você recebe o roteiro completo do vídeo (tarefa “KN – roteiros dos vídeos da semana”) · automático"),
  A("Ter 24/11 · 12h30", "Carrossel: 5 sinais de que a compra ocupa o lugar de outra coisa · automático"),
  A("Ter 24/11 · consultório", "<b>Gravação do vídeo de quinta · sua parte</b>"),
  A("Qua 25/11 · 18h50", "<b>Story antes da peça, com as suas fotos · sua parte: mandar as fotos</b>"),
  A("Qua 25/11 · 19h29", "Reflexão da semana no site · automático"),
  A("Qua 25/11 · 19h30", "Reels: comprei, e dez minutos depois o vazio voltou · automático"),
  A("Qua 25/11 · 19h35", "Story do Reels · automático"),
  A("Qua 25/11 · 21h30", "<b>Carrossel da noite com as quatro · sua parte: mandar as fotos</b>"),
  A("Qui 26/11 · 12h30", "Carrossel: quando alguém que você ama compra para preencher · automático"),
  A("Qui 26/11 · 19h30", "Seu vídeo como Reels (ou o carrossel reserva) · automático"),
  A("Qui 26/11 · 19h35", "Story com trecho do vídeo · automático"),
  A("Sex 27/11 · 12h29", "Texto “Black Friday com calma” no site · automático"),
  A("Sex 27/11 · 12h30", "Carrossel: 4 perguntas antes de comprar · automático"),
  A("Sex 27/11 · 12h35", "Story do carrossel · automático"),
  A("Sáb 28/11 · 10h30", "Story: pergunta da semana · automático"),
  A("Sáb 28/11 · 17h00", "Story: lembrete para agendar · automático"),
  A("Dom 29/11 · 19h30", "Carrossel: o que a Dra. Katheryne disse nesta semana · automático"),
  A("Dom 29/11 · 19h35", "Story com trecho de cerca de 20 segundos do vídeo · automático"),
  A("Seg 30/11 · 8h37", "Relatório da semana · automático"),
]) + """</dl>
  </header>

  <div class="rule-box"><b>Pendência sua, rápida:</b> o relatório ainda mostra 0 toques em contato. Em Editar perfil → Opções de contato, ative o botão de WhatsApp e ponha “Agende sua avaliação ↓” na primeira linha da bio.</div>
  <div class="rule-box"><b>O que ajustei sozinho a partir do relatório:</b> nenhum post sai sem legenda nem de madrugada; nunca há duas imagens soltas no mesmo dia (só carrosséis); toda legenda termina com uma pergunta ou um convite para encaminhar e com “Para agendar, fale com a KN pelo link da bio.”; tirei os emojis das legendas; e o último cartão dos carrosséis convida a mandar para quem precisa. A grade voltou aos horários combinados em 20/11 (Reels de quarta e seu vídeo às 19h30).</div>
  <div class="rule-box"><b>Autores da semana:</b> na reflexão, Melanie Klein (psicanálise) e Zygmunt Bauman (sociologia), com Cecília Meireles na literatura. Nenhum deles apareceu nas reflexões anteriores do site (conferi também a semana do preconceito). O texto de sexta é só meu, prático, sem citações.</div>"""

src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "page_src.html")).read()
src = src.replace("<title>Semana Fechar o Ano</title>", "<title>Semana Comprar para Preencher</title>")
i = src.index('<div class="eyebrow">KN Casa de Integração® · Programação para aprovação</div>')
j = src.index('<div id="days" class="wrap"></div>')
src = src[:i] + HEADER + "\n\n  " + src[j:]
src = src.replace("A reflexão entra hoje, ligada ao post de abertura. O segundo texto entra na quarta, ligado ao Reels. Cada um aparece no site só depois que o post correspondente for ao ar.",
                  "A reflexão entra na quarta, às 19h29, ligada ao Reels, e a reflexão da semana do preconceito passa para “Reflexões anteriores”. O texto curto entra na sexta, às 12h29, ligado ao carrossel da Black Friday. Cada um aparece no site só quando o post correspondente vai ao ar.")
old_cred = src[src.index('<p class="credits">'):src.index('</p>', src.index('<p class="credits">')) + 4]
src = src.replace(old_cred, '<p class="credits">Fotos de banco: Pexels (licença gratuita), sem marcas nem personagens; autor e link em cada dia. Fotos da própria KN só nos cartões finais. Cartões, telas animadas e linhas fluidas criados pelo Claude. Todos os arquivos finais saem sem metadados. Estas anotações de origem aparecem só neste quadro, nunca nas publicações.</p>')
media = {}
for d in days:
    for it in d["items"]: media[it["f"]] = "midia/" + it["f"]
src = src.replace("__ARTICLES__", ARTS).replace("__MEDIA__", json.dumps(media)).replace("__DAYS__", json.dumps(days, ensure_ascii=False))
os.makedirs(S + "/site_c2", exist_ok=True)
open(S + "/site_c2/index.html", "w").write(src)
print("ok", len(src), {d["chip"]: len(d.get("cap", "")) for d in days})
