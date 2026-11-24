"""Plantillas de imagen alineadas al design system "Compra en Fábricas Design System".

Reglas del sistema que se aplican aquí:
- Arial en todo (en este equipo se usa Liberation Sans, que tiene las mismas medidas).
- Logo real (brand/logo-horizontal.png). No se redibuja la marca.
- Fondo crema, tarjetas blancas, durazno para destacar. El degradado estrella solo en
  detalles chicos (barras, números, palabra clave), nunca de fondo grande.
- Fotos del banco de imágenes del sistema, redondeadas 24px.
- Badges en MAYÚSCULAS, rojo sobre durazno.

Uso: from ds import *   (desde tools/, después de importar imglib)
"""
import base64, io, os
from PIL import Image, ImageOps
import imglib as L

HERE = os.path.dirname(__file__)
BRAND = os.path.join(HERE, "..", "brand")
L.FONT = "Arial, Liberation Sans, Helvetica, sans-serif"
FONT = L.FONT


def _data_uri(path, max_w=None, box=None, quality=88):
    im = Image.open(path)
    if box:
        im = ImageOps.fit(im.convert("RGB"), box, Image.LANCZOS, centering=(0.5, 0.5))
    elif max_w and im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if im.mode == "RGBA":
        im.save(buf, "PNG"); mime = "png"
    else:
        im.convert("RGB").save(buf, "JPEG", quality=quality); mime = "jpeg"
    return f"data:image/{mime};base64," + base64.b64encode(buf.getvalue()).decode()


def logo(x, y, scale=1.0, light=False):
    """Logo horizontal real. Alto base 44px (scale 1)."""
    f = "logo-horizontal-blanco.png" if light else "logo-horizontal.png"
    h = 44 * scale
    w = h * 1947 / 529
    return f'<image x="{x}" y="{y}" width="{w:.0f}" height="{h:.0f}" href="{_data_uri(os.path.join(BRAND, f), max_w=600)}"/>'


L.logo = logo  # frame() y las demás plantillas usan el logo real


def foto(name):
    return os.path.join(BRAND, "fotos", name)


def _photo(path, x, y, w, h, r=24, focus=(0.5, 0.5)):
    im = ImageOps.fit(Image.open(path).convert("RGB"), (int(w * 1.5), int(h * 1.5)), Image.LANCZOS, centering=focus)
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=88)
    uri = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    cid = f"c{x}{y}{w}"
    return (f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
            f'<image x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#{cid})" href="{uri}"/>')


def _title(lines, x, y, size, hl):
    """Titular Arial 900, tracking -0.02em. Las palabras de `hl` van en degradado."""
    out = []
    for i, l in enumerate(lines):
        spans = []
        for w in l.split(" "):
            fill = "url(#gh)" if w.strip(".,:?¿").lower() in hl else L.TINTA
            spans.append(f'<tspan fill="{fill}">{L.esc(w)}</tspan>')
        out.append(f'<text x="{x}" y="{y + i * size * 1.1:.0f}" font-family="{FONT}" font-size="{size}" font-weight="900" letter-spacing="{-0.02*size:.1f}">{" ".join(spans)}</text>')
    return "\n".join(out)


def photo_cover(slug, name, cat, title, kicker, photo, alt, hl=(), focus=(0.5, 0.5)):
    lines = L.wrap(title, 20)
    size = 54 if len(lines) <= 4 else 46
    y0 = 214
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1200" height="630" viewBox="0 0 1200 630">{L.defs()}
<rect width="1200" height="630" fill="{L.CREMA}"/>
{_photo(foto(photo), 680, 40, 480, 550, 24, focus)}
{logo(60, 50, 0.95)}
{L.badge(60, 130, cat, 16)}
{_title(lines, 60, y0 + size, size, {w.lower() for w in hl})}
<text x="60" y="{y0 + size + len(lines)*size*1.1 + 22:.0f}" font-family="{FONT}" font-size="22" font-weight="400" fill="{L.GRIS}">{L.esc(kicker)}</text>
<rect x="60" y="560" width="220" height="6" rx="3" fill="url(#gh)"/>
<text x="60" y="596" font-family="{FONT}" font-size="17" font-weight="700" fill="{L.TINTA}">compraenfabricas.com/blog</text>
</svg>"""
    L.save(slug, name, svg, 1200, 630, alt, "portada")


def photo_social(slug, name, cat, title, kicker, photo, alt, hl=(), focus=(0.5, 0.5)):
    lines = L.wrap(title, 22)
    size = 62 if len(lines) <= 3 else 54
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1080" viewBox="0 0 1080 1080">{L.defs()}
<rect width="1080" height="1080" fill="{L.CREMA}"/>
{_photo(foto(photo), 60, 60, 960, 470, 24, focus)}
{L.badge(60, 570, cat, 20)}
{_title(lines, 60, 650 + size, size, {w.lower() for w in hl})}
<text x="60" y="{650 + size + len(lines)*size*1.1 + 18:.0f}" font-family="{FONT}" font-size="28" font-weight="400" fill="{L.GRIS}">{L.esc(kicker)}</text>
<rect x="60" y="960" width="960" height="1" fill="{L.BORDE}"/>
{logo(60, 984, 1.05)}
<text x="1020" y="1018" font-family="{FONT}" font-size="22" font-weight="700" fill="{L.TINTA}" text-anchor="end">compraenfabricas.com/blog</text>
</svg>"""
    L.save(slug, name, svg, 1080, 1080, alt, "redes")


def photo_body(slug, name, photo, alt, focus=(0.5, 0.5)):
    """Foto del banco a 1200x675 para el cuerpo de la nota."""
    os.makedirs(os.path.join(L.OUT, slug), exist_ok=True)
    im = ImageOps.fit(Image.open(foto(photo)).convert("RGB"), (1200, 675), Image.LANCZOS, centering=focus)
    path = os.path.join(L.OUT, slug, name)
    im.save(path, "WEBP", quality=82, method=6)
    L.manifest.append({"slug": slug, "file": name, "path": f"/blog/{slug}/{name}", "width": 1200, "height": 675,
                       "kind": "foto", "alt": alt, "bytes": os.path.getsize(path), "source": f"brand/fotos/{photo}"})
