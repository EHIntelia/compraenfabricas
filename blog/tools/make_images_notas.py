"""Imágenes del calendario de 10 notas (lote 2). Uso desde blog/:
    python3 tools/make_images_notas.py <slug> [<slug> ...]
Cada nota lleva 4 imágenes: portada 1200x630, 2 infografías 1200x675 y redes 1080x1080.
"""
import sys
from imglib import (NAR, ROJO, TINTA, GRIS, DUR, BLANCO, BORDE, FONT, esc, wrap, cover, social, frame, save,
                    steps_grid, table, cards_row, write_manifest)


def art_list(x, y, title, items):
    g = [f'<g transform="translate({x},{y})"><rect width="380" height="{70+len(items)*58}" rx="24" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2" filter="url(#sh)"/>']
    g.append(f'<rect width="380" height="56" rx="24" fill="url(#gh)"/><rect y="30" width="380" height="26" fill="url(#gh)"/>')
    g.append(f'<text x="24" y="37" font-family="{FONT}" font-size="20" font-weight="800" fill="#fff">{esc(title)}</text>')
    for i, it in enumerate(items):
        yy = 92 + i * 58
        g.append(f'<circle cx="40" cy="{yy}" r="15" fill="{DUR}"/><path d="M32,{yy} l6,6 l11,-12" stroke="{ROJO}" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
        g.append(f'<text x="70" y="{yy+7}" font-family="{FONT}" font-size="20" font-weight="700" fill="{TINTA}">{esc(it)}</text>')
    g.append("</g>")
    return "\n".join(g)


def art_receipt(x, y, title, rows, total):
    h = 120 + len(rows) * 46
    g = [f'<g transform="translate({x},{y})"><rect width="380" height="{h}" rx="22" fill="{BLANCO}" stroke="{BORDE}" stroke-width="2" filter="url(#sh)"/>']
    g.append(f'<text x="24" y="44" font-family="{FONT}" font-size="20" font-weight="800" fill="{TINTA}">{esc(title)}</text>')
    for i, (k, v) in enumerate(rows):
        yy = 86 + i * 46
        g.append(f'<text x="24" y="{yy}" font-family="{FONT}" font-size="18" font-weight="600" fill="{GRIS}">{esc(k)}</text>')
        g.append(f'<text x="356" y="{yy}" font-family="{FONT}" font-size="18" font-weight="800" fill="{TINTA}" text-anchor="end">{esc(v)}</text>')
        g.append(f'<line x1="24" y1="{yy+16}" x2="356" y2="{yy+16}" stroke="{BORDE}" stroke-dasharray="4 4"/>')
    ty = 86 + len(rows) * 46 + 10
    g.append(f'<rect x="16" y="{ty-30}" width="348" height="48" rx="12" fill="url(#gh)"/>')
    g.append(f'<text x="32" y="{ty+2}" font-family="{FONT}" font-size="20" font-weight="900" fill="#fff">{esc(total[0])}</text>')
    g.append(f'<text x="348" y="{ty+2}" font-family="{FONT}" font-size="22" font-weight="900" fill="#fff" text-anchor="end">{esc(total[1])}</text>')
    g.append("</g>")
    return "\n".join(g)


def nota_requisitos():
    s = "requisitos-para-importar-de-china-a-mexico"
    cover(s, "requisitos-para-importar-de-china-a-mexico-2026.webp", "Cómo importar", "Requisitos para importar de China a México",
          "Padrón, RFC y agente aduanal, explicado fácil",
          art_list(780, 120, "Para importar necesitas", ["RFC activo y e.firma", "Padrón de importadores", "Agente aduanal", "Fracción arancelaria", "NOM y etiquetado"]),
          "Requisitos para importar de China a México en 2026: RFC, padrón y agente aduanal")
    save(s, "lista-requisitos-para-importar-de-china.webp", frame("Requisitos para importar de China a México", "Lo que pide la ley en 2026, en orden", table(
        ["Requisito", "Qué es en simple", "¿Cuesta?"],
        [["RFC activo y e.firma", "Tu registro y tu firma ante el SAT", "No"],
         ["Estar al corriente", "Domicilio Localizado y buzón Validado", "No"],
         ["Padrón de importadores", "Registro para importar de forma regular", "No"],
         ["Agente aduanal + encargo", "Quien presenta tu mercancía en aduana", "Sus honorarios"],
         ["Fracción arancelaria", "El código que define tu arancel", "Según producto"],
         ["NOM y etiquetado", "Reglas y etiqueta en español", "Según producto"],
         ["Pedimento", "La declaración oficial e impuestos", "Impuestos"]],
        [330, 520, 230], top=136, row_h=58, hl_row=2), "Fuente: SAT, ficha 5/LA (DOF 12 de enero de 2026). Consultado el 11 de noviembre de 2026."), 1200, 675,
         "Tabla con la lista de requisitos para importar de China a México en 2026", "infografia")
    save(s, "pasos-padron-de-importadores-2026.webp", frame("Cómo inscribirte en el Padrón de Importadores", "Gratis y en línea en el portal del SAT", steps_grid([
        ("Revisa RFC y e.firma", "RFC activo y e.firma vigente."),
        ("Ponte al corriente", "Domicilio Localizado y buzón tributario Validado."),
        ("Elige agente aduanal", "Con patente vigente, que haga tus operaciones."),
        ("Solicita en el SAT", "Padrón de importadores, Inscripción. Firma con e.firma."),
        ("Da el encargo conferido", "Autoriza a tu agente y espera a que lo acepte."),
        ("Revisa sectores", "Algunos productos piden padrón de sectores específicos."),
    ], cols=3, top=145, card_h=215), "Fuente: SAT, ficha 5/LA y página de encargo conferido. Consultado el 11 de noviembre de 2026."), 1200, 675,
         "Pasos para inscribirte en el Padrón de Importadores del SAT en 2026", "infografia")
    social(s, "requisitos-para-importar-de-china-a-mexico-redes.webp", "Cómo importar", "Requisitos para importar de China en 2026",
           "RFC, padrón, agente aduanal y NOM", "Requisitos para importar de China a México en 2026, publicación para redes sociales")


def nota_costos():
    s = "cuanto-cuesta-importar-de-china"
    cover(s, "cuanto-cuesta-importar-de-china-2026.webp", "Cómo importar", "Cuánto cuesta importar de China a México",
          "Ejemplo con números: de US$2 a $73 por pieza",
          art_receipt(780, 110, "Ejemplo: 500 piezas", [("Mercancía", "$18,500"), ("Flete y seguro", "$4,500"), ("Arancel (ej. 20%)", "$4,600"),
                                                       ("DTA + IVA 16%", "$4,629"), ("Agente + envío", "$4,300")], ("Por pieza", "≈ $73")),
          "Cuánto cuesta importar de China a México en 2026, desglose de costos con números")
    save(s, "desglose-costos-importar-de-china-ejemplo.webp", frame("Cuánto cuesta importar 500 piezas de China", "Ejemplo hipotético. Solo las tasas de IVA y DTA son datos reales.", table(
        ["Concepto", "Cómo se calcula", "Monto"],
        [["Mercancía", "500 × US$2 × $18.50", "$18,500"], ["Flete y seguro", "Cotización de ejemplo", "$4,500"],
         ["Arancel", "20% del valor (ejemplo)", "$4,600"], ["DTA", "8 al millar (Ley Federal de Derechos)", "$184"],
         ["IVA de importación", "16% de valor + arancel + DTA", "$4,445"], ["Agente aduanal", "Honorarios de ejemplo", "$3,500"],
         ["Envío nacional", "Aduana a bodega", "$800"], ["Costo por pieza", "$36,529 ÷ 500", "≈ $73"]],
        [330, 560, 190], top=134, row_h=52, hl_row=7), "Arancel real: depende de la fracción de tu producto. Tipo de cambio de referencia: $18.50."), 1200, 675,
         "Desglose de cuánto cuesta importar de China con un ejemplo de 500 piezas", "infografia")
    save(s, "costo-por-pieza-importar-vs-caja-en-mexico.webp", frame("Importar tú o comprar una caja que ya está en México", "Comparación de costo por pieza", cards_row([
        ("!$37", "precio de fábrica", "US$2 por pieza en el ejemplo hipotético, antes de envío e impuestos."),
        ("$73", "puesto en México", "Mismo ejemplo con flete, arancel, IVA, agente y envío nacional."),
        ("$31", "caja S100 real", "Bocinas del catálogo con flete desde China incluido. Paquetería aparte."),
        ("x2", "regla de venta", "Vende al menos al doble de tu costo puesto en México."),
    ], top=160, h=420), "La caja S100 es un precio real publicado en /productos (noviembre de 2026)."), 1200, 675,
         "Costo por pieza al importar de China comparado con una caja que ya está en México", "infografia")
    social(s, "cuanto-cuesta-importar-de-china-redes.webp", "Costos 2026", "Cuánto cuesta importar de China", "De US$2 en fábrica a $73 puesto en México",
           "Cuánto cuesta importar de China a México en 2026, publicación para redes sociales")


NOTAS = {"requisitos-para-importar-de-china-a-mexico": nota_requisitos, "cuanto-cuesta-importar-de-china": nota_costos}

if __name__ == "__main__":
    for slug in sys.argv[1:] or NOTAS:
        NOTAS[slug]()
    write_manifest()
