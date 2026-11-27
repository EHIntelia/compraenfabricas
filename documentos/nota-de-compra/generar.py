"""Genera la nota de compra de Compra en fábricas en HTML a partir de un JSON.

Uso:
  python3 generar.py datos.json salida.html
Después convierte el HTML a documento imprimible con:
  node a-pdf.js salida.html salida.pdf

El sello oficial NO está en el repositorio (es público). Pon tu copia en
assets/sello-oficial.png; si no existe, la nota sale sin sello.
"""
import base64, json, os, sys

AQUI = os.path.dirname(os.path.abspath(__file__))
R, O, K, GR = "#DC2626", "#F97316", "#1A1A1A", "#6B6B6B"
DUR, CREMA, BORDE = "#FCE4DC", "#FFF8F5", "#D9CFC7"
GRAD = "linear-gradient(90deg,#F97316,#DC2626)"


def b64(ruta):
    ruta = os.path.join(AQUI, ruta)
    if not os.path.exists(ruta):
        return None
    tipo = "jpeg" if ruta.lower().endswith((".jpg", ".jpeg")) else "png"
    return f"data:image/{tipo};base64," + base64.b64encode(open(ruta, "rb").read()).decode()


def m(x):
    return f"${x:,.2f}"


def generar(d):
    p = d["producto"]
    total_merc = round(p["piezas"] * p["precio_pieza"], 2)
    ops = [dict(o, total=round(total_merc + o["precio"], 2)) for o in d["envio"]["opciones"]]
    cell = f"border:1px solid {BORDE};padding:7px 9px;font-size:10pt"
    logo, foto, sello = b64("assets/logo-horizontal.png"), b64(p.get("foto", "")), b64("assets/sello-oficial.png")

    def h2(txt, n):
        b = (f"<span style='display:inline-block;width:22px;height:22px;border-radius:11px;background:{GRAD};"
             f"color:#fff;text-align:center;font-size:11pt;line-height:22px;margin-right:8px'>{n}</span>")
        return f"<h2 style='color:{K};font-size:13pt;margin:12px 0 6px'>{b}{txt}</h2>"

    def fila(concepto, valores, estilo=""):
        celdas = "".join(f"<td style='{cell};text-align:right'>{v}</td>" for v in valores)
        return f"<tr{estilo}><td style='{cell}'>{concepto}</td>{celdas}</tr>"

    cab = "".join(f"<td style='{cell};border-color:{K};text-align:right'><b>{o['nombre'].split(' · ')[0]}</b></td>" for o in ops)
    tot = "".join(f"<td style='{cell};border-color:{O};text-align:right'><b style='font-size:12pt'>{m(o['total'])}</b></td>" for o in ops)
    envio_cards = "".join(
        f"<td style='{cell};text-align:center'><b>{o['nombre']}</b><br><span style='font-size:14pt;font-weight:bold'>{m(o['precio'])}</span></td>"
        for o in ops)
    foto_td = f"<td style='{cell};width:150px;padding:4px'><img src='{foto}' style='width:145px;border-radius:6px;display:block'></td>" if foto else ""
    sello_img = (f"<img src='{sello}' style='position:absolute;left:50%;top:0;margin-left:-65px;width:130px;height:130px;"
                 f"opacity:.9;transform:rotate(-8deg)'>") if sello else ""
    c, pg = d["cliente"], d["pago"]
    blank = "______________________"
    return f"""<html><head><meta charset="utf-8"></head><body style="font-family:Arial;color:{K};font-size:10.5pt">
<table style='width:100%'><tr><td style='width:170px'>{f"<img src='{logo}' style='width:160px'>" if logo else ""}</td>
<td style='vertical-align:bottom;padding-left:10px'><h1 style="font-size:22pt;margin:0;font-weight:900;letter-spacing:-0.02em">Nota de compra</h1></td>
<td style='text-align:right;font-size:9.5pt;color:{GR};vertical-align:bottom'>Orden <b style='color:{K}'>{d['orden']}</b><br>{d['fecha']}</td></tr></table>
<div style='height:4px;background:{GRAD};border-radius:2px;margin:10px 0 12px'></div>
<p style='margin:0 0 4px'><b>Cliente:</b> {c['nombre']} · Tel.: {c['telefono']}</p>
<p style='margin:0'><b>Entrega en:</b> {c['direccion']}</p>
{h2("Tu pedido", 1)}
<table style='width:100%;border-collapse:collapse;background:{CREMA}'><tr>{foto_td}
<td style='{cell}'><b style='font-size:11.5pt'>{p['piezas']} {p['nombre']}</b><br><span style='color:{GR};font-size:9pt'>{p['descripcion']}</span></td>
<td style='{cell};text-align:right;white-space:nowrap'>{p['piezas']} × {m(p['precio_pieza'])}<br><b style='font-size:14pt;color:{R}'>{m(total_merc)}</b></td></tr></table>
<p style='font-size:9pt;color:{GR};margin:4px 0 0'>{p['nota']}</p>
{h2("Elige tu envío", 2)}
<p style='margin:0 0 6px'>{d['envio']['texto']}</p>
<table style='width:100%;border-collapse:collapse'><tr>{envio_cards}</tr></table>
{h2("Cuánto pagas", 3)}
<table style='width:100%;border-collapse:collapse'>
<tr style='background:{K};color:#fff'><td style='{cell};border-color:{K}'><b>Concepto</b></td>{cab}</tr>
{fila(f"{p['piezas']} {p['nombre']}", [m(total_merc)] * len(ops))}
{fila("Envío con seguro", [m(o['precio']) for o in ops])}
<tr style='background:{GRAD};color:#fff'><td style='{cell};border-color:{O}'><b>Total a pagar</b></td>{tot}</tr></table>
<p style='font-size:9pt;color:{GR};margin:4px 0 0'>Se paga en una sola exhibición, antes del envío.</p>
{h2("Datos para tu pago", 4)}
<table style='width:100%;border-collapse:collapse;background:{CREMA}'>
<tr><td style='{cell};width:38%'><b>Banco</b></td><td style='{cell}'>{pg['banco']}</td></tr>
<tr><td style='{cell}'><b>A nombre de</b></td><td style='{cell}'>{pg['titular']}</td></tr>
<tr><td style='{cell}'><b>{pg.get('etiqueta_cuenta', 'Cuenta')}</b></td><td style='{cell}'><b style='font-size:12pt;letter-spacing:0.04em'>{pg['cuenta']}</b></td></tr>
<tr><td style='{cell}'><b>Concepto</b></td><td style='{cell}'>{d['orden']} {c['nombre']}</td></tr></table>
<p style='font-size:9pt;color:{GR};margin:4px 0 0'>Haz tu transferencia por el total de la opción que elijas y mándanos tu comprobante por WhatsApp.</p>
<p style='font-size:9pt;margin:14px 0 0;background:{DUR};border-left:5px solid {O};border-radius:12px;padding:8px 10px'><b style='color:{R}'>Importante:</b> el pago se hace antes de enviar tu mercancía. La mercancía siempre viaja con seguro. Una vez que sale, la entrega y el rastreo los hace la paquetería según sus políticas.</p>
<div style='page-break-inside:avoid;margin-top:10px'><table style='width:100%'><tr>
<td style='width:50%;text-align:center;vertical-align:bottom;padding-top:40px'>{blank}<br>{c['nombre']}<br>Cliente</td>
<td style='width:50%;text-align:center;vertical-align:bottom'><div style='position:relative;height:130px'>{sello_img}
<div style='position:absolute;bottom:2px;width:100%;font-family:"Brush Script MT",cursive;font-size:15pt;color:#1b2a6b'>{d['firma']}</div></div>{blank}<br>{d['firma']}<br>Compra en fábricas</td></tr></table></div>
<p style='font-size:9pt;color:{GR};margin:10px 0 0;text-align:center'><i>Al realizar tu pago, aceptas esta nota de compra.</i> · compraenfabricas.com</p>
</body></html>"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python3 generar.py datos.json salida.html")
    datos = json.load(open(sys.argv[1], encoding="utf-8"))
    open(sys.argv[2], "w", encoding="utf-8").write(generar(datos))
    print("Listo:", sys.argv[2])
