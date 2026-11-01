"""Render the 30 CleanAir Instagram posts (1080 x 1350, 4:5) and Story versions (1080 x 1920) to JPG.

Usage:  python3 social/render.py            # renders every post
        python3 social/render.py 5 6        # renders only days 5 and 6
Requires Node.js with Playwright (Chromium) and the Inter / Inter Display fonts.
"""
import sys
from pathlib import Path

from posts import POSTS, WEBSITE, WHATSAPP

ROOT = Path(__file__).resolve().parent
ASSETS = (ROOT.parent / "dist" / "assets").as_uri()
OUT = ROOT / "posts"
OUT.mkdir(exist_ok=True)
STORIES = ROOT / "stories"
STORIES.mkdir(exist_ok=True)

IMG = {
    "ductfit-vent": "ductfit-vent.png", "ductfit-mobile": "ductfit-mobile.png",
    "ductfit-kleansense-iaq-sensor": "ductfit-kleansense-iaq-sensor.png",
    "ductfit-cloud": "ductfit-cloud.jpeg", "ductfit-wall": "ductfit-wall.png",
    "ductfit-ceiling": "ductfit-ceiling.png", "ductfit-lampshade": "ductfit-lampshade.png",
    "ductfit-s": "ductfit-s.png", "ductfit-m": "ductfit-m.png",
}
NAMES = {"ductfit-vent": "Vent", "ductfit-cloud": "Cloud", "ductfit-wall": "Wall", "ductfit-mobile": "Mobile",
         "ductfit-lampshade": "Lampshade", "ductfit-kleansense-iaq-sensor": "KleanSense", "ductfit-ceiling": "Ceiling",
         "ductfit-s": "S", "ductfit-m": "M"}


def img(slug, cls=""):
    extra = " cloud" if slug == "ductfit-cloud" else ""
    return f'<img class="{cls}{extra}" src="{ASSETS}/{IMG[slug]}">'


CSS = """
:root{--ink:#00111d;--navy:#0b2c45;--deep:#00538a;--blue:#0592cc;--sky:#7bcee9;--ice:#bceaff;--mist:#edf8fd;--paper:#f6fafc;--grey:#4a5b68}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px}
body{font-family:Inter,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;overflow:hidden}
.post{position:relative;width:1080px;height:1350px;padding:80px 84px;display:flex;flex-direction:column;overflow:hidden}
h1,.big{font-family:"Inter Display",Inter,sans-serif;letter-spacing:-0.035em;font-weight:700;line-height:1.02}
h1{font-size:92px;position:relative;z-index:4}
.eyebrow{display:inline-flex;align-items:center;gap:14px;font-size:24px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:30px}
.eyebrow:before{content:"";width:44px;height:3px;background:currentColor;border-radius:2px}
.body{font-size:34px;line-height:1.42;color:var(--grey);margin-top:32px;max-width:860px}
.dark{background:radial-gradient(1200px 900px at 85% 110%,#0a4a75 0%,rgba(10,74,117,0) 60%),linear-gradient(160deg,var(--navy),var(--ink));color:#fff}
.dark .body{color:#b7d3e4}.dark .eyebrow{color:var(--sky)}
.light{background:linear-gradient(180deg,#fff 0%,var(--mist) 100%)}
.sky{background:linear-gradient(165deg,var(--mist) 0%,var(--ice) 100%)}
.brand{background:linear-gradient(150deg,#0aa5e0 0%,var(--blue) 40%,var(--deep) 100%);color:#fff}
.brand .eyebrow{color:#fff}.brand .body{color:#e2f5fd}
/* top + footer */
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:64px;position:relative;z-index:3}
.logo{height:84px}
.logo-pill{background:#fff;border-radius:999px;padding:6px 26px 6px 14px;display:flex;align-items:center}
.logo-pill img{height:72px}
.day{font-size:22px;font-weight:600;letter-spacing:.12em;color:var(--deep);border:2px solid currentColor;border-radius:999px;padding:10px 20px;opacity:.8}
.dark .day,.brand .day{color:#fff;opacity:.7}
.foot{margin-top:auto;display:flex;justify-content:space-between;align-items:center;font-size:26px;font-weight:600;position:relative;z-index:3;padding-top:28px;border-top:2px solid rgba(5,146,204,.22)}
.dark .foot,.brand .foot{border-top-color:rgba(255,255,255,.2)}
.foot span{display:flex;align-items:center;gap:12px}
.foot svg{width:30px;height:30px}
.flow{position:absolute;inset:0;z-index:0;pointer-events:none}
.post>*:not(.flow){position:relative;z-index:2}
/* product stage */
.stage{flex:1;display:flex;align-items:center;justify-content:center;position:relative;min-height:0;z-index:1}
.stage:before{content:"";position:absolute;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,#fff 0%,rgba(255,255,255,.85) 45%,rgba(188,234,255,0) 70%)}
.dark .stage:before{background:radial-gradient(circle,rgba(123,206,233,.55) 0%,rgba(5,146,204,.18) 45%,rgba(5,146,204,0) 70%)}
.stage img{position:relative;max-height:520px;max-width:620px;object-fit:contain;filter:drop-shadow(0 40px 50px rgba(0,40,70,.28))}
img.cloud{border-radius:36px;mix-blend-mode:multiply}
.dark img.cloud,.brand img.cloud{mix-blend-mode:normal}
.row{display:flex;gap:10px;align-items:flex-end;justify-content:center}
.row img{max-height:380px;max-width:330px}
/* specs */
.specs{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:10px}
.spec{background:#fff;border-radius:26px;padding:26px 30px;box-shadow:0 10px 30px rgba(0,83,138,.08)}
.spec b{display:block;font-size:20px;letter-spacing:.1em;text-transform:uppercase;color:var(--blue);margin-bottom:8px;font-weight:600}
.spec span{font-size:30px;font-weight:600;line-height:1.25}
/* lists */
.points{list-style:none;margin-top:40px;display:flex;flex-direction:column;gap:22px}
.points li{display:flex;gap:22px;align-items:flex-start;font-size:33px;line-height:1.32;font-weight:500}
.points li:before{content:"";flex:none;width:40px;height:40px;margin-top:2px;border-radius:50%;background:var(--blue) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='white' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5'/%3E%3C/svg%3E") center/24px no-repeat}
.dark .points li:before,.brand .points li:before{background-color:#fff;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%230592cc' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M5 12.5l4.5 4.5L19 7.5'/%3E%3C/svg%3E")}
"""

FLOW = """<svg class="flow" viewBox="0 0 1080 1350" preserveAspectRatio="none" fill="none">
<path d="M-60 {y1} C 260 {c1}, 620 {c2}, 1140 {y2}" stroke="{col}" stroke-opacity=".{o}" stroke-width="2"/>
<path d="M-60 {y3} C 300 {c3}, 700 {c4}, 1140 {y4}" stroke="{col}" stroke-opacity=".{o}" stroke-width="2"/>
<path d="M-60 {y5} C 340 {c5}, 760 {c6}, 1140 {y6}" stroke="{col}" stroke-opacity=".{o2}" stroke-width="2"/>
</svg>"""


def flow(dark=False, top=980):
    col = "#7bcee9" if dark else "#0592cc"
    return FLOW.format(col=col, o="35" if dark else "18", o2="2" if dark else "1",
                       y1=top, c1=top - 160, c2=top + 140, y2=top - 40,
                       y3=top + 60, c3=top - 90, c4=top + 200, y4=top + 30,
                       y5=top + 130, c5=top - 20, c6=top + 250, y6=top + 110)


WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 2s.9 2.3 1 2.5c.1.2 1.7 2.6 4.1 3.6 1.5.7 2.1.7 2.9.6.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.1-1.2l-.3-.2z"/></svg>'
GLOBE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9.5"/><path d="M2.5 12h19M12 2.5c2.6 2.8 3.9 6 3.9 9.5s-1.3 6.7-3.9 9.5c-2.6-2.8-3.9-6-3.9-9.5S9.4 5.3 12 2.5z"/></svg>'


def top(p, dark):
    logo = (f'<div class="logo-pill"><img src="{ASSETS}/cleanair-logo.png"></div>' if dark
            else f'<img class="logo" src="{ASSETS}/cleanair-logo.png">')
    return f'<div class="top">{logo}<div class="day">DAY {p["day"]:02d} / 30</div></div>'


def foot():
    return f'<div class="foot"><span>{GLOBE}{WEBSITE}</span><span>{WA}{WHATSAPP}</span></div>'


def head(p):
    return f'<div class="eyebrow">{p["eyebrow"]}</div><h1>{p["title"]}</h1>'


def lst(items, cls="points"):
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


# ---------------------------------------------------------------- layouts
def L_hero(p):
    prods = p["products"]
    imgs = img(prods[0]) if len(prods) == 1 else '<div class="row">' + "".join(img(s) for s in prods) + "</div>"
    return "dark", f"""<style>h1{{font-size:104px}}.stage:before{{width:820px;height:520px}}</style>
{head(p)}<p class="body">{p["body"]}</p><div class="stage">{imgs}</div>""", flow(True, 1050)


def L_fact(p):
    return "sky", f"""<style>.big{{font-size:330px;line-height:.9;background:linear-gradient(120deg,var(--blue),var(--deep));-webkit-background-clip:text;color:transparent;margin:10px 0 10px -10px}}
h1{{font-size:84px}}.src{{margin-top:auto;font-size:22px;color:var(--grey);opacity:.85;padding-bottom:26px}}</style>
<div class="eyebrow">{p["eyebrow"]}</div><div class="big">{p["big"]}</div><h1>{p["title"]}</h1>
<p class="body">{p["body"]}</p><div class="src">{p["source"]}</div>""", flow(False, 1120)


def L_audience(p):
    prods = p["products"]
    imgs = "".join(img(s) for s in prods)
    return "light", f"""<style>h1{{font-size:80px}}.panel{{flex:1;margin-top:40px;border-radius:40px;background:linear-gradient(140deg,var(--navy),var(--deep));display:flex;align-items:center;justify-content:center;gap:30px;overflow:hidden;position:relative;min-height:0;margin-bottom:34px}}
.panel:before{{content:"";position:absolute;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(123,206,233,.6),rgba(5,146,204,0) 70%)}}
.panel img{{position:relative;max-height:300px;max-width:{'420' if len(prods)==1 else '300'}px;filter:drop-shadow(0 30px 40px rgba(0,0,0,.35))}}
.panel img.cloud{{mix-blend-mode:normal;max-height:280px}}
.tag{{position:absolute;left:30px;top:28px;background:#fff;color:var(--deep);font-weight:700;font-size:22px;letter-spacing:.1em;text-transform:uppercase;padding:12px 22px;border-radius:999px}}
.points{{margin-top:34px;gap:16px}}.points li{{font-size:30px}}</style>
{head(p)}{lst(p["points"])}<div class="panel"><span class="tag">{p["audience"]}</span>{imgs}</div>""", ""


def L_steps(p):
    cards = "".join(f'<div class="card"><div class="n">{n}</div><div><h3>{t}</h3><p>{b}</p></div></div>' for n, t, b in p["steps"])
    return "light", f"""<style>h1{{font-size:80px}}.cards{{display:flex;flex-direction:column;gap:22px;margin-top:50px}}
.card{{display:flex;gap:30px;background:#fff;border-radius:30px;padding:32px 36px;box-shadow:0 14px 40px rgba(0,83,138,.09);align-items:flex-start}}
.n{{flex:none;width:86px;height:86px;border-radius:24px;background:linear-gradient(140deg,var(--blue),var(--deep));color:#fff;font:700 34px "Inter Display";display:flex;align-items:center;justify-content:center}}
h3{{font:700 38px "Inter Display";letter-spacing:-.02em;margin-bottom:8px}}.card p{{font-size:27px;line-height:1.4;color:var(--grey)}}</style>
{head(p)}<div class="cards">{cards}</div>""", flow(False, 1220)


def L_product(p):
    specs = "".join(f'<div class="spec"><b>{k}</b><span>{v}</span></div>' for k, v in p["specs"])
    return "sky", f"""<style>h1{{font-size:78px;max-width:900px}}.stage img{{max-height:430px}}.stage img.cloud{{max-height:330px}}.stage{{margin:40px 0 30px}}.specs{{margin-bottom:34px}}</style>
{head(p)}<div class="stage">{img(p["products"][0])}</div><div class="specs">{specs}</div>""", ""


def L_readings(p):
    r = [("PM2.5", "Fine particles"), ("TVOC", "Organic compounds"), ("CO₂", "Carbon dioxide"), ("CO", "Carbon monoxide"),
         ("O₃", "Ozone"), ("HCHO", "Formaldehyde"), ("Temp", "Temperature"), ("RH", "Humidity")]
    chip = lambda a, b: f'<div class="chip"><b>{a}</b><span>{b}</span></div>'
    left = "".join(chip(*x) for x in r[:4])
    right = "".join(chip(*x) for x in r[4:])
    return "dark", f"""<style>h1{{font-size:80px}}.wrap{{flex:1;display:grid;grid-template-columns:1fr 1.1fr 1fr;align-items:center;gap:26px;margin:30px 0 20px}}
.col{{display:flex;flex-direction:column;gap:18px}}.chip{{background:rgba(255,255,255,.07);border:1.5px solid rgba(123,206,233,.35);border-radius:24px;padding:20px 24px}}
.chip b{{display:block;font:700 42px "Inter Display";color:#fff;letter-spacing:-.02em}}.chip span{{font-size:21px;color:#9cc4da}}
.sens{{position:relative;display:flex;justify-content:center}}.sens:before{{content:"";position:absolute;inset:-70px;border-radius:50%;background:radial-gradient(circle,rgba(123,206,233,.5),rgba(5,146,204,0) 68%)}}
.sens img{{position:relative;width:100%;filter:drop-shadow(0 30px 40px rgba(0,0,0,.4))}}
.note{{text-align:center;font-size:27px;color:#b7d3e4;margin-bottom:30px}}</style>
{head(p)}<div class="wrap"><div class="col">{left}</div><div class="sens">{img("ductfit-kleansense-iaq-sensor")}</div><div class="col">{right}</div></div>
<p class="note">8 readings · Wi-Fi · Live dashboard & historical trends</p>""", flow(True, 1180)


def L_explainer(p):
    dots = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#0592cc" fill-opacity=".{o}"/>' for x, y, r, o in
                   [(900, 300, 46, 12), (980, 420, 18, 25), (840, 470, 10, 35), (1010, 250, 8, 4), (930, 560, 26, 15), (760, 360, 6, 5)])
    return "light", f"""<style>h1{{font-size:120px}}.dots{{position:absolute;inset:0;z-index:1}}.points li{{font-size:31px}}.ks{{margin-top:auto;margin-bottom:30px;display:flex;align-items:center;gap:28px;background:linear-gradient(140deg,var(--navy),var(--deep));color:#fff;border-radius:30px;padding:22px 34px 22px 22px}}.ks img{{width:130px;height:130px;object-fit:contain;background:rgba(255,255,255,.08);border-radius:22px;padding:10px}}.ks b{{display:block;font:700 36px "Inter Display"}}.ks span{{font-size:25px;color:#b7d3e4}}
.def{{margin-top:36px;background:#fff;border-left:8px solid var(--blue);border-radius:0 28px 28px 0;padding:30px 36px;font-size:33px;line-height:1.42;color:var(--ink);box-shadow:0 12px 34px rgba(0,83,138,.08)}}</style>
<svg class="dots flow" viewBox="0 0 1080 1350">{dots}</svg>
{head(p)}<div class="def">{p["body"]}</div>{lst(p["points"])}<div class="ks">{img("ductfit-kleansense-iaq-sensor")}<div><b>Measure it live</b><span>KleanSense tracks PM2.5, TVOC, CO₂ and 5 more readings</span></div></div>""", flow(False, 1170)


def L_poll(p):
    opts = "".join(f'<div class="opt"><b>{o[0]}</b>{o[1:].strip()}</div>' for o in p["options"])
    return "brand", f"""<style>h1{{font-size:96px}}.opts{{display:flex;flex-direction:column;gap:22px;margin:56px 0 30px}}
.opt{{display:flex;align-items:center;gap:28px;background:#fff;color:var(--ink);border-radius:30px;padding:28px 32px;font-size:38px;font-weight:600;box-shadow:0 16px 40px rgba(0,30,60,.18)}}
.opt b{{width:70px;height:70px;border-radius:20px;background:var(--mist);color:var(--blue);display:flex;align-items:center;justify-content:center;font:700 36px "Inter Display"}}
.cm{{font-size:30px;font-weight:600;color:#e2f5fd;margin-bottom:28px}}</style>
{head(p)}<div class="opts">{opts}</div><div class="cm">💬 Comment A, B, C or D</div>""", flow(True, 1240)


def L_question(p):
    bubbles = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" stroke="#7bcee9" stroke-opacity=".{o}" stroke-width="2"/>' for x, y, r, o in
                      [(880, 1020, 120, 3), (700, 1130, 60, 25), (980, 1180, 40, 3), (560, 1050, 24, 2), (820, 860, 30, 2), (400, 1160, 14, 3)])
    return "dark", f"""<style>h1{{font-size:118px;margin-top:20px}}.body{{font-size:38px;margin-top:44px}}</style>
<svg class="flow" viewBox="0 0 1080 1350" fill="none">{bubbles}<text x="880" y="1036" text-anchor="middle" font-family="Inter Display" font-weight="700" font-size="56" fill="#7bcee9" fill-opacity=".55">{p.get("bubble","CO₂")}</text></svg>
{head(p)}<p class="body">{p["body"]}</p>""", ""


def L_quote(p):
    return "dark", f"""<style>h1{{font-size:96px;margin-top:10px}}.q{{font:700 300px/0.75 Georgia,"DejaVu Serif",serif;color:var(--blue);height:120px;margin-top:30px}}
.stage{{justify-content:flex-end}}.stage:before{{right:-80px}}.stage img{{max-height:440px;margin-right:20px}}</style>
<div class="eyebrow">{p["eyebrow"]}</div><div class="q">“</div><h1>{p["title"]}</h1><div class="stage">{img(p["products"][0])}</div>""", flow(True, 1120)


def L_checklist(p):
    items = "".join(f'<div class="it"><span>{i+1}</span>{t}</div>' for i, t in enumerate(p["points"]))
    return "light", f"""<style>h1{{font-size:80px}}.list{{margin-top:46px;display:flex;flex-direction:column;gap:18px}}
.it{{display:flex;gap:26px;align-items:center;background:#fff;border-radius:26px;padding:26px 30px;font-size:31px;font-weight:600;line-height:1.3;box-shadow:0 10px 30px rgba(0,83,138,.08)}}
.it span{{flex:none;width:60px;height:60px;border-radius:50%;border:3px solid var(--blue);color:var(--blue);display:flex;align-items:center;justify-content:center;font:700 28px "Inter Display"}}
.save{{margin-top:28px;font-size:26px;color:var(--deep);font-weight:600;margin-bottom:26px}}</style>
{head(p)}<div class="list">{items}</div><div class="save">🔖 Save this for your next facilities review</div>""", ""


def L_myth(p):
    return "light", f"""<style>.box{{border-radius:34px;padding:44px 46px;margin-top:34px}}
.m{{background:#fff;border:2px dashed #c7d3db}}.f{{background:linear-gradient(140deg,var(--blue),var(--deep));color:#fff;box-shadow:0 24px 50px rgba(0,83,138,.25)}}
.lab{{display:inline-flex;align-items:center;gap:12px;font-size:24px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;margin-bottom:18px}}
.m .lab{{color:#9a5a5a}}.m p{{font:600 62px/1.12 "Inter Display";letter-spacing:-.02em;color:#6b7a85;text-decoration:line-through;text-decoration-color:rgba(154,90,90,.6);text-decoration-thickness:4px}}
.f p{{font:700 54px/1.15 "Inter Display";letter-spacing:-.02em}}h1.t{{font-size:100px}}.kn{{margin-top:40px;font-size:30px;font-weight:700;color:var(--deep)}}</style>
<div class="eyebrow">{p["eyebrow"]}</div><h1 class="t">Myth vs fact.</h1>
<div class="box m"><div class="lab">✕ Myth</div><p>{p["myth"]}</p></div>
<div class="box f"><div class="lab">✓ Fact</div><p>{p["fact"]}</p></div><div class="kn">Measure your air with KleanSense →</div>""", flow(False, 1230)


def L_finder(p):
    rows = "".join(f'<div class="r"><div class="ti">{img(s)}</div><div class="q">{q}</div><div class="a">{a}</div></div>' for q, a, s in p["finder"])
    return "sky", f"""<style>h1{{font-size:80px}}.rows{{margin-top:30px;display:flex;flex-direction:column;gap:14px}}
.r{{display:grid;grid-template-columns:116px 1fr auto;align-items:center;gap:26px;background:#fff;border-radius:28px;padding:18px 30px 18px 18px;box-shadow:0 10px 30px rgba(0,83,138,.08)}}
.ti{{width:116px;height:116px;border-radius:22px;background:var(--mist);display:flex;align-items:center;justify-content:center;overflow:hidden}}
.ti img{{max-width:100px;max-height:100px}}.ti img.cloud{{max-width:116px;max-height:116px;border-radius:0}}
.q{{font-size:29px;font-weight:600;line-height:1.25}}.a{{font:700 27px "Inter Display";color:#fff;background:var(--blue);padding:14px 22px;border-radius:999px;white-space:nowrap}}
.more{{margin-top:20px;font-size:26px;color:var(--deep);font-weight:600;margin-bottom:24px}}</style>
{head(p)}<div class="rows">{rows}</div><div class="more">+ ductFIT M for transport · KleanSense to measure it all</div>""", ""


def L_cta(p):
    return "brand", f"""<style>h1{{font-size:100px}}.points{{margin-top:50px}}.points li{{font-size:36px}}
.btn{{margin-top:60px;display:inline-flex;align-items:center;gap:20px;align-self:flex-start;background:#fff;color:var(--deep);font:700 40px "Inter Display";padding:30px 44px;border-radius:999px;box-shadow:0 20px 50px rgba(0,30,60,.25)}}
.btn svg{{width:46px;height:46px;color:#25a244}}.sub{{margin-top:22px;font-size:28px;color:#e2f5fd}}</style>
{head(p)}{lst(p["points"])}<div class="btn">{WA}WhatsApp us today</div><div class="sub">Or comment “AIR” and our team will reach out</div>""", flow(True, 1180)


def L_range(p):
    cells = "".join(f'<div class="c">{img(s)}<span>{NAMES[s]}</span></div>' for s in p["products"])
    return "light", f"""<style>h1{{font-size:104px}}.grid{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:46px 0 30px}}
.c{{background:#fff;border-radius:28px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:18px;box-shadow:0 10px 30px rgba(0,83,138,.08)}}
.c img{{max-height:200px;max-width:220px}}.c img.cloud{{border-radius:18px}}.c span{{font-size:24px;font-weight:700;color:var(--deep);letter-spacing:.04em}}</style>
{head(p)}<div class="grid">{cells}</div>""", ""


LAYOUTS = dict(hero=L_hero, fact=L_fact, audience=L_audience, steps=L_steps, product=L_product,
               readings=L_readings, explainer=L_explainer, poll=L_poll, question=L_question, quote=L_quote,
               checklist=L_checklist, myth=L_myth, finder=L_finder, cta=L_cta, range=L_range)


def page(p):
    theme, content, fl = LAYOUTS[p["layout"]](p)
    dark = theme in ("dark", "brand")
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>
<body><div class="post {theme}">{fl}{top(p, dark)}{content}{foot()}</div></body></html>"""


STORY_CSS = """
:root{--ink:#00111d;--navy:#0b2c45;--deep:#00538a;--blue:#0592cc;--sky:#7bcee9}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden}
body{font-family:Inter,sans-serif;-webkit-font-smoothing:antialiased;color:#fff;
background:radial-gradient(1000px 800px at 90% 0%,#0a4a75 0%,rgba(10,74,117,0) 60%),radial-gradient(900px 700px at 0% 100%,#0a4a75 0%,rgba(10,74,117,0) 60%),linear-gradient(170deg,var(--navy),var(--ink))}
.s{position:relative;width:1080px;height:1920px;display:flex;flex-direction:column;align-items:center;padding:230px 80px 0}
.head{display:flex;justify-content:space-between;align-items:center;width:920px;margin-bottom:40px}
.logo-pill{background:#fff;border-radius:999px;padding:6px 24px 6px 12px;display:flex}.logo-pill img{height:64px}
.tag{font-size:24px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--sky)}
.card{width:920px;height:1150px;border-radius:36px;overflow:hidden;box-shadow:0 40px 90px rgba(0,0,0,.45),0 0 0 2px rgba(123,206,233,.25)}
.card img{width:100%;height:100%;display:block}
.cta{margin-top:56px;display:flex;align-items:center;gap:18px;background:#fff;color:var(--deep);font:700 38px "Inter Display",Inter;padding:26px 40px;border-radius:999px}
.cta svg{width:44px;height:44px;color:#25a244}
.handle{margin-top:22px;font-size:28px;font-weight:600;color:#b7d3e4}
.flow{position:absolute;inset:0;width:100%;height:100%;z-index:0}.s>*:not(.flow){position:relative;z-index:1}
.card{flex:none}
"""


def story_page(p):
    post = (OUT / f"day-{p['day']:02d}-{p['layout']}.jpg").as_uri()
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{STORY_CSS}</style></head><body><div class="s">
{flow(True, 1650)}
<div class="head"><div class="logo-pill"><img src="{ASSETS}/cleanair-logo.png"></div><div class="tag">New post · Day {p['day']:02d}</div></div>
<div class="card"><img src="{post}"></div>
<div class="cta">{WA}WhatsApp {WHATSAPP}</div><div class="handle">@cleanairme_ · {WEBSITE}</div>
</div></body></html>"""


def main(days):
    html_dir = ROOT / ".build"
    html_dir.mkdir(exist_ok=True)
    jobs, story_jobs = [], []
    for p in POSTS:
        if days and p["day"] not in days:
            continue
        f = html_dir / f"day-{p['day']:02d}.html"
        f.write_text(page(p), encoding="utf-8")
        jobs.append((str(f), str(OUT / f"day-{p['day']:02d}-{p['layout']}.jpg")))
        fs = html_dir / f"story-{p['day']:02d}.html"
        fs.write_text(story_page(p), encoding="utf-8")
        story_jobs.append((str(fs), str(STORIES / f"story-{p['day']:02d}.jpg"), 1080, 1920))
    # screenshots are taken with Node Playwright (shot.cjs)
    import json, subprocess
    subprocess.run(["node", str(ROOT / "shot.cjs"), json.dumps(jobs)], check=True)
    subprocess.run(["node", str(ROOT / "shot.cjs"), json.dumps(story_jobs)], check=True)  # stories embed the feed posts


if __name__ == "__main__":
    main({int(a) for a in sys.argv[1:]})
