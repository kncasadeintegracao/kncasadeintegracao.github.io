import os, json
S = os.environ.get("KN_WORK", "/tmp/kn_work")
OUT = S + "/out_c2"

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
      <div class="eyebrow">Reflexão da semana · entra na quarta, 25/11, às 19h29, ligada ao Reels</div>
      <h2>Ou isto ou aquilo: o que a gente compra quando compra demais</h2>
      <div class="by">(Katheryne Nazer – nov/26)</div>
      <p>Na sexta-feira, dia 27, chega a Black Friday, e com ela uma avalanche de anúncios, contagens regressivas e descontos que parecem imperdíveis. Nesta semana, quero conversar sobre um lado da compra que quase nunca aparece nas vitrines. No consultório, escuto com frequência frases como "comprei e no dia seguinte nem lembrava por quê" ou "a caixa ainda está fechada no armário". Quando a gente olha com calma, quase sempre havia alguma coisa acontecendo antes do clique: um dia difícil, uma solidão que apertou à noite, um cansaço que pedia descanso e recebeu um pacote.</p>
      <p>O sociólogo Zygmunt Bauman, em <em>Vida para consumo</em>, observou que a sociedade de consumo depende de uma promessa que nunca se cumpre por inteiro. Se um objeto satisfizesse de verdade, a próxima compra perderia o sentido. Por isso, o desejo precisa ser renovado o tempo todo, e cada novidade já chega com prazo de validade. Daí o alívio de comprar durar tão pouco.</p>
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

