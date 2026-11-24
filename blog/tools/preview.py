"""Vista previa local de notas en borrador (el sitio solo muestra notas publicadas).
Uso (desde blog/): python3 tools/preview.py <slug> [<slug> ...]  ->  artifact/borradores.html
Las imágenes se referencian como blog/<slug>/<archivo> para publicarlas junto con la página."""
import re, sys, html, yaml, markdown

CAT = {"como-importar": "Cómo importar", "productos-que-se-venden": "Productos que se venden", "joyeria": "Joyería",
       "errores-y-consejos": "Errores y consejos", "historias-de-eduardo": "Historias de Eduardo"}


def render(slug):
    raw = open(f"posts/{slug}.md", encoding="utf-8").read()
    _, fm, body = raw.split("---", 2)
    m = yaml.safe_load(fm)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

    def block(mo):
        kind, inner = mo.group(1), mo.group(2).strip()
        if kind == "cta-clase":
            return '\n<aside class="cta"><p class="t">Aprende todo el proceso en vivo con Eduardo</p><a href="#">Ver la clase en vivo →</a></aside>\n'
        label = "Respuesta rápida" if kind == "respuesta" else "Consejo de Eduardo"
        return f'\n<aside class="box {kind}"><p class="lbl">{label}</p>{markdown.markdown(inner)}</aside>\n'

    body = re.sub(r"^:::(respuesta|consejo|cta-clase)[ \t]*\n(.*?)^:::[ \t]*$", block, body, flags=re.S | re.M)
    body_html = markdown.markdown(body, extensions=["tables"])
    body_html = re.sub(r'src="/blog/', 'src="blog/', body_html)
    body_html = re.sub(r'<p>(<img [^>]*title="([^"]*)"[^>]*>)</p>', r'<figure>\1<figcaption>\2</figcaption></figure>', body_html)
    pend = re.findall(r"\[PENDIENTE[^\]]*\]", raw)
    faq = "".join(f"<details><summary>{html.escape(f['q'])}</summary><p>{html.escape(f['a'])}</p></details>" for f in m["faq"])
    seo = (f'<div class="seo"><b>Google mostraría:</b><div class="g-t">{html.escape(m["meta_title"])}</div>'
           f'<div class="g-u">compraenfabricas.com › blog › {slug}</div><div class="g-d">{html.escape(m["meta_description"])}</div>'
           f'<p class="meta">Keyword: <b>{html.escape(m["focus_keyword"])}</b> · title {len(m["meta_title"])} car. · description {len(m["meta_description"])} car. · '
           f'{"[PENDIENTE] visibles: " + str(len(pend)) if pend else "Sin [PENDIENTE] visibles"}</p></div>')
    return (f'<article id="{slug}">{seo}<p class="cat">{CAT[m["category"]]} · Borrador</p><h1>{html.escape(m["title"])}</h1>'
            f'<img class="cover" src="blog/{slug}/{m["cover_image"].split("/")[-1]}" alt="{html.escape(m["cover_alt"])}" width="1200" height="630">'
            f'{body_html}<h2>Preguntas frecuentes</h2>{faq}</article>')


if __name__ == "__main__":
    slugs = sys.argv[1:]
    nav = "".join(f'<a href="#{s}">{s}</a>' for s in slugs)
    page = f"""<title>Borradores del blog</title>
<meta name="claude:viewport-fit-sides" content="cover">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800;900&display=swap">
<style>
:root {{ --bg:#FFF8F5; --card:#FFFFFF; --ink:#1A1A1A; --muted:#6B6B6B; --line:#D9CFC7; --peach:#FCE4DC; --orange:#F97316; --red:#DC2626; --grad:linear-gradient(120deg,#F97316,#DC2626); }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) {{ --bg:#17120F; --card:#221B17; --ink:#F5EEE9; --muted:#B8ADA6; --line:#3A2F29; --peach:#3B2218; color-scheme:dark }} }}
:root[data-theme="dark"] {{ --bg:#17120F; --card:#221B17; --ink:#F5EEE9; --muted:#B8ADA6; --line:#3A2F29; --peach:#3B2218; color-scheme:dark }}
body {{ background:var(--bg); color:var(--ink); font:16px/1.65 Inter, system-ui, sans-serif; padding-left:max(16px, env(safe-area-inset-left,0px)); padding-right:max(16px, env(safe-area-inset-right,0px)); padding-block:0 48px; }}
nav {{ position:sticky; top:env(safe-area-inset-top,0px); background:var(--bg); border-bottom:1px solid var(--line); padding-block:10px; display:flex; flex-wrap:wrap; gap:8px; z-index:2; max-width:760px; margin:0 auto; }}
nav a {{ font-size:13px; font-weight:700; color:var(--ink); background:var(--peach); padding:5px 10px; border-radius:999px; text-decoration:none; }}
article {{ max-width:760px; margin:32px auto 72px; }}
.seo {{ border:1px dashed var(--line); border-radius:12px; padding:14px 16px; background:var(--card); font-size:14px; }}
.g-t {{ color:#1a0dab; font-size:19px; margin-top:6px; }} .g-u {{ color:#188038; font-size:13px; }} .g-d {{ color:var(--muted); }}
@media (prefers-color-scheme: dark) {{ :root:not([data-theme="light"]) .g-t {{ color:#8ab4f8 }} }}
.meta {{ margin:8px 0 0; color:var(--muted); font-size:12px; }}
.cat {{ margin:24px 0 0; font-size:12px; font-weight:800; letter-spacing:.06em; text-transform:uppercase; color:var(--orange); }}
h1 {{ font-size:clamp(28px,5vw,40px); line-height:1.12; font-weight:900; margin:6px 0 18px; text-wrap:balance; }}
h2 {{ font-size:24px; line-height:1.2; font-weight:900; margin:36px 0 10px; text-wrap:balance; }}
h3 {{ font-size:19px; margin:24px 0 8px; }}
img {{ max-width:100%; height:auto; border-radius:12px; display:block; }}
.cover {{ width:100%; }}
figure {{ margin:22px 0; }} figcaption {{ font-size:13px; color:var(--muted); text-align:center; margin-top:6px; }}
a {{ color:var(--red); }}
table {{ width:100%; border-collapse:collapse; font-size:14px; display:block; overflow-x:auto; }}
th {{ background:var(--grad); color:#fff; text-align:left; padding:8px 10px; }} td {{ border-bottom:1px solid var(--line); padding:8px 10px; vertical-align:top; }}
.box {{ border-radius:14px; padding:14px 18px; margin:20px 0; background:var(--card); border:1px solid var(--line); }}
.box.respuesta {{ border-left:5px solid var(--orange); }} .box.consejo {{ background:var(--peach); border:none; }}
.lbl {{ margin:0 0 4px; font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:.05em; color:var(--red); }}
.cta {{ background:var(--grad); color:#fff; border-radius:16px; padding:18px 20px; margin:24px 0; }}
.cta .t {{ margin:0 0 8px; font-weight:900; font-size:18px; }} .cta a {{ color:#fff; font-weight:800; }}
details {{ border:1px solid var(--line); border-radius:12px; padding:10px 14px; margin:8px 0; background:var(--card); }}
summary {{ font-weight:700; cursor:pointer; }}
</style>
<nav>{nav}</nav>
{''.join(render(s) for s in slugs)}
"""
    open("artifact/borradores.html", "w", encoding="utf-8").write(page)
    print("artifact/borradores.html", len(page))
