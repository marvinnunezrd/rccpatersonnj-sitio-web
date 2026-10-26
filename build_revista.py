# -*- coding: utf-8 -*-
"""
REVISTA "El Carismático de Paterson" (edición semanal, sale los lunes).

Uso (cada lunes):
  python build_revista.py "<ruta al .html de la edición>" AAAA-MM-DD ["<ruta a og-portada.jpg>"]
    - El .html es el archivo único que entrega 6. Prensa y Contenido
      (p. ej. El-Carismatico-de-Paterson-Edicion-02-26-Oct-2026.html).
    - AAAA-MM-DD = el lunes de la semana de la edición.
    - og-portada.jpg (opcional) = imagen para compartir; si se omite se conserva la actual.
  Solo regenerar:  python build_revista.py

Resultado:
  revista/edicion-NN-AAAA-MM-DD/index.html  -> cada edición (solo se ajustan og:url, og:image y canonical)
  revista/descargas/<nombre original>.html  -> copia exacta para el botón "Descargar"
  revista/index.html                         -> portada: edición más reciente arriba, anteriores en cola
  revista/og-portada.jpg                     -> imagen para compartir (todas las ediciones)
  revista/ediciones/ y revista/2026-10-19/   -> redirecciones de direcciones antiguas
  sitemap.xml                                -> entradas de la revista
El texto y el diseño de cada edición NO se modifican.
"""
import sys, os, re, shutil, html as htmlmod
from datetime import date, timedelta
sys.path.insert(0, ".")
from common import head, footer, TAIL, SITE_URL

REV = "revista"
DESC_DIR = os.path.join(REV, "descargas")
ED_RE = re.compile(r"^edicion-(\d{2})-(\d{4}-\d{2}-\d{2})$")
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]
MES3 = ["ene","feb","mar","abr","may","jun","jul","ago","sep","oct","nov","dic"]
OG_IMG = f"{SITE_URL}/revista/og-portada.jpg"
# Direcciones antiguas -> nuevas (para no romper enlaces ya compartidos)
LEGACY = {"2026-10-19": "edicion-01-2026-10-19"}

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

def semana(d):
    a = date.fromisoformat(d); b = a + timedelta(days=6)
    if a.month == b.month:
        return f"{a.day} – {b.day} {MES3[b.month-1]} {b.year}"
    return f"{a.day} {MES3[a.month-1]} – {b.day} {MES3[b.month-1]} {b.year}"

def fecha_larga(d):
    y, m, dd = map(int, d.split("-"))
    return f"{dd} de {MESES[m-1]} de {y}"

def set_meta(s, prop, value, attr="property"):
    pat = re.compile(r'<meta %s="%s" content="[^"]*">' % (attr, re.escape(prop)))
    tag = f'<meta {attr}="{prop}" content="{value}">'
    if pat.search(s): return pat.sub(lambda m: tag, s, count=1)
    return s.replace("</head>", tag + "\n</head>", 1)

def set_canonical(s, url):
    tag = f'<link rel="canonical" href="{url}">'
    if re.search(r'<link rel="canonical"[^>]*>', s):
        return re.sub(r'<link rel="canonical"[^>]*>', lambda m: tag, s, count=1)
    return s.replace("</head>", tag + "\n</head>", 1)

def numero(s):
    m = re.search(r'Edici[óo]n n\.º\s*(\d+)', s)
    if not m: raise SystemExit("No se encontró 'Edición n.º N' en el título de la edición.")
    return int(m.group(1))

def info(s):
    d = re.search(r'<meta name="description" content="([^"]*)">', s)
    return htmlmod.unescape(d.group(1)) if d else ""

def ediciones():
    eds = []
    for x in os.listdir(REV) if os.path.isdir(REV) else []:
        m = ED_RE.match(x)
        if m and os.path.isfile(os.path.join(REV, x, "index.html")):
            eds.append((m.group(2), int(m.group(1)), x))
    return sorted(eds, reverse=True)

def descarga(n):
    if os.path.isdir(DESC_DIR):
        for f in sorted(os.listdir(DESC_DIR)):
            if re.search(r"Edicion-%02d-" % n, f): return f
    return None

def importar(archivo, d, og=None):
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", d): raise SystemExit("La fecha debe ser AAAA-MM-DD (el lunes de la semana).")
    if date.fromisoformat(d).weekday() != 0: print(f"AVISO: {d} no es lunes.")
    s = read(archivo); n = numero(s)
    slug = f"edicion-{n:02d}-{d}"
    write(os.path.join(REV, slug, "index.html"), s)
    os.makedirs(DESC_DIR, exist_ok=True)
    shutil.copyfile(archivo, os.path.join(DESC_DIR, os.path.basename(archivo)))
    if og: shutil.copyfile(og, os.path.join(REV, "og-portada.jpg"))
    print("Importada", slug)

def upsert_sitemap(urls):
    p = "sitemap.xml"; s = read(p)
    for loc, lastmod, freq, prio in urls:
        block = (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
                 f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>\n")
        pat = re.compile(r"  <url>\s*<loc>%s</loc>.*?</url>\n" % re.escape(loc), re.S)
        s = pat.sub(lambda m: block, s, count=1) if pat.search(s) else s.replace("</urlset>", block + "</urlset>", 1)
    write(p, s)

def quitar_sitemap(locs):
    s = read("sitemap.xml")
    for loc in locs:
        s = re.sub(r"  <url>\s*<loc>%s</loc>.*?</url>\n" % re.escape(loc), "", s, flags=re.S)
    write("sitemap.xml", s)

def redireccion(dst, motivo):
    return ('<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="robots" content="noindex">'
            f'<link rel="canonical" href="{SITE_URL}{dst}"><meta http-equiv="refresh" content="0; url={dst}">'
            f'<title>{motivo} · El Carismático de Paterson</title></head><body><p><a href="{dst}">{motivo}</a></p></body></html>\n')

def construir():
    eds = ediciones()
    if not eds: raise SystemExit("No hay ediciones en revista/edicion-NN-AAAA-MM-DD/.")
    for d, n, slug in eds:
        p = os.path.join(REV, slug, "index.html"); url = f"{SITE_URL}/revista/{slug}/"
        s = read(p)
        s = set_meta(s, "og:url", url); s = set_meta(s, "og:image", OG_IMG); s = set_canonical(s, url)
        write(p, s)

    def botones(d, n, slug, cls_leer, cls_desc):
        f = descarga(n)
        b = f'<a class="{cls_leer}" href="/revista/{slug}/">Leer la revista →</a>'
        if f: b += f' <a class="{cls_desc}" href="/revista/descargas/{f}" download="{f}">⬇ Descargar</a>'
        return b

    d0, n0, s0 = eds[0]
    destacada = f'''<div class="rev-destacada">
      <a class="rev-portada" href="/revista/{s0}/"><img src="/revista/og-portada.jpg" alt="Portada de El Carismático de Paterson" width="1200" height="630"></a>
      <div class="rev-info">
        <span class="badge-live"><span class="badge-dot"></span>Edición de esta semana</span>
        <h2>El Carismático de Paterson · Edición n.º {n0} · {semana(d0)}</h2>
        <p>{htmlmod.escape(info(read(os.path.join(REV, s0, "index.html"))))}</p>
        <div class="rev-botones">{botones(d0, n0, s0, "btn btn-primary", "btn btn-outline")}</div>
      </div>
    </div>'''
    items = []
    for d, n, slug in eds[1:]:
        items.append(f'''      <div class="rev-item">
        <div class="rev-num">n.º {n}</div>
        <div><h3><a href="/revista/{slug}/">Edición n.º {n} · {semana(d)}</a></h3>
        <p class="rev-fecha">Lunes {fecha_larga(d)}</p>
        <p class="rev-acciones">{botones(d, n, slug, "rev-btn", "rev-btn rev-btn--alt")}</p></div>
      </div>''')
    anteriores = "\n".join(items) if items else '      <p class="rev-vacio">Aquí irán apareciendo las ediciones anteriores, una debajo de otra, cada lunes.</p>'
    style = '''<style>
.rev-destacada{display:grid;grid-template-columns:1.15fr 1fr;gap:36px;max-width:var(--max-width);margin:0 auto;align-items:center;}
.rev-portada img{width:100%;height:auto;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.35);display:block;}
.rev-info h2{color:var(--white);margin:12px 0 10px;}
.rev-info p{color:rgba(255,243,214,.85);}
.rev-botones{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px;}
.rev-list{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:18px;}
.rev-item{display:grid;grid-template-columns:90px 1fr;gap:20px;align-items:center;background:var(--white);border:1px solid rgba(8,43,76,.12);border-radius:14px;padding:18px 20px;box-shadow:0 10px 26px rgba(8,43,76,.08);}
.rev-num{width:90px;height:90px;border-radius:50%;background:linear-gradient(135deg,var(--navy),var(--navy-deep));color:var(--gold);display:flex;align-items:center;justify-content:center;font-family:var(--font-title);font-size:1.4rem;}
.rev-item h3{margin:0 0 4px;font-size:1.1rem;}.rev-item h3 a{color:var(--navy);text-decoration:none;}
.rev-item .rev-fecha{color:var(--wine);font-weight:700;font-size:.85rem;margin:2px 0 10px;}
.rev-acciones{display:flex;gap:10px;flex-wrap:wrap;margin:0;}
.rev-btn{display:inline-block;font-size:.78rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:8px 14px;border-radius:8px;background:var(--wine);color:#fff;text-decoration:none;}
.rev-btn--alt{background:transparent;color:var(--navy);border:1px solid var(--navy);}
.rev-vacio{text-align:center;color:#6b5f4a;}
@media (max-width:760px){.rev-destacada{grid-template-columns:1fr;}.rev-item{grid-template-columns:64px 1fr;gap:14px;}.rev-num{width:64px;height:64px;font-size:1.05rem;}}
</style>'''
    page = head("El Carismático de Paterson — revista semanal | RCC Paterson NJ",
                "El Carismático de Paterson, la revista semanal de la Renovación Carismática Católica de la Diócesis de Paterson, NJ. Lea o descargue la edición de esta semana y consulte las ediciones anteriores. Sale cada lunes.",
                root="../", path="revista/index.html", og_image="revista/og-portada.jpg", extra=style) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / Revista</div>
    <h1>El Carismático de Paterson</h1>
    <p class="lema">La revista semanal de la Renovación Carismática Católica</p>
    <p class="subtitle">Diócesis de Paterson, NJ · Sale cada lunes</p>
  </div>
</header>

<section class="bg-navy" id="esta-semana">
  <div class="container">
    {destacada}
  </div>
</section>

<section id="anteriores">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Archivo</span>
      <h2>Ediciones anteriores</h2>
    </div>
    <div class="rev-list">
{anteriores}
    </div>
  </div>
</section>
''' + footer(root="../") + TAIL
    write(os.path.join(REV, "index.html"), page)

    write(os.path.join(REV, "ediciones", "index.html"), redireccion("/revista/#anteriores", "Ediciones"))
    for viejo, nuevo in LEGACY.items():
        if os.path.isdir(os.path.join(REV, nuevo)):
            write(os.path.join(REV, viejo, "index.html"), redireccion(f"/revista/{nuevo}/", "Edición"))

    upsert_sitemap([(f"{SITE_URL}/revista/", d0, "weekly", "0.8")] +
                   [(f"{SITE_URL}/revista/{slug}/", d, "yearly", "0.5") for d, n, slug in eds])
    quitar_sitemap([f"{SITE_URL}/revista/ediciones/"] + [f"{SITE_URL}/revista/{v}/" for v in LEGACY])
    print("Revista: actual =", s0, "· ediciones =", len(eds))

if __name__ == "__main__":
    if len(sys.argv) in (3, 4):
        importar(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) == 4 else None)
    elif len(sys.argv) != 1:
        raise SystemExit(__doc__)
    construir()
