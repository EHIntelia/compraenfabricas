"""Genera el acuerdo de compra de Compra en fábricas en HTML a partir de un JSON.

Uso:
  python3 generar.py datos.json salida.html
Después convierte el HTML a documento imprimible con:
  node a-pdf.js salida.html salida.pdf

Sello: usa assets/sello-oficial.png si existe; si no, el sello oficial naranja
del design system (design-system/artefacto/assets/sellos/sello-directo-de-fabrica.png).
El acuerdo siempre lleva el sello y las políticas de envío y devoluciones.
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


SELLO_DS = "../../design-system/artefacto/assets/sellos/sello-directo-de-fabrica.png"

# Políticas de envío y devoluciones (fuente: compraenfabricas.com/politicas-envio-devoluciones).
POLITICAS = [
    ("Apartado", "Apartas con un anticipo del 20%. Tienes 7 días naturales después de apartar para hacer el pago final: el 80% restante más el envío."),
    ("Envío", "Enviamos por DHL Express con la mercancía asegurada, una guía por caja. El costo depende del peso y del destino y te lo confirmamos antes de tu pago final. Normalmente llega al día hábil siguiente; en zonas con cobertura extendida de DHL puede tardar días adicionales. Te compartimos la guía de rastreo y, una vez que la caja sale, el traslado y la entrega se rigen por las políticas de DHL."),
    ("Cancelaciones", "El anticipo no es reembolsable si cambias de opinión: queda como crédito a tu favor, sin fecha límite, para cualquier caja disponible, la clase en vivo, la validación de proveedores, la asesoría o joyería JAICO."),
    ("Si nosotros no cumplimos", "Si no podemos entregarte la mercancía que apartaste (por ejemplo, por un error nuestro de inventario), te devolvemos el 100% de lo que pagaste."),
    ("Piezas dañadas o faltantes", "Avísanos dentro de las 48 horas siguientes a recibir tu paquete, con fotos o un video de la caja al abrirla. No reponemos piezas: te devolvemos en efectivo el valor de cada pieza afectada según su precio por pieza."),
]


def m(x):
    return f"${x:,.2f}"


def generar(d):
    p = d["producto"]
    total_merc = round(p["piezas"] * p["precio_pieza"], 2)
    ops = [dict(o, total=round(total_merc + o["precio"], 2)) for o in d["envio"]["opciones"]]
    cell = f"border:1px solid {BORDE};padding:7px 9px;font-size:10pt"
    logo, foto = b64("assets/logo-horizontal.png"), b64(p.get("foto", ""))
    sello = b64("assets/sello-oficial.png") or b64(SELLO_DS)

    def h2(txt, n):
        b = (f"<span style='display:inline-block;width:22px;height:22px;border-radius:11px;background:{GRAD};"
             f"color:#fff;text-align:center;font-size:11pt;line-height:22px;margin-right:8px'>{n}</span>")
        return f"<h2 style='color:{K};font-size:13pt;margin:10px 0 5px'>{b}{txt}</h2>"

    def fila(concepto, valores, estilo=""):
        celdas = "".join(f"<td style='{cell};text-align:right'>{v}</td>" for v in valores)
        return f"<tr{estilo}><td style='{cell}'>{concepto}</td>{celdas}</tr>"

    cab = "".join(f"<td style='{cell};border-color:{K};text-align:right'><b>{o['nombre'].split(' · ')[0] if len(ops) > 1 else 'Monto'}</b></td>" for o in ops)
    tot = "".join(f"<td style='{cell};border-color:{O};text-align:right'><b style='font-size:12pt'>{m(o['total'])}</b></td>" for o in ops)
    envio_cards = "".join(
        f"<td style='{cell};text-align:center'><b>{o['nombre']}</b><br><span style='font-size:14pt;font-weight:bold'>{m(o['precio'])}</span></td>"
        for o in ops)
    foto_td = f"<td style='{cell};width:150px;padding:4px'><img src='{foto}' style='width:145px;border-radius:6px;display:block'></td>" if foto else ""
    sello_img = (f"<img src='{sello}' style='position:absolute;left:50%;top:0;margin-left:-65px;width:130px;height:130px;"
                 f"opacity:.9;transform:rotate(-8deg)'>") if sello else ""
    c, pg = d["cliente"], d["pago"]
    titulo = d.get("titulo", "Acuerdo de compra")
    pie_doc = ("esta " if titulo.lower().startswith("nota") else "este ") + titulo.lower()
    cliente_linea = " · ".join([c["nombre"]] + ([f"Tel.: {c['telefono']}"] if c.get("telefono") else [])
                               + ([f"Correo: {c['correo']}"] if c.get("correo") else []))
    pols = d.get("politicas", POLITICAS)
    bloque_politicas = ("" if not pols else h2("Políticas de envío y devoluciones", 5)
        + "<ul style='margin:0;padding-left:18px;font-size:9pt;line-height:1.45'>"
        + "".join(f"<li style='margin:0 0 3px'><b>{t}:</b> {x}</li>" for t, x in pols)
        + f"</ul><p style='font-size:8.5pt;color:{GR};margin:3px 0 0'>Políticas completas: compraenfabricas.com/politicas-envio-devoluciones</p>")
    ne = d["envio"].get("nota")
    nota_envio = f"<p style='font-size:9pt;color:{GR};margin:4px 0 0'>{ne}</p>" if ne else ""
    ap = d.get("apartado")
    if ap:
        total = ops[0]["total"]
        resto = round(total - ap["monto"], 2)
        celda = f"{cell};text-align:right"
        bloque_pago = (f"<table style='width:100%;border-collapse:collapse;margin-top:8px;background:{CREMA}'>"
            f"<tr><td style='{cell}'><b>Para apartar tu pedido ({ap['porcentaje']}%)</b></td><td style='{celda}'><b style='font-size:12pt;color:{R}'>{m(ap['monto'])}</b></td></tr>"
            f"<tr><td style='{cell}'><b>Resto + envío</b>, a más tardar {ap['dias']} días después de apartar</td><td style='{celda}'><b style='font-size:12pt'>{m(resto)}</b></td></tr></table>"
            f"<p style='font-size:9pt;color:{GR};margin:4px 0 0'>Puedes apartar con el {ap['porcentaje']}% ({m(ap['monto'])}) y tienes {ap['dias']} días para liquidar el resto más el envío. "
            f"También puedes pagar el total de una vez. Tu pedido sale cuando está liquidado.</p>")
        instruccion_pago = "Haz tu transferencia por el apartado o por el total y mándanos tu comprobante por WhatsApp."
    else:
        bloque_pago = f"<p style='font-size:9pt;color:{GR};margin:4px 0 0'>Se paga en una sola exhibición, antes del envío.</p>"
        instruccion_pago = ("Haz tu transferencia por el total de la opción que elijas y mándanos tu comprobante por WhatsApp."
                            if len(ops) > 1 else "Haz tu transferencia por el total y mándanos tu comprobante por WhatsApp.")
    blank = "______________________"
    return f"""<html><head><meta charset="utf-8"></head><body style="font-family:Arial;color:{K};font-size:10.5pt">
<table style='width:100%'><tr><td style='width:170px'>{f"<img src='{logo}' style='width:160px'>" if logo else ""}</td>
<td style='vertical-align:bottom;padding-left:10px'><h1 style="font-size:22pt;margin:0;font-weight:900;letter-spacing:-0.02em">{d.get('titulo', 'Acuerdo de compra')}</h1></td>
<td style='text-align:right;font-size:9.5pt;color:{GR};vertical-align:bottom'>Orden <b style='color:{K}'>{d['orden']}</b><br>{d['fecha']}</td></tr></table>
<div style='height:4px;background:{GRAD};border-radius:2px;margin:10px 0 12px'></div>
<p style='margin:0 0 4px'><b>Cliente:</b> {cliente_linea}</p>
<p style='margin:0'><b>Entrega en:</b> {c['direccion']}</p>
{h2("Tu pedido", 1)}
<table style='width:100%;border-collapse:collapse;background:{CREMA}'><tr>{foto_td}
<td style='{cell}'><b style='font-size:11.5pt'>{p['piezas']} {p['nombre']}</b><br><span style='color:{GR};font-size:9pt'>{p['descripcion']}</span></td>
<td style='{cell};text-align:right;white-space:nowrap'>{p['piezas']} × {m(p['precio_pieza'])}<br><b style='font-size:14pt;color:{R}'>{m(total_merc)}</b></td></tr></table>
<p style='font-size:9pt;color:{GR};margin:4px 0 0'>{p['nota']}</p>
{h2("Elige tu envío" if len(ops) > 1 else "Tu envío", 2)}
<p style='margin:0 0 6px'>{d['envio']['texto']}</p>
<table style='width:100%;border-collapse:collapse'><tr>{envio_cards}</tr></table>{nota_envio}
{h2("Cuánto pagas", 3)}
<table style='width:100%;border-collapse:collapse'>
<tr style='background:{K};color:#fff'><td style='{cell};border-color:{K}'><b>Concepto</b></td>{cab}</tr>
{fila(f"{p['piezas']} {p['nombre']}", [m(total_merc)] * len(ops))}
{fila(d['envio'].get('concepto', 'Envío con seguro'), [m(o['precio']) for o in ops])}
<tr style='background:{GRAD};color:#fff'><td style='{cell};border-color:{O}'><b>Total a pagar</b></td>{tot}</tr></table>
{bloque_pago}
{h2("Datos para tu pago", 4)}
<table style='width:100%;border-collapse:collapse;background:{CREMA}'>
<tr><td style='{cell};width:38%'><b>Banco</b></td><td style='{cell}'>{pg['banco']}</td></tr>
<tr><td style='{cell}'><b>A nombre de</b></td><td style='{cell}'>{pg['titular']}</td></tr>
<tr><td style='{cell}'><b>{pg.get('etiqueta_cuenta', 'Cuenta')}</b></td><td style='{cell}'><b style='font-size:12pt;letter-spacing:0.04em'>{pg['cuenta']}</b></td></tr>
<tr><td style='{cell}'><b>Concepto</b></td><td style='{cell}'>{d['orden']} {c['nombre']}</td></tr></table>
<p style='font-size:9pt;color:{GR};margin:4px 0 0'>{instruccion_pago}</p>
{bloque_politicas}
<p style='font-size:9pt;margin:10px 0 0;background:{DUR};border-left:5px solid {O};border-radius:12px;padding:8px 10px'><b style='color:{R}'>Importante:</b> el pago se hace antes de enviar tu mercancía. La mercancía siempre viaja con seguro. Una vez que sale, la entrega y el rastreo los hace la paquetería según sus políticas.</p>
<div style='page-break-inside:avoid;margin-top:4px'><table style='width:100%'><tr>
<td style='width:50%;text-align:center;vertical-align:bottom;padding-top:30px'>{blank}<br>{c['nombre']}<br>Cliente</td>
<td style='width:50%;text-align:center;vertical-align:bottom'><div style='position:relative;height:130px'>{sello_img}
<div style='position:absolute;bottom:2px;width:100%;font-family:"Brush Script MT",cursive;font-size:15pt;color:#1b2a6b'>{d['firma']}</div></div>{blank}<br>{d['firma']}<br>Compra en fábricas</td></tr></table></div>
<p style='font-size:9pt;color:{GR};margin:6px 0 0;text-align:center'><i>Al realizar tu pago, aceptas {pie_doc}.</i> · compraenfabricas.com</p>
</body></html>"""


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit("Uso: python3 generar.py datos.json salida.html")
    datos = json.load(open(sys.argv[1], encoding="utf-8"))
    open(sys.argv[2], "w", encoding="utf-8").write(generar(datos))
    print("Listo:", sys.argv[2])
