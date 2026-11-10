import sys, os, subprocess, shutil
sys.path.insert(0, os.path.dirname(__file__))
import importlib
_m = importlib.import_module(os.environ.get('CONTENT','content'))
pieces, S, P, C, CR = _m.pieces, _m.S, _m.P, _m.C, _m.CR
from playwright.sync_api import sync_playwright

OUT = S + "/" + os.environ.get("OUTDIR","out"); FR = S + "/frames"
os.makedirs(OUT, exist_ok=True)
FONTS = S + "/fonts"
LOGO_W = "file://" + S + "/logo_white.png"; LOGO_G = "file://" + S + "/logo_green.png"
ONLY = sys.argv[1:]

def ff(name, w, st, fam):
    sub = "fontsource-cormorant-garamond-5.3.0" if fam == "cg" else "fontsource-montserrat-5.3.0"
    pre = "cormorant-garamond" if fam == "cg" else "montserrat"
    return f"@font-face{{font-family:'{name}';src:url('file://{FONTS}/{sub}/files/{pre}-latin-{w}-{st}.woff2');font-weight:{w};font-style:{st}}}"

FONTCSS = "".join([ff("CG", w, s, "cg") for w in (500, 600, 700) for s in ("normal", "italic")] +
                  [ff("MS", w, s, "ms") for w in (400, 500, 600, 700) for s in ("normal",)])

def dims(size): return (1080, 1350) if size == "feed" else (1080, 1920)

def is_dark(pal): return pal["fg"].upper() in ("#FFFFFF",)

def seal(pal, light=None):
    white = is_dark(pal) if light is None else light
    logo = LOGO_W if white else LOGO_G
    col = "#FFFFFF" if white else pal["fg"]
    return f"""<div class="seal" style="color:{col}"><img src="{logo}"><span class="bar" style="background:{col}"></span>
    <div><div class="sn">Katheryne Solange Muniz Nazer – RT</div><div class="sc">Psicóloga · Neuropsicóloga · CRP 06/117.713</div></div></div>"""

def foot(pal, page=None, light=None):
    white = is_dark(pal) if light is None else light
    col = "#FFFFFF" if white else pal["fg"]
    pg = f'<span class="pg">{page}</span>' if page else ""
    return f'<div class="foot" style="color:{col}">@kncasadeintegracao · www.kncasadeintegracao.com{pg}</div>'

BASE = """*{box-sizing:border-box;margin:0;padding:0}
html,body{width:__W__px;height:__H__px;overflow:hidden}
body{font-family:MS,sans-serif;position:relative;-webkit-font-smoothing:antialiased}
.seal{position:absolute;top:46px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;opacity:.92;z-index:5}
.seal img{height:58px}.seal .bar{width:2px;height:50px;opacity:.6}
.seal .sn{font-family:CG;font-weight:600;font-size:29px;line-height:1.1}.seal .sc{font-size:17px;letter-spacing:.04em;opacity:.85;margin-top:3px}
.foot{position:absolute;bottom:38px;left:0;right:0;text-align:center;font-size:20px;letter-spacing:.06em;opacity:.78;z-index:5}
.foot .pg{position:absolute;right:56px}
.k{font-size:24px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.t{font-family:CG;font-weight:600;line-height:1.06;text-wrap:balance}
.t i{font-style:italic;font-weight:500}
.s{line-height:1.45;text-wrap:pretty}
.rule{width:70px;height:3px;border-radius:2px}
.num{width:96px;height:96px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-family:CG;font-weight:700;font-size:58px}
.cta{font-size:24px;font-weight:600;letter-spacing:.04em}
.pill{display:inline-block;padding:22px 52px;border-radius:99px;font-weight:600;font-size:32px}
.blob{position:absolute;border-radius:50%;filter:blur(70px);opacity:.45}
"""

def page(w, h, css, body, script=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTCSS}{BASE.replace('__W__',str(w)).replace('__H__',str(h))}{css}</style></head>
<body>{body}<script>{script}</script></body></html>"""

def blobs(pal, w, h):
    return (f'<div class="blob" style="width:{int(w*.7)}px;height:{int(w*.7)}px;background:{pal["ac"]};top:-{int(w*.25)}px;right:-{int(w*.3)}px;opacity:.18"></div>'
            f'<div class="blob" style="width:{int(w*.6)}px;height:{int(w*.6)}px;background:#FFFFFF;bottom:-{int(w*.2)}px;left:-{int(w*.25)}px;opacity:{'.06' if is_dark(pal) else '.35'}"></div>')

def tpl_framed(d):
    w, h = dims(d["size"]); pal = d["pal"]
    ph = 560 if d["size"] == "feed" else 900
    num = f'<div class="num" style="position:absolute;right:30px;bottom:-40px;background:{pal["ac"]};color:#fff">{d["num"]}</div>' if d.get("num") else ""
    txtcol = pal["fg"]; box = ""
    inner = f"""<div class="k" style="color:{pal['ac']}">{d.get('k','')}</div>
      <div class="t" style="font-size:78px;color:{pal['fg']}">{d['t']}</div>
      <div class="s" style="font-size:31px;color:{pal['sub']}">{d.get('s','')}</div>
      {f'<div class="cta" style="color:{pal["ac"]}">{d["cta"]}</div>' if d.get('cta') else ''}"""
    if d.get("dark_box"):
        inner = f"""<div style="background:{pal['box']};border-radius:30px;padding:40px 44px;display:flex;flex-direction:column;gap:16px;align-items:center;text-align:center">
        <div class="k" style="color:#F7C548">{d.get('k','')}</div>
        <div class="t" style="font-size:80px;color:#fff">{d['t']}</div>
        <div class="s" style="font-size:31px;color:#E3DCFF">{d.get('s','')}</div>
        <div class="cta" style="color:#F7C548">{d.get('cta','')}</div></div>"""
    deco = ""
    if d.get("dark_box"):
        deco = ('<svg style="position:absolute;left:40px;top:640px;z-index:3" width="90" height="90" viewBox="0 0 24 24"><path fill="#F06C5B" d="M12 21s-8-4.6-8-11a5 5 0 0 1 8-3.9A5 5 0 0 1 20 10c0 6.4-8 11-8 11z"/></svg>'
                '<svg style="position:absolute;right:50px;top:610px;z-index:3" width="70" height="70" viewBox="0 0 24 24"><path fill="#F7C548" d="M12 0l3 9 9 3-9 3-3 9-3-9-9-3 9-3z"/></svg>')
    body = f"""<div style="position:absolute;inset:0;background:{pal['bg']}"></div>{blobs(pal,w,h)}{seal(pal)}
    <div style="position:absolute;top:150px;left:60px;right:60px;height:{ph}px;border-radius:30px;overflow:visible;z-index:2">
      <div style="position:absolute;inset:0;border-radius:30px;background:url('file://{d['photo']}') {d.get('pos','50% 50%')}/cover;box-shadow:0 30px 60px rgba(0,0,0,.18)"></div>{num}</div>{deco}
    <div style="position:absolute;top:{150+ph+ (40 if d.get('dark_box') else 66)}px;left:72px;right:72px;bottom:90px;display:flex;flex-direction:column;gap:18px;justify-content:center;z-index:2;{'text-align:left' if not d.get('dark_box') else ''}">{inner}</div>
    {foot(pal, d.get('page'))}"""
    return page(w, h, "", body)

def tpl_text(d, canvas=False):
    w, h = dims(d["size"]); pal = d["pal"]
    num = f'<div class="num" style="background:{pal["ac"]};color:{pal["bg"] if pal["ac"] not in ("#F06C5B",) else "#fff"}">{d["num"]}</div>' if d.get("num") else ""
    bg = f'<canvas id="cv" width="{w}" height="{h}" style="position:absolute;inset:0"></canvas>' if canvas else blobs(pal, w, h)
    body = f"""<div style="position:absolute;inset:0;background:{pal['bg']}"></div>{bg}{seal(pal)}
    <div id="tx" style="position:absolute;top:170px;bottom:120px;left:96px;right:96px;display:flex;flex-direction:column;justify-content:center;gap:30px;z-index:3">
      {num}
      {f'<div class="k" style="color:{pal["ac"]}">{d["k"]}</div>' if d.get('k') else ''}
      <div class="t" style="font-size:{98 if len(d['t'])<60 else 84}px;color:{pal['fg']}">{d['t']}</div>
      <div class="rule" style="background:{pal['ac']}"></div>
      <div class="s" style="font-size:36px;color:{pal['sub']}">{d.get('s','')}</div>
    </div>{foot(pal, d.get('page'))}"""
    return w, h, body

def tpl_text_page(d):
    w, h, body = tpl_text(d); return page(w, h, "", body)

def tpl_fullphoto(d):
    w, h = dims(d["size"]); pal = d["pal"]
    q = '<div style="font-family:CG;font-size:170px;line-height:1;color:#D9B86E;height:90px;margin-bottom:-10px">“</div>' if d.get("quote") else ""
    fs = 92 if d["size"] == "feed" else 104
    body = f"""<div style="position:absolute;inset:0;background:url('file://{d['photo']}') {d.get('pos','50% 50%')}/cover"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,40,42,.55) 0%,rgba(15,40,42,.05) 25%,rgba(15,40,42,.55) 42%,rgba(12,34,36,.9) 72%,rgba(12,34,36,.95) 100%)"></div>
    {seal(pal, True)}
    <div style="position:absolute;left:84px;right:84px;bottom:{150 if d['size']=='feed' else 260}px;display:flex;flex-direction:column;gap:24px;align-items:center;text-align:center;color:#fff">
      {q}{f'<div class="k" style="color:#D9B86E">{d["k"]}</div>' if d.get('k') else ''}
      <div class="t" style="font-size:{fs}px">{d['t']}</div>
      {f'<div class="s" style="font-size:34px;color:#E6F0EE">{d["s"]}</div>' if d.get('s') else ''}
      {f'<div class="cta" style="color:#D9B86E">{d["cta"]}</div>' if d.get('cta') else ''}
    </div>{foot(pal, d.get('page'), True)}"""
    return page(w, h, "", body)

def tpl_closing(d):
    w, h = dims(d["size"]); pal = d["pal"]
    items = "".join(f'<div>· {i} ·</div>' for i in d["items"])
    body = f"""<div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,#2B6E71 0%,#1F5558 45%,#163F42 100%)"></div>
    <div style="position:absolute;top:70px;left:80px;right:80px;bottom:90px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;color:#fff">
      <img src="{LOGO_W}" style="width:250px">
      <div class="t" style="font-size:58px;margin-top:6px">{d['t']}</div>
      <div style="font-size:26px;line-height:1.7;color:#D7E6E3">{items}</div>
      <div style="width:100%;height:300px;border-radius:24px;background:url('file://{d['photo']}') 50% 50%/cover;box-shadow:0 20px 40px rgba(0,0,0,.25)"></div>
      <div class="s" style="font-size:27px;color:#D7E6E3">{d['s']}<br>Leia mais no site: texto novo da semana.</div>
      <div class="pill" style="background:#D9B86E;color:#1F5558;padding:16px 44px;font-size:28px">kncasadeintegracao.com · link na bio</div>
      <div style="margin-top:auto;font-size:22px;line-height:1.5;color:#D7E6E3"><span style="font-family:CG;font-size:30px;color:#fff;font-weight:600">Katheryne Solange Muniz Nazer – RT</span><br>Psicóloga · Neuropsicóloga · CRP 06/117.713<br><i style="font-family:CG;font-size:28px;color:#D9B86E">Cuidar de pessoas. Formar profissionais. Transformar realidades.</i><br><span style="font-size:18px">{CR}</span></div>
    </div>{foot(pal, d.get('page'), True)}"""
    return page(w, h, "", body)

def tpl_storypost(d):
    w, h = 1080, 1920; pal = d["pal"]
    body = f"""<div style="position:absolute;inset:0;background:{pal['bg']}"></div>{blobs(pal,w,h)}{seal(pal)}
    <div style="position:absolute;top:220px;left:80px;right:80px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px">
      <div class="k" style="color:{pal['ac'] if not is_dark(pal) else '#D9B86E'}">{d['k']}</div>
      <div class="t" style="font-size:96px;color:{pal['fg']}">{d['t']}</div></div>
    <div style="position:absolute;top:640px;left:150px;right:150px;height:860px;border-radius:34px;background:url('file://{d['photo']}') 50% 50%/cover;box-shadow:0 40px 80px rgba(0,0,0,.25);transform:rotate(-2deg)"></div>
    <div style="position:absolute;top:1580px;left:0;right:0;text-align:center"><span class="pill" style="background:{pal['fg']};color:{pal['bg']}">{d['cta']}</span></div>
    {foot(pal)}<div style="position:absolute;bottom:12px;left:0;right:0;text-align:center;font-size:16px;opacity:.6;color:{pal['fg']}">{CR}</div>"""
    return page(w, h, "", body)

def tpl_ask(d):
    w, h = 1080, 1920; pal = d["pal"]
    body = f"""<div style="position:absolute;inset:0;background:url('file://{d['photo']}') 40% 50%/cover;filter:blur(2px) brightness(1.04)"></div>
    <div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(230,239,234,.92),rgba(230,239,234,.55) 50%,rgba(230,239,234,.9))"></div>{seal(pal)}
    <div style="position:absolute;top:330px;left:90px;right:90px;text-align:center;display:flex;flex-direction:column;gap:26px;align-items:center">
      <div class="k" style="color:{pal['ac']}">{d['k']}</div>
      <div class="t" style="font-size:110px;color:{pal['fg']}">{d['t']}</div>
      <div class="s" style="font-size:34px;color:{pal['sub']}">{d['s']}</div></div>
    
    {foot(pal)}"""
    return page(w, h, "", body)

# ---------- animações (render(t) determinístico) ----------
ANEL_JS = r"""
const cv=document.getElementById('cv'),x=cv.getContext('2d');const W=cv.width,H=cv.height;
const PAL=%s;const CY=%d,R=%d;
window.render=function(t){x.clearRect(0,0,W,H);
 const cx=W/2;for(let i=0;i<12;i++){const a0=-Math.PI/2+i*Math.PI*2/12+0.05,a1=a0+Math.PI*2/12-0.1;
  const start=0.25+i*0.28, p=Math.max(0,Math.min(1,(t-start)/0.45));
  x.lineCap='round';x.lineWidth=34;
  if(i<11){x.strokeStyle=PAL.ring;x.globalAlpha=0.22;x.beginPath();x.arc(cx,CY,R,a0,a1);x.stroke();
   x.globalAlpha=1;x.strokeStyle=(i==10)?PAL.hi:PAL.ring;if(p>0){x.beginPath();x.arc(cx,CY,R,a0,a0+(a1-a0)*p);x.stroke();}
   if(i==10&&p>=1){const g=0.5+0.5*Math.sin((t-3.6)*3);x.globalAlpha=0.25*g;x.lineWidth=70;x.beginPath();x.arc(cx,CY,R,a0,a1);x.stroke();x.globalAlpha=1;x.lineWidth=34;}}
  else{x.setLineDash([2,26]);x.strokeStyle=PAL.ring;x.globalAlpha=Math.min(1,Math.max(0,(t-3.4)));x.beginPath();x.arc(cx,CY,R,a0,a1);x.stroke();x.setLineDash([]);x.globalAlpha=1;}
  const lab=['J','F','M','A','M','J','J','A','S','O','N','D'][i];const am=(a0+a1)/2;
  x.globalAlpha=Math.min(1,Math.max(0,(t-start)*2));x.fillStyle=(i==10)?PAL.hi:PAL.lab;x.font='600 30px MS';x.textAlign='center';x.textBaseline='middle';
  x.fillText(lab,cx+Math.cos(am)*(R+62),CY+Math.sin(am)*(R+62));x.globalAlpha=1;}
 document.getElementById('tx').style.opacity=Math.min(1,Math.max(0,(t-0.2)/0.8));
 document.getElementById('tx').style.transform='translateY('+(20*(1-Math.min(1,t/1)))+'px)';
};render(%s);"""

def tpl_anim_anel(d, t0):
    w, h = 1080, 1920; pal = d["pal"]; dark = is_dark(pal)
    js_pal = '{ring:"%s",hi:"%s",lab:"%s"}' % ("#FFFFFF" if dark else pal["ac"], "#D9B86E" if dark else "#C0756A", "#D7E6E3" if dark else pal["sub"])
    if d.get("poll"):
        extra = '<div style="height:260px"></div>'
    else:
        extra = f'<div style="margin-top:24px"><span class="pill" style="background:#D9B86E;color:#1F5558">{d.get("cta","")}</span></div>'
    bgc = "radial-gradient(110% 70% at 50% 30%,#2B6E71 0%,#1F5558 50%,#153C3F 100%)" if dark else pal["bg"]
    body = f"""<div style="position:absolute;inset:0;background:{bgc}"></div><canvas id="cv" width="{w}" height="{h}" style="position:absolute;inset:0"></canvas>{seal(pal)}
    <div style="position:absolute;top:575px;left:0;right:0;text-align:center;font-family:CG;font-size:120px;font-weight:600;color:{'#fff' if dark else pal['fg']}">2026</div>
    <div id="tx" style="position:absolute;top:1130px;left:90px;right:90px;text-align:center;display:flex;flex-direction:column;gap:22px;align-items:center;color:{'#fff' if dark else pal['fg']}">
      <div class="k" style="color:{'#D9B86E' if dark else pal['ac']}">{d['k']}</div>
      <div class="t" style="font-size:84px">{d['t']}</div>
      {f'<div class="s" style="font-size:36px;color:{pal["sub"]}">{d["s"]}</div>' if d.get('s') else ''}{extra}</div>{foot(pal)}"""
    return page(w, h, "", body, ANEL_JS % (js_pal, 650, 320, t0))

SEDA_JS = r"""
const cv=document.getElementById('cv'),x=cv.getContext('2d');const W=cv.width,H=cv.height;const C1='%s',C2='%s';
window.render=function(t){x.clearRect(0,0,W,H);
 for(let k=0;k<14;k++){x.beginPath();const ph=k*0.42, amp=90+k*9, yb=H*0.18+k*(H*0.05);
  for(let X=-20;X<=W+20;X+=12){const y=yb+Math.sin(X/260+t*0.9+ph)*amp*0.6+Math.sin(X/120-t*0.6+ph*1.7)*amp*0.25;X==-20?x.moveTo(X,y):x.lineTo(X,y);}
  x.strokeStyle=k%%2?C1:C2;x.globalAlpha=0.10+0.05*Math.sin(t+k);x.lineWidth=3+ (k%%3)*2;x.stroke();}
 x.globalAlpha=1;
 const e=Math.min(1,Math.max(0,(t-0.3)/1.0));const tx=document.getElementById('tx');tx.style.opacity=e;tx.style.transform='translateY('+(30*(1-e))+'px)';
};render(%s);"""

def tpl_anim_seda(d, t0):
    w, h, body = tpl_text(d, canvas=True); pal = d["pal"]
    return page(w, h, "", body, SEDA_JS % (pal["ac"], pal["fg"], t0))

# Reels: cenas com crossfade
REELS_SCENES = [
 (0, 4.2, "photo", P+"8534054.jpg", "<div class='k' style='color:#D9B86E'>Novembro</div><div class='t' style='font-size:104px'>Se você já acorda cansado, <i>este vídeo é para você.</i></div>"),
 (4.2, 8.4, "seda", None, "<div class='t' style='font-size:96px'>O cansaço de fim de ano costuma ser <i>acumulado.</i></div><div class='s' style='font-size:40px;color:#D7E6E3'>São meses de demandas sem pausa de verdade.</div>"),
 (8.4, 12.6, "photo", P+"10069250.jpg", "<div class='k' style='color:#D9B86E'>Alguns sinais</div><div class='lst'><div>Sono que não descansa</div><div>Irritação fácil</div><div>Dificuldade de concentração</div><div>Vontade de sumir das conversas</div></div>"),
 (12.6, 16.2, "seda", None, "<div class='t' style='font-size:92px'>Isso diz menos sobre força de vontade</div><div class='t' style='font-size:92px;color:#D9B86E'><i>e mais sobre um ritmo que passou do ponto.</i></div>"),
 (16.2, 19.6, "photo", P+"16648202.jpg", "<div class='k' style='color:#D9B86E'>Pausas reais ajudam</div><div class='lst'><div>Recusar um compromisso</div><div>Dormir mais cedo</div><div>Uma conversa sem pressa</div></div>"),
 (19.6, 22.5, "end", C+"casa-8.jpg", ""),
]
def tpl_anim_reels(d, t0):
    w, h = 1080, 1920; pal = d["pal"]; sc = ""
    scenes = getattr(_m, 'REELS_SCENES', REELS_SCENES)
    for i, (a, b, kind, ph, html) in enumerate(scenes):
        if kind == "photo":
            bg = f"<div class='ph' style=\"background:url('file://{ph}') 50% 50%/cover\"></div><div style='position:absolute;inset:0;background:linear-gradient(180deg,rgba(12,34,36,.35),rgba(12,34,36,.2) 35%,rgba(12,34,36,.9) 80%)'></div>"
            pos = "bottom:300px"
        elif kind == "seda":
            bg = "<div style='position:absolute;inset:0;background:radial-gradient(110% 70% at 50% 30%,#2B6E71 0%,#1F5558 50%,#153C3F 100%)'></div>"
            pos = "top:560px"
        else:
            bg = "<div style='position:absolute;inset:0;background:radial-gradient(110% 70% at 50% 30%,#2B6E71 0%,#1F5558 50%,#153C3F 100%)'></div>"
            html = (f"<img src='{LOGO_W}' style='width:300px'>" + html.replace('__PH__', ph)) if html else f"""<img src='{LOGO_W}' style='width:300px'><div class='t' style='font-size:88px'>Se o cansaço persiste, <i>procure ajuda.</i></div>
            <div style="width:100%;height:520px;border-radius:30px;background:url('file://{ph}') 50% 50%/cover;box-shadow:0 30px 60px rgba(0,0,0,.3)"></div>
            <div class='s' style='font-size:36px;color:#D7E6E3'>KN Casa de Integração® · Mooca/SP e online<br><b style='color:#D9B86E'>Leia mais no site · link na bio</b></div>"""
            pos = "top:220px"
        sc += f"<div class='scn' id='sc{i}' data-a='{a}' data-b='{b}'>{bg}<div class='tx' style='{pos}'>{html}</div></div>"
    css = """.scn{position:absolute;inset:0;opacity:0}.ph{position:absolute;inset:-60px}
    .tx{position:absolute;left:90px;right:90px;display:flex;flex-direction:column;gap:30px;align-items:center;text-align:center;color:#fff}
    .lst{display:flex;flex-direction:column;gap:22px;font-size:46px;font-weight:500}.lst div{padding:18px 34px;border-radius:99px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.3)}"""
    js = r"""const cv=document.getElementById('cv'),x=cv.getContext('2d');const W=cv.width,H=cv.height;
    window.render=function(t){document.querySelectorAll('.scn').forEach(s=>{const a=+s.dataset.a,b=+s.dataset.b;let o=Math.min(1,(t-a)/0.5,(b-t)/0.5);if(b>22)o=Math.min(1,(t-a)/0.5);s.style.opacity=Math.max(0,o);
      const ph=s.querySelector('.ph');if(ph){const p=(t-a)/(b-a);ph.style.transform='scale('+(1.0+0.08*p)+') translateY('+(-20*p)+'px)';}
      s.querySelectorAll('.lst div').forEach((el,j)=>{const e=Math.max(0,Math.min(1,(t-a-0.5-j*0.55)/0.4));el.style.opacity=e;el.style.transform='translateX('+(40*(1-e))+'px)';});
      const tx=s.querySelector('.tx');const e=Math.max(0,Math.min(1,(t-a-0.15)/0.6));tx.style.transform='translateY('+(30*(1-e))+'px)';});
     x.clearRect(0,0,W,H);for(let k=0;k<12;k++){x.beginPath();const ph=k*.45,yb=H*.15+k*H*.06;for(let X=-20;X<=W+20;X+=14){const y=yb+Math.sin(X/260+t*.9+ph)*60+Math.sin(X/120-t*.6+ph*1.7)*25;X==-20?x.moveTo(X,y):x.lineTo(X,y);}
      x.strokeStyle=k%2?'#D9B86E':'#FFFFFF';x.globalAlpha=.08;x.lineWidth=3;x.stroke();}x.globalAlpha=1;};render(__T0__);""".replace("__T0__", str(t0))
    body = f"{sc}<canvas id='cv' width='{w}' height='{h}' style='position:absolute;inset:0;pointer-events:none;z-index:4'></canvas>{seal(pal, True)}{foot(pal, None, True)}"
    return page(w, h, css, body, js)

STATIC = dict(framed=tpl_framed, text=tpl_text_page, fullphoto=tpl_fullphoto, closing=tpl_closing, storypost=tpl_storypost, ask=tpl_ask)
ANIM = dict(anim_anel=tpl_anim_anel, anim_seda=tpl_anim_seda, anim_reels=tpl_anim_reels)

with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    for d in pieces:
        if ONLY and d["id"] not in ONLY: continue
        w, h = dims(d["size"])
        pg = br.new_page(viewport=dict(width=w, height=h))
        hp = f"{S}/build/html/{d['id']}.html"; os.makedirs(os.path.dirname(hp), exist_ok=True)
        if d["tpl"] in STATIC:
            open(hp, "w").write(STATIC[d["tpl"]](d)); pg.goto("file://" + hp); pg.wait_for_timeout(400)
            pg.evaluate("document.fonts.ready"); pg.screenshot(path=f"{OUT}/{d['id']}.jpg", type="jpeg", quality=92)
        else:
            open(hp, "w").write(ANIM[d["tpl"]](d, 0)); pg.goto("file://" + hp); pg.wait_for_timeout(400); pg.evaluate("document.fonts.ready")
            fd = f"{FR}/{d['id']}"; shutil.rmtree(fd, ignore_errors=True); os.makedirs(fd)
            fps = 30; n = int(d["dur"] * fps)
            for i in range(n):
                pg.evaluate(f"render({i/fps})"); pg.screenshot(path=f"{fd}/{i:04d}.jpg", type="jpeg", quality=90)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(fps), "-i", f"{fd}/%04d.jpg", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", f"{OUT}/{d['id']}.mp4"], check=True)
            pg.evaluate(f"render({d['dur']*0.8})"); pg.screenshot(path=f"{OUT}/{d['id']}_frame.jpg", type="jpeg", quality=90)
        pg.close(); print("ok", d["id"], flush=True)
    br.close()
