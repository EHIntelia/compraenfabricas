# Carrusel de Instagram (1080x1350, 4:5) con las cajas disponibles.
# Usa los datos y estilos de generar.py. Uso: python3 carrusel.py && node render.js
import json, os
from generar import CAJAS, DATA, CSS, FLAG, MIN_PZS, foto, m

AQUI = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1350
TOTAL = 8

# Precio de 10 piezas (número) para agrupar por presupuesto
MIN10 = {c[0]: c[5] * MIN_PZS for c in CAJAS}
def tramo(lo, hi):
    return [d for d in DATA if lo < MIN10[d["code"]] <= hi]

BASE = CSS + f"""
html,body{{width:{W}px;height:{H}px}}
.num{{position:absolute;right:56px;top:56px;font-size:22px;font-weight:700;color:var(--gris);letter-spacing:.08em}}
.lg{{position:absolute;left:56px;top:48px;height:50px}}
.swipe{{position:absolute;right:56px;bottom:52px;font-size:26px;font-weight:700;color:var(--n7)}}
.eyebrow{{font-size:24px;font-weight:700;letter-spacing:.08em;color:var(--n7);text-transform:uppercase}}
"""

def slide(n, body, extra="", logo=True, swipe=True):
    head = f"<div class='num'>{n}/{TOTAL}</div>"
    if logo:
        head += "<img class='lg' src='fotos/logo-horizontal.png'>"
    if swipe and n < TOTAL:
        head += "<div class='swipe'>Desliza →</div>"
    return f"<!doctype html><html lang='es'><head><meta charset='utf-8'><style>{BASE}{extra}</style></head><body>{head}{body}</body></html>"

# 1 · Hook
def s1():
    top6 = DATA[:6]
    tiles = "".join(
        f"<div class='photo t' style=\"background-image:url('{foto(d['code'])}')\"><span>{d['pp']}<small>/pieza</small></span></div>"
        for d in top6)
    extra = """
.b{position:absolute;left:56px;top:140px}
.b .badge{font-size:22px;padding:12px 24px}
.b h1{font-size:88px;margin-top:28px;width:968px}
.b p{font-size:32px;color:var(--gris);margin-top:22px;width:900px;line-height:1.35}
.g{position:absolute;left:56px;right:56px;top:660px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.t{height:270px;border-radius:16px;position:relative;background-size:cover;box-shadow:0 6px 20px rgba(26,26,26,.12)}
.t span{position:absolute;left:12px;bottom:12px;background:#fff;border-radius:999px;padding:6px 14px;
font-weight:900;font-size:28px;color:var(--n6)}
.t small{font-size:16px;color:var(--gris);font-weight:400}
"""
    body = f"""<div class='b'><span class='badge'>Mercancía ya en México</span>
<h1>Tu primer inventario por menos de <span class='grad'>$2,000</span>{FLAG}</h1>
<p>Electrónica directo de fábrica china. Te llevas desde 10 piezas de cada producto.</p></div>
<div class='g'>{tiles}</div>"""
    return slide(1, body, extra, logo=True)

# 2 · Cómo funciona
def s2():
    pasos = [
        ("Eliges producto y cuántas piezas", "Mínimo 10 piezas de cada caja, al mismo precio por pieza."),
        ("Apartas con el 20% por WhatsApp", "Tienes 7 días para pagar el resto y el envío."),
        ("Te llega por DHL Express asegurado", "Las cajas ya están en México: normalmente llega al día hábil siguiente."),
    ]
    items = "".join(f"<div class='p'><div class='c'>{i}</div><div><b>{t}</b><span>{d}</span></div></div>"
                    for i, (t, d) in enumerate(pasos, 1))
    extra = """
.w{position:absolute;left:56px;right:56px;top:170px}
.w h1{font-size:80px}
.p{display:flex;gap:28px;align-items:flex-start;background:#fff;border:1px solid var(--borde);border-radius:16px;
padding:38px 34px;margin-top:26px;box-shadow:0 6px 20px rgba(26,26,26,.06)}
.p:first-of-type{margin-top:48px}
.c{flex:none;width:64px;height:64px;border-radius:50%;background:var(--grad);color:#fff;font-weight:900;font-size:32px;
display:flex;align-items:center;justify-content:center}
.p b{display:block;font-size:36px;line-height:1.15}.p span{display:block;font-size:28px;color:var(--gris);margin-top:8px;line-height:1.35}
.pb{background:var(--durazno);border-left:6px solid var(--n);border-radius:12px;padding:26px 30px;margin-top:34px;
font-size:30px;color:var(--n9)}.pb b{color:var(--n7)}
"""
    body = f"""<div class='w'><div class='eyebrow'>Así funciona</div>
<h1>Sin contenedor. Sin importar. <span class='grad'>Sin esperar meses.</span></h1>{items}
<div class='pb'><b>Importante:</b> hay una sola caja de cada modelo. Cuando se acaba, se acaba.</div></div>"""
    return slide(2, body, extra)

# 3-6 · Productos por presupuesto (precio de 10 piezas)
TIER_CSS = """
.w{position:absolute;left:56px;right:56px;top:150px}
.w h1{font-size:72px;margin-top:6px}
.w .sub{font-size:28px;color:var(--gris);margin-top:10px}
.list{position:absolute;left:56px;right:56px;top:380px;bottom:120px;display:flex;flex-direction:column;gap:20px}
.list.g2{display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr}
.card{flex:1;background:#fff;border:1px solid var(--borde);border-radius:16px;box-shadow:0 6px 20px rgba(26,26,26,.08);
display:flex;overflow:hidden;min-height:0}
.card .ph{flex:none;width:42%;background-size:cover}
.g2 .card{flex-direction:column}.g2 .card .ph{width:100%;height:46%}
.tx{padding:22px 26px;display:flex;flex-direction:column;justify-content:center;flex:1}
.mod{font-size:20px;font-weight:700;letter-spacing:.08em;color:var(--n7)}
.nm{font-size:30px;font-weight:700;line-height:1.15;margin-top:4px}
.pp{font-weight:900;font-size:68px;letter-spacing:-.02em;line-height:1;margin-top:12px}
.pp small{font-size:22px;font-weight:400;letter-spacing:0;-webkit-text-fill-color:var(--gris);margin-left:8px}
.mn{margin-top:14px;align-self:flex-start;background:var(--grad);color:#fff;font-weight:700;border-radius:999px;padding:8px 18px;font-size:24px}
.cj{font-size:20px;color:var(--gris);margin-top:10px}
.g2 .tx{padding:18px 22px;justify-content:flex-start}
.g2 .nm{font-size:25px}.g2 .pp{font-size:56px;margin-top:8px}.g2 .mn{font-size:21px;margin-top:10px}
"""

def card(d):
    return f"""<div class='card'><div class='photo ph' style="background-image:url('{foto(d['code'])}')"></div>
<div class='tx'><div class='mod'>{d['model']}</div><div class='nm'>{d['name']}</div>
<div class='pp grad'>{d['pp']}<small>por pieza</small></div>
<div class='mn'>10 piezas: {d['min']}</div><div class='cj'>Quedan {d['pz']} en la caja</div></div></div>"""

def tier(n, eyebrow, titulo, sub, items):
    cls = "list g2" if len(items) == 4 else "list"
    body = f"""<div class='w'><div class='eyebrow'>{eyebrow}</div><h1>{titulo}</h1><div class='sub'>{sub}</div></div>
<div class='{cls}'>{''.join(card(d) for d in items)}</div>"""
    return slide(n, body, TIER_CSS)

# 7 · Confianza
def s7():
    pts = [
        "Te hacemos un acuerdo de compra por escrito.",
        "Recibos de cada pago con nuestro sello oficial.",
        "Te mandamos videos de tu pedido y hacemos videollamada contigo.",
        "Estamos en Monterrey, N.L.",
        "No usamos pago contra entrega.",
    ]
    items = "".join(f"<div class='ck'><span>✓</span>{p}</div>" for p in pts)
    extra = """
.w{position:absolute;left:56px;right:56px;top:170px}
.w h1{font-size:88px;margin-top:6px}
.box{background:#fff;border:1px solid var(--borde);border-radius:24px;padding:20px 36px;margin-top:48px;box-shadow:0 6px 20px rgba(26,26,26,.06)}
.ck{display:flex;gap:24px;align-items:center;font-size:34px;line-height:1.3;padding:32px 0;border-bottom:1px solid #EFE7E1}
.ck:last-child{border-bottom:0}
.ck span{flex:none;width:48px;height:48px;border-radius:50%;background:var(--grad);color:#fff;font-weight:900;font-size:26px;
display:flex;align-items:center;justify-content:center}
.sello{position:absolute;right:70px;bottom:120px;width:190px;transform:rotate(-8deg);opacity:.95}
"""
    body = f"""<div class='w'><div class='eyebrow'>Compra con confianza</div>
<h1>¿Cómo sé que <span class='grad'>es real?</span></h1><div class='box'>{items}</div></div>
<img class='sello' src='fotos/sello.png'>"""
    return slide(7, body, extra)

# 8 · CTA
def s8():
    mini = "".join(f"<div class='mi'><div class='photo' style=\"background-image:url('{foto(d['code'])}')\"></div><b>{d['pp']}</b></div>" for d in DATA)
    extra = """
.w{position:absolute;left:56px;right:56px;top:150px;text-align:center}
.w h1{font-size:104px}
.w p{font-size:32px;color:var(--gris);margin-top:14px}
.g{display:grid;grid-template-columns:repeat(6,1fr);gap:14px;margin-top:44px}
.mi .photo{height:150px;border-radius:12px;background-size:cover}
.mi b{display:block;font-size:26px;font-weight:900;color:var(--n6);margin-top:6px}
.dm{margin-top:48px;background:var(--grad);color:#fff;border-radius:24px;padding:40px 30px;box-shadow:0 8px 24px rgba(234,88,12,.3)}
.dm .a{font-size:48px;font-weight:900;letter-spacing:-.01em}
.dm .a span{background:#fff;color:var(--n6);border-radius:12px;padding:2px 16px;margin:0 4px}
.dm .b{font-size:28px;margin-top:14px}
.o{margin-top:34px;font-size:30px;line-height:1.4}.o b{color:var(--n7)}
.sv{margin-top:26px;font-size:26px;color:var(--gris)}
"""
    body = f"""<div class='w'><h1>¿Cuál te <span class='grad'>llevas?</span></h1>
<p>12 productos, mínimo 10 piezas de cada uno.</p><div class='g'>{mini}</div>
<div class='dm'><div class='a'>Mándanos DM con la palabra <span>CAJA</span></div>
<div class='b'>Te pasamos fotos, videos y te ayudamos a apartar.</div></div>
<div class='o'>O escríbenos por WhatsApp <b>81 2018 1761</b><br>o entra a <b>compraenfabricas.com/productos</b></div>
<div class='sv'>Guarda este post para cuando estés listo.</div></div>"""
    return slide(8, body, extra, swipe=False)

if __name__ == "__main__":
    out = {
        "K-01-hook": s1(),
        "K-02-como-funciona": s2(),
        "K-03-menos-de-2000": tier(3, "Si tienes menos de $2,000", "Empieza con <span class='grad'>10 piezas</span> de:", "Lo más barato para arrancar tu negocio.", tramo(0, 2000)),
        "K-04-menos-de-3500": tier(4, "Si tienes menos de $3,500", "Micrófonos y <span class='grad'>dashcam</span>", "Para creadores de contenido y conductores.", tramo(2000, 3500)),
        "K-05-menos-de-7000": tier(5, "Si tienes menos de $7,000", "Ventilador, cámara <span class='grad'>y reloj</span>", "Productos de mayor valor por pieza.", tramo(3500, 7000)),
        "K-06-para-ir-en-grande": tier(6, "Para ir en grande", "Lo más <span class='grad'>premium</span>", "Traductor con IA y cámara de bolsillo 4K.", tramo(7000, 10**9)),
        "K-07-confianza": s7(),
        "K-08-cta": s8(),
    }
    for k, v in out.items():
        with open(os.path.join(AQUI, f"_{k}.html"), "w") as f:
            f.write(v)
    json.dump(sorted(out), open(os.path.join(AQUI, "_lista_carrusel.json"), "w"))
    print(len(out), "slides")
