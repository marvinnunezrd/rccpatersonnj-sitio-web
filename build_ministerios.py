import sys
from urllib.parse import quote
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']
IG_ICON = SOCIAL_ICONS['ig']
WA_ICON = SOCIAL_ICONS['wa']

def wa_href(digits, mensaje):
    return f"https://wa.me/{digits}?text={quote(mensaje)}"

def leader_card(nombre, rol, wa_digits, mensaje, sub="Escríbenos por WhatsApp"):
    href = wa_href(wa_digits, mensaje)
    return f'''<div class="leader-contact-card">
      <h4>{nombre}</h4>
      <p class="role">{rol}</p>
      <div class="card-divider"></div>
      <a class="contact-wa-icon" href="{href}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{WA_ICON}</a>
      <p class="contact-sub">{sub}</p>
    </div>'''

def leader_grid(*cards):
    items = "\n    ".join(cards)
    return f'<div class="leader-contact-grid">\n    {items}\n    </div>'

def page(filename, title, desc, escudo, breadcrumb_name, subtitle, content_html, extra_head="", og_image="", extra_subtitle_class=""):
    html = head(title, desc, root=R, path=filename, extra=extra_head, og_image=og_image) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="{R}index.html">Inicio</a> / <a href="{R}index.html#ministerios">Ministerios</a> / {breadcrumb_name}</div>
    <img class="hero-shield-sm" src="{R}assets/img/{escudo}" alt="Logo {breadcrumb_name}" width="560" height="560">
    <h1>{breadcrumb_name}</h1>
    <p class="subtitle{extra_subtitle_class}">{subtitle}</p>
  </div>
</header>
{content_html}
''' + footer(root=R) + TAIL
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(filename, len(html.encode("utf-8")), "bytes")

# ---------- HOMBRES DE ALABANZA ----------
HOMBRES_WA = wa_href("16465001305", "Hola, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hombres de Alabanza.")
page(
  "ministerios/hombres-alabanza.html",
  "Hombres de Alabanza — RCC Paterson NJ",
  "Hombres de Alabanza: Ministerio Diocesano de Acompañamiento Espiritual para el hombre, de la Renovación Carismática Católica de la Diócesis de Paterson.",
  "escudo-hombres-alabanza.png",
  "Hombres de Alabanza",
  "Ministerio Diocesano de Acompañamiento Espiritual para el hombre.",
  f'''
<section>
  <div class="container">
    <div class="split-content">
      <div class="min-content" style="max-width:none;">
        <span class="eyebrow">Para el hombre que lucha en silencio</span>
        <h2 style="color:var(--navy);">No estás solo en esta lucha</h2>
        <p>Si hoy estás atravesando momentos de dolor, angustia, confusión o cansancio interior, queremos que sepas que no estás solo. Dios conoce tu corazón y ve cada una de tus luchas. El Señor desea levantarte, restaurar tu corazón y fortalecerte con su amor.</p>
        <p>Inspirados en el ejemplo de San José, hombre justo y fiel, Hombres de Alabanza te acompaña para que redescubras tu identidad como hijo de Dios, sanes las heridas que cargas y te levantes con la fuerza que solo el Espíritu Santo puede dar — para vivir con integridad y cuidar con firmeza de tu familia.</p>
        <a class="wa-cta-btn" href="{HOMBRES_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Habla con nosotros por WhatsApp</span></a>
      </div>
      <div class="side-image">
        <img src="{R}assets/img/apoyo-hombres-alabanza.jpg" alt="Ilustración pastoral del ministerio Hombres de Alabanza" width="900" height="1350">
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>Hombres restaurados, firmes en la fe</h2>
      <p>Ser un ministerio diocesano que forme hombres restaurados, firmes en la fe y llenos del Espíritu Santo, capaces de vivir una vida cristiana madura y de alabar a Dios con todo su corazón — hombres que, fortalecidos en Cristo, impacten positivamente a sus familias, comunidades y a la Iglesia.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">Hombres de Alabanza nace como un ministerio diocesano al servicio del hombre dentro de la Renovación Carismática Católica de la Diócesis de Paterson — un espacio de encuentro, fraternidad y acompañamiento espiritual a través de la oración, la alabanza y la acción del Espíritu Santo. Este llamado nació discernido en oración durante una reunión del Equipo Diocesano, inspirado en hombres de fe como Abraham, Moisés, Josué y San José. Con el tiempo, esta misma inspiración dio origen también a Mujeres de Alabanza y, después, a Jóvenes de Alabanza.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Comunión</h4><p>Caminamos como hermanos en unidad, parte de un mismo Cuerpo en Cristo.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Escucha y Acompañamiento</h4><p>Acogemos a cada hombre con respeto, discreción y misericordia.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Fidelidad al Espíritu Santo</h4><p>Discerniendo en oración cada paso, dóciles a su voz.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Coordinadores</span>
      <h2>Ministerio Diocesano de Acompañamiento Espiritual</h2>
    </div>
    {leader_grid(
      leader_card("Lenin Jiménez (Baldera)", "Coordinador", "16465001305", "Hola Lenin, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hombres de Alabanza."),
      leader_card("Nelson Cabrera", "Coordinador", "19732725775", "Hola Nelson, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hombres de Alabanza."),
      leader_card("George Martínez", "Coordinador", "18626003149", "Hola George, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hombres de Alabanza."),
    )}
  </div>
</section>
''',
  og_image="assets/img/ministerios/hombres-alabanza-og.jpg")

# ---------- MUJERES DE ALABANZA ----------
MUJERES_WA = wa_href("12016026818", "Hola, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Mujeres de Alabanza.")
page(
  "ministerios/mujeres-alabanza.html",
  "Mujeres de Alabanza — RCC Paterson NJ",
  "Mujeres de Alabanza: Ministerio Diocesano de Acompañamiento Espiritual para la mujer, de la Renovación Carismática Católica de la Diócesis de Paterson.",
  "escudo-mujeres-alabanza.png",
  "Mujeres de Alabanza",
  "Ministerio Diocesano de Acompañamiento Espiritual para la mujer.",
  f'''
<section>
  <div class="container">
    <div class="split-content">
      <div class="side-image" style="order:-1;">
        <img src="{R}assets/img/maria-mujeres-alabanza.jpg" alt="Ilustración pastoral del ministerio Mujeres de Alabanza, inspirada en María" width="900" height="1350">
      </div>
      <div class="min-content" style="max-width:none;">
        <span class="eyebrow">Para la mujer que atraviesa el dolor en silencio</span>
        <h2 style="color:var(--navy);">Aquí no estás sola</h2>
        <p>Si hoy estás atravesando momentos de dolor, angustia, tristeza o confusión, queremos que sepas que no estás sola. Dios conoce tu corazón y ve tus lágrimas — y desea levantarte, devolverte la paz y fortalecerte con su amor.</p>
        <p>Como María, Madre que permanece junto a sus hijos en el dolor y en la esperanza, Mujeres de Alabanza te acompaña con un corazón disponible, sin juzgar, y confiado en que Dios sigue obrando en tu vida aún en medio de la dificultad.</p>
        <a class="wa-cta-btn" href="{MUJERES_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Habla con nosotras por WhatsApp</span></a>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>Acompañar con amor, fe y discreción</h2>
      <p>Si necesitas apoyo, oración o simplemente alguien que te escuche, no dudes en comunicarte. Estamos aquí para acompañarte con amor, fe y discreción.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">Mujeres de Alabanza nace como un ministerio diocesano al servicio de la mujer dentro de la Renovación Carismática Católica de la Diócesis de Paterson, a través de la escucha, la oración y el acompañamiento espiritual. Este ministerio nace de la misma inspiración que dio origen a Hombres de Alabanza — un llamado discernido en oración dentro del Equipo Diocesano.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Amor</h4><p>Acompañamos sin juzgar, con un corazón disponible para escuchar.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Fe</h4><p>Ponemos los ojos en Jesucristo como camino de esperanza.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Discreción</h4><p>Escuchamos con respeto y confidencialidad, en confianza.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Coordinadoras</span>
      <h2>Ministerio Diocesano de Acompañamiento Espiritual</h2>
    </div>
    {leader_grid(
      leader_card("Fanny Anderson", "Coordinadora", "12016026818", "Hola Fanny, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Mujeres de Alabanza."),
      leader_card("Virginia Sánchez de Rivas", "Coordinadora", "13477774645", "Hola Virginia, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Mujeres de Alabanza."),
      leader_card("Mercedes Javier", "Coordinadora", "18627031680", "Hola Mercedes, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Mujeres de Alabanza."),
    )}
  </div>
</section>
''',
  og_image="assets/img/ministerios/mujeres-alabanza-og.jpg")

# ---------- INTERCESION ----------
INTERCESION_WA = "https://wa.me/18622493313?text=" + quote(
    "Saludos, equipo de Intercesión. Le escribo desde la página web de la RCC Paterson "
    "porque quisiera pedir su oración de intercesión."
)
page(
  "ministerios/intercesion.html",
  "Intercesión — RCC Paterson NJ",
  "Ministerio de Intercesión de la RCC Paterson NJ: el corazón orante de la comunidad, sosteniendo en oración a la diócesis, líderes, eventos y familias.",
  "escudo-intercesion.png",
  "Intercesión",
  "El corazón orante de la Renovación Carismática Católica de la Diócesis de Paterson.",
  f'''
<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">¿Necesitas oración?</span>
      <h2 style="color:var(--navy);">Aquí siempre hay alguien orando por ti</h2>
      <p>Si hoy cargas una enfermedad propia o de un ser querido, una situación familiar que no sabes cómo resolver, una decisión difícil, una pérdida, o simplemente sientes que ya no tienes fuerzas para seguir orando tú solo — este ministerio existe para ti. El Ministerio de Intercesión de la RCC Paterson recibe tu petición y la lleva delante de Dios con la misma fe y constancia con la que orarías por un hijo.</p>
      <p>No necesitas explicar todo, ni pertenecer a ningún grupo, ni tener nada resuelto antes de pedirlo. Escríbenos tu petición — con el nombre que quieras compartir, o en total anonimato — y un equipo de intercesores orará por ti con total confidencialidad.</p>
      <a class="wa-cta-btn" href="{INTERCESION_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Pedir oración por WhatsApp</span></a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>Un ministerio de silencio fecundo</h2>
      <p>Su misión es sostener en oración a toda la comunidad diocesana, los eventos, los líderes y las familias, ejerciendo el sacerdocio bautismal común a todo cristiano.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">Su fundamento doctrinal cita el Catecismo (CIC 2634-2636) sobre la intercesión como oración que nos conforma a la de Cristo, y a la RCC Hispana sobre las categorías de personas por quienes se debe interceder — autoridades, quienes sirven al Señor, enfermos y más (1 Tim 2:1-2, Stg 5:14-16). Fundamento bíblico adicional: Rm 8:26, Ef 6:18, Mt 5:44, Gn 18:16-33 (Abraham), Éx 32:30-32 (Moisés), Jn 2:3-5 (María en Caná).</p>
      <p style="color:rgba(255,243,214,.85);">Sus miembros oran antes, durante y después de cada actividad diocesana, reciben peticiones de la comunidad, sostienen a los servidores, interceden por enfermos y familias en crisis, y guardan vigilia en momentos especiales como Pentecostés Diocesano y los Seminarios de Vida en el Espíritu. Operan en equipos con horario de oración, registro de peticiones y confidencialidad absoluta — sin protagonismo ni visibilidad.</p>
      <p style="color:rgba(255,243,214,.85);">Si sientes que Dios te está llamando a servir como intercesor, este ministerio también te recibe con alegría — escríbenos para conocer cómo unirte a este servicio de oración constante.</p>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:10px;">
      <p style="color:var(--gold-light);">&ldquo;Una comunidad cristiana vive de la intercesión de sus miembros; de lo contrario, muere.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Dietrich Bonhoeffer, citado en la Guía Pastoral del Ministerio de Intercesión, RCC Paterson NJ</cite>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Liderazgo</span>
      <h2>Ministerio de Intercesión</h2>
    </div>
    <div class="leader-contact-card">
      <h4>Marizabel Pérez</h4>
      <p class="role">Coordinadora</p>
      <div class="card-divider"></div>
      <a class="contact-wa-icon" href="{INTERCESION_WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">{WA_ICON}</a>
      <p class="contact-sub">Escríbenos por WhatsApp para peticiones de oración</p>
    </div>
  </div>
</section>
''',
  og_image="assets/img/ministerios/intercesion-og.jpg")

# ---------- MINISTERIOS DE MÚSICA ----------
SOCIAL_LABELS = {"ig": "Instagram", "fb": "Facebook", "tt": "TikTok", "yt": "YouTube", "spotify": "Spotify", "applemusic": "Apple Music", "wa": "WhatsApp", "mail": "Correo"}
ICON_ORDER = ["ig", "fb", "tt", "yt", "spotify", "applemusic", "wa", "mail"]

MUSICOS = [
    {"name": "Marvin Núñez", "role": "Director de Ministerios de Música", "photo": "comite/marvin-nunez.webp",
     "ig": ("@marvinnunezrd", "https://www.instagram.com/marvinnunezrd/"),
     "fb": "https://www.facebook.com/marvinnunezrd",
     "tt": "https://www.tiktok.com/@marvinnunezrd",
     "yt": "https://www.youtube.com/@marvinnunezrd",
     "spotify": "https://open.spotify.com/intl-es/artist/0vheEY20pbheuQIwpVD3RR?si=tZMP7yV7S0iPEW2hJfA6Aw",
     "applemusic": "https://music.apple.com/us/artist/marvin-n%C3%BA%C3%B1ez/996812382",
     "wa": "https://wa.me/19295308974",
     "mail": "mailto:marvinnunezrd@gmail.com"},
    {"name": "Los Hijos del Padre", "role": "Ministerio de Música", "honor": "Rafael Beato — Ex-Director de los Ministerios de Música", "photo": "musica-los-hijos-del-padre.webp",
     "wa": "https://wa.me/18626688233"},
    {"name": "Luis Castillo", "role": "Ministerio de Música", "honor": "Ex-Director de los Ministerios de Música", "photo": "pentecostes-2026-musica-luis-castillo.webp",
     "ig": ("@luiscastilloministry", "https://www.instagram.com/luiscastilloministry/"),
     "fb": "https://www.facebook.com/luiscastilloministry",
     "yt": "https://www.youtube.com/channel/UC1Wl7143vd6w33pKbysx4dQ",
     "tt": "https://www.tiktok.com/@luiscastilloministry",
     "wa": "https://wa.me/19734135500"},
    {"name": "Johanna Tavarez", "role": "Ministerio de Música", "photo": "pentecostes-2026-musica-johanna-tavarez.webp",
     "ig": ("@johannatavarez", "https://www.instagram.com/johannatavarez/"),
     "fb": "https://www.facebook.com/johannatavarezlozano",
     "yt": "https://www.youtube.com/watch?v=6ehiny01doM"},
    {"name": "Salvatore Moreno", "role": "Ministerio de Música", "photo": "pentecostes-2026-musica-salvatore-moreno.webp",
     "ig": ("@salvatoremusicdr", "https://www.instagram.com/salvatoremusicdr/"),
     "yt": "https://www.youtube.com/@SalvatoreMusic",
     "fb": "https://www.facebook.com/salvatore.moreno1",
     "tt": "https://www.tiktok.com/@salvatoremoreno1",
     "wa": "https://wa.me/19739791977"},
    {"name": "Starlyn Veloz", "role": "Ministerio de Música", "photo": "musica-starlyn-veloz.webp",
     "ig": ("@starlynveloz98", "https://www.instagram.com/starlynveloz98/"),
     "fb": "https://www.facebook.com/starlin.velozbaez",
     "yt": "https://www.youtube.com/channel/UCJt5eRy_uWbR4xNB3r16VjQ",
     "wa": "https://wa.me/18622834237",
     "mail": "mailto:Starlinveloz98@gmail.com"},
    {"name": "Son D' Fe", "role": "Ministerio de Música", "photo": "pentecostes-2026-musica-starlyn-veloz-son-de-fe.webp",
     "ig": ("@son_dfe", "https://www.instagram.com/son_dfe/"),
     "fb": "https://www.facebook.com/profile.php?id=61579764351173",
     "wa": "https://wa.me/18622834237"},
    {"name": "Griselda Ortiz", "role": "Ministerio de Música", "photo": "musica-griselda-ortiz.webp",
     "ig": ("@griseldacieloytierra", "https://www.instagram.com/griseldacieloytierra/"),
     "fb": "https://www.facebook.com/GriseldaCieloyTierra",
     "tt": "https://www.tiktok.com/@griseldaortiz378",
     "yt": "https://www.youtube.com/channel/UCx5yPk_pg3XT4XH96wolqQw",
     "spotify": "https://open.spotify.com/intl-es/artist/0M1lin0wvyJ4HjkvmCmhkS",
     "applemusic": "https://music.apple.com/us/artist/griselda-ortiz/1576749077",
     "wa": "https://wa.me/12014968246",
     "mail": "mailto:GRISELDACIELOYTIERA@gmail.com"},
    {"name": "Ministerio Luz de Cristo", "role": "Ministerio de Música", "photo": "musica-luz-de-cristo.webp",
     "wa": "https://wa.me/19733561292"},
]

def musico_card(m):
    icons = []
    for key in ICON_ORDER:
        val = m.get(key)
        if not val:
            continue
        href = val[1] if key == "ig" else val
        icons.append(f'<a href="{href}" target="_blank" rel="noopener" aria-label="{SOCIAL_LABELS[key]}">{SOCIAL_ICONS[key]}</a>')
    icons_html = "\n          ".join(icons)
    ig_line = ""
    if m.get("ig"):
        handle, ig_url = m["ig"]
        ig_line = f'<a class="ig-handle" href="{ig_url}" target="_blank" rel="noopener">{handle}</a>'
    honor_html = f'<p class="musico-honor">{m["honor"]}</p>' if m.get("honor") else ""
    return f'''
        <div class="guest-card">
          <div class="guest-photo"><img src="{R}assets/img/{m["photo"]}" alt="{m["name"]}" width="700" height="700" loading="lazy"></div>
          <h3>{m["name"]}</h3>
          <p>{m["role"]}</p>
          {honor_html}
          <div class="musico-social">
          {icons_html}
          </div>
          {ig_line}
        </div>'''

musico_cards = "\n".join(musico_card(m) for m in MUSICOS)

MUSICA_STYLE = '''<style>
.hero-sub .subtitle-quote{font-style:italic;}
.hero-sub .subtitle-quote .quote-text::before{content:"\\201C";}
.hero-sub .subtitle-quote .quote-text::after{content:"\\201D";}
.hero-sub .subtitle-quote cite{display:block;margin-top:8px;font-size:.8rem;font-style:normal;color:rgba(255,255,255,.72);}
#musicos .guests-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:34px;max-width:820px;margin:0 auto;}
#musicos .guest-card{flex:0 0 240px;}
#musicos .guest-card .musico-social{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-top:12px;}
#musicos .guest-card .musico-social a{width:30px;height:30px;border-radius:50%;border:1.5px solid var(--wine);display:flex;align-items:center;justify-content:center;color:var(--wine);transition:.15s;}
#musicos .guest-card .musico-social a:hover{background:var(--wine);color:var(--ivory);}
#musicos .guest-card .musico-social svg{width:15px;height:15px;}
#musicos .guest-card .musico-honor{font-size:.72rem;font-style:italic;font-weight:600;color:var(--wine);margin:2px 0 4px;line-height:1.35;}
#musicos .guest-card .ig-handle{display:block;margin-top:8px;font-size:.78rem;font-weight:600;color:var(--wine);text-decoration:none;}
#musicos .guest-card .ig-handle:hover{color:var(--red);}
</style>'''

page(
  "ministerios/musica.html",
  "Ministerios de Música — RCC Paterson NJ",
  "Ministerios de Música de la Renovación Carismática Católica de la Diócesis de Paterson: los cantantes, músicos y grupos que animan con su talento nuestros eventos y celebraciones.",
  "ministerios/musica.webp",
  "Ministerios de Música",
  '<span class="quote-text">El que canta ora dos veces</span><cite>— San Agustín</cite>',
  og_image="assets/img/ministerios/musica-og.jpg",
  extra_subtitle_class=" subtitle-quote",
  content_html=f'''
<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">Identidad y Misión</span>
      <h2 style="color:var(--navy);">La música que prepara el corazón para el encuentro con Dios</h2>
      <p>Los Ministerios de Música de la Renovación Carismática Católica de la Diócesis de Paterson acompañan con su talento cada Seminario de Vida en el Espíritu, Asamblea, Congreso, Vigilia de Pentecostés y demás actividades de nuestra comunidad diocesana. Su misión es preparar el corazón del pueblo para el encuentro con Dios a través del canto, la alabanza y la adoración.</p>
      <p>Coordinados por Marvin Núñez, Director de Ministerios de Música de la RCC Paterson, estos hermanos y hermanas ponen sus dones y su talento al servicio del Espíritu Santo, conscientes siempre de que cada canto es, ante todo, una ofrenda de oración.</p>
    </div>
  </div>
</section>

<section id="musicos">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Voces y Talentos</span>
      <h2>Algunos de nuestros ministerios de música</h2>
      <p>Estos son algunos de los servidores que forman parte de este ministerio — ¡vienen más!</p>
    </div>
    <div class="guests-grid">
{musico_cards}
    </div>
  </div>
</section>
''',
  extra_head=MUSICA_STYLE
)

# ---------- HOSPITALIDAD Y CARIDAD ----------
HOSPITALIDAD_WA = wa_href("18626860358", "Hola, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Ministerio de Hospitalidad y Caridad.")
page(
  "ministerios/hospitalidad-caridad.html",
  "Ministerio de Hospitalidad y Caridad — RCC Paterson NJ",
  "Ministerio de Hospitalidad y Caridad de la Renovación Carismática Católica de la Diócesis de Paterson: acogida fraterna, servicio humilde y atención a quienes atraviesan enfermedad, soledad o dificultad.",
  "escudo-hospitalidad-caridad.webp",
  "Ministerio de Hospitalidad y Caridad",
  "Acoger al hermano es recibir a Cristo; atenderlo con amor es hacer visible su misericordia.",
  f'''
<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">¿Te sientes solo o necesitas apoyo?</span>
      <h2 style="color:var(--navy);">Aquí serás recibido con amor</h2>
      <p>Si estás enfermo, atraviesas una dificultad, acabas de llegar a la comunidad o simplemente te sientes solo, el Ministerio de Hospitalidad y Caridad existe para recibirte con dignidad, alegría, respeto y discreción. Acoger al hermano es recibir a Cristo; atenderlo con amor es hacer visible su misericordia.</p>
      <p>No tienes que atravesar esto sin compañía — este ministerio te acompaña en la enfermedad, la crisis, la soledad o la dificultad, manifestando el amor de Cristo a través de la acogida fraterna, el servicio humilde y la oración.</p>
      <a class="wa-cta-btn" href="{HOSPITALIDAD_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Pide apoyo por WhatsApp</span></a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>Una presencia fraterna, no un protocolo</h2>
      <p>No es solamente un equipo de protocolo, orden o acomodadores: es una presencia fraterna que recibe, escucha, orienta y acompaña — un puente entre la persona, la comunidad, los grupos de oración y los recursos pastorales.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">Su misión es manifestar el amor de Cristo a través de la acogida fraterna, el servicio humilde, la oración y la atención organizada a las necesidades de quienes participan en las actividades diocesanas o atraviesan enfermedad, crisis, soledad o dificultad. Su visión es consolidar una cultura de hospitalidad, caridad y solidaridad dentro de la Renovación Carismática Católica de la Diócesis de Paterson, para que cada persona que llegue se sienta recibida, acompañada e integrada a una comunidad donde pueda experimentar el amor de Dios.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Amor fraterno</h4><p>El punto de partida de toda acogida.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Caridad</h4><p>Servicio humilde a quien lo necesita.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Humildad</h4><p>Sin protagonismo ni exposición pública.</p></div>
      <div class="value-card"><div class="vnum">IV</div><h4>Hospitalidad</h4><p>Recibir con dignidad, alegría y respeto.</p></div>
      <div class="value-card"><div class="vnum">V</div><h4>Discreción y confidencialidad</h4><p>Cuidar la privacidad de cada hermano.</p></div>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:50px;">
      <p style="color:var(--gold-light);">&ldquo;Porque tuve hambre y ustedes me dieron de comer; tuve sed y me dieron de beber; fui forastero y me recibieron; estuve desnudo y me vistieron; enfermo y me visitaron; en la cárcel y vinieron a verme.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Mateo 25,35-36 · fundamento bíblico del Ministerio de Hospitalidad y Caridad</cite>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Coordinadoras</span>
      <h2>Ministerio de Hospitalidad y Caridad</h2>
    </div>
    {leader_grid(
      leader_card("Marisol Parra", "Coordinadora", "18626860358", "Hola Marisol, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hospitalidad y Caridad."),
      leader_card("Griselda Ortiz", "Coordinadora", "12014968246", "Hola Griselda, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hospitalidad y Caridad."),
      leader_card("Justina Peña (Luz)", "Coordinadora", "18622710877", "Hola Justina, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre Hospitalidad y Caridad."),
    )}
  </div>
</section>
''',
  og_image="assets/img/ministerios/hospitalidad-caridad-og.jpg")

# ---------- COLABORADORES ----------
COLABORADORES_WA = wa_href("18626687852", "Hola, le escribo desde la página web de la RCC Paterson porque siento el llamado a servir y quisiera más información sobre el Ministerio de Colaboradores.")
page(
  "ministerios/colaboradores.html",
  "Ministerio de Colaboradores — RCC Paterson NJ",
  "Ministerio de Colaboradores de la Renovación Carismática Católica de la Diócesis de Paterson: la puerta de entrada al servicio, con formación y acompañamiento para quienes comienzan a servir.",
  "escudo-colaboradores.webp",
  "Ministerio de Colaboradores",
  "Les he dado ejemplo para que hagan lo mismo que yo hice con ustedes.",
  f'''
<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">¿Sientes el llamado a servir?</span>
      <h2 style="color:var(--navy);">La puerta de entrada al servicio</h2>
      <p>Si sientes que el Espíritu Santo te está llamando a servir pero no sabes por dónde empezar, el Ministerio de Colaboradores es tu puerta de entrada. Aquí sirves de manera formada, acompañada y vinculada a una comunidad — no es solamente cubrir un evento, sino un proceso pastoral de acogida, formación, acompañamiento y crecimiento en el servicio.</p>
      <p>Como Simón de Cirene, quien venía del campo con sus propios afanes y terminó compartiendo la carga de Jesús, aquí aprendes a caminar con Cristo y a colaborar con su misión: no cargas en lugar de Cristo, aprendes a cargar con Cristo.</p>
      <a class="wa-cta-btn" href="{COLABORADORES_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Quiero empezar a servir</span></a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>Un camino, no un ascenso</h2>
      <p>Ninguno de los requisitos de este ministerio es una barrera. Todos son un camino: se caminan poco a poco, siempre acompañados.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">Su misión es acoger, formar y acompañar a quienes comienzan a servir, para que el servicio nazca del amor y edifique la comunión. Su visión: colaboradores maduros, perseverantes y unidos a su parroquia y a su grupo de oración, listos para un servicio reconocido.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Humildad</h4><p>La base de todo servicio auténtico.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Caridad</h4><p>El servicio nace del amor, no del deber.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Comunión</h4><p>Nadie sirve solo: se sirve en comunidad.</p></div>
      <div class="value-card"><div class="vnum">IV</div><h4>Perseverancia</h4><p>Un camino sostenido, no un impulso.</p></div>
      <div class="value-card"><div class="vnum">V</div><h4>Disponibilidad</h4><p>Un corazón dispuesto a aprender y servir.</p></div>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:50px;">
      <p style="color:var(--gold-light);">&ldquo;El colaborador no carga en lugar de Cristo; aprende a cargar con Cristo.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Como Simón de Cirene, Guía Pastoral del Ministerio de Colaboradores · RCC Paterson NJ</cite>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Coordinadoras</span>
      <h2>Ministerio de Colaboradores</h2>
    </div>
    {leader_grid(
      leader_card("Mercedes González", "Coordinadora", "18626687852", "Hola Mercedes, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Ministerio de Colaboradores."),
      leader_card("Lidia Tapia", "Coordinadora", "12018873188", "Hola Lidia, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Ministerio de Colaboradores."),
      leader_card("María Payano (Charo)", "Coordinadora", "19739315033", "Hola María, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Ministerio de Colaboradores."),
    )}
    <div class="pull-quote" style="margin-top:44px;">
      <p>&ldquo;Señor Jesús, Maestro y Servidor, enséñanos a reconocer tu rostro en cada persona. Danos un corazón humilde, manos disponibles, palabras que edifiquen y la sabiduría de tu Espíritu. Que nuestro servicio nazca del amor, fortalezca la comunión y conduzca a otros hacia ti. Amén.&rdquo;</p>
      <cite>— Oración final, Guía Pastoral del Ministerio de Colaboradores · RCC Paterson NJ</cite>
    </div>
  </div>
</section>
''',
  og_image="assets/img/ministerios/colaboradores-og.jpg")

# ---------- SEMINARIO DE VIDA EN EL ESPÍRITU ----------
SVE_WA = wa_href("19739304226", "Hola, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Seminario de Vida en el Espíritu.")
SVE_STYLE = '''<style>
.hero-sub .subtitle-quote{font-style:italic;}
.hero-sub .subtitle-quote .quote-text::before{content:"\\201C";}
.hero-sub .subtitle-quote .quote-text::after{content:"\\201D";}
.hero-sub .subtitle-quote cite{display:block;margin-top:8px;font-size:.8rem;font-style:normal;color:rgba(255,255,255,.72);}
</style>'''

page(
  "ministerios/seminario-vida-espiritu.html",
  "Seminario de Vida en el Espíritu — RCC Paterson NJ",
  "Seminario de Vida en el Espíritu (SVE) de la Renovación Carismática Católica de la Diócesis de Paterson: la puerta de entrada a la experiencia del Bautismo en el Espíritu Santo.",
  "escudo-sve.webp",
  "Seminario de Vida en el Espíritu",
  '<span class="quote-text">Yo enviaré sobre ustedes la promesa de mi Padre.</span><cite>— Lucas 24,49</cite>',
  og_image="assets/img/ministerios/sve-og.jpg",
  extra_subtitle_class=" subtitle-quote",
  extra_head=SVE_STYLE,
  content_html=f'''
<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">¿Buscas un encuentro real con Dios?</span>
      <h2 style="color:var(--navy);">La puerta de entrada a la Renovación</h2>
      <p>Si sientes que tu fe necesita algo más — un encuentro real con Jesucristo vivo, no solo una idea sobre él — el Seminario de Vida en el Espíritu (SVE) es para ti. No es una clase teológica: es una experiencia diseñada para llevarte a una transformación espiritual profunda — un encuentro personal con Cristo, la conversión del corazón, la experiencia del Espíritu Santo y la integración en una comunidad viva.</p>
      <p>El SVE no &ldquo;crea&rdquo; algo nuevo — actualiza lo que Dios ya hizo en tu bautismo y confirmación. Se desarrolla en siete semanas: el amor del Padre, el pecado y sus consecuencias, Jesús Salvador del mundo, fe y conversión, el señorío de Jesús, la promesa del Padre —momento central de oración por la efusión del Espíritu Santo— y la comunidad como vida nueva en Cristo.</p>
      <a class="wa-cta-btn" href="{SVE_WA}" target="_blank" rel="noopener">{WA_ICON}<span>Quiero más información</span></a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">¿Quieres ir más profundo?</span>
      <h2>El Espíritu Santo es el agente principal</h2>
      <p>El seminario busca mover el corazón, no solamente informar la mente. El Espíritu Santo es el agente principal de la transformación; los servidores somos instrumentos en sus manos.</p>
    </div>
    <div class="min-content" style="max-width:800px;margin:0 auto;">
      <p style="color:rgba(255,243,214,.85);">El ministerio del Seminario de Vida en el Espíritu está compuesto por un equipo base de 6 a 8 servidores comprometidos con la misión evangelizadora: coordinación, predicación, música, servidores de los grupos de diálogo e intercesión.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Unidad</h4><p>Trabajar en comunión, en amor humilde, sin divisiones.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Unción</h4><p>Comunicar una experiencia real con el Señor.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Humildad</h4><p>El coordinador no es el protagonista.</p></div>
      <div class="value-card"><div class="vnum">IV</div><h4>Conocimiento</h4><p>Fieles a lo que enseña la Iglesia y su doctrina.</p></div>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:50px;">
      <p style="color:var(--gold-light);">&ldquo;El coordinador no es el protagonista: es quien cuida que todos puedan servir.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Rol del coordinador, Guía Pastoral del Seminario de Vida en el Espíritu · RCC Paterson NJ</cite>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:24px;">
      <p style="color:var(--gold-light);">&ldquo;Yo enviaré sobre ustedes la promesa de mi Padre.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Lucas 24,49 · texto central del Seminario de Vida en el Espíritu</cite>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Coordinación</span>
      <h2>Seminario de Vida en el Espíritu</h2>
    </div>
    {leader_card("Fiordaliza Moya (Fior)", "Coordinadora", "19739304226", "Hola Fior, le escribo desde la página web de la RCC Paterson porque quisiera más información sobre el Seminario de Vida en el Espíritu.")}
  </div>
</section>
''')

print("Páginas de ministerio generadas.")
