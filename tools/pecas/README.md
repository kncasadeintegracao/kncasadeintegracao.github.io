# Peças do Instagram da KN Casa de Integração®

Scripts usados pelo Claude para produzir as peças semanais (feed 1080×1350, stories/Reels 1080×1920).

## Preparar o ambiente
```
export KN_WORK=/tmp/kn_work; mkdir -p $KN_WORK/fotos $KN_WORK/build/html $KN_WORK/fonts
cp tools/pecas/logo_*.png $KN_WORK/
cd $KN_WORK/fonts && npm pack -s @fontsource/cormorant-garamond@5.3.0 @fontsource/montserrat@5.3.0 \
  && for t in *.tgz; do tar xzf $t; mv package ${t%.tgz}; done
```
(Os scripts procuram as fontes em `fontsource-cormorant-garamond-5.3.0` e `fontsource-montserrat-5.3.0`; renomeie as pastas se a versão mudar.)
Fotos de bancos gratuitos (Pexels): baixar com
`curl -o $KN_WORK/fotos/ID.jpg "https://images.pexels.com/photos/ID/pexels-photo-ID.jpeg?auto=compress&cs=tinysrgb&w=1200"`.
Fotos da casa: `fotos/` deste repositório.

## Arquivos
- `content.py` / `content_b.py`: exemplos de conteúdo de uma semana (lista `pieces`, paletas, `REELS_SCENES`).
- `render.py`: gera as peças. `CONTENT=content_b OUTDIR=out_b python3 render.py [ids...]`.
  Modelos: framed, text, fullphoto, closing, storypost, ask, anim_anel, anim_seda, anim_reels.
- `assemble_b.py` + `page_src.html`: montam o quadro de aprovação (artefato) com peças, legendas e textos do site.
- `to_repo.py`: grava mídias em `midia/`, cria `posts/*/post.json` (status "aprovado") e o `index_novo.html` da semana.
- `aniv.py`: exemplo de carrossel especial (1 ano da KN).

## Regras combinadas (resumo)
Horários: carrossel/post único 12h30 em dia útil (domingo 19h30); Reels 19h30; story 5 min depois; sábado só stories.
Selo discreto no topo (logo KN + "Katheryne Solange Muniz Nazer – RT" + credenciais), rodapé com @kncasadeintegracao e site.
Legendas terminam com assinatura, slogan e "© 2026 KN Casa de Integração®. Todos os direitos reservados."
Textos autorais, fontes citadas, sem plágio e sem cara de IA. Sem nomes de campanhas de mês colorido.
Publicar só depois de ela aprovar ("pode publicar").
