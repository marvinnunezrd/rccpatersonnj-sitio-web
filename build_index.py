import sys
sys.path.insert(0, ".")
from common import head, footer, TAIL, social_row, SOCIAL_ICONS
from data import COMITE, ZONA_COORDINADORES, GRUPOS_ORACION, AGENDA, MINISTERIOS, PARROQUIA_URLS

PHONE_ICON = SOCIAL_ICONS['phone']

IMG = {
  "escudo_rcc": "assets/img/escudo-rcc-oficial.webp",
  "escudo_efl": "assets/img/escudo-efl.webp",
  "m_intercesion": "assets/img/ministerios/intercesion.webp",
  "m_hombres": "assets/img/ministerios/hombres-alabanza.webp",
  "m_mujeres": "assets/img/ministerios/mujeres-alabanza.webp",
  "m_comunicacion": "assets/img/ministerios/comunicacion.webp",
  "m_musica": "assets/img/ministerios/musica.webp",
  "m_youth": "assets/img/ministerios/youth.webp",
  "m_sve": "assets/img/ministerios/sve.webp",
  "eccads_mini": "assets/img/eccads-mini.png",
  "pentecostes_mini": "assets/img/pentecostes-2026-mini.webp",
  "featured": "assets/img/featured-comite-obispo.webp",
}

CAROUSEL_FILES = [f"assets/img/carousel/slide-{i:02d}.webp" for i in range(11)]
carousel_slides = "\n".join(
    # La primera slide lleva "is-first" ademas de "is-active": esa clase
    # anula la transicion de opacidad SOLO en la primera pintura de la
    # pagina, para que el elemento LCP (esta imagen de fondo) no espere la
    # animacion de 1.6s antes de considerarse "pintado". site.js le quita
    # la clase "is-first" en el primer cambio de slide, asi que el efecto
    # de fundido del carrusel sigue intacto para todos los demas cambios
    # (agregado 2026-08-22, hallazgo de PageSpeed Insights: "Retraso en la
    # renderizacion del elemento" ~2s coincidia con esta transicion).
    f'<div class="hero-bg-slide{" is-active is-first" if i == 0 else ""}" style="background-image:url({f})"></div>'
    for i, f in enumerate(CAROUSEL_FILES)
)

# Precarga la primera imagen del carrusel del hero -- es el elemento LCP (Largest
# Contentful Paint) de la portada, pero al cargarse como background-image de un
# <div> (no como <img>) el navegador no la descubre hasta que corre el JS del
# carrusel. Este preload la hace descubrible desde el HTML y con fetchpriority
# alto, tal como recomienda el reporte de PageSpeed Insights (agregado 2026-08-21).
HERO_LCP_PRELOAD = f'<link rel="preload" as="image" href="{CAROUSEL_FILES[0]}" fetchpriority="high">'

# Fotos individuales del Comité Diocesano (agregadas 2026-08-22). Recortadas
# y centradas en el rostro de cada persona para el marco circular de la
# tarjeta -- ver assets/img/comite/.
COMITE_PHOTOS = {
    "Rev. Yasid Salas": "assets/img/comite/yasid-salas.webp",
    "Teresa Amparo": "assets/img/comite/teresa-amparo.webp",
    "Librada Rosario": "assets/img/comite/librada-rosario.webp",
    "Dariberkis Taveras-Beato": "assets/img/comite/dariberkis-taveras.webp",
    "Alis Amparo": "assets/img/comite/alis-amparo.webp",
    "Juana De Jesús": "assets/img/comite/juana-de-jesus.webp",
    "Marvin Núñez": "assets/img/comite/marvin-nunez.webp",
    "Marizabel Pérez": "assets/img/comite/marizabel-perez.webp",
}

def parish_link(name):
    """Devuelve el nombre de la parroquia como enlace a su sitio web oficial
    si lo tenemos verificado en PARROQUIA_URLS; si no, el nombre en texto plano."""
    url = PARROQUIA_URLS.get(name)
    if not url:
        return name
    return f'<a href="{url}" target="_blank" rel="noopener">{name}</a>'

def comite_card(name, role, parish):
    parish_html = f'<p class="parish">{parish_link(parish)}</p>' if parish else ""
    photo = COMITE_PHOTOS.get(name)
    photo_html = (
        f'<div class="comite-photo"><img src="{photo}" alt="{name}" width="180" height="180" loading="lazy"></div>'
        if photo else ""
    )
    return f'''
        <div class="comite-card">
          {photo_html}
          <h3>{name}</h3>
          <p class="role">{role}</p>
          {parish_html}
        </div>'''

comite_cards = "\n".join(comite_card(*c) for c in COMITE)

def min_card(key, name, desc, href):
    return f'''
        <div class="min-card">
          <a href="{href}">
          <img src="{IMG[key]}" alt="Logo {name}" width="360" height="360">
          <h3>{name}</h3>
          <p>{desc}</p>
          <span class="card-cta">Conocer más →</span>
          </a>
        </div>'''

min_cards = "\n".join(min_card(*m) for m in MINISTERIOS)

def agenda_item(d, mes, anio, titulo, hora, lugar, nota, href=None):
    nota_html = f'<p class="agenda-note">{nota}</p>' if nota else ""
    link_html = f'<p class="agenda-note"><a class="agenda-link" href="{href}">Ver detalles y flyer completo →</a></p>' if href else ""
    return f'''
      <div class="agenda-item">
        <div class="agenda-date"><div class="d">{d}</div><div class="m">{mes}</div><div class="y">{anio}</div></div>
        <div class="agenda-body">
          <h4>{titulo}</h4>
          <p class="agenda-meta">🕑 {hora} &nbsp;·&nbsp; 📍 {lugar}</p>
          {nota_html}{link_html}
        </div>
      </div>'''

agenda_items_html = "\n".join(agenda_item(*a) for a in AGENDA)

zona_legend = "\n".join(f'<div class="zona-chip"><strong>{z}</strong> — {c}</div>' for z, c in ZONA_COORDINADORES)

def _tel_href(telefono):
    # usa solo el primer numero si hay varios separados por " / "
    first = telefono.split(" / ")[0]
    digits = "".join(ch for ch in first if ch.isdigit())
    return f"tel:+1{digits}" if digits else "#"

def grupo_row(g):
    horario = g["horario"] or "Por confirmar"
    return f'''
        <div class="grupo-row">
          <div class="gr-col gr-horario"><span class="gr-label">Horario</span><span class="gr-value">{horario}</span></div>
          <div class="gr-col gr-nombre"><span class="gr-label">Grupo</span><span class="gr-value">{g["grupo"]}</span></div>
          <div class="gr-col gr-parroquia"><span class="gr-label">Parroquia</span><span class="gr-value">{parish_link(g["parroquia"])}</span></div>
          <div class="gr-col gr-direccion"><span class="gr-label">Dirección</span><span class="gr-value">{g["direccion"]}</span></div>
          <div class="gr-col gr-coord"><span class="gr-label">Coordinador(a)</span><span class="gr-value">{g["coordinador"]}</span></div>
          <div class="gr-col gr-tel"><span class="gr-label">Teléfono</span><span class="gr-value"><a href="{_tel_href(g["telefono"])}">{PHONE_ICON} {g["telefono"]}</a></span></div>
          <div class="gr-col gr-zona"><span class="gr-label">Zona</span><span class="gr-value">{g["zona"]}</span></div>
        </div>'''

DIAS_ORDEN = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def build_grupos_by_day(grupos):
    por_dia = {d: [] for d in DIAS_ORDEN}
    for g in grupos:
        por_dia[g["dia"]].append(g)
    blocks = []
    for d in DIAS_ORDEN:
        dia_grupos = por_dia[d]
        if not dia_grupos:
            continue
        rows = "\n".join(grupo_row(g) for g in dia_grupos)
        blocks.append(f'''
      <div class="oracion-day">
        <h3 class="oracion-day-heading">{d}</h3>
        <div class="grupo-rows">{rows}
        </div>
      </div>''')
    return "\n".join(blocks)

grupos_by_day_html = build_grupos_by_day(GRUPOS_ORACION)

FAQ_JSONLD = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "¿Qué es la Renovación Carismática Católica?",
      "acceptedAnswer": {"@type": "Answer", "text": "Es un movimiento dentro de la Iglesia Católica que promueve la experiencia del Bautismo en el Espíritu Santo y busca renovar la vida de fe de la comunidad a través de la oración, la alabanza y el servicio. En la Diócesis de Paterson, NJ, agrupa a 18 grupos de oración y 8 ministerios diocesanos bajo un mismo Comité Diocesano."}},
    {"@type": "Question", "name": "¿La Renovación Carismática Católica es parte de la Iglesia Católica?",
      "acceptedAnswer": {"@type": "Answer", "text": "Sí. La RCC es un movimiento eclesial reconocido que vive y sirve en comunión con la Iglesia Católica, sus pastores y la Diócesis de Paterson — no es una iglesia aparte ni una denominación distinta."}},
    {"@type": "Question", "name": "¿Cuál es la diferencia entre la Renovación Carismática Católica y una iglesia pentecostal?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ambas valoran la experiencia del Espíritu Santo, pero la RCC es un movimiento dentro de la Iglesia Católica —con Misa, sacramentos y comunión con el Papa y los obispos— mientras que las iglesias pentecostales son denominaciones protestantes independientes. La RCC Paterson funciona a través de las parroquias católicas de la diócesis."}},
    {"@type": "Question", "name": "¿Cómo me uno a un grupo de oración de la RCC Paterson?",
      "acceptedAnswer": {"@type": "Answer", "text": "Puedes visitar cualquiera de los 18 grupos de oración de la RCC Paterson, organizados por parroquia, día y zona — consulta el horario, la dirección y el coordinador de cada uno en la sección \\"Grupos de Oración\\" de esta página, o contáctanos directamente para que te orientemos hacia el más cercano a ti."}},
    {"@type": "Question", "name": "¿Qué ministerios tiene la RCC Paterson?",
      "acceptedAnswer": {"@type": "Answer", "text": "Ocho: Intercesión, Hombres de Alabanza, Mujeres de Alabanza, Comunicación y Publicidad, Ministerios de Música, RCC Youth, la Escuela de Formación de Líderes y el Seminario de Vida en el Espíritu. Puedes conocer cada uno en la sección \\"Ministerios\\" de esta página."}},
    {"@type": "Question", "name": "¿Cómo contacto a la RCC Paterson?",
      "acceptedAnswer": {"@type": "Answer", "text": "Puedes escribirnos a renovacion@rccpaterson.org, seguirnos en Instagram, Facebook, TikTok y YouTube como @rccpatersonnj, o contactar directamente al coordinador del grupo de oración o ministerio de tu interés."}}
  ]
}
</script>'''

HTML = head(
    "RCC Paterson NJ — Renovación Carismática Católica",
    "Sitio web oficial de la Renovación Carismática Católica de la Diócesis de Paterson, NJ: grupos de oración, ministerios, eventos y el Comité Diocesano.",
    path="",
    og_description="El Centro Carismático Católico Digital de la Diócesis de Paterson: grupos de oración, ministerios, eventos y el Comité Diocesano, todos bajo un mismo techo.",
    extra=HERO_LCP_PRELOAD + FAQ_JSONLD,
) + f'''
<header class="hero-main">
  <div class="hero-bg-carousel">{carousel_slides}</div>
  <div class="hero-bg-overlay"></div>
  <div class="container">
    <img class="hero-shield" src="{IMG['escudo_rcc']}" alt="Escudo oficial de la Renovación Carismática Católica de la Diócesis de Paterson" width="700" height="700">
    <span class="eyebrow">Diócesis de Paterson, Nueva Jersey</span>
    <h1>Renovación Carismática<br>Católica</h1>
    <p class="hero-tagline">El Centro Carismático Católico Digital de la Diócesis de Paterson</p>
    <p class="hero-lema">&ldquo;Ven Espíritu Santo, enciende tu fuego&rdquo;</p>
    <div class="hero-cta">
      <a class="btn btn-primary" href="eccads/index.html">ECCADS 2026 →</a>
      <a class="btn btn-outline" href="#ministerios">Conoce nuestros ministerios</a>
    </div>
    {social_row("hero-social")}
  </div>
  <div class="scroll-cue">↓ Desliza para conocernos</div>
</header>

<section id="quienes-somos">
  <div class="container">
    <div class="about-grid">
      <div>
        <span class="eyebrow">Quiénes somos</span>
        <h2 style="color:var(--navy);font-size:1.9rem;">Una comunidad, muchos ministerios, un mismo Espíritu</h2>
        <p>La <strong>Renovación Carismática Católica de la Diócesis de Paterson</strong> reúne a los grupos de oración de toda la diócesis bajo un mismo Comité Diocesano, con un escudo que resume nuestra identidad: la paloma del Espíritu Santo, los siete dones, y María, Nuestra Señora de Pentecostés.</p>
        <p>Vivimos y servimos dentro de la Iglesia Católica, en comunión con nuestros pastores y con la Diócesis de Paterson, y en comunión con la Renovación Carismática Católica a nivel regional (Región 2) y nacional (Estados Unidos y Canadá) — presentes en la vida parroquial a través de nuestros ministerios, escuelas de formación y encuentros diocesanos.</p>
        <div class="about-stats">
          <div class="about-stat"><div class="num">18</div><div class="lbl">Grupos de oración</div></div>
          <div class="about-stat"><div class="num">8</div><div class="lbl">Ministerios diocesanos</div></div>
          <div class="about-stat"><div class="num">2026</div><div class="lbl">1ª Edición ECCADS</div></div>
        </div>
      </div>
      <div class="about-photo">
        <img src="{IMG['featured']}" alt="Monseñor Kevin Sweeney junto al Comité Diocesano de la RCC Paterson en el ECCADS 2026" width="1200" height="800">
        <div class="caption"><strong>Mons. Kevin Sweeney</strong> junto al Comité Diocesano — ECCADS 2026</div>
      </div>
    </div>
  </div>
</section>

<section id="identidad" class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Nuestra identidad</span>
      <h2>Misión, Visión y Valores</h2>
      <p>En comunión con la Renovación Carismática Católica Región 2 y de los Estados Unidos y Canadá.</p>
    </div>
    <div class="identity-cards">
      <div class="identity-card">
        <span class="eyebrow">Visión</span>
        <h3>Hacia dónde caminamos</h3>
        <p>Ser una Renovación Carismática Católica viva, evangelizadora y en comunión en la Diócesis de Paterson, que forme discípulos misioneros, llenos del Espíritu Santo, comprometidos con la santidad, el servicio y la formación integral.</p>
      </div>
      <div class="identity-card">
        <span class="eyebrow">Misión</span>
        <h3>Lo que hacemos cada día</h3>
        <p>Promover la experiencia del Bautismo en el Espíritu Santo, renovar la vida de fe en las comunidades hispanas de la Diócesis de Paterson, y fortalecer nuestros ministerios y grupos de oración como espacios de encuentro con Dios, formación y misión evangelizadora.</p>
      </div>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Oración y Alabanza</h4><p>Fuente de toda acción pastoral.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Docilidad al Espíritu Santo</h4><p>Quien guía, corrige y renueva.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Comunión Eclesial</h4><p>En unidad con los pastores y la Iglesia.</p></div>
      <div class="value-card"><div class="vnum">IV</div><h4>Servicio Fraterno</h4><p>Expresión viva del amor en acción.</p></div>
      <div class="value-card"><div class="vnum">V</div><h4>Formación Continua</h4><p>Para madurar en los dones y en la fe.</p></div>
    </div>
    <p class="attribution-note">Inspirados en el Plan Pastoral Nacional 2026–2028 del Comité Nacional de Servicio Hispano (RCC Hispana), aplicado a nuestra realidad como Renovación Carismática Católica de la Diócesis de Paterson.</p>
    <div class="verbs-strip" style="margin-top:48px;">
      <div class="verb-item"><h3>Promover</h3><p>La experiencia del Bautismo en el Espíritu Santo.</p></div>
      <div class="verb-item"><h3>Evangelizar</h3><p>Desde una auténtica Cultura de Pentecostés.</p></div>
      <div class="verb-item"><h3>Servir</h3><p>A la Iglesia y a las comunidades de la Renovación Carismática Católica de la Diócesis de Paterson.</p></div>
    </div>
  </div>
</section>

<section id="comite">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Liderazgo diocesano</span>
      <h2>Comité Diocesano</h2>
      <p>Los servidores que coordinan la vida de la Renovación Carismática Católica de la Diócesis de Paterson.</p>
    </div>
    <div class="comite-grid">{comite_cards}
    </div>
  </div>
</section>

<section id="ministerios" class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Nuestros Ministerios</span>
      <h2>Ocho ministerios, una misma misión</h2>
      <p>Cada ministerio de la RCC Paterson tiene un llamado específico dentro del cuerpo de Cristo. Conoce su identidad y propósito.</p>
    </div>
    <div class="min-grid">{min_cards}
    </div>
  </div>
</section>

<section id="escuela">
  <div class="container">
    <div class="featured-banner">
      <img src="{IMG['escudo_efl']}" alt="Logo Escuela de Formación de Líderes" width="560" height="560">
      <div>
        <span class="eyebrow">Formación</span>
        <h2>Escuela de Formación de Líderes<span class="badge-live">Inscripciones abiertas</span></h2>
        <p>Un espacio formativo que equipa y madura servidores capaces de liderar con sabiduría y fidelidad a la Iglesia. Próximo taller: <strong>Módulo 3 — Seminario de Vida en el Espíritu</strong>, 28 y 29 de agosto de 2026.</p>
        <a class="btn btn-outline" href="ministerios/escuela-formacion-lideres.html">Ver detalles e inscribirme →</a>
      </div>
    </div>
  </div>
</section>

<section id="grupos-oracion" class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Vida de oración</span>
      <h2>Grupos de Oración</h2>
      <p>Los grupos de oración que conforman la Renovación Carismática Católica de la Diócesis de Paterson, organizados por parroquia.</p>
    </div>
    <div class="zona-legend">{zona_legend}</div>
    <div class="grupos-by-day">{grupos_by_day_html}
    </div>
    <p class="grupos-note">El horario de 7:00 pm – 9:30 pm es provisional para todos los grupos mientras se confirma el horario real de cada uno con el Comité Diocesano. Si coordinas un grupo y tu información no aparece o necesita corrección, contáctanos.</p>
  </div>
</section>

<section id="eventos">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Vida diocesana</span>
      <h2>Nuestros próximos eventos</h2>
      <p>Los próximos encuentros abiertos a toda la comunidad de la Renovación Carismática Católica de la Diócesis de Paterson.</p>
    </div>
    <div class="agenda-list">{agenda_items_html}
    </div>
    <p class="agenda-sync-note">Esta agenda se sincroniza con el calendario público oficial de la RCC Paterson. Horarios y sedes sujetos a confirmación final por el Comité Diocesano.</p>
  </div>
</section>

<section id="eccads-recap" class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Eventos insignia</span>
      <h2>Nuestros eventos insignia</h2>
      <p>Los grandes encuentros de la Renovación Carismática Católica de la Diócesis de Paterson, ya realizados.</p>
    </div>
    <div class="events-grid">
      <div class="event-card">
        <div class="ev-top"><img src="{IMG['pentecostes_mini']}" alt="Logo Gran Vigilia de Pentecostés 2026" width="420" height="420"></div>
        <div class="ev-body">
          <span class="event-tag event-tag--done">Realizado · 16 may 2026</span>
          <h3>Gran Vigilia de Pentecostés 2026</h3>
          <p>Resumen de la noche, nuestro obispo y sacerdotes, ministerios de música y más de 120 fotos del evento.</p>
          <a class="card-link" href="pentecostes-2026/index.html">Ver evento completo →</a>
        </div>
      </div>
      <div class="event-card">
        <div class="ev-top"><img src="{IMG['eccads_mini']}" alt="Logo ECCADS 2026" width="420" height="420"></div>
        <div class="ev-body">
          <span class="event-tag event-tag--done">Realizado · 1 ago 2026</span>
          <h3>ECCADS 2026</h3>
          <p>Programa completo, invitados especiales, galería de fotos y video resumen del primer encuentro.</p>
          <a class="card-link" href="eccads/index.html">Ver evento completo →</a>
        </div>
      </div>
    </div>
  </div>
</section>


<section id="preguntas-frecuentes">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2>Todo lo que debes saber sobre la RCC Paterson</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <h3>¿Qué es la Renovación Carismática Católica?</h3>
        <p>Es un movimiento dentro de la Iglesia Católica que promueve la experiencia del Bautismo en el Espíritu Santo y busca renovar la vida de fe de la comunidad a través de la oración, la alabanza y el servicio. En la Diócesis de Paterson, NJ, agrupa a 18 grupos de oración y 8 ministerios diocesanos bajo un mismo Comité Diocesano.</p>
      </div>
      <div class="faq-item">
        <h3>¿La Renovación Carismática Católica es parte de la Iglesia Católica?</h3>
        <p>Sí. La RCC es un movimiento eclesial reconocido que vive y sirve en comunión con la Iglesia Católica, sus pastores y la Diócesis de Paterson — no es una iglesia aparte ni una denominación distinta.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cuál es la diferencia entre la Renovación Carismática Católica y una iglesia pentecostal?</h3>
        <p>Ambas valoran la experiencia del Espíritu Santo, pero la RCC es un movimiento dentro de la Iglesia Católica —con Misa, sacramentos y comunión con el Papa y los obispos— mientras que las iglesias pentecostales son denominaciones protestantes independientes. La RCC Paterson funciona a través de las parroquias católicas de la diócesis.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo me uno a un grupo de oración de la RCC Paterson?</h3>
        <p>Puedes visitar cualquiera de los 18 grupos de oración de la RCC Paterson, organizados por parroquia, día y zona — consulta el horario, la dirección y el coordinador de cada uno en la sección <a href="#grupos-oracion">Grupos de Oración</a> de esta página, o contáctanos directamente para que te orientemos hacia el más cercano a ti.</p>
      </div>
      <div class="faq-item">
        <h3>¿Qué ministerios tiene la RCC Paterson?</h3>
        <p>Ocho: Intercesión, Hombres de Alabanza, Mujeres de Alabanza, Comunicación y Publicidad, Ministerios de Música, RCC Youth, la Escuela de Formación de Líderes y el Seminario de Vida en el Espíritu. Puedes conocer cada uno en la sección <a href="#ministerios">Ministerios</a> de esta página.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo contacto a la RCC Paterson?</h3>
        <p>Puedes escribirnos a <a href="mailto:renovacion@rccpaterson.org">renovacion@rccpaterson.org</a>, seguirnos en Instagram, Facebook, TikTok y YouTube como @rccpatersonnj, o contactar directamente al coordinador del grupo de oración o ministerio de tu interés.</p>
      </div>
    </div>
  </div>
</section>

''' + footer() + TAIL

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML)
print("index.html bytes:", len(HTML.encode("utf-8")))
