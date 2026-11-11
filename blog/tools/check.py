import yaml, re, glob, unicodedata, sys
def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    return ''.join(c for c in s if unicodedata.category(c) != 'Mn')
def load(p):
    raw = open(p, encoding='utf-8').read()
    _, fm, body = raw.split('---', 2)
    return yaml.safe_load(fm), body.strip()
for p in sorted(glob.glob('posts/*.md')):
    m, body = load(p)
    text = re.sub(r'<!--.*?-->', '', body, flags=re.S)
    plain = re.sub(r'[#*|:\[\]\(\)>!_`-]', ' ', re.sub(r'\(/[^)]*\)|\(https?://[^)]*\)', '', text))
    words = len(plain.split()) + sum(len((f['q']+' '+f['a']).split()) for f in m['faq'])
    kw = norm(m['focus_keyword'])
    kwcore = norm(m["focus_keyword"]).replace("como ", "")
    first100 = norm(' '.join(plain.split()[:110]))
    h2s = [norm(h) for h in re.findall(r'^## (.+)$', body, re.M)]
    resp = re.search(r':::respuesta\n(.*?)\n:::', body, re.S).group(1)
    rw = len(re.sub(r'[*]', '', resp).split())
    print(f"\n== {m['slug']}  words~{words}  read={round(words/200)}min")
    print(f"  meta_title {len(m['meta_title'])}c  | meta_desc {len(m['meta_description'])}c | respuesta {rw}w | faq {len(m['faq'])}")
    tok=lambda t: all(w in norm(t) for w in kwcore.split() if len(w)>2)
    print("  tokens title/meta/alt/first100:", tok(m["title"]), tok(m["meta_title"]), tok(m["meta_description"]), tok(m["cover_alt"]), tok(first100))
    print("  kw in title:", kwcore in norm(m['title']), "| meta_title:", kwcore in norm(m['meta_title']), "| meta_desc:", kwcore in norm(m['meta_description']), "| alt:", kwcore in norm(m['cover_alt']), "| first100:", kwcore in first100, "| H2:", any(kwcore in h for h in h2s))
    print("  alt words:", len(m['cover_alt'].split()))
    links = re.findall(r'\]\((/[^)\s]*|https?://[^)\s]*)', body)
    print("  links:", sorted(set(links)))
