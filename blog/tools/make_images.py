"""Genera las imágenes del blog (SVG -> PNG -> WebP) con la identidad de Compra en Fábricas de China.

Uso: python3 tools/make_images.py   (desde la carpeta blog/)
Salida: img/<slug>/<archivo>.webp  +  img/manifest.json (nombre, tamaño y alt de cada imagen)
"""
import io, json, os
import cairosvg
from PIL import Image

NAR, ROJO, TINTA, GRIS = "#F97316", "#DC2626", "#1A1A1A", "#6B6B6B"
DUR, CREMA, BORDE, BLANCO = "#FCE4DC", "#FFF8F5", "#D9CFC7", "#FFFFFF"
FONT = "Inter, DejaVu Sans, sans-serif"
OUT = os.path.join(os.path.dirname(__file__), "..", "img")
manifest = []


def esc(t):
    return t.replace("&", "y").replace("<", "").replace(">", "")


def wrap(text, max_chars):
    lines, cur = [], ""
    for w in text.split():
        if len(cur) + len(w) + (1 if cur else 0) <= max_chars:
            cur = f"{cur} {w}".strip()
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def defs():
    return f"""<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{NAR}"/><stop offset="1" stop-color="{ROJO}"/></linearGradient>
<linearGradient id="gh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{NAR}"/><stop offset="1" stop-color="{ROJO}"/></linearGradient>
<filter id="sh" x="-10%" y="-10%" width="120%" height="130%"><feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="{ROJO}" flood-opacity="0.16"/></filter>
</defs>"""


def text_lines(lines, x, y, size, weight=800, fill=TINTA, lh=1.15, anchor="start"):
    out = []
    for i, l in enumerate(lines):
        out.append(f'<text x="{x}" y="{y + i * size * lh:.0f}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{esc(l)}</text>')
    return "\n".join(out)


def logo(x, y, scale=1.0, light=False):
    ink = BLANCO if light else TINTA
    sub = BLANCO if light else GRIS
    s = scale
    return f"""<g transform="translate({x},{y}) scale({s})">
<rect width="44" height="44" rx="11" fill="url(#g)"/>
{zhong(22, 22, 1.0, "#fff")}
<text x="58" y="20" font-family="{FONT}" font-size="18" font-weight="800" fill="{ink}">Compra en Fábricas de China</text>
<text x="58" y="40" font-family="{FONT}" font-size="14" font-weight="600" fill="{sub}">Xijiao Shops</text>
</g>"""


def zhong(cx, cy, k, color):
    # caracter 中 dibujado con trazos (no hay fuente CJK en el sistema)
    w, h, sw = 18*k, 11*k, 3.2*k
    return (f'<g fill="none" stroke="{color}" stroke-width="{sw:.1f}" stroke-linecap="round" stroke-linejoin="round">'
            f'<rect x="{cx-w/2:.1f}" y="{cy-h/2-1*k:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{1.2*k:.1f}"/>'
            f'<line x1="{cx:.1f}" y1="{cy-12*k:.1f}" x2="{cx:.1f}" y2="{cy+12*k:.1f}"/></g>')


def star(cx, cy, r, fill):
    # rombo dibujado con path (el carácter estrella no existe en la fuente)
    return f'<path d="M{cx},{cy-r} L{cx+r*0.6},{cy} L{cx},{cy+r} L{cx-r*0.6},{cy} Z" fill="{fill}"/>'


def badge(x, y, label, size=18):
    w = len(label) * size * 0.8 + 40
    return f'<rect x="{x}" y="{y}" width="{w:.0f}" height="{size*2:.0f}" rx="{size}" fill="{DUR}"/><text x="{x+18}" y="{y+size*1.36:.0f}" font-family="{FONT}" font-size="{size}" font-weight="800" fill="{ROJO}" letter-spacing="1">{esc(label.upper())}</text>'


def save(slug, name, svg, w, h, alt, kind):
    os.makedirs(os.path.join(OUT, slug), exist_ok=True)
    png = cairosvg.svg2png(bytestring=svg.encode("utf-8"), output_width=w, output_height=h)
    im = Image.open(io.BytesIO(png)).convert("RGB")
    path = os.path.join(OUT, slug, name)
    im.save(path, "WEBP", quality=86, method=6)
    manifest.append({"slug": slug, "file": name, "path": f"/blog/{slug}/{name}", "width": w, "height": h, "kind": kind, "alt": alt, "bytes": os.path.getsize(path)})


# ---------- ilustraciones simples por tema (lado derecho de la portada) ----------
def art_boxes(x, y):
    # cajas apiladas + avión/barco simplificado
    g = [f'<g transform="translate({x},{y})">']
    g.append(f'<circle cx="190" cy="190" r="185" fill="url(#g)" opacity="0.12"/>')
    for i, (bx, by, s) in enumerate([(60, 200, 120), (190, 200, 120), (125, 90, 120)]):
        g.append(f'<rect x="{bx}" y="{by}" width="{s}" height="{s}" rx="10" fill="{BLANCO}" stroke="{NAR}" stroke-width="4" filter="url(#sh)"/>')
        g.append(f'<rect x="{bx+s/2-10}" y="{by}" width="20" height="{s}" fill="{DUR}"/>')
        g.append(zhong(bx+s/2, by+s/2, 1.7, ROJO) if i == 2 else "")
    g.append(f'<path d="M20,350 C120,300 260,300 360,350" stroke="{ROJO}" stroke-width="4" fill="none" stroke-dasharray="10 10"/>')
    g.append(f'<g transform="translate(320,326)"><path d="M0,24 L46,24 L40,36 L6,36 Z" fill="{ROJO}"/><rect x="10" y="10" width="12" height="14" fill="{NAR}"/><rect x="24" y="4" width="12" height="20" fill="{NAR}"/></g>')
    g.append("</g>")
    return "\n".join(g)


def art_numbers(x, y, items):
    g = [f'<g transform="translate({x},{y})">']
    for i, (num, lab) in enumerate(items):
        cx, cy = (i % 2) * 200, (i // 2) * 170
        g.append(f'<rect x="{cx}" y="{cy}" width="185" height="150" rx="22" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2" filter="url(#sh)"/>')
        g.append(f'<text x="{cx+92}" y="{cy+76}" font-family="{FONT}" font-size="52" font-weight="900" fill="url(#gh)" text-anchor="middle">{esc(num)}</text>')
        for j, l in enumerate(wrap(lab, 16)):
            g.append(f'<text x="{cx+92}" y="{cy+108+j*20}" font-family="{FONT}" font-size="17" font-weight="600" fill="{GRIS}" text-anchor="middle">{esc(l)}</text>')
    g.append("</g>")
    return "\n".join(g)


def art_checklist(x, y, items):
    g = [f'<g transform="translate({x},{y})"><rect width="380" height="{70+len(items)*58}" rx="24" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2" filter="url(#sh)"/>']
    g.append(f'<rect width="380" height="56" rx="24" fill="url(#gh)"/><rect y="30" width="380" height="26" fill="url(#gh)"/>')
    g.append(f'<text x="24" y="37" font-family="{FONT}" font-size="20" font-weight="800" fill="#fff">Antes de pagar un curso</text>')
    for i, it in enumerate(items):
        yy = 92 + i * 58
        g.append(f'<circle cx="40" cy="{yy}" r="15" fill="{DUR}"/><path d="M32,{yy} l6,6 l11,-12" stroke="{ROJO}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<text x="70" y="{yy+7}" font-family="{FONT}" font-size="20" font-weight="700" fill="{TINTA}">{esc(it)}</text>')
    g.append("</g>")
    return "\n".join(g)


def art_tech_vs_jewel(x, y):
    g = [f'<g transform="translate({x},{y})">']
    # tarjeta electrónica
    g.append(f'<rect x="0" y="40" width="175" height="300" rx="22" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2" filter="url(#sh)"/>')
    g.append(f'<rect x="52" y="90" width="70" height="110" rx="35" fill="none" stroke="{TINTA}" stroke-width="6"/><circle cx="62" cy="200" r="18" fill="{TINTA}"/><circle cx="112" cy="200" r="18" fill="{TINTA}"/>')
    g.append(f'<text x="87" y="262" font-family="{FONT}" font-size="20" font-weight="800" fill="{TINTA}" text-anchor="middle">Electrónica</text><text x="87" y="290" font-family="{FONT}" font-size="15" font-weight="600" fill="{GRIS}" text-anchor="middle">novedad</text>')
    # tarjeta joyería (destacada)
    g.append(f'<rect x="195" y="0" width="185" height="340" rx="22" fill="url(#g)" filter="url(#sh)"/>')
    g.append(f'<circle cx="287" cy="120" r="48" fill="none" stroke="#fff" stroke-width="9"/>{star(287, 62, 22, "#fff")}')
    g.append(f'<text x="287" y="232" font-family="{FONT}" font-size="22" font-weight="900" fill="#fff" text-anchor="middle">Joyería</text><text x="287" y="262" font-family="{FONT}" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">más margen</text><text x="287" y="284" font-family="{FONT}" font-size="15" font-weight="700" fill="#fff" text-anchor="middle">menos envío</text>')
    g.append("</g>")
    return "\n".join(g)


def art_jewel(x, y):
    g = [f'<g transform="translate({x},{y})"><circle cx="190" cy="180" r="180" fill="url(#g)" opacity="0.12"/>']
    g.append(f'<path d="M70,120 Q190,300 310,120" stroke="{NAR}" stroke-width="6" fill="none"/>')
    g.append(f'<circle cx="190" cy="232" r="30" fill="#fff" stroke="{ROJO}" stroke-width="6"/>{star(190, 232, 16, ROJO)}')
    g.append(f'<circle cx="100" cy="300" r="34" fill="none" stroke="{TINTA}" stroke-width="7"/><circle cx="100" cy="266" r="9" fill="{NAR}"/>')
    g.append(f'<circle cx="290" cy="300" r="26" fill="none" stroke="{ROJO}" stroke-width="7"/><circle cx="330" cy="300" r="26" fill="none" stroke="{NAR}" stroke-width="7"/>')
    g.append(f'<rect x="20" y="40" width="120" height="44" rx="22" fill="{BLANCO}" stroke="{BORDE}" filter="url(#sh)"/><text x="80" y="69" font-family="{FONT}" font-size="18" font-weight="800" fill="{ROJO}" text-anchor="middle">Mayoreo</text>')
    g.append("</g>")
    return "\n".join(g)


# ---------- plantillas ----------
def cover(slug, name, cat, title, kicker, art, alt):
    lines = wrap(title, 22)
    size = 58 if len(lines) <= 3 else 50
    if len(lines) > 4:
        lines = wrap(title, 26); size = 44
    y0 = 200
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">{defs()}
<rect width="1200" height="630" fill="{CREMA}"/>
<rect x="0" y="0" width="1200" height="10" fill="url(#gh)"/>
<circle cx="1180" cy="-40" r="220" fill="url(#g)" opacity="0.10"/>
{logo(64, 46)}
{badge(64, 128, cat)}
{text_lines(lines, 64, y0 + size, size, 900)}
<text x="64" y="{y0 + size + len(lines)*size*1.15 + 26:.0f}" font-family="{FONT}" font-size="24" font-weight="600" fill="{GRIS}">{esc(kicker)}</text>
<rect x="64" y="560" width="300" height="8" rx="4" fill="url(#gh)"/>
<text x="64" y="600" font-family="{FONT}" font-size="18" font-weight="700" fill="{TINTA}">compraenfabricas.com/blog</text>
{art}
</svg>"""
    save(slug, name, svg, 1200, 630, alt, "portada")


def social(slug, name, cat, title, kicker, alt):
    lines = wrap(title, 18)
    size = 76 if len(lines) <= 4 else 64
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1080" viewBox="0 0 1080 1080">{defs()}
<rect width="1080" height="1080" fill="url(#g)"/>
<circle cx="980" cy="120" r="260" fill="#fff" opacity="0.08"/><circle cx="60" cy="1000" r="300" fill="#fff" opacity="0.06"/>
{logo(80, 80, 1.3, light=True)}
<rect x="80" y="230" width="{len(cat)*14+56:.0f}" height="48" rx="24" fill="#fff"/><text x="108" y="263" font-family="{FONT}" font-size="22" font-weight="800" fill="{ROJO}" letter-spacing="1">{esc(cat.upper())}</text>
{text_lines(lines, 80, 360 + size, size, 900, fill="#fff")}
<text x="80" y="{360 + size + len(lines)*size*1.15 + 40:.0f}" font-family="{FONT}" font-size="32" font-weight="600" fill="#fff" opacity="0.92">{esc(kicker)}</text>
<rect x="80" y="960" width="920" height="2" fill="#fff" opacity="0.4"/>
<text x="80" y="1012" font-family="{FONT}" font-size="28" font-weight="800" fill="#fff">Lee la nota en compraenfabricas.com/blog</text>
</svg>"""
    save(slug, name, svg, 1080, 1080, alt, "redes")


def frame(title, subtitle, body, note=""):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="675" viewBox="0 0 1200 675">{defs()}
<rect width="1200" height="675" fill="{CREMA}"/><rect width="1200" height="8" fill="url(#gh)"/>
<text x="60" y="78" font-family="{FONT}" font-size="38" font-weight="900" fill="{TINTA}">{esc(title)}</text>
<text x="60" y="114" font-family="{FONT}" font-size="20" font-weight="600" fill="{GRIS}">{esc(subtitle)}</text>
{body}
<text x="60" y="648" font-family="{FONT}" font-size="15" font-weight="600" fill="{GRIS}">{esc(note)}</text>
{logo(870, 616, 0.8)}
</svg>"""


def steps_grid(items, cols=4, top=150, card_h=222):
    out, gap = [], 20
    w = (1080 - gap * (cols - 1)) / cols
    for i, (t, d) in enumerate(items):
        x, y = 60 + (i % cols) * (w + gap), top + (i // cols) * (card_h + gap)
        out.append(f'<rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="{card_h}" rx="18" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2"/>')
        out.append(f'<circle cx="{x+40:.0f}" cy="{y+42}" r="22" fill="url(#g)"/><text x="{x+40:.0f}" y="{y+50}" font-family="{FONT}" font-size="22" font-weight="900" fill="#fff" text-anchor="middle">{i+1}</text>')
        for j, l in enumerate(wrap(t, 20)):
            out.append(f'<text x="{x+20:.0f}" y="{y+98+j*26}" font-family="{FONT}" font-size="21" font-weight="800" fill="{TINTA}">{esc(l)}</text>')
        nt = len(wrap(t, 20))
        for j, l in enumerate(wrap(d, 28)[:3]):
            out.append(f'<text x="{x+20:.0f}" y="{y+104+nt*26+j*22}" font-family="{FONT}" font-size="16" font-weight="500" fill="{GRIS}">{esc(l)}</text>')
    return "\n".join(out)


def table(headers, rows, col_w, top=150, row_h=56, hl_row=None):
    out, x0 = [], 60
    total = sum(col_w)
    out.append(f'<rect x="{x0}" y="{top}" width="{total}" height="{row_h}" rx="14" fill="url(#gh)"/>')
    x = x0
    for h, w in zip(headers, col_w):
        out.append(f'<text x="{x+16}" y="{top+row_h/2+7:.0f}" font-family="{FONT}" font-size="18" font-weight="800" fill="#fff">{esc(h)}</text>')
        x += w
    for r, row in enumerate(rows):
        y = top + row_h * (r + 1)
        fill = DUR if r == hl_row else (BLANCO if r % 2 == 0 else CREMA)
        out.append(f'<rect x="{x0}" y="{y}" width="{total}" height="{row_h}" fill="{fill}"/>')
        out.append(f'<line x1="{x0}" y1="{y+row_h}" x2="{x0+total}" y2="{y+row_h}" stroke="{BORDE}"/>')
        x = x0
        for c, (val, w) in enumerate(zip(row, col_w)):
            out.append(f'<text x="{x+16}" y="{y+row_h/2+7:.0f}" font-family="{FONT}" font-size="{18 if c else 18}" font-weight="{800 if c == 0 else 600}" fill="{TINTA}">{esc(val)}</text>')
            x += w
    return "\n".join(out)


def hbars(items, top=160, max_val=None, unit="$", w_label=380):
    max_val = max_val or max(v for _, v in items)
    out, bar_h, gap = [], 46, 20
    span = 1080 - w_label - 110
    for i, (lab, v) in enumerate(items):
        y = top + i * (bar_h + gap)
        out.append(f'<text x="60" y="{y+bar_h/2+7:.0f}" font-family="{FONT}" font-size="19" font-weight="700" fill="{TINTA}">{esc(lab)}</text>')
        bw = max(6, span * v / max_val)
        out.append(f'<rect x="{60+w_label}" y="{y}" width="{bw:.0f}" height="{bar_h}" rx="4" fill="{NAR}"/>')
        out.append(f'<text x="{60+w_label+bw+12:.0f}" y="{y+bar_h/2+7:.0f}" font-family="{FONT}" font-size="19" font-weight="800" fill="{TINTA}">{unit}{v:,.0f} MXN</text>')
    out.append(f'<line x1="{60+w_label}" y1="{top-10}" x2="{60+w_label}" y2="{top+len(items)*(bar_h+gap)-10}" stroke="{GRIS}" stroke-width="1"/>')
    return "\n".join(out)


def cards_row(items, top=160, h=400):
    out, gap = [], 18
    n = len(items)
    w = (1080 - gap * (n - 1)) / n
    for i, (big, t, d) in enumerate(items):
        x = 60 + i * (w + gap)
        hl = i == 0 and big.startswith("!")
        big = big.lstrip("!")
        out.append(f'<rect x="{x:.0f}" y="{top}" width="{w:.0f}" height="{h}" rx="20" fill="{"url(#g)" if hl else BLANCO}" stroke="{BORDE}" stroke-width="{0 if hl else 2}"/>')
        ink, sub = ("#fff", "#fff") if hl else (TINTA, GRIS)
        out.append(f'<text x="{x+w/2:.0f}" y="{top+96}" font-family="{FONT}" font-size="54" font-weight="900" fill="{"#fff" if hl else "url(#gh)"}" text-anchor="middle">{esc(big)}</text>')
        for j, l in enumerate(wrap(t, 14)):
            out.append(f'<text x="{x+w/2:.0f}" y="{top+160+j*28}" font-family="{FONT}" font-size="23" font-weight="800" fill="{ink}" text-anchor="middle">{esc(l)}</text>')
        nt = len(wrap(t, 14))
        for j, l in enumerate(wrap(d, 20)[:6]):
            out.append(f'<text x="{x+w/2:.0f}" y="{top+176+nt*28+j*24}" font-family="{FONT}" font-size="17" font-weight="500" fill="{sub}" text-anchor="middle">{esc(l)}</text>')
    return "\n".join(out)


# ======================= NOTA 1 =======================
s = "como-importar-de-china-a-mexico"
cover(s, "como-importar-de-china-a-mexico-guia-2026.webp", "Cómo importar", "Cómo importar de China a México paso a paso", "Guía 2026: de la fábrica a tu puerta", art_boxes(760, 140),
      "Guía de cómo importar de China a México paso a paso en 2026")
save(s, "pasos-para-importar-de-china-a-mexico.webp", frame("Los 8 pasos para importar de China a México", "Del producto correcto a tus cajas en la puerta", steps_grid([
    ("Elige un producto que deje", "Chico, ligero y con margen. Haz cuentas antes."),
    ("Encuentra la fábrica", "Fábricas, no revendedores con sobreprecio."),
    ("Valida antes de pagar", "Licencia, video en vivo y fotos de tu mercancía."),
    ("Negocia y pide muestra", "Precio por volumen, pedido mínimo y tiempos."),
    ("Paga seguro y en partes", "Anticipo y resto contra revisión. Canales rastreables."),
    ("Elige Incoterm y envío", "Aéreo para poco volumen, marítimo para volumen."),
    ("Pasa la aduana en regla", "Agente aduanal, fracción, NOM, aranceles e IVA."),
    ("Recibe y vende", "Saca tu costo real por pieza y pon tu precio."),
])), 1200, 675, "Infografía con los 8 pasos para importar de China a México, de la fábrica a tu puerta", "infografia")
save(s, "incoterms-exw-fob-cif-ddp-explicados.webp", frame("Incoterms explicados fácil", "Hasta dónde paga la fábrica y desde dónde pagas tú", table(
    ["Incoterm", "La fábrica se encarga de...", "Tú pagas..."],
    [["EXW", "Tenerlo listo en su puerta", "Todo: recolección, flete, aduana"],
     ["FOB", "Subirlo al barco en el puerto chino", "Flete, seguro, aduana y entrega"],
     ["CIF", "Flete y seguro hasta puerto de México", "Aduana, impuestos y entrega"],
     ["DDP", "Entregarlo en tu puerta con impuestos", "El precio. Pregunta quién importa"]],
    [180, 470, 430], top=160, row_h=88, hl_row=1), "FOB es el más común para importar de China."), 1200, 675,
     "Tabla de Incoterms EXW, FOB, CIF y DDP explicados fácil para importar de China", "infografia")
social(s, "como-importar-de-china-a-mexico-guia-2026-redes.webp", "Guía 2026", "Cómo importar de China a México paso a paso", "Fábrica, pago, envío y aduana sin intermediarios",
       "Cómo importar de China a México paso a paso, guía 2026 para redes sociales")

# ======================= NOTA 2 =======================
s = "eduardo-hernandez-importaciones-china"
cover(s, "eduardo-hernandez-importaciones-china-26-anos.webp", "Historias de Eduardo", "Quién es Eduardo Hernández", "26 años de importaciones de China, de fábrica en fábrica",
      art_numbers(760, 120, [("26+", "años importando de China"), ("5", "negocios funcionando"), ("300+", "empresas asesoradas"), ("2", "bancarrotas superadas")]),
      "Eduardo Hernández, más de 26 años en importaciones de China y fábricas chinas")
save(s, "eduardo-hernandez-en-numeros-importaciones-china.webp", frame("Eduardo Hernández en números", "Autoridad con hechos, no con presunción", cards_row([
    ("!26+", "años importando", "Caminando fábricas y negociando en persona en China."),
    ("5", "negocios", "Funcionando hoy, entre ellos JAICO, Xijiao Shops y Xijiao LOG."),
    ("300+", "empresas asesoradas", "Emprendedores y negocios en los últimos 8 años."),
    ("50+", "empresas a China", "Acompañadas a comprar directo de fábrica."),
    ("2", "bancarrotas", "Superadas. Los errores ya los pagó él."),
], top=160, h=420)), 1200, 675, "Eduardo Hernández en números: 26 años importando de China, 5 negocios y 300 empresas asesoradas", "infografia")
save(s, "negocios-eduardo-hernandez-jaico-xijiao.webp", frame("Los negocios de Eduardo Hernández", "Del contenido a la mercancía en tu puerta", cards_row([
    ("!1", "Compra en Fábricas de China", "Enseña a importar directo de fábrica: clase en vivo y Escuela."),
    ("2", "JAICO", "Importación de joyería y abastecimiento para importadores."),
    ("3", "Xijiao Shops", "Joyería fabricada en China al mayoreo para negocios en México."),
    ("4", "Xijiao LOG", "Logística: de China hasta la puerta de tu negocio."),
], top=160, h=420), "Equipo propio en China: chinos que negocian con chinos."), 1200, 675,
     "Negocios de Eduardo Hernández: Compra en Fábricas de China, JAICO, Xijiao Shops y Xijiao LOG", "infografia")
social(s, "eduardo-hernandez-importaciones-china-redes.webp", "Historias de Eduardo", "26 años comprando en fábricas de China", "2 bancarrotas, 5 negocios y 300+ empresas asesoradas",
       "Eduardo Hernández, 26 años en importaciones de China, historia para redes sociales")

# ======================= NOTA 3 =======================
s = "cursos-para-importar-de-china"
cover(s, "cursos-para-importar-de-china-comparativa-2026.webp", "Cómo importar", "Cursos para importar de China en 2026", "Comparativa honesta: precio, formato y soporte",
      art_checklist(780, 130, ["Enseña alguien que importa", "Es en vivo y con grabación", "Incluye proveedores", "Tiene comunidad", "Precio que recuperas"]),
      "Comparativa de cursos para importar de China en 2026: precio, formato y soporte")
save(s, "tabla-comparativa-cursos-importar-de-china.webp", frame("Cursos para importar de China: comparativa 2026", "Precios publicados en noviembre de 2026. Confírmalos en cada sitio.", table(
    ["Opción", "Precio", "Formato", "Proveedores"],
    [["Clase en vivo con Eduardo", "$990 MXN", "En vivo + grabación", "5 de regalo"],
     ["Escuela de Negocios", "$250 MXN/mes", "Grabado + Zooms en vivo", "No lo indica"],
     ["CETYS Educación Continua", "$8,603 MXN", "Presencial, 24 h", "No lo indica"],
     ["INCEA / LatinoTrainers", "Desde $790 MXN", "En línea", "No lo indica"],
     ["100negocios", "$39 USD", "En línea", "No lo indica"],
     ["Kuinsen", "$2,999 MXN", "Virtual", "No lo indica"],
     ["Elevify", "Básico sin costo / $37 USD", "A tu ritmo, tutor IA", "No lo indica"]],
    [340, 250, 290, 200], top=140, row_h=58, hl_row=0), "La clase en vivo y la Escuela son de Eduardo Hernández (transparencia)."), 1200, 675,
     "Tabla comparativa de cursos para importar de China en 2026 por precio, formato y proveedores", "infografia")
save(s, "criterios-elegir-curso-importar-de-china.webp", frame("7 criterios para elegir un curso para importar de China", "Revísalos antes de pagar", steps_grid([
    ("Precio", "Que lo recuperes con tu primera compra."),
    ("En vivo o grabado", "Poder preguntar tu caso vale oro."),
    ("Quién enseña", "Negocios reales funcionando hoy."),
    ("Proceso completo", "Fábrica, pago, envío, aduana, NOM."),
    ("Proveedores", "Fábricas ya revisadas para empezar."),
    ("Comunidad", "Gente en el mismo camino."),
    ("Soporte", "A quién escribirle después."),
], cols=4, top=145, card_h=215)), 1200, 675, "Los 7 criterios para elegir un curso para importar de China antes de pagar", "infografia")
social(s, "cursos-para-importar-de-china-redes.webp", "Comparativa 2026", "Cursos para importar de China: cuál elegir", "7 criterios para no tirar tu dinero",
       "Cursos para importar de China en 2026, comparativa honesta para redes sociales")

# ======================= NOTA 4 =======================
s = "productos-para-importar-de-china"
cover(s, "productos-para-importar-de-china-revender-2026.webp", "Productos que se venden", "Productos para importar de China y revender", "Electrónica de vanguardia y joyería, con números",
      art_tech_vs_jewel(790, 140), "Productos para importar de China en 2026 y revender: electrónica de vanguardia y joyería")
save(s, "precio-por-pieza-electronica-importada-de-china.webp", frame("Precio por pieza de electrónica importada de China", "Cajas del catálogo, flete desde China incluido (paquetería nacional aparte)", hbars([
    ("Bocina chica S100", 31), ("Bocina chica M1", 50), ("Lentes Bluetooth YJ12", 71), ("Speaker + audífonos KOS-500", 173),
    ("Micrófono inalámbrico MK26", 184), ("Lentes deportivos con IA SAG20", 269), ("Lentes AI WK104", 921)], top=150), "Precios publicados en noviembre de 2026; pueden cambiar."), 1200, 675,
     "Gráfica del precio por pieza de productos de electrónica importados de China en cajas para revender", "infografia")
save(s, "comparativa-electronica-vs-joyeria-importada-de-china.webp", frame("Electrónica vs. joyería importada de China", "Ejemplo hipotético para comparar la lógica (no son precios reales)", table(
    ["Concepto", "Audífonos", "Joyería"],
    [["Costo por pieza puesto en México", "$90", "$25"], ["Precio de venta", "$199", "$149"], ["Ganancia por pieza", "$109", "$124"],
     ["Margen sobre costo", "~121%", "~496%"], ["Peso aproximado por pieza", "~85 g", "unos gramos"], ["Riesgo de pieza defectuosa", "Medio", "Bajo"]],
    [520, 280, 280], top=150, row_h=64, hl_row=3), "Ejemplo hipotético con números redondos."), 1200, 675,
     "Comparativa electrónica contra joyería importada de China: margen, peso y riesgo por pieza", "infografia")
social(s, "productos-para-importar-de-china-redes.webp", "Qué importar en 2026", "Productos para importar de China que sí dejan", "Electrónica vs. joyería, con números",
       "Productos para importar de China en 2026 y revender, publicación para redes sociales")

# ======================= NOTA 5 =======================
s = "importar-joyeria-de-china-para-vender"
cover(s, "importar-joyeria-de-china-para-vender-mayoreo.webp", "Joyería", "Importar joyería de China para vender", "Márgenes, tipos de joyería y cómo empezar",
      art_jewel(780, 130), "Importar joyería de China para vender por mayoreo en México: acero, plata y bisutería")
save(s, "por-que-la-joyeria-importada-de-china-deja-margen.webp", frame("Por qué la joyería importada de China deja margen", "Cinco razones difíciles de juntar en otro producto", cards_row([
    ("!g", "Pesa gramos", "El flete por pieza queda en centavos."),
    ("1", "cajón", "Tu inventario no necesita bodega."),
    ("0", "caducidad", "Sin batería, sin fecha de vencimiento."),
    ("365", "días de venta", "Cumpleaños, 10 de mayo, Navidad, XV años."),
    ("x3", "o más", "Se suele vender varias veces arriba de su costo."),
], top=160, h=420)), 1200, 675, "Por qué la joyería importada de China deja buen margen: peso, envío, rotación y caducidad", "infografia")
save(s, "donde-vender-joyeria-importada-de-china.webp", frame("Dónde vender joyería importada de China", "Combina dos canales al principio: uno para mostrar y otro para vender", steps_grid([
    ("Por catálogo", "Con vendedoras y conocidas a precio de mayoreo."),
    ("Redes y WhatsApp", "Fotos con luz natural y videos con la pieza puesta."),
    ("Tianguis y bazares", "La gente la toca y se la prueba."),
    ("Boutiques y estéticas", "Exhibidor con surtido: tú surtes, ellos venden."),
    ("Tienda en línea", "Para llegar más lejos."),
    ("Marketplaces", "Más alcance, más competencia por precio."),
], cols=3, top=145, card_h=215)), 1200, 675, "Dónde vender joyería importada de China: catálogo, redes, tianguis, tiendas y en línea", "infografia")
social(s, "importar-joyeria-de-china-para-vender-redes.webp", "Joyería al mayoreo", "Importar joyería de China para vender", "Por qué es de los negocios con mejor margen",
       "Importar joyería de China para vender por mayoreo, publicación para redes sociales")

json.dump(manifest, open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(manifest), "imágenes;", sum(m["bytes"] for m in manifest) // 1024, "KB en total")
