# Genera los creativos horizontales (1920x1080) de cajas disponibles.
# Datos: src/lib/cajas.ts del proyecto Lovable "China Direct Connect" (25 nov 2026),
# solo cajas no vendidas, no ocultas y no apartadas.
# Uso: python3 generar.py && node render.js
import json, os

AQUI = os.path.dirname(os.path.abspath(__file__))
MIN_PZS = 10

# (código, modelo, nombre corto, piezas, total MXN, precio por pieza MXN exacto)
CAJAS = [
    ("CF-022", "CH-M802", "Mochila Bluetooth con luz", 50, 7868, 157.365119),
    ("CF-017", "KOS-500", "Bocina 2 en 1 con audífonos", 100, 17272, 172.717814),
    ("CF-039", "MK26", "Micrófono inalámbrico", 100, 18423, 184.232335),
    ("CF-037", "MK50", "Micrófono inalámbrico", 100, 28786, 287.863023),
    ("CF-023", "MS18", "Micrófono", 50, 15928, 318.568412),
    ("CF-018", "D8", "Cámara para auto (dashcam)", 100, 33776, 337.75928),
    ("CF-024", "QY77", "Micrófono 4 en 1", 100, 33776, 337.75928),
    ("CF-020", "F118", "Ventilador multifunción", 16, 9212, 575.726046),
    ("CF-008", "Q8", "Cámara deportiva", 40, 24564, 614.107782),
    ("CF-001", "TK70", "Reloj inteligente", 50, 34544, 690.871255),
    ("CF-011", "S85 Pro", "Traductor con IA", 100, 101712, 1017.116015),
    ("CF-007", "Pocket 4K", "Cámara de bolsillo 4K", 40, 45290, 1132.261224),
]

def m(n):
    return "$" + f"{round(n):,}"

def info(c):
    code, model, name, pz, total, pp = c
    return dict(code=code, model=model, name=name, pz=pz, total=m(total), pp=m(pp), min=m(pp * MIN_PZS))

DATA = [info(c) for c in CAJAS]

FLAG = ('<svg class="flag" viewBox="0 0 30 20"><rect width="30" height="20" fill="#DE2910"/>'
        '<g fill="#FFDE00"><polygon points="5,2 6.2,5.6 10,5.6 6.9,7.8 8.1,11.4 5,9.2 1.9,11.4 3.1,7.8 0,5.6 3.8,5.6"/>'
        '<circle cx="10" cy="2" r=".9"/><circle cx="12" cy="4" r=".9"/><circle cx="12" cy="7" r=".9"/><circle cx="10" cy="9" r=".9"/></g></svg>')

CSS = """
*{box-sizing:border-box;margin:0;padding:0}
:root{--n:#F97316;--n6:#EA580C;--n7:#C2410C;--n9:#9A3412;--tinta:#1A1A1A;--gris:#6B6B6B;
--durazno:#FFEDD5;--crema:#FFF8F5;--borde:#D9CFC7;--grad:linear-gradient(90deg,#F97316,#EA580C)}
html,body{width:1920px;height:1080px;overflow:hidden}
body{font-family:Arial,"Liberation Sans",Helvetica,sans-serif;color:var(--tinta);background:var(--crema)}
.grad{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}
.badge{display:inline-block;background:var(--grad);color:#fff;font-weight:700;letter-spacing:.08em;
text-transform:uppercase;border-radius:999px}
.badge.soft{background:var(--durazno);color:var(--n7)}
.flag{width:1.15em;height:.77em;border-radius:3px;vertical-align:-.04em;margin-left:.2em}
.photo{background-size:auto 100%;background-position:center;background-repeat:no-repeat;background-color:#3a3a3a}
.logo{display:block}
h1{font-weight:900;letter-spacing:-.02em;line-height:1.05}
.foot{position:absolute;left:0;right:0;bottom:0;background:var(--tinta);color:#fff;display:flex;
align-items:center;justify-content:space-between;padding:0 64px;font-size:26px}
.foot b{color:#FDBA74}
.pill{background:var(--grad);color:#fff;font-weight:700;border-radius:999px;box-shadow:0 8px 24px rgba(234,88,12,.3)}
"""

def page(body, extra=""):
    return f"<!doctype html><html lang='es'><head><meta charset='utf-8'><style>{CSS}{extra}</style></head><body>{body}</body></html>"

def foto(code):
    return f"fotos/{code}.jpg"

FOOT = ("<div class='foot' style='height:84px'><span>Aparta con el 20% por WhatsApp <b>81 2018 1761</b></span>"
        "<span>Precios en pesos. Envío DHL Express asegurado aparte.</span><span><b>compraenfabricas.com/productos</b></span></div>")

# ---------- A: catálogo 12 cajas ----------
def prop_a():
    cards = ""
    for d in DATA:
        cards += f"""<div class='card'>
  <div class='photo ph' style="background-image:url('{foto(d['code'])}')"></div>
  <div class='tx'>
    <div class='mod'>{d['model']}</div><div class='nm'>{d['name']}</div>
    <div class='pp'><span class='grad'>{d['pp']}</span><small>por pieza</small></div>
    <div class='mn'>10 piezas: <b>{d['min']}</b></div>
    <div class='cj'>Caja de {d['pz']} pzs: {d['total']}</div>
  </div></div>"""
    extra = """
.top{height:190px;padding:40px 64px 0;display:flex;justify-content:space-between;align-items:flex-start}
.top h1{font-size:62px}.top p{font-size:28px;color:var(--gris);margin-top:12px}
.top .r{text-align:right}.top .badge{font-size:22px;padding:14px 28px;margin-top:22px}
.grid{position:absolute;top:196px;left:64px;right:64px;display:grid;grid-template-columns:repeat(4,1fr);gap:20px}
.card{background:#fff;border:1px solid var(--borde);border-radius:16px;box-shadow:0 6px 20px rgba(26,26,26,.08);
height:250px;display:flex;overflow:hidden}
.ph{width:200px;flex:none}
.tx{padding:18px 18px 0;display:flex;flex-direction:column;flex:1}
.mod{font-size:15px;font-weight:700;letter-spacing:.08em;color:var(--n7)}
.nm{font-size:21px;font-weight:700;line-height:1.15;margin-top:4px;height:50px}
.pp{margin-top:10px;font-weight:900;font-size:46px;letter-spacing:-.02em;line-height:1}
.pp small{display:block;font-size:17px;color:var(--gris);font-weight:400;letter-spacing:0;margin-top:2px}
.mn{margin-top:14px;font-size:18px;background:var(--durazno);color:var(--n9);border-radius:8px;padding:6px 10px}
.mn b{color:var(--n7)}
.cj{margin-top:8px;font-size:16px;color:var(--gris)}
"""
    body = f"""<div class='top'><div><img class='logo' src='fotos/logo-horizontal.png' style='height:64px'>
<h1 style='margin-top:18px'>Cajas <span class='grad'>disponibles</span> ya en México{FLAG}</h1></div>
<div class='r'><span class='badge'>Mínimo 10 piezas por caja</span>
<p>Precio final por pieza, directo de fábrica</p></div></div>
<div class='grid'>{cards}</div>{FOOT}"""
    return page(body, extra)

# ---------- B: una caja por imagen ----------
def prop_b(d):
    extra = """
.l{position:absolute;left:64px;top:64px;width:960px;height:868px;border-radius:24px;overflow:hidden;
box-shadow:0 16px 40px rgba(26,26,26,.12)}
.l .photo{width:100%;height:100%;background-size:cover}
.l .badge{position:absolute;left:28px;top:28px;font-size:22px;padding:12px 24px}
.r{position:absolute;left:1088px;right:64px;top:64px;bottom:148px;display:flex;flex-direction:column}
.mod{font-size:26px;font-weight:700;letter-spacing:.08em;color:var(--n7);margin-top:44px}
.r h1{font-size:68px;margin-top:8px}
.big{font-weight:900;font-size:150px;letter-spacing:-.03em;line-height:1;margin-top:36px}
.sub{font-size:30px;color:var(--gris);margin-top:4px}
.box{margin-top:auto;background:var(--durazno);border-left:6px solid var(--n);border-radius:12px;padding:22px 28px}
.box .a{font-size:34px;font-weight:700;color:var(--n9)}.box .a b{color:var(--n6);font-size:44px}
.box .c{font-size:26px;color:var(--tinta);margin-top:8px}
"""
    body = f"""<div class='l'><div class='photo' style="background-image:url('{foto(d['code'])}')"></div>
<span class='badge'>Disponible · ya en México</span></div>
<div class='r'><img class='logo' src='fotos/logo-horizontal.png' style='height:62px;align-self:flex-start'>
<div class='mod'>MODELO {d['model'].upper()}</div><h1>{d['name']}</h1>
<div class='big grad'>{d['pp']}</div><div class='sub'>precio final por pieza</div>
<div class='box'><div class='a'>Llévate desde 10 piezas: <b>{d['min']}</b></div>
<div class='c'>Caja completa: {d['pz']} piezas por {d['total']}</div></div></div>{FOOT}"""
    return page(body, extra)

# ---------- C: 6 cajas por imagen, tarjetas grandes ----------
def prop_c(parte, titulo, sub):
    cards = ""
    for d in parte:
        cards += f"""<div class='card'><div class='photo ph' style="background-image:url('{foto(d['code'])}')">
<span class='badge soft'>{d['pz']} pzs en caja</span></div>
<div class='tx'><div class='nm'><span>{d['model']}</span> {d['name']}</div>
<div class='row'><div><div class='pp grad'>{d['pp']}</div><div class='lb'>por pieza</div></div>
<div class='rt'><div class='mn'>10 pzs <b>{d['min']}</b></div><div class='cj'>Caja: {d['total']}</div></div></div></div></div>"""
    extra = """
.top{height:200px;padding:44px 64px 0;display:flex;justify-content:space-between;align-items:flex-start}
.top h1{font-size:66px}.top p{font-size:28px;color:var(--gris);margin-top:10px}
.grid{position:absolute;top:210px;left:64px;right:64px;display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.card{background:#fff;border:1px solid var(--borde);border-radius:16px;box-shadow:0 6px 20px rgba(26,26,26,.08);
height:370px;overflow:hidden;display:flex;flex-direction:column}
.ph{height:210px;position:relative;background-size:cover}
.ph .badge{position:absolute;left:16px;top:16px;font-size:16px;padding:8px 16px}
.tx{padding:16px 22px}
.nm{font-size:24px;font-weight:700}.nm span{color:var(--n7)}
.row{display:flex;justify-content:space-between;align-items:flex-end;margin-top:12px}
.pp{font-weight:900;font-size:62px;letter-spacing:-.02em;line-height:1}
.lb{font-size:18px;color:var(--gris)}
.rt{text-align:right}
.mn{background:var(--durazno);color:var(--n9);border-radius:999px;padding:8px 16px;font-size:20px}.mn b{color:var(--n7)}
.cj{font-size:18px;color:var(--gris);margin-top:8px}
"""
    body = f"""<div class='top'><div><h1>{titulo}{FLAG}</h1><p>{sub}</p></div>
<img class='logo' src='fotos/logo-horizontal.png' style='height:70px'></div>
<div class='grid'>{cards}</div>{FOOT}"""
    return page(body, extra)

# ---------- D: lista de precios ----------
def prop_d():
    rows = ""
    for d in DATA:
        rows += f"""<div class='rw'><div class='photo th' style="background-image:url('{foto(d['code'])}')"></div>
<div class='nm'><span>{d['model']}</span>{d['name']}</div>
<div class='pp grad'>{d['pp']}</div><div class='mn'>{d['min']}</div><div class='cj'>{d['pz']} pzs · {d['total']}</div></div>"""
    extra = """
.side{position:absolute;left:0;top:0;bottom:84px;width:560px;background:#fff;border-right:1px solid var(--borde);
padding:64px 56px;display:flex;flex-direction:column}
.side h1{font-size:62px;margin-top:56px}
.side p{font-size:28px;color:var(--gris);margin-top:24px;line-height:1.4}
.side .box{margin-top:auto;background:var(--durazno);border-left:6px solid var(--n);border-radius:12px;padding:24px}
.side .box b{display:block;font-size:44px;color:var(--n6);font-weight:900}
.side .box span{font-size:24px;color:var(--n9)}
.list{position:absolute;left:600px;right:56px;top:40px}
.hd,.rw{display:grid;grid-template-columns:110px 1fr 170px 170px 230px;align-items:center;column-gap:20px}
.hd{font-size:16px;font-weight:700;letter-spacing:.08em;color:var(--gris);padding:0 18px 10px;text-transform:uppercase}
.hd div:nth-child(n+3){text-align:right}
.rw{background:#fff;border:1px solid var(--borde);border-radius:12px;height:68px;margin-bottom:9px;padding:0 18px 0 0;overflow:hidden}
.th{height:68px;background-size:cover}
.nm{font-size:23px;font-weight:700}.nm span{color:var(--n7);margin-right:10px}
.pp{font-weight:900;font-size:36px;text-align:right;letter-spacing:-.02em}
.mn{font-size:24px;font-weight:700;text-align:right;color:var(--n9)}
.cj{font-size:20px;color:var(--gris);text-align:right}
"""
    body = f"""<div class='side'><img class='logo' src='fotos/logo-horizontal.png' style='height:64px;align-self:flex-start'>
<h1>Lista de <span class='grad'>cajas disponibles</span>{FLAG}</h1>
<p>Electrónica directo de fábrica. Las cajas ya están en México y llegan por DHL al día hábil siguiente.</p>
<div class='box'><b>Mínimo 10 piezas</b><span>de cada caja, al mismo precio por pieza</span></div></div>
<div class='list'><div class='hd'><div></div><div>Producto</div><div>Por pieza</div><div>10 piezas</div><div>Caja completa</div></div>{rows}</div>{FOOT}"""
    return page(body, extra)

# ================= HISTORIAS (vertical 1080x1920) =================
# Zonas seguras: arriba 0-220 (perfil de IG) y abajo 1700-1920 (barra de respuesta) sin info clave.
V = "html,body{width:1080px;height:1920px}"
VCTA = """
.cta{position:absolute;left:56px;right:56px;top:1560px;height:120px;background:var(--tinta);color:#fff;
border-radius:24px;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center}
.cta .a{font-size:30px;font-weight:700}.cta .a b{color:#FDBA74}
.cta .b{font-size:21px;color:#D6D3D1;margin-top:6px}
.web{position:absolute;left:0;right:0;top:1712px;text-align:center;font-size:26px;font-weight:700;color:var(--n7)}
"""
CTA_V = ("<div class='cta'><div class='a'>Aparta con el 20% por WhatsApp <b>81 2018 1761</b></div>"
         "<div class='b'>Precios en pesos. Envío DHL Express asegurado aparte.</div></div>"
         "<div class='web'>compraenfabricas.com/productos</div>")

def hist_head(titulo, sub):
    return (f"<div class='hh'><img class='logo' src='fotos/logo-horizontal.png' style='height:58px'>"
            f"<h1>{titulo}{FLAG}</h1><p>{sub}</p></div>")

HH = """
.hh{position:absolute;left:56px;right:56px;top:200px}
.hh h1{font-size:64px;margin-top:22px}.hh p{font-size:28px;color:var(--gris);margin-top:10px}
"""

# B vertical: una caja por historia
def hist_b(d):
    extra = V + VCTA + """
.ph{position:absolute;left:56px;right:56px;top:200px;height:720px;border-radius:24px;overflow:hidden;
box-shadow:0 16px 40px rgba(26,26,26,.12);background-size:cover}
.ph .badge{position:absolute;left:24px;top:24px;font-size:22px;padding:12px 24px}
.logo2{position:absolute;right:56px;top:952px;height:52px}
.mod{position:absolute;left:56px;top:960px;font-size:26px;font-weight:700;letter-spacing:.08em;color:var(--n7)}
.t{position:absolute;left:56px;right:56px;top:1010px}
.t h1{font-size:64px}
.big{font-weight:900;font-size:170px;letter-spacing:-.03em;line-height:1;margin-top:26px}
.sub{font-size:30px;color:var(--gris)}
.box{position:absolute;left:56px;right:56px;top:1390px;background:var(--durazno);border-left:6px solid var(--n);
border-radius:12px;padding:20px 26px}
.box .a{font-size:34px;font-weight:700;color:var(--n9)}.box .a b{color:var(--n6);font-size:44px}
.box .c{font-size:26px;margin-top:6px}
"""
    body = f"""<div class='photo ph' style="background-image:url('{foto(d['code'])}')"><span class='badge'>Disponible · ya en México</span></div>
<div class='mod'>MODELO {d['model'].upper()}</div><img class='logo logo2' src='fotos/logo-horizontal.png'>
<div class='t'><h1>{d['name']}</h1><div class='big grad'>{d['pp']}</div><div class='sub'>precio final por pieza</div></div>
<div class='box'><div class='a'>Llévate desde 10 piezas: <b>{d['min']}</b></div>
<div class='c'>Caja completa: {d['pz']} piezas por {d['total']}</div></div>{CTA_V}"""
    return page(body, extra)

# C vertical: 6 cajas por historia (2 x 3)
def hist_c(parte, titulo, sub):
    cards = ""
    for d in parte:
        cards += f"""<div class='card'><div class='photo ph' style="background-image:url('{foto(d['code'])}')">
<span class='badge soft'>{d['pz']} pzs</span></div>
<div class='tx'><div class='nm'><span>{d['model']}</span> {d['name']}</div>
<div class='pp grad'>{d['pp']}<small>por pieza</small></div>
<div class='mn'>10 pzs: <b>{d['min']}</b></div><div class='cj'>Caja: {d['total']}</div></div></div>"""
    extra = V + VCTA + HH + """
.grid{position:absolute;top:470px;left:56px;right:56px;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.card{background:#fff;border:1px solid var(--borde);border-radius:16px;box-shadow:0 6px 20px rgba(26,26,26,.08);
height:345px;overflow:hidden;display:flex;flex-direction:column}
.ph{height:150px;position:relative;background-size:cover;flex:none}
.ph .badge{position:absolute;left:12px;top:12px;font-size:15px;padding:6px 12px}
.tx{padding:12px 18px}
.nm{font-size:21px;font-weight:700;line-height:1.15;height:48px}.nm span{color:var(--n7)}
.pp{font-weight:900;font-size:50px;letter-spacing:-.02em;line-height:1;margin-top:6px}
.pp small{font-size:17px;color:var(--gris);font-weight:400;letter-spacing:0;margin-left:8px;-webkit-text-fill-color:var(--gris)}
.mn{margin-top:10px;background:var(--durazno);color:var(--n9);border-radius:8px;padding:5px 10px;font-size:19px}.mn b{color:var(--n7)}
.cj{font-size:16px;color:var(--gris);margin-top:6px}
"""
    body = hist_head(titulo, sub) + f"<div class='grid'>{cards}</div>{CTA_V}"
    return page(body, extra)

# D vertical: lista de precios de las 12
def hist_d():
    rows = ""
    for d in DATA:
        rows += f"""<div class='rw'><div class='photo th' style="background-image:url('{foto(d['code'])}')"></div>
<div class='nm'><span>{d['model']}</span><br>{d['name']}</div>
<div class='r'><div class='pp grad'>{d['pp']}</div><div class='mn'>10 pzs {d['min']}</div></div></div>"""
    extra = V + VCTA + HH + """
.list{position:absolute;left:56px;right:56px;top:450px}
.rw{display:grid;grid-template-columns:110px 1fr auto;align-items:center;column-gap:18px;background:#fff;
border:1px solid var(--borde);border-radius:12px;height:85px;margin-bottom:6px;padding-right:20px;overflow:hidden}
.th{height:85px;background-size:cover}
.nm{font-size:22px;font-weight:700;line-height:1.15}.nm span{color:var(--n7);font-size:16px;letter-spacing:.06em}
.r{text-align:right}
.pp{font-weight:900;font-size:38px;letter-spacing:-.02em;line-height:1}
.mn{font-size:17px;color:var(--n9);margin-top:2px}
"""
    body = hist_head("Cajas <span class='grad'>disponibles</span>", "Precio final por pieza. Mínimo 10 piezas de cada caja.") + f"<div class='list'>{rows}</div>{CTA_V}"
    return page(body, extra)

out = {}
out["A-catalogo-12-cajas"] = prop_a()
out["C1-desde-157-por-pieza"] = prop_c(DATA[:6], f"Desde <span class='grad'>{DATA[0]['pp']}</span> por pieza", "Mínimo 10 piezas de cada caja. Mercancía ya en México.")
out["C2-camaras-relojes-y-mas"] = prop_c(DATA[6:], "Más cajas <span class='grad'>disponibles</span>", "Mínimo 10 piezas de cada caja. Mercancía ya en México.")
out["D-lista-de-precios"] = prop_d()
for i, d in enumerate(DATA, 1):
    out[f"B{i:02d}-{d['model'].lower().replace(' ', '-')}"] = prop_b(d)
# Historias (prefijo H-): van a png/historias/
out["H-C1-desde-157-por-pieza"] = hist_c(DATA[:6], f"Desde <span class='grad'>{DATA[0]['pp']}</span> por pieza", "Mínimo 10 piezas de cada caja. Ya en México.")
out["H-C2-mas-cajas-disponibles"] = hist_c(DATA[6:], "Más cajas <span class='grad'>disponibles</span>", "Mínimo 10 piezas de cada caja. Ya en México.")
out["H-D-lista-de-precios"] = hist_d()
for i, d in enumerate(DATA, 1):
    out[f"H-B{i:02d}-{d['model'].lower().replace(' ', '-')}"] = hist_b(d)

for k, v in out.items():
    with open(os.path.join(AQUI, f"_{k}.html"), "w") as f:
        f.write(v)
json.dump(sorted(out), open(os.path.join(AQUI, "_lista.json"), "w"))
print(len(out), "html")
