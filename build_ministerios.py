import sys
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']

def page(filename, title, desc, escudo, breadcrumb_name, subtitle, content_html):
    html = head(title, desc, root=R) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="{R}index.html">Inicio</a> / <a href="{R}index.html#ministerios">Ministerios</a> / {breadcrumb_name}</div>
    <img class="hero-shield-sm" src="{R}assets/img/{escudo}" alt="Logo {breadcrumb_name}">
    <h1>{breadcrumb_name}</h1>
    <p class="subtitle">{subtitle}</p>
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
  "Ministerio Hombres de Alabanza de la Renovación Carismática Católica de la Diócesis de Paterson.",
  "escudo-hombres-alabanza.png",
  "Hombres de Alabanza",
  "Varones de oración, de la Palabra y de carácter, al servicio de la adoración.",
  f'''
<section>
  <div class="container">
    <div class="split-content">
      <div class="min-content" style="max-width:none;">
        <span class="eyebrow">Identidad y Misión</span>
        <h2 style="color:var(--navy);">Adoradores antes que músicos</h2>
        <p>Los Hombres de Alabanza son un grupo de varones al servicio de la adoración y la alabanza dentro de la RCC de la Diócesis de Paterson. Su llamado es glorificar a Dios con sus voces e instrumentos, conduciendo a la comunidad a un encuentro auténtico con el Señor a través del canto.</p>
        <p>Se definen a sí mismos no como músicos sino como adoradores: su servicio es un acto de entrega, no de exhibición. Antes que talento musical, exigen carácter — hombres de oración, de la Palabra, de carácter íntegro, de comunidad y de equipo. Sirven bajo la autoridad del animador del grupo de oración y preparan el ambiente espiritual antes de la predicación.</p>
        <p>Fundamento bíblico: Salmo 98:1 (&ldquo;Canten al Señor un cántico nuevo&rdquo;), Salmo 150, Efesios 5:18-19, Colosenses 3:16 y 1 Crónicas 15:16. El Catecismo (CIC 1156) enseña que &ldquo;el canto y la música son señales del gozo del corazón&rdquo;. Creen que el hombre que alaba transforma también su hogar y su entorno cotidiano — la alabanza es estilo de vida, no solo servicio dominical.</p>
      </div>
      <div class="side-image">
        <img src="{R}assets/img/apoyo-hombres-alabanza.jpg" alt="Ilustración pastoral del ministerio Hombres de Alabanza">
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);">
      <p style="color:var(--gold-light);">&ldquo;Si hoy estás atravesando momentos de dolor, angustia, confusión o cansancio interior, queremos que sepas que no estás solo. Dios conoce tu corazón y ve cada una de tus luchas... Inspirados en el ejemplo de San José, hombre justo y fiel, queremos acompañarte para que redescubras tu identidad como hijo de Dios.&rdquo;</p>
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
  "Ministerio Mujeres de Alabanza de la Renovación Carismática Católica de la Diócesis de Paterson.",
  "escudo-mujeres-alabanza.png",
  "Mujeres de Alabanza",
  "Mujeres consagradas a la adoración, inspiradas en María.",
  f'''
<section>
  <div class="container">
    <div class="split-content">
      <div class="side-image" style="order:-1;">
        <img src="{R}assets/img/maria-mujeres-alabanza.jpg" alt="Ilustración pastoral del ministerio Mujeres de Alabanza, inspirada en María">
      </div>
      <div class="min-content" style="max-width:none;">
        <span class="eyebrow">Identidad y Misión</span>
        <h2 style="color:var(--navy);">Inspiradas en la primera adoradora</h2>
        <p>Las Mujeres de Alabanza son un grupo de mujeres consagradas al servicio de la adoración dentro de la RCC de la Diócesis de Paterson. Su misión es glorificar a Dios con sus voces y dones, abriendo los corazones de la comunidad a la presencia del Espíritu Santo mediante el canto y la alabanza.</p>
        <p>Se inspiran en María como &ldquo;la primera adoradora del Nuevo Testamento&rdquo;, en cuatro momentos marianos como modelo: la Anunciación (el &ldquo;sí&rdquo; de fe, Lc 1:38), el Magníficat (alabanza profética, Lc 1:46-55), Caná (intercesión sencilla, Jn 2:3-5) y Pentecostés (perseverancia en oración, Hch 1:14).</p>
        <p>Fundamento bíblico adicional: Salmo 68:26 y Éxodo 15:20-21 (Miriam guiando al pueblo con el pandero), Efesios 5:19, Colosenses 3:16. Buscan ser adoradoras genuinas, mujeres de la Palabra, humildes, obedientes al liderazgo y de testimonio de vida coherente — creen que &ldquo;la mujer que alaba levanta su casa&rdquo;.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="pull-quote" style="background:rgba(255,255,255,.05);border-left-color:var(--gold);">
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
  "Ministerio de Intercesión de la Renovación Carismática Católica de la Diócesis de Paterson.",
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

print("Páginas de ministerio generadas.")
