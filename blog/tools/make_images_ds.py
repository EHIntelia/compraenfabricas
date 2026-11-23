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


def nota_envio():
    s = "envio-aereo-o-maritimo-desde-china"
    photo_cover(s, "envio-aereo-o-maritimo-desde-china.webp", "Envíos desde China",
                "Envío aéreo o marítimo desde China: cuál te conviene",
                "Cómo se cobra cada uno y cuánto tarda",
                "bodega-cajas-montacargas.jpg",
                "Envío aéreo o marítimo desde China: bodega con cajas listas para embarcar a México",
                hl=("aéreo", "marítimo"), focus=(0.5, 0.5))
    body = L.table(["", "Aéreo", "Marítimo consolidado"], [
        ["Cómo se cobra", "Por kilo (real o volumétrico)", "Por metro cúbico"],
        ["Tiempo", "Días", "Semanas"],
        ["Conviene para", "Muestras y pedidos chicos", "Volumen y costo por pieza"],
        ["Producto ideal", "Chico, caro o urgente", "Grande o pesado"],
        ["Ojo con", "Cajas grandes y ligeras", "Planear con tiempo"],
    ], [250, 415, 415], top=150, row_h=74)
    L.save(s, "aereo-vs-maritimo-desde-china.webp",
           L.frame("Envío aéreo o marítimo desde China", "Cómo se cobra, cuánto tarda y para qué conviene cada uno",
                   body, "El costo exacto depende de tu producto y tu volumen: pide tu cotización."),
           1200, 675, "Envío aéreo o marítimo desde China: cómo se cobra, cuánto tarda y para qué conviene cada uno", "infografia")
    body = L.cards_row([
        ("60×40×40", "Medidas de la caja", "En centímetros, ya empacada para exportar"),
        ("16 kg", "Peso volumétrico", "60 × 40 × 40 ÷ 6,000 (carga aérea). Con ÷ 5,000 serían 19.2 kg"),
        ("10 kg", "Peso real", "Lo que marca la báscula. Te cobran el mayor: 16 kg"),
    ], top=160, h=330)
    L.save(s, "peso-volumetrico-envio-desde-china.webp",
           L.frame("Cómo calcular el peso volumétrico", "Ejemplo con una caja para envío aéreo desde China",
                   body, "Divisor 6,000 en carga aérea general; muchas mensajerías exprés usan 5,000."),
           1200, 675, "Cómo calcular el peso volumétrico de una caja para envío aéreo desde China", "infografia")
    photo_body(s, "entrega-mercancia-de-china-en-tu-negocio.webp", "entrega-cajas-en-negocio.jpg",
               "Entrega de cajas importadas de China en la puerta de un negocio en México", focus=(0.5, 0.5))
    photo_social(s, "envio-aereo-o-maritimo-desde-china-redes.webp", "Envíos desde China",
                 "Envío aéreo o marítimo desde China: cuál te conviene",
                 "Por kilo o por metro cúbico, días o semanas",
                 "puerto-contenedores-anochecer.jpg",
                 "Envío aéreo o marítimo desde China, versión para redes", hl=("aéreo", "marítimo"))


def nota_yiwu():
    s = "que-es-yiwu"
    photo_cover(s, "que-es-yiwu-mercado-mayorista-china.webp", "Comprar en China",
                "Qué es Yiwu: el mercado mayorista más grande de China",
                "Qué se compra, para quién conviene y cómo traerlo",
                "mercado-yiwu-pasillo.jpg",
                "Qué es Yiwu: pasillo del mercado mayorista de Yiwu en China con compradores",
                hl=("yiwu",), focus=(0.5, 0.5))
    body = L.cards_row([
        ("80,000", "puestos", "Casi 80,000 puestos en el Yiwu International Trade City (China Daily, 2026)"),
        ("2.1 M", "tipos de productos", "Más de 2.1 millones de productos de surtido general"),
        ("1.5 a 2 h", "desde Shanghái", "En tren de alta velocidad desde la estación Hongqiao"),
    ], top=160, h=330)
    L.save(s, "yiwu-en-numeros.webp",
           L.frame("Yiwu en números", "El mercado mayorista más grande de China",
                   body, "Fuentes: China Daily (marzo de 2026) y Travel China Guide."),
           1200, 675, "Yiwu en números: casi 80,000 puestos, más de 2.1 millones de productos y a unas 2 horas de Shanghái en tren", "infografia")
    body = L.table(["", "Puesto en Yiwu", "Fábrica directa"], [
        ["Variedad", "Muchísima", "Solo lo que produce"],
        ["Pedido mínimo", "Más bajo, por lo general", "Más alto"],
        ["Precio por pieza", "Buen precio de mayoreo", "El más bajo, con volumen"],
        ["Personalización", "Limitada", "Logo, empaque y cambios"],
        ["Conviene para", "Surtido y probar productos", "Volumen de un solo producto"],
    ], [250, 415, 415], top=150, row_h=74)
    L.save(s, "yiwu-o-fabrica-cual-conviene.webp",
           L.frame("Yiwu o fábrica: cuál te conviene", "Comprar en el mercado de Yiwu o directo a una fábrica en China",
                   body, "En los dos casos: valida al proveedor y revisa la mercancía antes de pagar."),
           1200, 675, "Yiwu o fábrica: cuándo conviene comprar en el mercado de Yiwu y cuándo directo de fábrica", "infografia")
    photo_body(s, "puesto-mercado-mayorista-yiwu.webp", "puesto-mercado-mayorista.jpg",
               "Vendedora en un puesto de mercado mayorista con mercancía de surtido general", focus=(0.85, 0.5))
    photo_social(s, "que-es-yiwu-redes.webp", "Comprar en China",
                 "Qué es Yiwu y cómo comprar en el mercado mayorista",
                 "80,000 puestos de surtido general en un solo lugar",
                 "mercado-yiwu-pasillo.jpg",
                 "Qué es Yiwu y cómo comprar ahí, versión para redes", hl=("yiwu",), focus=(0.5, 0.4))


NOTAS = {"que-es-yiwu": nota_yiwu, "aranceles-china-mexico-2026": nota_aranceles, "envio-aereo-o-maritimo-desde-china": nota_envio}

if __name__ == "__main__":
    for slug in sys.argv[1:] or NOTAS:
        NOTAS[slug]()
    L.write_manifest()
