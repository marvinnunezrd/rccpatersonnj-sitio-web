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

ARCHIVO_LINK = ('<p class="small rev-archivo" style="margin-top:auto"><a href="/revista/#anteriores" '
                'style="color:var(--gold-soft)">Todas las ediciones ›</a></p>')

def preparar(s, url_pagina, url_imagen):
    s = set_meta(s, "og:url", url_pagina)
    s = set_meta(s, "og:image", url_imagen)
    s = set_canonical(s, url_pagina)
    s = s.replace('href="/revista/ediciones/" style="color:var(--gold-soft)">Ediciones anteriores ›', 'href="/revista/#anteriores" style="color:var(--gold-soft)">Todas las ediciones ›')
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
    shutil.copyfile(os.path.join(REV, ult, "og-portada.jpg"), os.path.join(REV, "og-portada.jpg"))

    def descarga(d):
        # Si Prensa entrega un PDF (revista/AAAA-MM-DD/*.pdf) se ofrece ese; si no, la revista
        # completa como un solo archivo .html que se abre sin conexión.
        pdfs = sorted(f for f in os.listdir(os.path.join(REV, d)) if f.lower().endswith(".pdf"))
        if pdfs:
            return f"/revista/{d}/{pdfs[0]}", f"El-Carismatico-de-Paterson-{d}.pdf", "Descargar PDF"
        return f"/revista/{d}/index.html", f"El-Carismatico-de-Paterson-{d}.html", "Descargar edición"

    t, desc = info(read(os.path.join(REV, ult, "index.html")))
    href, fname, label = descarga(ult)
    destacada = f'''<div class="rev-destacada">
      <a class="rev-portada" href="/revista/{ult}/"><img src="/revista/{ult}/og-portada.jpg" alt="Portada: {htmlmod.escape(t)}" width="1200" height="630"></a>
      <div class="rev-info">
        <span class="badge-live"><span class="badge-dot"></span>Edición de esta semana</span>
        <h2>{htmlmod.escape(t)}</h2>
        <p class="rev-fecha">Lunes {fecha_larga(ult)}</p>
        <p>{htmlmod.escape(desc)}</p>
        <div class="rev-botones">
          <a class="btn btn-primary" href="/revista/{ult}/">Leer en línea →</a>
          <a class="btn btn-outline" href="{href}" download="{fname}">⬇ {label}</a>
        </div>
      </div>
    </div>'''

    items = []
    for d in eds[1:]:
        t2, desc2 = info(read(os.path.join(REV, d, "index.html")))
        h2, f2, l2 = descarga(d)
        items.append(f'''      <div class="rev-item">
        <a href="/revista/{d}/"><img src="/revista/{d}/og-portada.jpg" alt="Portada: {htmlmod.escape(t2)}" width="1200" height="630" loading="lazy"></a>
        <div><h3><a href="/revista/{d}/">{htmlmod.escape(t2)}</a></h3><p class="rev-fecha">Lunes {fecha_larga(d)}</p><p>{htmlmod.escape(desc2)}</p>
        <p class="rev-acciones"><a href="/revista/{d}/">Leer →</a> · <a href="{h2}" download="{f2}">{l2}</a></p></div>
      </div>''')
    anteriores = ("\n".join(items) if items else
                  '      <p class="rev-vacio">Aquí irán apareciendo las ediciones anteriores, una debajo de otra, cada lunes.</p>')

    style = '''<style>
.rev-destacada{display:grid;grid-template-columns:1.15fr 1fr;gap:36px;max-width:var(--max-width);margin:0 auto;align-items:center;}
.rev-portada img{width:100%;height:auto;border-radius:14px;box-shadow:0 20px 50px rgba(0,0,0,.35);display:block;}
.rev-info h2{color:var(--white);margin:12px 0 4px;}
.rev-info p{color:rgba(255,243,214,.85);}
.rev-info .rev-fecha{color:var(--gold);font-weight:700;}
.rev-botones{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px;}
.rev-list{max-width:820px;margin:0 auto;display:flex;flex-direction:column;gap:22px;}
.rev-item{display:grid;grid-template-columns:240px 1fr;gap:22px;align-items:center;background:var(--white);border:1px solid rgba(8,43,76,.12);border-radius:14px;padding:16px;box-shadow:0 10px 26px rgba(8,43,76,.08);}
.rev-item img{width:100%;height:auto;border-radius:10px;display:block;}
.rev-item h3{margin:0 0 4px;}.rev-item h3 a{color:var(--navy);text-decoration:none;}
.rev-item .rev-fecha{color:var(--wine);font-weight:700;font-size:.85rem;margin:4px 0;}
.rev-item p{margin:0 0 6px;font-size:.92rem;}
.rev-acciones a{font-weight:700;color:var(--wine);}
.rev-vacio{text-align:center;color:#6b5f4a;}
@media (max-width:760px){.rev-destacada{grid-template-columns:1fr;}.rev-item{grid-template-columns:1fr;}}
</style>'''
    page = head("El Carismático de Paterson — revista semanal | RCC Paterson NJ",
                "El Carismático de Paterson, la revista semanal de la Renovación Carismática Católica de la Diócesis de Paterson. Lea en línea o descargue la edición de esta semana y consulte las ediciones anteriores. Sale cada lunes.",
                root="../", path="revista/index.html", og_image="revista/og-portada.jpg",
                og_description=desc or None, extra=style) + f'''
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

    # /revista/ediciones/ (enlace antiguo) -> redirige a /revista/#anteriores
    write(os.path.join(REV, "ediciones", "index.html"),
          '<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><meta name="robots" content="noindex">'
          f'<link rel="canonical" href="{SITE_URL}/revista/"><meta http-equiv="refresh" content="0; url=/revista/#anteriores">'
          '<title>Ediciones · El Carismático de Paterson</title></head><body><p><a href="/revista/#anteriores">Ver las ediciones</a></p></body></html>\n')

    urls = [(f"{SITE_URL}/revista/", ult, "weekly", "0.8")]
    urls += [(f"{SITE_URL}/revista/{d}/", d, "yearly", "0.5") for d in eds]
    upsert_sitemap(urls)
    sm = read("sitemap.xml")
    sm = re.sub(r"  <url>\s*<loc>%s</loc>.*?</url>\n" % re.escape(f"{SITE_URL}/revista/ediciones/"), "", sm, flags=re.S)
    write("sitemap.xml", sm)
    print("Revista: actual =", ult, "· ediciones =", len(eds))

if __name__ == "__main__":
    if len(sys.argv) == 3:
        importar(sys.argv[1], sys.argv[2])
    elif len(sys.argv) != 1:
        raise SystemExit(__doc__)
    construir()
