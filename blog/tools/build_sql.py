"""Genera el SQL para cargar/actualizar notas en la tabla posts (upsert por slug).

Uso (desde blog/):
  python3 tools/build_sql.py > out/posts.sql                       # lote 1 (las 5 notas originales, publicadas)
  python3 tools/build_sql.py --status draft <slug> [<slug> ...]    # notas nuevas como borrador
  python3 tools/build_sql.py --status published --date "2026-11-18 09:00:00-06" <slug>

Quita los comentarios <!-- ... --> antes de cargar; esos se quedan solo en el markdown.
Un borrador queda con published_at NULL (no sale en el sitio ni en el sitemap)."""
import argparse, json, re, math
import yaml

LOTE1 = ["como-importar-de-china-a-mexico", "eduardo-hernandez-importaciones-china", "productos-para-importar-de-china",
         "importar-joyeria-de-china-para-vender", "cursos-para-importar-de-china"]


def q(s, tag="t"):
    assert f"${tag}$" not in s
    return f"${tag}${s}${tag}$"


def stmt(slug, status, pub):
    raw = open(f"posts/{slug}.md", encoding="utf-8").read()
    _, fm, body = raw.split("---", 2)
    m = yaml.safe_load(fm)
    body = re.sub(r"\n?<!--.*?-->\n?", "\n", body, flags=re.S).strip() + "\n"
    assert "[PENDIENTE" not in body or status == "draft", f"{slug} tiene [PENDIENTE] visibles: no se puede publicar"
    words = len(re.sub(r"[#*|:\[\]()>!_`-]", " ", body).split())
    rt = max(1, math.ceil(words / 200))
    tags = "ARRAY[" + ",".join(q(t) for t in m["tags"]) + "]::text[]"
    howto = q(json.dumps(m["howto"], ensure_ascii=False), "j") + "::jsonb" if m.get("howto") else "NULL"
    cols = dict(title=q(m["title"]), slug=q(m["slug"]), meta_title=q(m["meta_title"]), meta_description=q(m["meta_description"]),
                excerpt=q(m["excerpt"]), content=q(body, "md"), cover_image=q(m["cover_image"]), cover_alt=q(m["cover_alt"]),
                category=q(m["category"]), tags=tags, author="'eduardo-hernandez'", published_at=pub, reading_time=str(rt),
                faq=q(json.dumps(m["faq"], ensure_ascii=False), "j") + "::jsonb", howto=howto, focus_keyword=q(m["focus_keyword"]),
                featured="true" if m.get("featured") else "false", status=f"'{status}'")
    upd = ", ".join(f"{k} = EXCLUDED.{k}" for k in cols if k != "slug")
    return f"INSERT INTO public.posts ({', '.join(cols)}) VALUES ({', '.join(cols.values())})\nON CONFLICT (slug) DO UPDATE SET {upd};"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--status", choices=["draft", "published"])
    ap.add_argument("--date", help="published_at, p. ej. '2026-11-18 09:00:00-06'")
    ap.add_argument("slugs", nargs="*")
    a = ap.parse_args()
    out = []
    if not a.slugs:
        for i, slug in enumerate(LOTE1):
            out.append(stmt(slug, "published", f"timestamptz '2026-11-11 09:00:00-06' - interval '{i} hours'"))
    else:
        status = a.status or "draft"
        pub = "NULL" if status == "draft" else (f"timestamptz '{a.date}'" if a.date else "now()")
        out = [stmt(s, status, pub) for s in a.slugs]
    print("\n\n".join(out))
