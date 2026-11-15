import os, json, base64
S = os.environ.get("KN_WORK", "/tmp/kn_work")
OUT = S + "/out_sm"
HERE = os.path.dirname(os.path.abspath(__file__))

FOOT = ("Katheryne Solange Muniz Nazer – RT · Psicóloga · Neuropsicóloga · CRP 06/117.713\n"
        "KN Casa de Integração® · Mooca/SP e online\n"
        "Cuidar de pessoas. Formar profissionais. Transformar realidades.\n"
        "© 2026 KN Casa de Integração®. Todos os direitos reservados.")
def cap(body, tags):
    return body.strip() + "\n\n" + FOOT + "\n\n" + tags

SIGN = lambda dia: f"""<div class="sign">
        <div><b>Katheryne Solange Muniz Nazer (KN)</b> · Psicóloga · CRP 06/117.713 · Responsável Técnica · KN Casa de Integração®</div>
        <div>Mooca/SP, {dia} de novembro de 2026</div>
        <div class="slogan">Cuidar de pessoas. Formar profissionais. Transformar realidades.</div>
        <div class="copyr">© 2026 KN Casa de Integração®. Todos os direitos reservados.</div>
      </div>"""

ARTS = f"""
    <article>
      <div class="eyebrow">Reflexão da semana · entra na segunda, com o post de abertura</div>
      <h2>A terceira margem do silêncio</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Nesta semana, quero conversar sobre a saúde mental dos homens. No consultório, é comum que eles cheguem depois de muito tempo de espera: alguém insistiu, o corpo deu sinal, o casamento balançou, o trabalho deixou de fazer sentido. Muitos começam a primeira sessão pedindo desculpas, como se estivessem ocupando um tempo que não lhes pertence.</p>
      <p>Guimarães Rosa conta, em "A terceira margem do rio", a história de um pai que o filho descreve como "homem cumpridor, ordeiro, positivo". Um dia, ele manda fazer uma canoa, entra no rio e não volta mais. Não vai embora, nem fica: passa o resto da vida no meio da água, perto da família e sem nenhuma explicação. O filho deixa comida na margem durante anos, à espera de uma palavra que nunca chega. Sempre que releio esse conto, penso nos homens que estão em casa, cumprem tudo o que se espera deles e, ainda assim, vivem num lugar onde ninguém consegue alcançá-los.</p>
      <p>Bion nos ajuda a pensar o que se passa ali. Para ele, a experiência emocional em estado bruto precisa ser transformada para que possa ser pensada, sonhada e lembrada; ele chamou esse trabalho de função alfa. Quando essa transformação não acontece, o que se sente não vira pensamento: fica no corpo, vira ação, explode em irritação ou se esconde atrás do excesso de trabalho, da bebida e do silêncio. E ninguém aprende a fazer isso sozinho. Desde bebês, precisamos de alguém que receba aquilo que nos inunda e nos devolva de uma forma mais suportável.</p>
      <p>Christian Dunker, por sua vez, mostra que o sofrimento também depende das palavras e das histórias que uma cultura oferece para reconhecê-lo. Se o menino ouve desde cedo que homem não chora, ele não aprende só a esconder as lágrimas. Aprende que certas dores não têm nome. E o que não tem nome dificilmente chega ao médico, ao amigo ou ao psicólogo.</p>
      <p>Por isso, cuidar da saúde mental do homem começa antes da crise. Começa quando a família pergunta de verdade como ele está, quando um amigo aguenta ouvir a resposta, quando o próprio homem se autoriza a dizer "não estou bem" sem sentir que perdeu alguma coisa com isso. Força também é isso.</p>
      <p>Ninguém precisa morar no meio do rio. Há outras margens possíveis, e a terapia pode ser uma delas: um lugar sigiloso, sem julgamento, para transformar em palavra o que até agora só pesava.</p>
      <p>Se você se reconheceu neste texto, ou pensou em alguém que ama, a KN Casa de Integração® está de portas abertas, com psicoterapia de adultos, avaliação psicológica e neuropsicológica e orientação profissional para quem vive uma transição de carreira, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Bion, W. R. (2021). <em>Aprender da experiência</em> (E. H. Sandler, Trad.). São Paulo: Blucher. (Obra original de 1962)</p>
        <p>Dunker, C. I. L. (2015). <em>Mal-estar, sofrimento e sintoma: uma psicopatologia do Brasil entre muros</em>. São Paulo: Boitempo.</p>
        <p>Rosa, J. G. (1962). A terceira margem do rio. In <em>Primeiras estórias</em>. Rio de Janeiro: José Olympio.</p>
      </div>
      {SIGN(16)}
    </article>

    <article>
      <div class="eyebrow">Texto autoral · entra na quarta, ligado ao Reels</div>
      <h2>O que muitos homens não aprenderam a dizer</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Os homens procuram menos os serviços de saúde e, muitas vezes, só chegam quando o quadro já está avançado. O Ministério da Saúde reconheceu isso em 2009, ao instituir a Política Nacional de Atenção Integral à Saúde do Homem, que aponta, entre as barreiras, os estereótipos de gênero, o peso do papel de provedor e a ideia de que "homem não adoece". Na saúde mental, essa distância costuma ser ainda maior.</p>
      <p>O sofrimento masculino raramente se apresenta como tristeza. Ele aparece de lado: na irritação por pouco, no trabalho que não termina nunca, na bebida que virou a única pausa do dia, na insônia, no aperto no peito, no silêncio que vai afastando o homem dos amigos e da própria família.</p>
      <p>Mia Couto, em <em>Antes de nascer o mundo</em>, conta a história de Silvestre Vitalício, um pai que, depois da morte da esposa, leva os filhos para um lugar isolado e proíbe que se fale do passado. O luto que ele não consegue viver vira regra para a casa inteira: ninguém lembra, ninguém pergunta. O narrador, o filho caçula, cresce sem saber direito o que perdeu. Para mim, é um romance sobre como a dor calada de um homem atravessa uma família inteira.</p>
      <p>Ferenczi, num texto de 1928 sobre a elasticidade da técnica psicanalítica, falou do tato do analista como a capacidade de "sentir com" o paciente. Gosto de pensar que essa delicadeza não precisa ficar restrita ao consultório. Um filho, uma companheira, um amigo podem oferecer algo dela: perguntar sem pressa, escutar sem corrigir e aceitar o silêncio do começo sem desistir da conversa.</p>
      <p>Quando os sinais duram semanas, atrapalham o trabalho, o sono e as relações, ou vêm acompanhados de desesperança, é hora de buscar ajuda profissional. Em momentos de sofrimento intenso, o CVV atende 24 horas pelo telefone 188; em emergências, o SAMU atende pelo 192.</p>
      <p>Na KN Casa de Integração®, homens de todas as idades encontram escuta com ciência e afeto, em psicoterapia individual, avaliação e orientação profissional, presencialmente na Mooca/SP ou online.</p>
      <div class="refs">
        <div class="eyebrow" style="margin-bottom:6px">Referências</div>
        <p>Brasil. Ministério da Saúde. (2009). <em>Política Nacional de Atenção Integral à Saúde do Homem: princípios e diretrizes</em> (Portaria nº 1.944, de 27 de agosto de 2009). Brasília: Ministério da Saúde.</p>
        <p>Couto, M. (2016). <em>Antes de nascer o mundo</em>. São Paulo: Companhia das Letras. (Obra original de 2009, publicada em Portugal como <em>Jesusalém</em>)</p>
        <p>Ferenczi, S. (2011). Elasticidade da técnica psicanalítica. In <em>Obras completas: Psicanálise IV</em>. São Paulo: Martins Fontes. (Obra original de 1928)</p>
      </div>
      {SIGN(18)}
    </article>"""

TAGS = "#saudementaldohomem #saudemental #psicologia #psicoterapia #mooca #kncasadeintegracao"
days = [
 dict(chip="Segunda 16/11 · 12h30", h="Post de abertura", kind="Post único no feed às 12h30 e story às 12h35",
  items=[dict(f="seg_post.jpg", c="Foto Pexels · cartão KN"), dict(f="seg_story.jpg", st=1, c="Story 12h35")],
  cap=cap("Força também é conseguir dizer: \"não estou bem\". 💚\n\nMuitos homens aprenderam cedo a resolver tudo sozinhos, a não chorar e a não incomodar ninguém. O resultado costuma aparecer mais tarde, no corpo, no trabalho, nas relações e no silêncio.\n\nNesta semana, a KN Casa de Integração® vai conversar sobre a saúde mental do homem: os sinais que passam despercebidos, as frases que pesam e o lugar da escuta.\n\n📖 A reflexão completa, \"A terceira margem do silêncio\", já está no site: kncasadeintegracao.com (link na bio).", TAGS + " #masculinidade"),
  nocr=1, notes="<b>Site:</b> entra a reflexão \"A terceira margem do silêncio\", com o link deste post. A da semana passada (\"Boletim não é retrato\") e o texto \"Quando o corpo fala antes das palavras\" vão para Reflexões anteriores."),
 dict(chip="Terça 17/11 · 12h30", h="Carrossel: nem todo sofrimento parece tristeza", kind="Carrossel com 7 cartões + story às 12h35",
  items=[dict(f="ter_c01.jpg", c="1 · foto Pexels"), dict(f="ter_c02.jpg", c="2"), dict(f="ter_c03.mp4", c="3 · animado, criado por mim"), dict(f="ter_c04.jpg", c="4 · foto Pexels"), dict(f="ter_c05.jpg", c="5"), dict(f="ter_c06.jpg", c="6"), dict(f="ter_c07.jpg", c="7 · sala da KN"), dict(f="ter_story.jpg", st=1, c="Story 12h35")],
  cap=cap("Nem todo sofrimento parece tristeza. 🌿\n👉 Arraste e veja 5 sinais que muitos homens não reconhecem como pedido de ajuda.\n\nIrritação constante, trabalho sem fim, sintomas no corpo, mais álcool e menos conversa, isolamento. Quando esses sinais se repetem, vale olhar com atenção, sem julgamento.\n\n💚 A KN Casa de Integração® acolhe homens em todas as fases da vida, presencialmente na Mooca/SP e online.\n📌 Salve e envie para alguém que precisa ver isto.", TAGS + " #autocuidado"),
  nocr=1),
 dict(chip="Quarta 18/11 · 19h30", h="Reels: por que eles só pedem ajuda no limite?", kind="Reels de 23 segundos (capa + vídeo) + story às 19h35 + texto autoral no site às 19h29",
  items=[dict(f="qua_reels_capa.jpg", st=1, c="Capa do Reels"), dict(f="qua_reels.mp4", st=1, c="Reels: fotos Pexels com movimento e telas criadas por mim; final com a recepção da KN"), dict(f="qua_story.jpg", st=1, c="Story 19h35")],
  cap=cap("Por que tantos homens só pedem ajuda quando já não aguentam mais? 🤍\n\nMuitos aprenderam cedo que sentir era sinal de fraqueza. Então o sofrimento aparece de outro jeito: irritação, trabalho sem pausa, álcool para relaxar, silêncio.\n\nPedir ajuda não é desistir. É começar a cuidar.\n\n📖 Leia mais no site: \"O que muitos homens não aprenderam a dizer\" (link na bio).\n💚 Psicoterapia de adultos na KN Casa de Integração® · Mooca/SP e online.", TAGS),
  nocr=1, notes="<b>Áudio:</b> instrumental calmo da biblioteca do Instagram, escolhido na hora de publicar. <b>Site:</b> entra o texto \"O que muitos homens não aprenderam a dizer\", com o link do Reels. <b>Lembrete:</b> quarta, 10h, gravar o seu vídeo da semana."),
 dict(chip="Quinta 19/11 · 12h30", h="Carrossel fixo de quinta: frases que já podem se aposentar", kind="Carrossel com 7 cartões + story às 12h35. Seu vídeo, se vier, entra nos stories à tarde.",
  items=[dict(f="qui_c01.jpg", c="1 · foto Pexels"), dict(f="qui_c02.jpg", c="2"), dict(f="qui_c03.jpg", c="3"), dict(f="qui_c04.jpg", c="4 · foto Pexels"), dict(f="qui_c05.mp4", c="5 · animado, criado por mim"), dict(f="qui_c06.jpg", c="6"), dict(f="qui_c07.jpg", c="7 · sala da KN"), dict(f="qui_story.jpg", st=1, c="Story 12h35")],
  cap=cap("\"Homem não chora.\" \"Engole o choro.\" \"Seja homem.\" 💬\n👉 Arraste e veja 5 frases que muitos homens ouviram desde a infância, e o que dizer no lugar delas.\n\nAs palavras que ouvimos cedo ensinam o que pode e o que não pode ser sentido. Trocar uma frase já muda a conversa dentro de casa.\n\n💚 A KN Casa de Integração® acolhe homens, famílias e casais, presencialmente na Mooca/SP e online.\n📌 Salve e compartilhe com quem cria meninos.", TAGS + " #paternidade #educacaoemocional"),
  nocr=1, notes="<b>Seu vídeo da semana (opcional):</b> tema sugerido \"O que eu gostaria que todo homem soubesse sobre terapia\". Grave na quarta e me mande; eu coloco marca d'água, legendas e título."),
 dict(chip="Sexta 20/11 · 12h30", h="Psicoterapia de adultos", kind="Post único no feed + story às 12h35",
  items=[dict(f="sex_post.jpg", c="Foto Pexels"), dict(f="sex_story.jpg", st=1, c="Story 12h35")],
  cap=cap("Terapia também é lugar de homem. 🌿\n\nUm espaço sigiloso, sem julgamento, para pensar o trabalho, as relações, a paternidade, as perdas e o que anda pesando, com tempo e escuta.\n\nNa KN Casa de Integração®, a psicoterapia de adultos acontece presencialmente na Mooca/SP e online, com profissionais de abordagens diferentes, entre elas a ciência psicológica e a leitura psicanalítica.\n\n👉 Agende pelo link da bio.", TAGS + " #terapia"),
  nocr=1, notes="Sexta, 20/11, é feriado nacional (Dia da Consciência Negra). Mantive o horário fixo das 12h30; o post não faz referência à data."),
 dict(chip="Sábado 21/11", h="Só stories", kind="Três stories, sem post no feed (sugestão: 10h, 14h e 18h). Caixinha e enquete vão com as figurinhas do próprio Instagram.",
  items=[dict(f="sab_story1.jpg", st=1, c="10h · caixinha de perguntas"), dict(f="sab_story2.mp4", st=1, c="14h · enquete animada, criada por mim (opções: \"Falam\" / \"Quase nunca\")"), dict(f="sab_story3.jpg", st=1, c="18h · lembrete da reflexão")]),
 dict(chip="Domingo 22/11 · 19h30", h="Trecho da reflexão", kind="Post único no feed às 19h30 + story às 19h35",
  items=[dict(f="dom_post.jpg", c="Foto Pexels"), dict(f="dom_story.jpg", st=1, c="Story 19h35")],
  cap=cap("Calar não é o mesmo que estar bem. 💚\n\nNo conto \"A terceira margem do rio\", de Guimarães Rosa, um pai entra numa canoa e passa a vida no meio da água, perto da família e sem dizer uma palavra. Ninguém precisa morar no meio do rio: há outras margens possíveis, e a escuta pode ser uma delas.\n\nA reflexão completa da semana, com Bion, Christian Dunker e Guimarães Rosa, está no site da KN Casa de Integração® (link na bio).\n\nBom domingo para você e para os seus. 🌿", "#reflexao #psicanalise #saudementaldohomem #guimaraesrosa #kncasadeintegracao"),
  nocr=1),
]

if __name__ == "__main__":
    media = {}
    for d in days:
        for it in d["items"]:
            f = it["f"]; mime = "video/mp4" if f.endswith(".mp4") else "image/jpeg"
            media[f] = f"data:{mime};base64," + base64.b64encode(open(f"{S}/prev/{f}", "rb").read()).decode()
    src = open(HERE + "/page_src.html").read()
    rep = [
     ("<title>Semana Fechar o Ano</title>", "<title>Semana Saúde do Homem</title>"),
     ("<h1>Fechar o ano sem se fechar</h1>", "<h1>Saúde mental do homem</h1>"),
     ("Semana de 9 a 15 de novembro de 2026", "Semana de 16 a 22 de novembro de 2026"),
     ("""      <dt>Seg 9/11 · 12h30</dt><dd>Post de abertura + story animado do grupo (hoje, 19h)</dd>
      <dt>Ter 10/11 · 12h30</dt><dd>Carrossel: balanço de fim de ano sem tribunal</dd>
      <dt>Qua 11/11 · 19h30</dt><dd>Reels: o cansaço de novembro + texto no site</dd>
      <dt>Qui 12/11 · 12h30</dt><dd>Carrossel: nem todo mundo está em clima de festa</dd>
      <dt>Sex 13/11 · 12h30</dt><dd>Convite do grupo: venha em dupla</dd>
      <dt>Sáb 14/11</dt><dd>Só stories: caixinha, enquete e lembrete</dd>
      <dt>Dom 15/11 · 19h30</dt><dd>Trecho da reflexão, com "leia mais no site"</dd>""",
      """      <dt>Seg 16/11 · 12h30</dt><dd>Post de abertura + story 12h35 + reflexão no site</dd>
      <dt>Ter 17/11 · 12h30</dt><dd>Carrossel: nem todo sofrimento parece tristeza</dd>
      <dt>Qua 18/11 · 19h30</dt><dd>Reels: por que eles só pedem ajuda no limite? + texto no site</dd>
      <dt>Qui 19/11 · 12h30</dt><dd>Carrossel: frases que já podem se aposentar</dd>
      <dt>Sex 20/11 · 12h30</dt><dd>Psicoterapia de adultos: terapia também é lugar de homem</dd>
      <dt>Sáb 21/11</dt><dd>Só stories: caixinha, enquete e lembrete</dd>
      <dt>Dom 22/11 · 19h30</dt><dd>Trecho da reflexão, com "leia mais no site"</dd>"""),
     ("""<div class="rule-box"><b>Quinta-feira, novo padrão:</b> toda quinta terá um post feito por mim, independentemente do seu vídeo. O formato escolhido é o <b>carrossel às 12h30</b>, que é o melhor horário fixo de quinta para carrossel e o formato que mais tem trazido público. Seu vídeo, quando vier, entra nos stories da quinta (e, se você quiser, também como Reels às 19h30). Se o vídeo não vier, o carrossel segura a quinta sozinho.</div>""",
      """<div class="rule-box"><b>Autores da semana:</b> Bion, Christian Dunker e Guimarães Rosa na reflexão; Ferenczi e Mia Couto no texto de quarta. Nenhum deles foi usado nas reflexões anteriores do site. <b>Quinta:</b> carrossel às 12h30, como combinado; seu vídeo, se vier, entra nos stories da tarde.</div>"""),
     ("A reflexão entra hoje, ligada ao post de abertura.", "A reflexão entra na segunda, às 12h29, ligada ao post de abertura."),
     ("Fotos: Pexels (licença gratuita) e fotos da própria KN Casa de Integração® nos cartões finais. Imagens animadas (anel do ano e linhas fluidas) criadas por Claude.",
      "Fotos: Pexels (licença gratuita), sem marcas nem personagens, e fotos da própria KN Casa de Integração® só nos cartões finais. Telas animadas (linhas fluidas) criadas por Claude."),
    ]
    for a, b in rep:
        assert a in src, a[:60]
        src = src.replace(a, b)
    src = src.replace("__ARTICLES__", ARTS).replace("__MEDIA__", json.dumps(media)).replace("__DAYS__", json.dumps(days, ensure_ascii=False))
    open(S + "/semana-saude-do-homem.html", "w").write(src)
    print(len(src) / 1e6, "MB")
