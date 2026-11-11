"""Genera el SQL para cargar/actualizar las notas en la tabla posts (upsert por slug).
Uso: python3 tools/build_sql.py > out/posts.sql   (desde blog/)
Quita los comentarios <!-- PENDIENTE --> antes de cargar; esos se quedan solo en el markdown."""
import glob, json, re, yaml, math
ORDER = ["como-importar-de-china-a-mexico", "eduardo-hernandez-importaciones-china", "productos-para-importar-de-china", "importar-joyeria-de-china-para-vender", "cursos-para-importar-de-china"]
def q(s, tag="t"):
    assert f"${tag}$" not in s
    return f"${tag}${s}${tag}$"
stmts = []
for i, slug in enumerate(ORDER):
    raw = open(f"posts/{slug}.md", encoding="utf-8").read()
    _, fm, body = raw.split("---", 2)
    m = yaml.safe_load(fm)
    body = re.sub(r"\n?<!--.*?-->\n?", "\n", body, flags=re.S).strip() + "\n"
    words = len(re.sub(r"[#*|:\[\]()>!_`-]", " ", body).split())
    rt = max(1, math.ceil(words / 200))
    tags = "ARRAY[" + ",".join(q(t) for t in m["tags"]) + "]::text[]"
    howto = q(json.dumps(m["howto"], ensure_ascii=False), "j") + "::jsonb" if m.get("howto") else "NULL"
    pub = f"timestamptz '2026-11-11 09:00:00-06' - interval '{i * 3} hours'"
    cols = dict(title=q(m["title"]), slug=q(m["slug"]), meta_title=q(m["meta_title"]), meta_description=q(m["meta_description"]),
                excerpt=q(m["excerpt"]), content=q(body, "md"), cover_image=q(m["cover_image"]), cover_alt=q(m["cover_alt"]),
                category=q(m["category"]), tags=tags, author="'eduardo-hernandez'", published_at=pub, reading_time=str(rt),
                faq=q(json.dumps(m["faq"], ensure_ascii=False), "j") + "::jsonb", howto=howto, focus_keyword=q(m["focus_keyword"]),
                featured="true" if m.get("featured") else "false", status="'published'")
    upd = ", ".join(f"{k} = EXCLUDED.{k}" for k in cols if k != "slug")
    stmts.append(f"INSERT INTO public.posts ({', '.join(cols)}) VALUES ({', '.join(cols.values())})\nON CONFLICT (slug) DO UPDATE SET {upd};")
print("\n\n".join(stmts))
