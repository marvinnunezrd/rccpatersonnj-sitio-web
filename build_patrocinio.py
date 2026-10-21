# -*- coding: utf-8 -*-
"""
PATROCINIO — brochure bilingüe "Sembremos juntos / Let's sow together".

Uso:
  python build_patrocinio.py ["<carpeta Version Digital>"]
  (por defecto: ../Comunicacion y Publicidad/Contenido y Diseños/Propuesta de Patrocinio/Version Digital 2026-10-20)

Resultado en patrocinio/:
  index.html  (brochure original; solo se añade en el <head> favicon + Open Graph/Twitter,
               y en la última lámina los botones de descarga de los PDF)
  Sembremos-Juntos-Patrocinio-RCC-Paterson-ES.pdf
  Lets-Sow-Together-Sponsorship-RCC-Paterson-EN.pdf
  og-sembremos-juntos.jpg (1200x630: portada + Escudo Oficial)

Accesos directos por idioma: /patrocinio/#es y /patrocinio/#en
"""
import sys, os, re, io, shutil, base64
sys.path.insert(0, ".")
from common import SITE_URL
from PIL import Image, ImageDraw, ImageFilter, ImageFont

SRC = sys.argv[1] if len(sys.argv) > 1 else os.path.join("..", "Comunicacion y Publicidad", "Contenido y Diseños", "Propuesta de Patrocinio", "Version Digital 2026-10-20")
HTML_SRC = "Sembremos-Juntos-RCC-Paterson-Brochure-Movil.html"
PDF_ES = "Sembremos-Juntos-Patrocinio-RCC-Paterson-ES.pdf"
PDF_EN = "Lets-Sow-Together-Sponsorship-RCC-Paterson-EN.pdf"
OUT = "patrocinio"
OG = "og-sembremos-juntos.jpg"
URL = f"{SITE_URL}/patrocinio/"

TITLE = "Sembremos juntos · Let’s sow together | RCC Paterson NJ"
DESC = ("Propuesta de patrocinio de la Renovación Carismática Católica Hispana de la Diócesis de Paterson, NJ. "
        "Sponsorship proposal of the Hispanic Catholic Charismatic Renewal, Diocese of Paterson, NJ.")

HEAD_TAGS = f'''<link rel="canonical" href="{URL}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon/favicon-32x32.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta property="og:type" content="website">
<meta property="og:site_name" content="RCC Paterson NJ">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{URL}{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_US">
<meta property="og:locale:alternate" content="en_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{TITLE}">
<meta name="twitter:description" content="{DESC}">
<meta name="twitter:image" content="{URL}{OG}">
'''

PDF_CSS = ('.pdfs{display:flex;gap:8px;justify-content:center;flex-wrap:wrap;margin-top:6px}'
           '.pdfs a{font-size:12px;font-weight:700;text-decoration:none;color:var(--cream-soft);border:1px solid rgba(226,182,92,.55);'
           'border-radius:999px;padding:6px 12px}.pdfs a:hover{background:var(--navy-2)}\n')
PDF_BTNS = (f'<div class="pdfs"><a href="{PDF_ES}" download lang="es">Descargar PDF (ES)</a>'
            f'<a href="{PDF_EN}" download lang="en">Download PDF (EN)</a></div>')

def data_uri_img(s, key):
    m = re.search(r'"%s":\s*"data:image/[a-z]+;base64,([^"]+)"' % re.escape(key), s)
    if not m: raise SystemExit(f"No se encontró la imagen {key} en el brochure.")
    return Image.open(io.BytesIO(base64.b64decode(m.group(1))))

def font(paths, size):
    for p in paths:
        if os.path.exists(p): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def og_image(s, dst):
    W, H = 1200, 630
    bg = data_uri_img(s, "alabanza").convert("RGB")
    r = max(W / bg.width, H / bg.height)
    bg = bg.resize((round(bg.width * r), round(bg.height * r)), Image.LANCZOS)
    x, y = (bg.width - W) // 2, (bg.height - H) // 2
    bg = bg.crop((x, y, x + W, y + H))
    ov = Image.new("RGBA", (W, H))
    d = ImageDraw.Draw(ov)
    for i in range(W):  # degradado navy de izquierda a derecha
        a = int(245 - 150 * (i / W))
        d.line([(i, 0), (i, H)], fill=(20, 33, 61, a))
    img = Image.alpha_composite(bg.convert("RGBA"), ov)
    crest = data_uri_img(s, "escudo").convert("RGBA")
    crest.thumbnail((210, 210), Image.LANCZOS)
    img.alpha_composite(crest, (70, (H - crest.height) // 2 - 95))
    d = ImageDraw.Draw(img)
    serif = ["/usr/share/fonts/truetype/google-fonts/Lora-Variable.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", "C:/Windows/Fonts/georgiab.ttf"]
    sans = ["/usr/share/fonts/truetype/lato/Lato-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "C:/Windows/Fonts/arialbd.ttf"]
    f1 = font(serif, 82); 
    try: f1.set_variation_by_name("Bold")
    except Exception: pass
    f2 = font(serif, 46)
    f3 = font(sans, 26)
    tx = 70; ty = H // 2 + 30
    d.text((tx, ty), "Sembremos juntos", font=f1, fill=(251, 246, 236))
    d.text((tx, ty + 96), "Let’s sow together", font=f2, fill=(226, 182, 92))
    d.text((tx, ty + 165), "RENOVACIÓN CARISMÁTICA CATÓLICA · DIÓCESIS DE PATERSON, NJ", font=f3, fill=(230, 220, 200))
    img.convert("RGB").save(dst, "JPEG", quality=86, optimize=True, progressive=True)

def main():
    s = open(os.path.join(SRC, HTML_SRC), encoding="utf-8").read()
    # 1) <head>: título bilingüe en las etiquetas sociales, favicon y Open Graph/Twitter
    anchor = re.search(r'<meta name="description"[^>]*>\n', s)
    if not anchor: raise SystemExit("No se encontró <meta name=description> en el brochure.")
    s = s[:anchor.end()] + HEAD_TAGS + s[anchor.end():]
    # 2) CSS de los botones de descarga (al final del <style> existente)
    s = s.replace("</style>", PDF_CSS + "</style>", 1)
    # 3) Botones en la última lámina (después de las redes sociales del agradecimiento)
    marca = '<a class="chip lk" href="${SOC.tt}" target="_blank" rel="noopener">TikTok</a></div>\n    </div></section>`);'
    if s.count(marca) != 1: raise SystemExit("No se encontró el cierre de la lámina final del brochure.")
    s = s.replace(marca, marca.replace("</div>\n    </div></section>", "</div>\n    " + PDF_BTNS + "\n    </div></section>"))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8", newline="\n") as f: f.write(s)
    for pdf in (PDF_ES, PDF_EN): shutil.copyfile(os.path.join(SRC, pdf), os.path.join(OUT, pdf))
    og_image(s, os.path.join(OUT, OG))
    from build_revista import upsert_sitemap
    upsert_sitemap([(URL, "2026-10-21", "monthly", "0.6")])
    print("patrocinio/ generado:", sorted(os.listdir(OUT)))

if __name__ == "__main__":
    main()
