# Componentes compartidos: nav, footer, estilos base, datos institucionales
SOCIAL_ICONS = {
"ig": '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.2" cy="6.8" r="1.1" fill="currentColor"/></svg>',
"fb": '<svg viewBox="0 0 24 24"><path d="M14 21v-8h2.6l.4-3H14V8c0-.9.3-1.5 1.6-1.5H17V4c-.3 0-1.3-.1-2.4-.1-2.4 0-4 1.5-4 4.1V10H8v3h2.6v8h3.4z" fill="currentColor"/></svg>',
"tt": '<svg viewBox="0 0 24 24"><path d="M16 2h2.8c.3 2 1.8 3.5 3.7 3.8v2.9c-1.4 0-2.7-.4-3.7-1.1v6.6c0 3.4-2.7 6-6.1 6a6 6 0 0 1-1.4-11.9v3.1a2.9 2.9 0 1 0 2.4 2.9V2z" fill="currentColor"/></svg>',
"yt": '<svg viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="4" fill="none" stroke="currentColor" stroke-width="1.8"/><path d="M10 9.5l6 2.5-6 2.5z" fill="currentColor"/></svg>',
"mail": '<svg class="mail-icon" viewBox="0 0 24 24"><path d="M4 6h16a1 1 0 0 1 1 1v10a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1zm0 2.4V17h16V8.4l-7.4 5.1a1 1 0 0 1-1.2 0L4 8.4zm.6-.4 7.4 5 7.4-5H4.6z" fill="currentColor"/></svg>',
"phone": '<svg class="phone-icon" viewBox="0 0 24 24"><path d="M6.6 10.8c1.4 2.8 3.8 5.1 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1C10.6 21 3 13.4 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.6.1.4 0 .8-.3 1L6.6 10.8z" fill="currentColor"/></svg>',
"wa": '<svg viewBox="0 0 24 24"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.79.47 3.48 1.32 4.95L2 22l5.25-1.38c1.41.77 3 1.18 4.79 1.18h.01c5.46 0 9.91-4.45 9.91-9.91 0-2.65-1.03-5.14-2.9-7.01A9.82 9.82 0 0 0 12.04 2m0 1.67c2.19 0 4.25.85 5.79 2.4a8.2 8.2 0 0 1 2.41 5.84c0 4.55-3.7 8.25-8.25 8.25h-.01c-1.57 0-3.1-.44-4.43-1.28l-.32-.19-3.11.82.83-3.04-.21-.31a8.19 8.19 0 0 1-1.27-4.4c0-4.55 3.71-8.25 8.26-8.25M8.53 6.9c-.16 0-.42.06-.64.31s-.85.83-.85 2.02.87 2.35.99 2.51 1.7 2.73 4.19 3.73c2.07.83 2.49.66 2.94.62.45-.04 1.44-.59 1.65-1.16s.21-1.06.15-1.16-.24-.16-.5-.28-1.55-.76-1.79-.85-.42-.13-.6.13-.68.85-.84 1.03-.31.19-.58.06a7.3 7.3 0 0 1-2.15-1.33 8.06 8.06 0 0 1-1.49-1.85c-.16-.27-.02-.41.12-.55.12-.12.27-.31.4-.47.13-.16.17-.27.26-.45.09-.19.04-.35-.02-.49s-.6-1.45-.82-1.98c-.22-.53-.44-.44-.6-.45z" fill="currentColor"/></svg>',
}

def social_row(cls="social-row"):
    return f'''<div class="{cls}" aria-label="Redes sociales">
      <a href="https://instagram.com/rccpatersonnj" target="_blank" rel="noopener" aria-label="Instagram">{SOCIAL_ICONS['ig']}</a>
      <a href="https://facebook.com/rccpatersonnj" target="_blank" rel="noopener" aria-label="Facebook">{SOCIAL_ICONS['fb']}</a>
      <a href="https://tiktok.com/@rccpatersonnj" target="_blank" rel="noopener" aria-label="TikTok">{SOCIAL_ICONS['tt']}</a>
      <a href="https://youtube.com/@rccpatersonnj" target="_blank" rel="noopener" aria-label="YouTube">{SOCIAL_ICONS['yt']}</a>
    </div>'''

def nav(root=""):
    """root = '' para paginas en la raiz, '../' para paginas en subcarpetas"""
    r = root
    return f'''<nav class="site-nav">
  <div class="container">
    <a class="nav-brand" href="{r}index.html">
      <img src="{r}assets/img/escudo-rcc-oficial.webp" alt="RCC Paterson NJ" width="700" height="700">
      RCC Paterson NJ
    </a>
    <button class="nav-toggle" aria-label="Abrir menú" onclick="document.querySelector('.nav-links').classList.toggle('is-open')">☰</button>
    <div class="nav-links">
      <div class="nav-item has-dropdown">
        <a href="{r}index.html#quienes-somos">Quiénes Somos</a>
        <div class="nav-dropdown">
          <a href="{r}index.html#quienes-somos">Quiénes Somos</a>
          <a href="{r}index.html#identidad">Misión, Visión y Valores</a>
          <a href="{r}index.html#comite">Comité Diocesano</a>
          <a href="{r}index.html#departamentos">Departamentos</a>
        </div>
      </div>
      <div class="nav-item has-dropdown">
        <a href="{r}index.html#ministerios">Ministerios</a>
        <div class="nav-dropdown">
          <a href="{r}ministerios/intercesion.html">Intercesión</a>
          <a href="{r}ministerios/hombres-alabanza.html">Hombres de Alabanza</a>
          <a href="{r}ministerios/mujeres-alabanza.html">Mujeres de Alabanza</a>
          <a href="{r}index.html#ministerios">Comunicación y Publicidad</a>
          <a href="{r}ministerios/musica.html">Ministerios de Música</a>
          <a href="{r}index.html#ministerios">RCC Youth</a>
          <a href="{r}ministerios/escuela-formacion-lideres.html">Escuela de Formación de Líderes</a>
          <a href="{r}index.html#ministerios">Seminario de Vida en el Espíritu</a>
          <a href="{r}ministerios/hospitalidad-caridad.html">Hospitalidad y Caridad</a>
          <a href="{r}ministerios/colaboradores.html">Colaboradores</a>
        </div>
      </div>
      <a href="{r}index.html#grupos-oracion">Grupos de Oración</a>
      <a href="{r}ministerios/escuela-formacion-lideres.html">Escuela de Líderes</a>
      <a href="{r}index.html#eventos">Eventos</a>
      <a href="{r}index.html#preguntas-frecuentes">Preguntas</a>
      <a href="{r}index.html#contacto">Contacto</a>
    </div>
  </div>
</nav>'''

def footer(root=""):
    r = root
    return f'''<footer class="site-footer" id="contacto">
  <img class="footer-logo" src="{r}assets/img/escudo-rcc-oficial.webp" alt="Logo RCC Paterson NJ" width="700" height="700">
  {social_row()}
  <div class="footer-affiliations">
    <span class="footer-affiliations-label">En comunión con</span>
    <div class="affiliation-logos">
      <a href="https://rcdop.org/" target="_blank" rel="noopener" class="affiliation-logo">
        <img src="{r}assets/img/logo-diocesis-paterson.webp" alt="Diócesis de Paterson" width="508" height="196" loading="lazy">
        <span>Diócesis de Paterson</span>
      </a>
      <a href="https://rcchispana.org/" target="_blank" rel="noopener" class="affiliation-logo">
        <img src="{r}assets/img/logo-rcc-hispana.webp" alt="Renovación Carismática Católica de los Estados Unidos y Canadá" width="358" height="179" loading="lazy">
        <span>Renovación Carismática Católica de Estados Unidos y Canadá</span>
      </a>
    </div>
  </div>
  <p class="footer-org">Renovación Carismática Católica &middot; Diócesis de Paterson</p>
  <p class="footer-email">
    <a href="mailto:renovacion@rccpaterson.org">{SOCIAL_ICONS['mail']} renovacion@rccpaterson.org</a>
  </p>
  <p><a class="back-home" href="{r}index.html">&larr; Volver al inicio</a></p>
  <p class="fine-print">&copy; 2026 Renovación Carismática Católica — Diócesis de Paterson. Todos los derechos reservados.</p>
</footer>

<script src="{r}assets/js/site.js"></script>'''

SITE_URL = "https://rccpatersonnj.com"
SITE_NAME = "RCC Paterson NJ"
GA_MEASUREMENT_ID = "G-ZNXPXCSJ95"

GA_SNIPPET = f'''<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_MEASUREMENT_ID}');
</script>'''

# Verificacion de propiedad en Google Search Console (metodo secundario,
# ademas de la verificacion automatica via Google Analytics) -- agregado
# 2026-08-22. No quitar aunque la verificacion ya este activa.
GSC_VERIFICATION = '<meta name="google-site-verification" content="NYK79oYRoS6LrTeZdFkwwYazL9m3hNlgPl2D6oS4g9c" />'

# Datos estructurados (JSON-LD) de la organización -- se inyectan en TODAS las
# paginas via head() para que Google/IA puedan identificar quienes somos,
# donde estamos y como contactarnos (AEO). No se declara una direccion fisica
# propia porque la RCC no tiene sede unica -- opera a traves de los grupos de
# oracion en distintas parroquias de la Diocesis de Paterson.
ORG_JSONLD = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ReligiousOrganization",
  "name": "Renovación Carismática Católica - Diócesis de Paterson",
  "alternateName": ["RCC Paterson NJ", "Centro Carismático Católico Digital de la Diócesis de Paterson"],
  "url": "{SITE_URL}/",
  "logo": "{SITE_URL}/assets/img/escudo-rcc-oficial.webp",
  "image": "{SITE_URL}/assets/img/escudo-rcc-oficial.webp",
  "email": "renovacion@rccpaterson.org",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "Diócesis de Paterson, Nueva Jersey"
  }},
  "sameAs": [
    "https://instagram.com/rccpatersonnj",
    "https://facebook.com/rccpatersonnj",
    "https://tiktok.com/@rccpatersonnj",
    "https://youtube.com/@rccpatersonnj"
  ]
}}
</script>'''

def head(title, desc, root="", extra="", path="", og_image="", og_description=""):
    """path = ruta relativa desde la raiz del sitio para la URL canonica,
    ej. '' (home), 'eccads/', 'ministerios/intercesion.html'.
    og_image = ruta relativa a una imagen 1200x630 para redes sociales;
    si se omite, usa la imagen genérica del sitio.
    og_description = texto para la vista previa al compartir el link (WhatsApp,
    Telegram, Facebook, etc.) -- si se omite, usa el mismo texto que `desc`
    (la meta description de SEO). Se agregó 2026-08 para poder tener un mensaje
    de marca distinto al compartir el link sin afectar el snippet de Google."""
    r = root
    canonical = f"{SITE_URL}/{path}"
    image = f"{SITE_URL}/{og_image}" if og_image else f"{SITE_URL}/assets/img/og-image.jpg"
    share_desc = og_description if og_description else desc
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
{GSC_VERIFICATION}
{GA_SNIPPET}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{share_desc}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_US">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{share_desc}">
<meta name="twitter:image" content="{image}">
<link rel="icon" type="image/x-icon" href="{r}favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="{r}assets/img/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{r}assets/img/favicon/favicon-16x16.png">
<link rel="apple-touch-icon" href="{r}apple-touch-icon.png">
<link rel="manifest" href="{r}site.webmanifest">
<link rel="stylesheet" href="{r}assets/css/fonts.css">
<link rel="stylesheet" href="{r}assets/css/style.css">
{ORG_JSONLD}
{extra}
</head>
<body>
{nav(r)}'''

TAIL = '''
</body>
</html>
'''
