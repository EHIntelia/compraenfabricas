"""Imágenes de las notas nuevas con el design system "Compra en Fábricas Design System".

Uso (desde blog/): python3 tools/make_images_ds.py <slug> [<slug> ...]
Salida: img/<slug>/*.webp y entradas nuevas en img/manifest.json.
Las fotos salen de brand/fotos/ (copias del banco de imágenes del design system).
"""
import sys
import imglib as L
import ds
from ds import photo_cover, photo_social, photo_body

FONT = ds.FONT


def bars(items, top=170, w_label=230, max_val=None, unit=""):
    """Barras horizontales: naranja sobre crema, valor en tinta."""
    max_val = max_val or max(v for _, v in items)
    out, bar_h, gap = [], 48, 18
    span = 1080 - w_label - 120
    for i, (lab, v) in enumerate(items):
        y = top + i * (bar_h + gap)
        out.append(f'<text x="60" y="{y+bar_h/2+8:.0f}" font-family="{FONT}" font-size="22" font-weight="700" fill="{L.TINTA}">{L.esc(lab)}</text>')
        bw = max(8, span * v / max_val)
        out.append(f'<rect x="{60+w_label}" y="{y}" width="{bw:.0f}" height="{bar_h}" rx="8" fill="{L.NAR}"/>')
        out.append(f'<text x="{60+w_label+bw+14:.0f}" y="{y+bar_h/2+8:.0f}" font-family="{FONT}" font-size="22" font-weight="900" fill="{L.TINTA}">{v:,}{unit}</text>')
    return "\n".join(out)


def nota_aranceles():
    s = "aranceles-china-mexico-2026"
    photo_cover(s, "aranceles-a-china-2026-mexico.webp", "Aranceles 2026",
                "Aranceles a China 2026: qué subió y cuánto pagas",
                "Lo que cambió en México y cómo calcularlo",
                "puerto-contenedores-atardecer.jpg",
                "Aranceles a China 2026 en México: puerto con contenedores al atardecer",
                hl=("aranceles", "2026:"), focus=(0.55, 0.5))
    body = L.cards_row([
        ("1,463", "fracciones subieron", "Desde el 1 de enero de 2026, con tasas de 5% a 50%"),
        ("185", "fracciones más", "Desde el 24 de abril de 2026, con tasas de 5% a 35%"),
        ("33.5%", "en paquetería", "Tasa global para envíos de China por mensajería"),
    ], top=160, h=330)
    L.save(s, "que-cambio-aranceles-a-china-2026.webp",
           L.frame("Qué cambió en los aranceles a China en 2026", "Los tres números que tienes que conocer",
                   body, "Fuentes: DOF 29/12/2025 y 23/04/2026; RGCE 2026, regla 3.7.35."),
           1200, 675, "Lo que cambió en los aranceles a China en 2026: 1,463 fracciones, 185 fracciones y 33.5% en paquetería", "infografia")
    body = bars([("25%", 669), ("35%", 612), ("30%", 76), ("50%", 18), ("Otras tasas", 86), ("Exentas", 2)],
                top=170, w_label=200)
    L.save(s, "tasas-aranceles-a-china-2026.webp",
           L.frame("Aranceles a China 2026: fracciones por tasa", "Decreto del DOF del 29 de diciembre de 2025 (1,463 fracciones)",
                   body, "Conteo hecho sobre la tabla del decreto. Revisa siempre la fracción de tu producto."),
           1200, 675, "Cuántas fracciones quedaron en cada tasa con los aranceles a China 2026", "infografia")
    photo_body(s, "revision-en-aduana-contenedores.webp", "patio-aduana-contenedores-inspector.jpg",
               "Contenedores en patio de aduana mientras un inspector revisa la mercancía", focus=(0.5, 0.5))
    photo_social(s, "aranceles-a-china-2026-redes.webp", "Aranceles 2026",
                 "Aranceles a China 2026: qué subió y cuánto pagas",
                 "1,463 fracciones, 185 más y 33.5% en paquetería",
                 "puerto-contenedores-vista-aerea.jpg",
                 "Aranceles a China 2026 para importar a México, versión para redes", hl=("aranceles",))


NOTAS = {"aranceles-china-mexico-2026": nota_aranceles}

if __name__ == "__main__":
    for slug in sys.argv[1:] or NOTAS:
        NOTAS[slug]()
    L.write_manifest()
