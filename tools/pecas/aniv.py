"""Carrossel especial: 1 ano da KN Casa de Integração® (10/11/2026)."""
import os, subprocess, shutil, sys
from playwright.sync_api import sync_playwright

S = os.environ.get("KN_WORK", "/tmp/kn_work")
F = "/home/claude/kncasadeintegracao.github.io/fotos/"
OUT = S + "/out_aniv"; os.makedirs(OUT, exist_ok=True)
FONTS = S + "/fonts"
LW = "file://" + S + "/logo_white.png"; LG = "file://" + S + "/logo_green.png"
ONLY = sys.argv[1:]

def ff(n, w, st, fam):
    sub = "fontsource-cormorant-garamond-5.3.0" if fam == "cg" else "fontsource-montserrat-5.3.0"
    pre = "cormorant-garamond" if fam == "cg" else "montserrat"
    return f"@font-face{{font-family:'{n}';src:url('file://{FONTS}/{sub}/files/{pre}-latin-{w}-{st}.woff2');font-weight:{w};font-style:{st}}}"
FONTCSS = "".join([ff("CG", w, s, "cg") for w in (500, 600, 700) for s in ("normal", "italic")] +
                  [ff("MS", w, "normal", "ms") for w in (400, 500, 600, 700)])

GREEN = "#1F5558"; DEEP = "#163F42"; GOLD = "#D9B86E"; MINT = "#E6EFEA"; BEGE = "#EAD8C4"; CREAM = "#F6EFE6"

def page(w, h, body, css="", js=""):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTCSS}
*{{box-sizing:border-box;margin:0;padding:0}}html,body{{width:{w}px;height:{h}px;overflow:hidden}}
body{{font-family:MS,sans-serif;position:relative;-webkit-font-smoothing:antialiased}}
.seal{{position:absolute;top:46px;left:0;right:0;display:flex;justify-content:center;align-items:center;gap:18px;opacity:.92;z-index:9}}
.seal img{{height:58px}}.seal .bar{{width:2px;height:50px;opacity:.6}}
.seal .sn{{font-family:CG;font-weight:600;font-size:29px;line-height:1.1}}.seal .sc{{font-size:17px;letter-spacing:.04em;opacity:.85;margin-top:3px}}
.foot{{position:absolute;bottom:38px;left:0;right:0;text-align:center;font-size:20px;letter-spacing:.06em;opacity:.78;z-index:9}}
.foot .pg{{position:absolute;right:56px}}
.k{{font-size:24px;font-weight:600;letter-spacing:.18em;text-transform:uppercase}}
.t{{font-family:CG;font-weight:600;line-height:1.06;text-wrap:balance}}.t i{{font-style:italic;font-weight:500}}
.s{{line-height:1.5;text-wrap:pretty}}
{css}</style></head><body>{body}<script>{js}</script></body></html>"""

def seal(white):
    c = "#FFFFFF" if white else GREEN
    return f"""<div class="seal" style="color:{c}"><img src="{LW if white else LG}"><span class="bar" style="background:{c}"></span>
    <div><div class="sn">Katheryne Solange Muniz Nazer – RT</div><div class="sc">Psicóloga · Neuropsicóloga · CRP 06/117.713</div></div></div>"""

def foot(white, pg=None):
    c = "#FFFFFF" if white else GREEN
    p = f'<span class="pg">{pg}</span>' if pg else ""
    return f'<div class="foot" style="color:{c}">@kncasadeintegracao · www.kncasadeintegracao.com{p}</div>'

W, H = 1080, 1350

# 1 · capa com a foto dela (arco)
def c01():
    body = f"""<div style="position:absolute;inset:0;background:radial-gradient(120% 90% at 50% 20%,#F3EADF 0%,{BEGE} 60%,#E2CDB4 100%)"></div>
    {seal(False)}
    <div style="position:absolute;top:150px;left:50%;transform:translateX(-50%);width:560px;height:660px;border-radius:280px 280px 30px 30px;
      background:url('file://{F}katheryne-2.jpg') 50% 30%/cover;box-shadow:0 30px 70px rgba(78,45,12,.25);border:6px solid #FFF8EF"></div>
    <div style="position:absolute;top:150px;left:50%;transform:translateX(-50%);width:600px;height:690px;margin-top:-20px;border-radius:300px 300px 40px 40px;border:2px solid {GOLD};opacity:.9"></div>
    <div style="position:absolute;top:760px;left:50%;transform:translateX(-50%);width:200px;height:200px;border-radius:50%;background:{GREEN};
      display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;box-shadow:0 18px 40px rgba(22,63,66,.35);border:3px solid {GOLD}">
      <div style="font-family:MS;font-weight:500;font-size:96px;line-height:1">1</div><div style="font-size:22px;letter-spacing:.2em;font-weight:600">ANO</div></div>
    <div style="position:absolute;top:985px;left:70px;right:70px;text-align:center;display:flex;flex-direction:column;gap:14px;align-items:center">
      <div class="t" style="font-size:76px;color:{GREEN}">Um ano no nosso <i>novo espaço</i></div>
      <div class="s" style="font-size:28px;color:#5B4632">KN Casa de Integração® · Mooca/SP · 10 de novembro</div>
      <div style="font-size:24px;font-weight:600;color:#8A6A2E;letter-spacing:.04em">Arraste →</div></div>
    {foot(False, "1/8")}"""
    return page(W, H, body)

# 2 · ela falando
def c02():
    body = f"""<div style="position:absolute;inset:0;background:{MINT}"></div>
    <div style="position:absolute;width:760px;height:760px;border-radius:50%;background:{GOLD};opacity:.12;filter:blur(60px);top:-200px;right:-260px"></div>
    {seal(False)}
    <div style="position:absolute;top:170px;left:80px;display:flex;align-items:center;gap:30px">
      <div style="width:230px;height:230px;border-radius:50%;background:url('file://{F}katheryne.jpg') 50% 35%/cover;border:5px solid #fff;box-shadow:0 14px 34px rgba(31,85,88,.25)"></div>
      <div><div style="font-family:CG;font-size:46px;font-weight:600;color:{GREEN};line-height:1.1">Dra. Katheryne</div>
      <div style="font-size:22px;color:#3F5F5C;margin-top:6px">Fundadora e Responsável Técnica</div></div></div>
    <div style="position:absolute;top:470px;left:80px;right:80px;display:flex;flex-direction:column;gap:30px">
      <div style="font-family:CG;font-size:180px;line-height:.5;color:{GOLD};height:60px">“</div>
      <div class="t" style="font-size:62px;color:{GREEN}">Há um ano, a KN ganhou este novo espaço, <i>pensado para cuidar de pessoas com escuta, ciência e afeto.</i></div>
      <div class="s" style="font-size:32px;color:#3F5F5C">Ele chegou depois de quase duas décadas de Psicologia e de uma trajetória que começou no Direito. Hoje, o que eu mais sinto é gratidão.</div></div>
    {foot(False, "2/8")}"""
    return page(W, H, body)

def framed(n, photo, pos, kicker, title, sub, bg, fg, ac, subc, white=False):
    body = f"""<div style="position:absolute;inset:0;background:{bg}"></div>
    <div style="position:absolute;width:700px;height:700px;border-radius:50%;background:{ac};opacity:.14;filter:blur(70px);bottom:-240px;left:-220px"></div>
    {seal(white)}
    <div style="position:absolute;top:150px;left:60px;right:60px;height:640px;border-radius:30px;background:url('file://{photo}') {pos}/cover;box-shadow:0 30px 60px rgba(0,0,0,.2)"></div>
    <div style="position:absolute;top:830px;left:76px;right:76px;bottom:95px;display:flex;flex-direction:column;justify-content:center;gap:16px">
      <div class="k" style="color:{ac}">{kicker}</div>
      <div class="t" style="font-size:70px;color:{fg}">{title}</div>
      <div class="s" style="font-size:30px;color:{subc}">{sub}</div></div>
    {foot(white, f"{n}/8")}"""
    return page(W, H, body)

def c03(): return framed(3, F+"casa-1.jpg", "50% 60%", "Obrigada", "Aos nossos pacientes, <i>pela confiança</i>",
    "Cada pessoa que entrou por esta porta nos confiou a sua história. Esse é o maior presente que uma casa de cuidado pode receber.",
    CREAM, GREEN, "#8A6A2E", "#5B4632")
def c04(): return framed(4, F+"casa-3.jpg", "50% 50%", "Obrigada", "Às famílias, <i>que caminharam junto</i>",
    "Mães, pais, avós e responsáveis que chegaram com uma preocupação e ficaram para construir um caminho com a gente.",
    "#DDEBEC", GREEN, "#518E91", "#3F5F5C")
def c05(): return framed(5, F+"casa-6.jpg", "50% 50%", "Obrigada", "À equipe e aos parceiros, <i>que escolheram esta casa</i>",
    "Profissionais da saúde, da educação e do direito que fazem da KN um lugar de verdade multi e interdisciplinar.",
    GREEN, "#FFFFFF", GOLD, "#D7E6E3", white=True)
def c06(): return framed(6, F+"casa-2b.jpg", "50% 55%", "Obrigada", "Aos amigos e visitantes, <i>que vieram nos conhecer</i>",
    "Aqui a porta fica aberta, o café está sempre pronto e cada chegada é recebida com carinho.",
    "#F3E4C7", "#4E2D0C", GREEN, "#6B4A2A")

# 7 · animado: o "1" desenhado em dourado com luzes suaves
JS7 = r"""
const cv=document.getElementById('cv'),x=cv.getContext('2d');const W=cv.width,H=cv.height;
const P=[];for(let i=0;i<46;i++){P.push({x:(i*137.5)%W, y:(i*263.1)%H, r:6+((i*7)%22), sp:12+((i*11)%30), ph:i*0.7});}
const path=new Path2D('M470 520 L560 455 L560 900 M480 900 L640 900');
window.render=function(t){x.clearRect(0,0,W,H);
 for(const p of P){const y=(p.y - t*p.sp + H*4)%H, a=0.10+0.10*Math.sin(t*1.3+p.ph);
  const g=x.createRadialGradient(p.x,y,0,p.x,y,p.r*3);g.addColorStop(0,'rgba(217,184,110,'+(a*2.2)+')');g.addColorStop(1,'rgba(217,184,110,0)');
  x.fillStyle=g;x.beginPath();x.arc(p.x,y,p.r*3,0,Math.PI*2);x.fill();}
 const e=Math.min(1,Math.max(0,(t-0.2)/1.8));x.save();x.lineCap='round';x.lineJoin='round';
 x.setLineDash([1400]);x.lineDashOffset=1400*(1-e);x.strokeStyle='#D9B86E';x.lineWidth=26;x.shadowColor='rgba(217,184,110,.6)';x.shadowBlur=30;x.stroke(path);x.restore();
 const r=Math.min(1,Math.max(0,(t-0.9)/1.4));x.save();x.strokeStyle='rgba(255,255,255,.55)';x.lineWidth=2;x.beginPath();x.arc(555,690,300,-Math.PI/2,-Math.PI/2+Math.PI*2*r);x.stroke();x.restore();
 const tx=document.getElementById('tx');const e2=Math.min(1,Math.max(0,(t-1.6)/1.0));tx.style.opacity=e2;tx.style.transform='translateY('+(24*(1-e2))+'px)';
};render(__T0__);"""
def c07(t0=0):
    body = f"""<div style="position:absolute;inset:0;background:radial-gradient(110% 80% at 50% 40%,#2B6E71 0%,{GREEN} 50%,{DEEP} 100%)"></div>
    <canvas id="cv" width="{W}" height="{H}" style="position:absolute;inset:0"></canvas>{seal(True)}
    <div id="tx" style="position:absolute;top:1030px;left:90px;right:90px;text-align:center;color:#fff;display:flex;flex-direction:column;gap:14px">
      <div class="t" style="font-size:64px">E a todos que ajudaram <i>a construir esta casa</i></div>
      <div class="s" style="font-size:28px;color:#D7E6E3">tijolo por tijolo, encontro por encontro.</div></div>
    {foot(True, "7/8")}"""
    return page(W, H, body, js=JS7.replace("__T0__", str(t0)))

# 8 · fechamento
def c08():
    body = f"""<div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 0%,#2B6E71 0%,{GREEN} 45%,{DEEP} 100%)"></div>
    <div style="position:absolute;top:70px;left:80px;right:80px;bottom:90px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;color:#fff">
      <img src="{LW}" style="width:260px">
      <div class="t" style="font-size:66px;margin-top:4px">Que venham muitos anos <i>de cuidado</i></div>
      <div style="width:100%;height:330px;border-radius:24px;background:url('file://{F}casa-8.jpg') 50% 50%/cover;box-shadow:0 20px 40px rgba(0,0,0,.25)"></div>
      <div class="s" style="font-size:28px;color:#D7E6E3">Com amor e gratidão,<br><span style="font-family:CG;font-size:44px;color:#fff;font-weight:600">Katheryne</span></div>
      <div style="margin-top:auto;font-size:22px;line-height:1.5;color:#D7E6E3"><span style="font-family:CG;font-size:30px;color:#fff;font-weight:600">Katheryne Solange Muniz Nazer – RT</span><br>Psicóloga · Neuropsicóloga · CRP 06/117.713<br>
        <i style="font-family:CG;font-size:30px;color:{GOLD}">Cuidar de pessoas. Formar profissionais. Transformar realidades.</i><br><span style="font-size:18px">© 2026 KN Casa de Integração®. Todos os direitos reservados.</span></div>
    </div>{foot(True, "8/8")}"""
    return page(W, H, body)

# story de chamada
def story():
    body = f"""<div style="position:absolute;inset:0;background:radial-gradient(120% 80% at 50% 20%,#F3EADF 0%,{BEGE} 60%,#E2CDB4 100%)"></div>
    {seal(False)}
    <div style="position:absolute;top:230px;left:80px;right:80px;text-align:center;display:flex;flex-direction:column;gap:20px;align-items:center">
      <div class="k" style="color:#8A6A2E">10 de novembro</div>
      <div class="t" style="font-size:100px;color:{GREEN}">Um ano no nosso <i>novo espaço</i></div></div>
    <div style="position:absolute;top:640px;left:50%;transform:translateX(-50%) rotate(-2deg);width:720px;height:900px;border-radius:34px;background:url('file://{S}/out_aniv/c01.jpg') 50% 50%/cover;box-shadow:0 40px 80px rgba(78,45,12,.3)"></div>
    <div style="position:absolute;top:1610px;left:0;right:0;text-align:center"><span style="display:inline-block;padding:22px 52px;border-radius:99px;background:{GREEN};color:#fff;font-weight:600;font-size:32px">Ver o post</span></div>
    {foot(False)}"""
    return page(1080, 1920, body)

STATIC = [("c01", c01), ("c02", c02), ("c03", c03), ("c04", c04), ("c05", c05), ("c06", c06), ("c08", c08), ("story", story)]
with sync_playwright() as pw:
    br = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    for name, fn in STATIC:
        if ONLY and name not in ONLY: continue
        w, h = (1080, 1920) if name == "story" else (W, H)
        pg = br.new_page(viewport=dict(width=w, height=h)); hp = f"{S}/build/html/aniv_{name}.html"
        open(hp, "w").write(fn()); pg.goto("file://" + hp); pg.wait_for_timeout(500); pg.evaluate("document.fonts.ready")
        pg.screenshot(path=f"{OUT}/{name}.jpg", type="jpeg", quality=92); pg.close(); print("ok", name, flush=True)
    if not ONLY or "c07" in ONLY:
        pg = br.new_page(viewport=dict(width=W, height=H)); hp = f"{S}/build/html/aniv_c07.html"
        open(hp, "w").write(c07()); pg.goto("file://" + hp); pg.wait_for_timeout(500); pg.evaluate("document.fonts.ready")
        fd = f"{S}/frames/aniv_c07"; shutil.rmtree(fd, ignore_errors=True); os.makedirs(fd)
        for i in range(30 * 7):
            pg.evaluate(f"render({i/30})"); pg.screenshot(path=f"{fd}/{i:04d}.jpg", type="jpeg", quality=90)
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", "30", "-i", f"{fd}/%04d.jpg", "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart", f"{OUT}/c07.mp4"], check=True)
        pg.evaluate("render(5.5)"); pg.screenshot(path=f"{OUT}/c07_frame.jpg", type="jpeg", quality=90); pg.close(); print("ok c07")
    br.close()
