import sys
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']
IG_ICON = SOCIAL_ICONS['ig']

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
        <span class="eyebrow">Identidad y Misión</span>
        <h2 style="color:var(--navy);">Un espacio de encuentro y acompañamiento para el hombre</h2>
        <p>Hombres de Alabanza nace como un ministerio diocesano al servicio del hombre dentro de la Renovación Carismática Católica de la Diócesis de Paterson. Es un espacio de encuentro, fraternidad y acompañamiento espiritual para hombres que desean fortalecer su relación con Dios, crecer en su fe y asumir con valentía su llamado como hijos de Dios, esposos, padres y servidores dentro de la Iglesia y la sociedad.</p>
        <p>Este ministerio busca fortalecer al hombre a través de la oración, la alabanza y la acción del Espíritu Santo, ayudándolo a descubrir su identidad en Cristo y a caminar hacia una vida espiritual más plena. Aquí los hombres son llamados a levantarse con fe, a vivir con integridad, a cuidar de sus familias y a ser testimonio vivo del amor de Dios en sus hogares, comunidades y en la Iglesia.</p>
        <p>Este llamado nació discernido en oración durante una reunión del Equipo Diocesano, inspirado en hombres de fe como Abraham, Moisés, Josué y San José. Con el tiempo, esta misma inspiración dio origen también a Mujeres de Alabanza y, después, a Jóvenes de Alabanza.</p>
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
      <span class="eyebrow">Visión y Misión</span>
      <h2>Hombres restaurados, firmes en la fe</h2>
      <p>Ser un ministerio diocesano que forme hombres restaurados, firmes en la fe y llenos del Espíritu Santo, capaces de vivir una vida cristiana madura y de alabar a Dios con todo su corazón — hombres que, fortalecidos en Cristo, impacten positivamente a sus familias, comunidades y a la Iglesia.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Comunión</h4><p>Caminamos como hermanos en unidad, parte de un mismo Cuerpo en Cristo.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Escucha y Acompañamiento</h4><p>Acogemos a cada hombre con respeto, discreción y misericordia.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Fidelidad al Espíritu Santo</h4><p>Discerniendo en oración cada paso, dóciles a su voz.</p></div>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:50px;">
      <p style="color:var(--gold-light);">&ldquo;Si hoy estás atravesando momentos de dolor, angustia, confusión o cansancio interior, queremos que sepas que no estás solo. Dios conoce tu corazón y ve cada una de tus luchas... El Señor desea levantarte, restaurar tu corazón y fortalecerte con su amor. Inspirados en el ejemplo de San José, hombre justo y fiel, queremos acompañarte para que redescubras tu identidad como hijo de Dios.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Carta Pastoral, Hombres de Alabanza · RCC Paterson NJ</cite>
    </div>
    <div class="section-title">
      <span class="eyebrow">Coordinadores</span>
      <h2>Ministerio Diocesano de Acompañamiento Espiritual</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Lenin Jiménez (Baldera)</h4><p class="role">Coordinador</p><a class="phone" href="https://wa.me/16465001305" target="_blank" rel="noopener">{PHONE_ICON} (646) 500-1305</a></div>
      <div class="team-card"><h4>Nelson Cabrera</h4><p class="role">Coordinador</p><a class="phone" href="https://wa.me/19732725775" target="_blank" rel="noopener">{PHONE_ICON} (973) 272-5775</a></div>
      <div class="team-card"><h4>George Martínez</h4><p class="role">Coordinador</p><a class="phone" href="https://wa.me/18626003149" target="_blank" rel="noopener">{PHONE_ICON} (862) 600-3149</a></div>
    </div>
  </div>
</section>
''')

# ---------- MUJERES DE ALABANZA ----------
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
        <span class="eyebrow">Identidad y Misión</span>
        <h2 style="color:var(--navy);">Aquí no estás sola</h2>
        <p>Mujeres de Alabanza nace como un ministerio diocesano al servicio de la mujer dentro de la Renovación Carismática Católica de la Diócesis de Paterson. Es un espacio de escucha, oración y acompañamiento espiritual para mujeres que hoy atraviesan momentos de dolor, angustia, tristeza o confusión — un lugar para saber que no están solas, que Dios conoce su corazón y ve sus lágrimas.</p>
        <p>A través del acompañamiento espiritual, este ministerio ayuda a cada mujer a abrir su corazón a la acción del Espíritu Santo, para que descubra que, aún en medio de la dificultad, Dios sigue obrando en su vida. El Señor desea levantarla, devolverle la paz y fortalecerla con su amor.</p>
        <p>Como María, Madre que permanece junto a sus hijos en el dolor y en la esperanza, las Mujeres de Alabanza acompañan con un corazón disponible y confiado en Dios. Este ministerio nace de la misma inspiración que dio origen a Hombres de Alabanza — un llamado discernido en oración dentro del Equipo Diocesano.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Nuestro Compromiso</span>
      <h2>Acompañar con amor, fe y discreción</h2>
      <p>Si necesitas apoyo, oración o simplemente alguien que te escuche, no dudes en comunicarte. Estamos aquí para acompañarte con amor, fe y discreción.</p>
    </div>
    <div class="values-grid">
      <div class="value-card"><div class="vnum">I</div><h4>Amor</h4><p>Acompañamos sin juzgar, con un corazón disponible para escuchar.</p></div>
      <div class="value-card"><div class="vnum">II</div><h4>Fe</h4><p>Ponemos los ojos en Jesucristo como camino de esperanza.</p></div>
      <div class="value-card"><div class="vnum">III</div><h4>Discreción</h4><p>Escuchamos con respeto y confidencialidad, en confianza.</p></div>
    </div>
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);margin-top:50px;">
      <p style="color:var(--gold-light);">&ldquo;Si hoy estás atravesando momentos de dolor, angustia, tristeza o confusión, no estás sola. Dios conoce tu corazón y ve tus lágrimas... Como María, Madre que permanece junto a sus hijos en el dolor y en la esperanza, queremos acompañarte con un corazón disponible y confiado en Dios.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Carta Pastoral, Mujeres de Alabanza · RCC Paterson NJ</cite>
    </div>
    <div class="section-title">
      <span class="eyebrow">Coordinadoras</span>
      <h2>Ministerio Diocesano de Acompañamiento Espiritual</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Fanny Anderson</h4><p class="role">Coordinadora</p><a class="phone" href="https://wa.me/12016026818" target="_blank" rel="noopener">{PHONE_ICON} (201) 602-6818</a></div>
      <div class="team-card"><h4>Virginia Sánchez de Rivas</h4><p class="role">Coordinadora</p><a class="phone" href="https://wa.me/13477774645" target="_blank" rel="noopener">{PHONE_ICON} (347) 777-4645</a></div>
      <div class="team-card"><h4>Mercedes Javier</h4><p class="role">Coordinadora</p><a class="phone" href="https://wa.me/18627031680" target="_blank" rel="noopener">{PHONE_ICON} (862) 703-1680</a></div>
    </div>
  </div>
</section>
''')

# ---------- INTERCESION ----------
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
      <span class="eyebrow">Identidad y Misión</span>
      <h2 style="color:var(--navy);">Un ministerio de silencio fecundo</h2>
      <p>El Ministerio de Intercesión es el corazón orante de la Renovación Carismática Católica de la Diócesis de Paterson. Su misión es sostener en oración a toda la comunidad diocesana, los eventos, los líderes y las familias, ejerciendo el sacerdocio bautismal común a todo cristiano.</p>
      <p>Su fundamento doctrinal cita el Catecismo (CIC 2634-2636) sobre la intercesión como oración que nos conforma a la de Cristo, y a la RCC Hispana sobre las categorías de personas por quienes se debe interceder — autoridades, quienes sirven al Señor, enfermos y más (1 Tim 2:1-2, Stg 5:14-16). Fundamento bíblico adicional: Rm 8:26, Ef 6:18, Mt 5:44, Gn 18:16-33 (Abraham), Éx 32:30-32 (Moisés), Jn 2:3-5 (María en Caná).</p>
      <p>Sus miembros oran antes, durante y después de cada actividad diocesana, reciben peticiones de la comunidad, sostienen a los servidores, interceden por enfermos y familias en crisis, y guardan vigilia en momentos especiales como Pentecostés Diocesano y los Seminarios de Vida en el Espíritu. Operan en equipos con horario de oración, registro de peticiones y confidencialidad absoluta — sin protagonismo ni visibilidad.</p>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);">
      <p style="color:var(--gold-light);">&ldquo;Una comunidad cristiana vive de la intercesión de sus miembros; de lo contrario, muere.&rdquo;</p>
      <cite style="color:rgba(255,243,214,.6);">— Dietrich Bonhoeffer, citado en la Guía Pastoral del Ministerio de Intercesión, RCC Paterson NJ</cite>
    </div>
    <div class="section-title">
      <span class="eyebrow">Liderazgo</span>
      <h2>Ministerio de Intercesión</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Marizabel Pérez</h4><p class="role">Coordinadora</p></div>
      <div class="team-card"><h4>Rev. Yasid Salas</h4><p class="role">Director Espiritual</p></div>
    </div>
    <div class="contact-block">
      <span class="eyebrow">Contacto de Intercesión</span>
      <a class="contact-phone" href="https://wa.me/18622493313" target="_blank" rel="noopener">{PHONE_ICON} (862) 249-3313</a>
      <p class="contact-sub">Escríbenos por WhatsApp para peticiones de oración</p>
    </div>
  </div>
</section>
''')

# ---------- MINISTERIOS DE MÚSICA ----------
SOCIAL_LABELS = {"ig": "Instagram", "fb": "Facebook", "tt": "TikTok", "yt": "YouTube", "wa": "WhatsApp", "mail": "Correo"}
ICON_ORDER = ["ig", "fb", "tt", "yt", "wa", "mail"]

MUSICOS = [
    {"name": "Marvin Núñez", "role": "Director de Ministerios de Música", "photo": "comite/marvin-nunez.webp",
     "ig": ("@marvinnunezrd", "https://www.instagram.com/marvinnunezrd/"),
     "fb": "https://www.facebook.com/marvinnunezrd",
     "tt": "https://www.tiktok.com/@marvinnunezrd",
     "yt": "https://www.youtube.com/@marvinnunezrd",
     "wa": "https://wa.me/19295308974",
     "mail": "mailto:marvinnunezrd@gmail.com"},
    {"name": "Luis Castillo", "role": "Ministerio de Música", "photo": "pentecostes-2026-musica-luis-castillo.webp",
     "ig": ("@luiscastilloministry", "https://www.instagram.com/luiscastilloministry/"),
     "fb": "https://www.facebook.com/luiscastilloministry",
     "yt": "https://www.youtube.com/channel/UC1Wl7143vd6w33pKbysx4dQ",
     "tt": "https://www.tiktok.com/@luiscastilloministry",
     "wa": "https://wa.me/19734135500"},
    {"name": "Los Hijos del Padre", "role": "Ministerio de Música", "photo": "musica-los-hijos-del-padre.webp",
     "wa": "https://wa.me/18626688233"},
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
    return f'''
        <div class="guest-card">
          <div class="guest-photo"><img src="{R}assets/img/{m["photo"]}" alt="{m["name"]}" width="700" height="700" loading="lazy"></div>
          <h3>{m["name"]}</h3>
          <p>{m["role"]}</p>
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

print("Páginas de ministerio generadas.")
