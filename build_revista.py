# -*- coding: utf-8 -*-
"""
REVISTA "El Carismático de Paterson" (edición semanal, sale los lunes).

Uso:
  1) Importar la edición nueva que entrega 6. Prensa y Contenido:
       python build_revista.py "<carpeta de entrega>" AAAA-MM-DD
     (la carpeta contiene index.html + og-portada.jpg; AAAA-MM-DD = lunes de la semana)
  2) Solo regenerar (sin importar nada):
       python build_revista.py

Resultado:
  revista/AAAA-MM-DD/index.html + og-portada.jpg   -> cada edición, permanente
  revista/index.html + og-portada.jpg              -> copia de la edición más reciente
  revista/ediciones/index.html                     -> listado "Ediciones anteriores"
  sitemap.xml                                      -> entradas de la revista actualizadas

El diseño y el texto de cada edición NO se modifican; solo se ajustan og:url,
og:image, canonical y se añade el enlace "Ediciones anteriores".
"""
import sys, os, re, shutil, html as htmlmod
from datetime import date
sys.path.insert(0, ".")
from common import head, footer, TAIL, SITE_URL

REV = "revista"
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre"]

def fecha_larga(d):
    y, m, dd = map(int, d.split("-"))
    return f"{dd} de {MESES[m-1]} de {y}"

def read(p):
    with open(p, encoding="utf-8") as f: return f.read()

def write(p, s):
    os.makedirs(os.path.dirname(p) or ".", exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f: f.write(s)

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

ARCHIVO_LINK = ('<p class="small rev-archivo" style="margin-top:auto"><a href="/revista/ediciones/" '
                'style="color:var(--gold-soft)">Ediciones anteriores ›</a></p>')

def preparar(s, url_pagina, url_imagen):
    s = set_meta(s, "og:url", url_pagina)
    s = set_meta(s, "og:image", url_imagen)
    s = set_canonical(s, url_pagina)
    if "rev-archivo" not in s:
        # Se coloca en la última página (Fuentes), antes del cierre de la edición
        i = s.rfind('<p class="small" style="margin-top:auto">')
        if i == -1:
            raise SystemExit("No se encontró el cierre de la página Fuentes para insertar 'Ediciones anteriores'.")
        s = s[:i] + ARCHIVO_LINK + "\n      " + s[i:].replace('style="margin-top:auto"', 'style="margin-top:10px"', 1)
    return s

def info(s):
    t = re.search(r'<meta property="og:title" content="([^"]*)">', s)
    d = re.search(r'<meta property="og:description" content="([^"]*)">', s)
    return (htmlmod.unescape(t.group(1)) if t else "El Carismático de Paterson",
            htmlmod.unescape(d.group(1)) if d else "")

def importar(carpeta, d):
    if not DATE_RE.match(d): raise SystemExit("La fecha debe ser AAAA-MM-DD (el lunes de la semana).")
    if date.fromisoformat(d).weekday() != 0: print(f"AVISO: {d} no es lunes.")
    for f in ("index.html", "og-portada.jpg"):
        if not os.path.isfile(os.path.join(carpeta, f)): raise SystemExit(f"Falta {f} en la carpeta de entrega.")
    dst = os.path.join(REV, d)
    os.makedirs(dst, exist_ok=True)
    shutil.copyfile(os.path.join(carpeta, "og-portada.jpg"), os.path.join(dst, "og-portada.jpg"))
    write(os.path.join(dst, "index.html"), read(os.path.join(carpeta, "index.html")))
    print("Importada la edición", d)

def ediciones():
    if not os.path.isdir(REV): return []
    return sorted([x for x in os.listdir(REV) if DATE_RE.match(x) and os.path.isfile(os.path.join(REV, x, "index.html"))], reverse=True)

def upsert_sitemap(urls):
    p = "sitemap.xml"; s = read(p)
    for loc, lastmod, freq, prio in urls:
        block = (f"  <url>\n    <loc>{loc}</loc>\n    <lastmod>{lastmod}</lastmod>\n"
                 f"    <changefreq>{freq}</changefreq>\n    <priority>{prio}</priority>\n  </url>\n")
        pat = re.compile(r"  <url>\s*<loc>%s</loc>.*?</url>\n" % re.escape(loc), re.S)
        s = pat.sub(lambda m: block, s, count=1) if pat.search(s) else s.replace("</urlset>", block + "</urlset>", 1)
    write(p, s)

def construir():
    eds = ediciones()
    if not eds: raise SystemExit("No hay ediciones en revista/AAAA-MM-DD/.")
    for d in eds:
        p = os.path.join(REV, d, "index.html")
        write(p, preparar(read(p), f"{SITE_URL}/revista/{d}/", f"{SITE_URL}/revista/{d}/og-portada.jpg"))
    ult = eds[0]
    s = read(os.path.join(REV, ult, "index.html"))
    write(os.path.join(REV, "index.html"), preparar(s, f"{SITE_URL}/revista/", f"{SITE_URL}/revista/og-portada.jpg"))
    shutil.copyfile(os.path.join(REV, ult, "og-portada.jpg"), os.path.join(REV, "og-portada.jpg"))

    items = []
    for d in eds:
        t, desc = info(read(os.path.join(REV, d, "index.html")))
        actual = ' <span class="badge-live"><span class="badge-dot"></span>Edición actual</span>' if d == ult else ""
        items.append(f'''      <a class="rev-item" href="/revista/{d}/">
        <img src="/revista/{d}/og-portada.jpg" alt="Portada: {htmlmod.escape(t)}" width="1200" height="630" loading="lazy">
        <div><h3>{htmlmod.escape(t)}</h3>{actual}<p class="rev-fecha">Lunes {fecha_larga(d)}</p><p>{htmlmod.escape(desc)}</p></div>
      </a>''')
    style = '''<style>
.rev-list{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:22px;}
.rev-item{display:grid;grid-template-columns:240px 1fr;gap:22px;align-items:center;background:var(--white);border:1px solid rgba(8,43,76,.12);border-radius:14px;padding:16px;text-decoration:none;color:inherit;box-shadow:0 10px 26px rgba(8,43,76,.08);}
.rev-item img{width:100%;height:auto;border-radius:10px;display:block;}
.rev-item h3{color:var(--navy);margin:0 0 6px;}
.rev-item .rev-fecha{color:var(--wine);font-weight:700;font-size:.85rem;margin:6px 0 4px;}
.rev-item p{margin:0;font-size:.92rem;}
@media (max-width:640px){.rev-item{grid-template-columns:1fr;}}
</style>'''
    page = head("Ediciones de El Carismático de Paterson | RCC Paterson NJ",
                "Todas las ediciones de El Carismático de Paterson, la revista semanal de la Renovación Carismática Católica de la Diócesis de Paterson. Sale cada lunes.",
                root="../../", path="revista/ediciones/index.html",
                og_image="revista/og-portada.jpg", extra=style) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/revista/">Revista</a> / Ediciones</div>
    <h1>El Carismático de Paterson</h1>
    <p class="lema">Ediciones anteriores</p>
    <p class="subtitle">La revista semanal de la Renovación Carismática Católica de la Diócesis de Paterson · Sale cada lunes</p>
  </div>
</header>

<section>
  <div class="container">
    <div class="rev-list">
{chr(10).join(items)}
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="/revista/">Leer la edición de esta semana →</a>
</section>
''' + footer(root="../../") + TAIL
    write(os.path.join(REV, "ediciones", "index.html"), page)

    hoy = date.today().isoformat()
    urls = [(f"{SITE_URL}/revista/", ult, "weekly", "0.8"), (f"{SITE_URL}/revista/ediciones/", ult, "weekly", "0.5")]
    urls += [(f"{SITE_URL}/revista/{d}/", d, "yearly", "0.4") for d in eds]
    upsert_sitemap(urls)
    print("Revista: actual =", ult, "· ediciones =", len(eds))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        importar(sys.argv[1], sys.argv[2])
    elif len(sys.argv) != 1:
        raise SystemExit(__doc__)
    construir()
