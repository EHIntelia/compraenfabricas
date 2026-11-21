import os
import qrcode
from PIL import Image, ImageDraw
from pptx import Presentation
from pptx.util import Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

HERE = os.path.dirname(os.path.abspath(__file__))
IC = os.path.join(HERE, "icons")

BG = "0D0D0D"; CARD = "1A1A1A"; TIP = "222222"; REDCARD = "A0121D"; DARKRED = "241012"
RED = "C41424"; GOLD = "D4A547"; GRAY = "B5B5B5"; FOOT = "666666"; PINK = "F3D9DB"; WHITE = "FFFFFF"
H = "Arial"; B = "Calibri"
JAICO_URL = "https://info.joyeria.shop/"
SKOOL_URL = "https://www.skool.com/emprende-importando-4690/about"
FOOTER = "COMPRA EN FÁBRICAS DE CHINA  ·  EDUARDO HERNÁNDEZ"

# ---------- generated assets ----------
def make_icons():
    gold = (211, 165, 71, 255)
    # gem
    im = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(48, 92), (88, 40), (168, 40), (208, 92), (128, 220)], fill=gold)
    dark = (13, 13, 13, 255)
    d.line([(48, 92), (208, 92)], fill=dark, width=10)
    d.line([(88, 40), (104, 92), (128, 220)], fill=dark, width=8)
    d.line([(168, 40), (152, 92), (128, 220)], fill=dark, width=8)
    d.line([(104, 92), (128, 40), (152, 92)], fill=dark, width=8)
    im.save(os.path.join(IC, "gem.png"))
    # box
    im = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(128, 30), (226, 76), (128, 122), (30, 76)], fill=gold)
    d.polygon([(30, 92), (120, 136), (120, 230), (30, 186)], fill=gold)
    d.polygon([(136, 136), (226, 92), (226, 186), (136, 230)], fill=gold)
    im.save(os.path.join(IC, "box.png"))
    # graduation-ish: book
    im = Image.new("RGBA", (256, 256), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon([(128, 40), (240, 92), (128, 144), (16, 92)], fill=gold)
    d.polygon([(64, 122), (128, 152), (192, 122), (192, 182), (128, 212), (64, 182)], fill=gold)
    d.rectangle([222, 92, 232, 170], fill=gold)
    im.save(os.path.join(IC, "cap.png"))

def make_qr(url, name):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=0)
    q.add_data(url); q.make(fit=True)
    q.make_image(fill_color="black", back_color="white").save(os.path.join(HERE, name))

make_icons()
make_qr(JAICO_URL, "qr_jaico.png")
make_qr(SKOOL_URL, "qr_skool.png")

# ---------- helpers ----------
prs = Presentation()
prs.slide_width = Pt(720); prs.slide_height = Pt(405)
BLANK = prs.slide_layouts[6]
TOTAL = 22
state = {"n": 0}

def rgb(h): return RGBColor.from_string(h)

def new_slide(bg=BG, footer=True):
    s = prs.slides.add_slide(BLANK)
    state["n"] += 1
    f = s.background.fill; f.solid(); f.fore_color.rgb = rgb(bg)
    if footer:
        text(s, 36, 384, 400, 12, FOOTER, B, 9, FOOT)
        text(s, 600, 384, 84, 12, f"{state['n']} / {TOTAL}", B, 9, FOOT, align="r")
    return s

def rect(s, x, y, w, h, fill, r=6, shape=None):
    shp = s.shapes.add_shape(shape or (MSO_SHAPE.ROUNDED_RECTANGLE if r else MSO_SHAPE.RECTANGLE), Pt(x), Pt(y), Pt(w), Pt(h))
    if r and shape is None:
        shp.adjustments[0] = r / min(w, h)
    shp.fill.solid(); shp.fill.fore_color.rgb = rgb(fill)
    shp.line.fill.background(); shp.shadow.inherit = False
    shp.text_frame.text = ""
    return shp

def circle(s, x, y, d, fill):
    return rect(s, x, y, d, d, fill, shape=MSO_SHAPE.OVAL)

def icon(s, name, x, y, size):
    s.shapes.add_picture(os.path.join(IC, name + ".png"), Pt(x), Pt(y), Pt(size), Pt(size))

def icon_circle(s, name, x, y, d, fill=TIP, pad=0.25):
    circle(s, x, y, d, fill)
    icon(s, name, x + d * pad, y + d * pad, d * (1 - 2 * pad))

ALIGN = {"l": PP_ALIGN.LEFT, "c": PP_ALIGN.CENTER, "r": PP_ALIGN.RIGHT}
ANCH = {"t": MSO_ANCHOR.TOP, "m": MSO_ANCHOR.MIDDLE, "b": MSO_ANCHOR.BOTTOM}

def text(s, x, y, w, h, content, font=B, size=14, color=WHITE, bold=False, italic=False,
         align="l", anchor="t", spacing=None, space_after=0):
    """content: str | list of paragraphs; paragraph = str | list of runs (text, {opts})."""
    tb = s.shapes.add_textbox(Pt(x), Pt(y), Pt(w), Pt(h))
    tf = tb.text_frame; tf.word_wrap = True
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = ANCH[anchor]
    paras = content if isinstance(content, list) else [content]
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = ALIGN[align]
        if spacing: para.line_spacing = spacing
        para.space_after = Pt(space_after)
        runs = [(p, {})] if isinstance(p, str) else p
        for t, o in runs:
            r = para.add_run(); r.text = t
            f = r.font
            f.name = o.get("font", font); f.size = Pt(o.get("size", size))
            f.bold = o.get("bold", bold); f.italic = o.get("italic", italic)
            f.color.rgb = rgb(o.get("color", color))
    return tb

def eyebrow(s, t, color=GOLD):
    text(s, 36, 13, 600, 16, t, B, 12, color, bold=True)

def title(s, t, size=28):
    text(s, 36, 36, 648, 40, t, H, size, WHITE, bold=True, anchor="m")

def callout(s, y, label, head, body, fill=REDCARD, label_color=GOLD, body_color=PINK, h=61):
    rect(s, 36, y, 648, h, fill)
    text(s, 54, y + 12, 600, 14, label, B, 11, label_color, bold=True)
    text(s, 54, y + 33, 615, 20, [[(head + "  —  ", {"bold": True, "color": WHITE}), (body, {"color": body_color})]], B, 13)

def tipbox(s, y, label, body, h=44, fill=TIP, label_color=GOLD, size=13.5):
    rect(s, 36, y, 648, h, fill)
    text(s, 54, y, 626, h, [[(label + " ", {"bold": True, "color": label_color}), (body, {})]], B, size, anchor="m")

def qr_card(s, x, y, size, qr):
    rect(s, x, y, size, size, WHITE, r=12)
    pad = size * 0.09
    s.shapes.add_picture(os.path.join(HERE, qr), Pt(x + pad), Pt(y + pad), Pt(size - 2 * pad), Pt(size - 2 * pad))

E = "…"

# =============== 1. PORTADA ===============
s = new_slide()
circle(s, 518, -158, 432, "151515")
text(s, 43, 78, 600, 18, "CLASE EN VIVO  ·  COMPRA EN FÁBRICAS DE CHINA", B, 14, GOLD, bold=True)
text(s, 43, 104, 640, 64, "COMPRA E IMPORTA", H, 54, WHITE, bold=True)
text(s, 43, 174, 640, 64, "DIRECTO DE CHINA", H, 54, RED, bold=True)
text(s, 43, 247, 640, 22, "SIN INTERMEDIARIOS. SIN RODEOS. CON EL PROCESO COMPLETO.", B, 18, WHITE, bold=True)
text(s, 43, 283, 640, 18, "Con Eduardo Hernández  ·  26+ años importando de China  ·  300+ empresas asesoradas", B, 14, GRAY)
b = rect(s, 43, 320, 295, 44, "C41424", r=5)
text(s, 43, 320, 295, 44, "HOY PUEDE CAMBIAR TU NEGOCIO", H, 15, WHITE, bold=True, align="c", anchor="m")

# =============== 2. PROMESA ===============
s = new_slide()
eyebrow(s, "LA PROMESA DE HOY")
title(s, "Al terminar esta clase vas a saber" + E)
items = [("p2_0", "Encontrar proveedores REALES en China, no revendedores"),
         ("p2_1", "Pagarles de forma segura sin que te estafen"),
         ("p2_2", "Importar legal a tu país y calcular tus costos reales"),
         ("p2_3", "Vender tu producto y convertirlo en dinero")]
for i, (ic, t) in enumerate(items):
    y = 97 + i * 59
    icon_circle(s, ic, 43, y, 40)
    text(s, 97, y, 560, 40, t, B, 17, anchor="m")
rect(s, 36, 340, 648, 39, CARD)
text(s, 36, 340, 648, 39, [[("El mismo proceso completo, ", {}), ("de principio a fin, sin guardarnos nada.", {"bold": True, "color": GOLD})]], B, 15, align="c", anchor="m")

# =============== 3. POR QUÉ ESCUCHARME ===============
s = new_slide()
eyebrow(s, "¿POR QUÉ ESCUCHARME?")
title(s, "No te hablo de teoría. Te hablo de fábricas.", 26)
for i, (num, l1) in enumerate([("26+", "años importando\ndirecto de China"), ("300+", "empresas\nasesoradas"), ("5", "negocios propios\nfuncionando hoy")]):
    x = 36 + i * 223
    rect(s, x, 101, 202, 144, CARD)
    text(s, x, 118, 202, 64, num, H, 54, GOLD, bold=True, align="c")
    text(s, x, 197, 202, 34, l1.split("\n"), B, 13, GRAY, align="c")
text(s, 46, 283, 628, 44, [[("He caminado esas fábricas, he negociado en persona y he cometido los errores ", {}), ("para que tú no tengas que pagarlos.", {"bold": True, "color": RED})]], B, 17, align="c")

# =============== 4. CUÁL ERES ===============
s = new_slide()
eyebrow(s, "SÉ EXACTAMENTE CÓMO TE SIENTES", RED)
title(s, "¿Cuál de estos eres tú?", 30)
cards = [("p4_0", "TRABAJAS Y NO ALCANZA", "Quieres un ingreso extra real, no otro 'negocito' que muere en 3 meses."),
         ("p4_1", "QUIERES EMPRENDER", "Tienes las ganas, pero nadie te enseña el proceso completo y te da miedo que te estafen."),
         ("p4_2", "YA TIENES NEGOCIO O YA IMPORTAS", "Le compras a intermediarios que se quedan con TU margen" + E + " y lo sabes.")]
for i, (ic, h, t) in enumerate(cards):
    x = 36 + i * 223
    rect(s, x, 97, 202, 227, CARD)
    icon_circle(s, ic, x + 79, 115, 44)
    text(s, x + 14, 172, 174, 50, h, H, 14, GOLD, bold=True, align="c", anchor="m")
    text(s, x + 16, 246, 170, 60, t, B, 12.5, align="c")
text(s, 36, 347, 648, 22, "Escríbeme en el chat: ¿eres el 1, el 2 o el 3?", B, 16, RED, bold=True, italic=True, align="c")

# =============== 5. INTERMEDIARIO ===============
s = new_slide()
eyebrow(s, "LA VERDAD INCÓMODA", RED)
title(s, "El intermediario vive de que tú NO sepas esto", 26)
rect(s, 36, 97, 313, 231, CARD); rect(s, 371, 97, 313, 231, DARKRED)
text(s, 36, 114, 313, 20, "CON INTERMEDIARIOS", H, 16, GRAY, bold=True, align="c")
text(s, 371, 114, 313, 20, "DIRECTO A FÁBRICA", H, 16, GOLD, bold=True, align="c")
L = ["Cada eslabón le sube al precio", "No sabes qué fábrica lo hace", "Dependes de su inventario y su humor", "Tu margen se queda en SU bolsillo"]
R = ["Precio de fábrica, sin eslabones", "Hablas con quien lo produce", "Tú decides producto y volumen", "El margen completo es TUYO"]
for i in range(4):
    y = 144 + i * 45
    icon(s, "p5_0", 61, y, 22); text(s, 94, y, 240, 22, L[i], B, 12.5, anchor="m")
    icon(s, "p5_4", 396, y, 22); text(s, 428, y, 240, 22, R[i], B, 12.5, anchor="m")
text(s, 36, 341, 648, 36, [[("Ejemplo hipotético: un producto que en tu país cuesta $100, en fábrica puede costarte una fracción. ", {"color": GRAY}), ("Esa diferencia es tu negocio.", {"bold": True, "color": RED})]], B, 13.5, align="c")

# =============== 6. MAPA ===============
s = new_slide()
eyebrow(s, "EL MAPA COMPLETO")
title(s, "De tu idea a tu bodega: 6 pasos")
steps = [("p6_0", "1. ENCONTRAR", "Proveedores reales"), ("p6_1", "2. VALIDAR", "Y negociar"), ("p6_2", "3. PAGAR", "Sin estafas"),
         ("p6_3", "4. IMPORTAR", "Legal en tu país"), ("p6_4", "5. RECIBIR", "Logística y costos"), ("p6_5", "6. VENDER", "Y multiplicar")]
for i, (ic, h, t) in enumerate(steps):
    x = 36 + (i % 3) * 223; y = 104 + (i // 3) * 126
    rect(s, x, y, 202, 108, CARD)
    icon_circle(s, ic, x + 14, y + 15, 36)
    text(s, x + 61, y + 24, 140, 20, h, H, 15, bold=True)
    text(s, x + 61, y + 57, 140, 16, t, B, 12, GRAY)
text(s, 36, 352, 648, 20, "En cada paso te digo exactamente cómo hacerlo TÚ" + E + " sin guardarme nada.", B, 14, GOLD, bold=True, align="c")

# =============== 7. PASO 1 ===============
s = new_slide()
eyebrow(s, "PASO 1 DE 6")
title(s, "Encontrar proveedores chinos REALES")
text(s, 36, 92, 600, 18, "Las plataformas donde están las fábricas de verdad:", B, 15, GRAY)
plats = ["Alibaba", "1688.com", "Made-in-China", "Yiwugo", "Chinagoods", "AliExpress"]
for i, p in enumerate(plats):
    x = 36 + (i % 3) * 223; y = 122 + (i // 3) * 62
    rect(s, x, y, 202, 47, CARD)
    icon(s, f"p7_{i}", x + 18, y + 12, 23)
    text(s, x + 54, y, 144, 47, p, H, 16, bold=True, anchor="m")
tipbox(s, 256, "Tip de oro:", "1688.com es el mercado interno chino — ahí compran los propios chinos. Precios aún más bajos.")
callout(s, 313, "SEÑAL DE ALERTA", "OJO CON EL REVENDEDOR",
        "Sin fotos reales, sin empresa y con precio \"regalado\": sigue buscando.",
        fill=DARKRED, label_color=RED, body_color=GRAY)

# =============== 8. PASO 2 ===============
s = new_slide()
eyebrow(s, "PASO 2 DE 6")
title(s, "Contactar y validar: aquí se separan los pros", 26)
its = [("p8_0", "Pide fotos, videos y cotizaciones reales del producto"),
       ("p8_1", "Revisa estrellas e insignias de verificación de la plataforma"),
       ("p8_2", "Valida el TAX ID de la empresa ANTES de ordenar"),
       ("p8_3", "Negocia precio por volumen: en China TODO se negocia")]
for i, (ic, t) in enumerate(its):
    y = 94 + i * 52
    icon_circle(s, ic, 43, y, 38)
    text(s, 94, y, 580, 38, t, B, 16, anchor="m")
callout(s, 310, "REGLA DE ORO", "PRIMERO LA MUESTRA",
        "Nunca hagas un pedido grande sin probar una muestra. Es barata; el error, carísimo.",
        fill=DARKRED, label_color=GOLD, body_color=GRAY)

# =============== 9. PASO 3 ===============
s = new_slide()
eyebrow(s, "PASO 3 DE 6")
title(s, "Pagar sin miedo y sin estafas")
pays = [("WECHAT PAY", "Para muestras y montos chicos, directo con el proveedor"),
        ("ALIPAY", "El estándar en China para pagos rápidos y seguros"),
        ("TRANSFERENCIA B2B", "Empresa a empresa — debe pagar la empresa que va a importar")]
for i, (h, t) in enumerate(pays):
    y = 97 + i * 68.5
    rect(s, 36, y, 648, 57, CARD)
    text(s, 58, y + 10, 600, 18, h, H, 15, GOLD, bold=True)
    text(s, 58, y + 36, 600, 16, t, B, 13)
callout(s, 313, "MI CONSEJO", "EMPIEZA CHIQUITO",
        "Paga poco para muestras. Cuando ya confías en la fábrica, subes volumen y pagas por B2B.",
        fill=DARKRED, label_color=GOLD, body_color=GRAY)

# =============== 10. PASO 4 ===============
s = new_slide()
eyebrow(s, "PASO 4 DE 6")
title(s, "Importar legal: lo que nadie te explica")
legal = [("p10_0", "Empresa importadora", "Alta en Hacienda y Padrón de Importadores"),
         ("p10_1", "Encargo conferido", "Autorización para que el agente aduanal actúe por ti"),
         ("p10_2", "Cumplir las NOMs", "Normas del producto para que no se quede en la aduana"),
         ("p10_3", "Agente aduanal", "Tu aliado para liberar la mercancía sin dolores de cabeza")]
for i, (ic, h, t) in enumerate(legal):
    x = 36 + (i % 2) * 335; y = 97 + (i // 2) * 105
    rect(s, x, y, 313, 90, CARD)
    icon_circle(s, ic, x + 14, y + 15, 35)
    text(s, x + 61, y + 16, 240, 18, h, H, 14.5, bold=True)
    text(s, x + 61, y + 46, 240, 32, t, B, 11.5, GRAY)
tipbox(s, 317, "Tip con IA:", "pregúntale a ChatGPT o Claude los requisitos exactos para importar TU producto a TU país.")

# =============== 11. PASO 5 ===============
s = new_slide()
eyebrow(s, "PASO 5 DE 6")
title(s, "Traerlo a tu país: aéreo vs marítimo")
for i, (ic, h, t) in enumerate([("p11_0", "VÍA AÉREA", ["Se paga POR KILO.", "Rápido: ideal para muestras y producto ligero de alto valor."]),
                                 ("p11_1", "VÍA MARÍTIMA", ["Consolidado POR METRO CÚBICO o contenedor completo.", "El costo por pieza más bajo para volumen."])]):
    x = 36 + i * 335
    rect(s, x, 94, 313, 151, CARD)
    icon_circle(s, ic, x + 18, 108, 40)
    text(s, x + 72, 108, 230, 40, h, H, 17, GOLD, bold=True, anchor="m")
    text(s, x + 18, 175, 275, 55, t, B, 13)
text(s, 36, 262, 648, 36, [[("Pro tip: ", {"bold": True, "color": RED}), ("pide al proveedor que él arregle el envío al puerto o un contacto door-to-door con seguro. Ellos hacen la logística todos los días.", {})]], B, 14)
callout(s, 313, "GUARDA ESTA IDEA", "POR ESO LO CHIQUITO GANA",
        "Si el aéreo se cobra por kilo, lo que pesa poco y vale mucho llega rápido y barato.",
        fill=DARKRED, label_color=GOLD, body_color=GRAY)

# =============== 12. PASO 6 ===============
s = new_slide()
eyebrow(s, "PASO 6 DE 6")
title(s, "Ya llegó tu producto. Ahora: a venderlo")
sell = [("p12_0", "Graba TODO el proceso", "Del pedido al unboxing — ese contenido genera confianza y ventas"),
        ("p12_1", "Crea tu anuncio con IA", "Foto publicitaria con mensaje y llamado a la acción claros + video corto"),
        ("p12_2", "Pauta a WhatsApp Business", "Campañas en Meta directo a WhatsApp: cada mensaje es un cliente potencial")]
for i, (ic, h, t) in enumerate(sell):
    y = 94 + i * 72
    rect(s, 36, y, 648, 61, CARD)
    icon_circle(s, ic, 50, y + 11, 38)
    text(s, 104, y + 10, 560, 18, h, H, 15, bold=True)
    text(s, 104, y + 37, 560, 16, t, B, 12.5, GRAY)
text(s, 36, 326, 648, 20, "El producto barato es la mitad del juego. Saber venderlo es la otra mitad.", B, 15, GOLD, bold=True, italic=True, align="c")

# =============== 13. DOS CAMINOS ===============
s = new_slide()
eyebrow(s, "EL MOMENTO DE LA VERDAD", RED)
title(s, "Tienes 2 caminos frente a ti", 30)
rect(s, 36, 101, 313, 230, CARD); rect(s, 371, 101, 313, 230, REDCARD)
text(s, 36, 120, 313, 22, "CAMINO 1: SOLO", H, 17, GRAY, bold=True, align="c")
text(s, 371, 120, 313, 22, "CAMINO 2: CON JAICO", H, 17, GOLD, bold=True, align="c")
text(s, 61, 160, 263, 150, ["Con lo que aprendiste hoy y tu hoja de trabajo, PUEDES importar lo que tú quieras.", "",
                            "Te va a costar tiempo, prueba y error" + E + " pero es 100% posible. Yo empecé así."], B, 13.5, anchor="m")
text(s, 396, 160, 263, 150, ["Te saltas la parte difícil: vendes joyería que ya importamos nosotros, a precio de mayoreo.", "",
                             "Sin aduana, sin bodega, sin esperar meses. Tu primera venta, YA."], B, 13.5, anchor="m")
text(s, 36, 348, 648, 22, "Los dos caminos llegan. Uno llega mucho antes.", B, 16, bold=True, align="c")

# =============== 14. POR QUÉ JOYERÍA ===============
s = new_slide()
eyebrow(s, "MI RECOMENDACIÓN, DE IMPORTADOR A IMPORTADOR")
title(s, "Si hoy empezara de cero, empezaría con joyería", 26)
why = [("box", "Chiquita y ligera", "Llega en cajas, no en contenedores. Pesa poco y vale mucho: el envío casi no se nota."),
       ("p4_2", "Siempre se está vendiendo", "Cumpleaños, 14 de febrero, Día de las Madres, Navidad… y cualquier martes."),
       ("p15_1", "No necesitas bodega", "Tu inventario cabe en un cajón. Vendes desde casa, WhatsApp, Instagram o un bazar."),
       ("p2_1", "Margen que sí deja", "Una pieza chica se vende en varias veces lo que te costó. Cada venta deja ganancia real.")]
for i, (ic, h, t) in enumerate(why):
    x = 36 + (i % 2) * 335; y = 94 + (i // 2) * 112
    rect(s, x, y, 313, 98, CARD)
    icon_circle(s, ic, x + 16, y + 16, 40)
    text(s, x + 70, y + 18, 230, 20, h, H, 15, GOLD, bold=True)
    text(s, x + 70, y + 44, 230, 48, t, B, 12.5)
rect(s, 36, 324, 648, 47, TIP)
text(s, 54, 324, 615, 47, [[("Ejemplo hipotético: ", {"bold": True, "color": GOLD}),
                           ("te cuesta $25 y la vendes en $149. Multiplícalo por 100 piezas", {}),
                           (" — y caben en una caja.", {"bold": True, "color": RED})]], B, 13.5, anchor="m")

# =============== 15. JAICO ===============
s = new_slide()
eyebrow(s, "CAMINO 2  ·  JOYERÍA AL MAYOREO")
title(s, "Por qué te recomiendo vender con JAICO", 26)
s.shapes.add_picture(os.path.join(HERE, "jaico_logo_white.png"), Pt(36), Pt(90), height=Pt(26))
pts = [("Variedad enorme", "aretes, collares, pulseras, anillos y más — modelos nuevos todo el tiempo."),
       ("Mejores precios", "compramos directo en fábrica, sin intermediarios. Lo mismo que te enseñé hoy."),
       ("Buen margen para revender", "precios de mayoreo pensados para que TÚ ganes."),
       ("Sin complicarte", "ya está importada: eliges, recibes tus cajas y a vender.")]
for i, (h, t) in enumerate(pts):
    y = 132 + i * 48
    icon(s, f"p16_{i}", 36, y + 4, 26)
    text(s, 74, y, 420, 40, [[(h + ": ", {"bold": True, "color": GOLD}), (t, {})]], B, 14, anchor="m")
qr_card(s, 528, 100, 156, "qr_jaico.png")
text(s, 516, 264, 180, 18, "ESCANEA Y VE EL CATÁLOGO", H, 11.5, GOLD, bold=True, align="c")
text(s, 516, 282, 180, 16, "info.joyeria.shop", B, 13, GRAY, align="c")
rect(s, 36, 330, 648, 41, REDCARD)
text(s, 36, 330, 648, 41, "Tú pones las ganas de vender. Nosotros ponemos el producto, el precio y el margen.", B, 15, bold=True, align="c", anchor="m")

# =============== 16. ESCUELA: QUÉ INCLUYE ===============
s = new_slide()
eyebrow(s, "PARA LOS DOS CAMINOS  ·  ESCUELA EN SKOOL")
title(s, "Escuela de Negocios y Emprendimiento", 28)
text(s, 36, 80, 648, 18, "Todo lo que necesitas para construir y hacer crecer tu negocio, en un solo lugar.", B, 15, GRAY)
inc = [("p4_2", "De 0 a 1 Millón", "Construye tu negocio y diseña el camino para escalar"),
       ("p7_0", "Importación de China", "Trae producto de fábrica sin que te estafen"),
       ("p10_0", "Guía rápida", "Para importar de China y empezar ya"),
       ("p2_1", "Sube tus Ventas en 5 Pasos", "Vende más y multiplica resultados"),
       ("p12_0", "Zooms EN VIVO", "Cada fin de semana resuelvo TODAS tus dudas"),
       ("p8_3", "Comunidad", "Emprendedores como tú + contenido nuevo cada mes")]
for i, (ic, h, t) in enumerate(inc):
    x = 36 + (i % 3) * 223; y = 108 + (i // 3) * 104
    rect(s, x, y, 202, 92, CARD)
    icon_circle(s, ic, x + 14, y + 14, 34)
    text(s, x + 56, y + 14, 140, 34, h, H, 13, GOLD, bold=True, anchor="m")
    text(s, x + 14, y + 56, 178, 32, t, B, 12)
rect(s, 36, 324, 648, 47, TIP)
text(s, 54, 324, 615, 47, [[("No es teoría: ", {"bold": True, "color": GOLD}),
                           ("+26 años importando de China y 300+ empresas asesoradas. Aquí está el método.", {})]], B, 13.5, anchor="m")

# =============== 17. ESCUELA: CÓMO ENTRAR ===============
s = new_slide()
eyebrow(s, "CÓMO ENTRAR A LA ESCUELA")
title(s, "Entras gratis. Y por $15 USD desbloqueas mucho más.", 24)
tiers = [(CARD, GRAY, "GRATIS", "$0", ["Entras a la comunidad", "Conoces a emprendedores como tú", "Ves cómo funciona todo por dentro"]),
         (REDCARD, GOLD, "MEMBRESÍA", "$15 USD", ["Curso De 0 a 1 Millón INCLUIDO", "Curso Sube tus Ventas en 5 Pasos INCLUIDO", "El mejor punto de partida"]),
         (CARD, GRAY, "CURSOS PREMIUM", "a la carta", ["Importación de China completo: $230 USD", "Arma tu negocio con IA: $50 USD", "Guía rápida: $50 USD"])]
for i, (fill, lc, lab, price, lines) in enumerate(tiers):
    x = 36 + i * 162
    rect(s, x, 92, 150, 188, fill)
    text(s, x + 12, 104, 126, 14, lab, B, 11, lc, bold=True)
    text(s, x + 12, 120, 126, 30, price, H, 22 if i < 2 else 18, WHITE, bold=True, anchor="m")
    text(s, x + 12, 160, 130, 110, ["•  " + l for l in lines], B, 11.5, PINK if i == 1 else WHITE, space_after=6)
qr_card(s, 538, 92, 146, "qr_skool.png")
text(s, 526, 246, 170, 16, "ESCANEA Y ENTRA", H, 11.5, GOLD, bold=True, align="c")
text(s, 526, 263, 170, 14, "Entra gratis en Skool", B, 11, GRAY, align="c")
rect(s, 36, 296, 648, 75, DARKRED)
icon(s, "p2_3", 54, 316, 34)
text(s, 104, 300, 566, 67, [[("REGALO: LA GUÍA RÁPIDA YA ES TUYA. ", {"bold": True, "color": GOLD}),
                            ("Es justo esta clase. Entra a la Escuela y escríbele al staff para que te la habiliten — sin pagar los $50 USD.", {})]], B, 14, anchor="m")

# =============== 18. PERFILES ===============
s = new_slide()
eyebrow(s, "ESTO ES PARA TI SI" + E)
title(s, "Cada perfil gana algo distinto")
prof = [("p15_0", "EMPIEZAS DE CERO", "Arranca con joyería: inversión chica, sin bodega y vendes desde tu celular. La Escuela te lleva de la mano."),
        ("p15_1", "YA TIENES NEGOCIO", "Agrega joyería a tu tienda o mostrador: un ticket extra con buen margen — o arma la vuelta para un hijo, sobrino o tu pareja."),
        ("p15_2", "YA IMPORTAS", "Afina proveedores, costos y ventas con los cursos y los Zooms en vivo = MÁS utilidad.")]
for i, (ic, h, t) in enumerate(prof):
    x = 36 + i * 223
    rect(s, x, 97, 202, 216, CARD)
    icon_circle(s, ic, x + 79, 115, 44)
    text(s, x + 10, 178, 182, 24, h, H, 14, GOLD, bold=True, align="c", anchor="m")
    text(s, x + 16, 218, 170, 86, t, B, 12, align="c", anchor="m")
text(s, 36, 338, 648, 22, "No importa dónde empiezas. Importa que HOY decidas moverte.", B, 16, RED, bold=True, align="c")

# =============== 19. POR QUÉ NOSOTROS ===============
s = new_slide()
eyebrow(s, "POR QUÉ CON NOSOTROS SÍ")
title(s, "No es teoría. Es lo que hacemos todos los días.", 24)
chk = ["Compramos e importamos con este proceso HOY, no hace 10 años",
       "Visitamos fábricas en persona en China — proveedores de carne y hueso",
       "Te enseñamos todo el proceso aunque no nos compres nada",
       "Vendemos la joyería que te recomiendo: sabemos qué se mueve porque la movemos"]
for i, t in enumerate(chk):
    y = 104 + i * 54
    icon(s, f"p16_{i}", 43, y, 27)
    text(s, 86, y, 590, 27, t, B, 16, anchor="m")
tipbox(s, 324, "Transparencia total:", "si puedes hacerlo solo, hazlo solo. Nosotros estamos para acelerarte, no para amarrarte.", h=47, size=14)

# =============== 20-21. REGALOS ===============
def gift(eb, ttl, sub, items, foot, foot_r):
    s = new_slide(bg="000000", footer=False)
    text(s, 32, 69, 600, 14, eb, H, 10, RED, bold=True)
    text(s, 30, 112, 660, 34, ttl, H, 26, WHITE, bold=True)
    text(s, 32, 164, 640, 36, sub, H, 12, "CFCFCF")
    n = len(items); gap = 16; w = (656 - gap * (n - 1)) / n
    for i, (h, t) in enumerate(items):
        x = 27 + i * (w + gap)
        rect(s, x, 208, w, 105, "141414")
        circle(s, x + 16, 221, 30, REDCARD)
        text(s, x + 16, 221, 30, 30, str(i + 1), H, 15, "000000", bold=True, align="c", anchor="m")
        text(s, x + 59, 221, w - 70, 30, h, H, 15, RED, bold=True, anchor="m")
        text(s, x + 21, 278, w - 30, 16, t, H, 10, "E8E8E8")
    text(s, 32, 328, 656, 16, foot, H, 11, WHITE, bold=True, italic=True)
    text(s, 32, 384, 300, 9, "Compra en Fábricas de China", H, 6, "9A9A9A")
    text(s, 450, 384, 238, 9, f"{foot_r}  ·  {state['n']} / {TOTAL}", H, 6, "9A9A9A", align="r")

gift("REGALO 1 DE 2 · POR ESTAR HOY AQUÍ", "Te regalamos 3 proveedores directos de China",
     "Contactos directos en Yiwu, la ciudad de los mercados mayoristas más grande de China. Puedes escribirles HOY MISMO.",
     [("Grace", "30,000+ productos de uso diario"), ("Wilhem", "10,000+ artículos a precio de fábrica"), ("Vincent", "30,000+ productos · todo en uno")],
     "Da clic al enlace en el chat y llévate los 3 contactos con sus videos. Y todavía falta el regalo 2.", "Regalo · 3 proveedores")
gift("REGALO 2 DE 2 · PROVEEDORES DE TECNOLOGÍA", "Y 2 proveedores más de TECNOLOGÍA",
     "Son los mismos proveedores que ves en los videos de Eduardo. Electrónica directo de fábrica, sin intermediarios.",
     [("ELECTRÓNICA", "Relojes, audífonos, bocinas y cámaras deportivas"), ("GADGETS Y NOVEDADES", "Lentes con IA, traductores, dashcams y accesorios")],
     "En el grupo de WhatsApp te enviamos la guía y el WeChat de estos 2 proveedores.", "Regalo · 2 proveedores de tecnología")

# =============== 22. CIERRE ===============
s = new_slide()
text(s, 36, 40, 648, 90, [[("Puedes hacerlo todo ", {}), ("tú solo", {"color": GOLD}), (".", {})],
                          [("O empezar hoy ", {}), ("con ventaja", {"color": RED}), (".", {})]], H, 34, WHITE, bold=True, align="c")
text(s, 36, 128, 648, 20, "Lo único que no puedes hacer" + E + " es quedarte donde estás.", B, 15, GRAY, italic=True, align="c")
for i, (fill, lab, h, t, qr) in enumerate([(REDCARD, "VENDE JOYERÍA", "JAICO", "info.joyeria.shop", "qr_jaico.png"),
                                            (CARD, "APRENDE CONMIGO", "ESCUELA", "Entra gratis en Skool", "qr_skool.png")]):
    x = 76 + i * 296
    rect(s, x, 162, 272, 206, fill)
    qr_card(s, x + 16, 178, 128, qr)
    text(s, x + 156, 196, 106, 14, lab, B, 11, GOLD, bold=True)
    text(s, x + 156, 214, 112, 30, h, H, 20, WHITE, bold=True)
    text(s, x + 156, 252, 106, 60, t, B, 12.5, PINK if i == 0 else GRAY)
    text(s, x + 16, 318, 240, 40, "Escanea con la cámara de tu celular", B, 11.5, WHITE if i == 0 else GRAY, anchor="m")

assert state["n"] == TOTAL, state["n"]
out = os.path.join(HERE, "CLASE_EN_VIVO_JOYERIA_ESCUELA_v3.pptx")
prs.save(out); print("saved", out)
