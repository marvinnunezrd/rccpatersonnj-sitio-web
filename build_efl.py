import sys
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']

html = head(
  "Escuela de Formación de Líderes — RCC Paterson NJ",
  "Escuela de Formación de Líderes (EFL) de la Renovación Carismática Católica de la Diócesis de Paterson. Inscripciones abiertas al Módulo 3.",
  root=R,
  path="ministerios/escuela-formacion-lideres.html",
  og_image="assets/img/ministerios/escuela-formacion-lideres-og.jpg"
) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="{R}index.html">Inicio</a> / <a href="{R}index.html#ministerios">Ministerios</a> / Escuela de Formación de Líderes</div>
    <img class="hero-shield-sm" src="{R}assets/img/escudo-efl.webp" alt="Logo Escuela de Formación de Líderes" width="560" height="560">
    <h1>Escuela de Formación de Líderes</h1>
    <p class="subtitle">Formando servidores que lideran desde el servicio, como Jesús.</p>
  </div>
</header>

<section class="bg-navy" style="padding-top:56px;">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Próximo taller</span>
      <h2>Talleres de Formación Nacional</h2>
      <p>Módulo 3: Seminario de Vida en el Espíritu — en comunión con el Comité Nacional de Servicio Hispano (CNSH).</p>
    </div>
    <div class="flyer-block">
      <img src="{R}assets/img/modulo-3-flyer.webp" alt="Flyer Módulo 3: Seminario de Vida en el Espíritu — Talleres de Formación Nacional, RCC Paterson NJ" width="853" height="1280">
      <div class="flyer-details">
        <h3>Módulo 3 — Seminario de Vida en el Espíritu</h3>
        <p class="detail-line"><strong>Coordina</strong> Enrique Méndez, Coordinador de la Formación Nacional de la RCC de EE.UU. y Canadá</p>
        <p class="detail-line"><strong>Viernes</strong> 28 de agosto, 2026 — 7:00 pm – 9:30 pm</p>
        <p class="detail-line"><strong>Sábado</strong> 29 de agosto, 2026 — 8:30 am – 5:30 pm</p>
        <p class="detail-line"><strong>Lugar</strong> Salón Parroquial, Escuela Sta. Teresita — 765 14th Ave, Paterson, NJ 07504</p>
        <p class="detail-line"><strong>Donación</strong> $30 (incluye desayuno y almuerzo)</p>
        <p class="detail-line"><strong>Info</strong> <a href="https://wa.me/18622647885" target="_blank" rel="noopener" style="color:var(--gold-light);">862-264-7885 (WhatsApp) →</a></p>
        <div style="margin-top:22px;">
          <a class="btn btn-primary" href="https://docs.google.com/forms/d/e/1FAIpQLSc4Bcl6dMDr8Fw4jNe8nhwONLmG1qfJqn7XYCEmh6HuPJWSrQ/viewform?usp=header" target="_blank" rel="noopener">Inscribirme al Módulo 3 →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="min-content">
      <span class="eyebrow">Identidad y Misión</span>
      <h2 style="color:var(--navy);">Primero discípulo, luego líder</h2>
      <p>La Escuela de Formación de Líderes es el espacio formativo de la Renovación Carismática Católica de la Diócesis de Paterson dedicado a equipar, madurar y enviar servidores capaces de guiar a la comunidad carismática con sabiduría, fe y fidelidad a la Iglesia. No forma solo &ldquo;organizadores&rdquo; — forma discípulos que lideran desde el servicio, como Jesús.</p>
      <p style="font-family:var(--font-title);font-style:italic;color:var(--wine);">&ldquo;El que quiera ser grande entre ustedes, que sea su servidor.&rdquo; — Mateo 20:26</p>
      <p>La Escuela aborda tres dimensiones del servidor: <strong>formación humana</strong> (autoconocimiento, manejo de emociones, liderazgo relacional), <strong>formación espiritual</strong> (vida de oración, discernimiento, devoción mariana) y <strong>formación doctrinal</strong> (Biblia, Catecismo, historia de la Renovación Carismática, Doctrina Social de la Iglesia).</p>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Plan de estudios</span>
      <h2>Cursos por Nivel</h2>
      <p>Programa oficial de la Escuela de Formación de Líderes, según el Manual del Estudiante (Edición 2025).</p>
    </div>
    <div class="course-levels">
      <div class="course-level">
        <h3>Nivel I</h3>
        <ol>
          <li>Introducción a la Biblia</li>
          <li>El Antiguo Testamento y sus Libros e Historia</li>
          <li>El Nuevo Testamento sus Libros e Historia</li>
          <li>Cristología</li>
          <li>Mariología</li>
          <li>Eclesiología</li>
          <li>Doctrina Social de la Iglesia</li>
          <li>Introducción al Catecismo y la Profesión</li>
          <li>La Moral y el Cristiano</li>
          <li>Los Sacramentos y Liturgia</li>
        </ol>
      </div>
      <div class="course-level">
        <h3>Nivel II</h3>
        <ol>
          <li>La Renovación Carismática y el Espíritu Santo</li>
          <li>Los Seminarios de Vida en el Espíritu Santo</li>
          <li>Los Grupos de Oración y sus Elementos <em>(prerrequisito: curso anterior)</em></li>
          <li>La Vida de un Servidor como Seguidor del Señor</li>
          <li>Introducción a las Sagradas Escrituras como Palabra de Dios</li>
          <li>Los Dones y Carismas Dentro de los Grupos de Oración y Comunidad Católica</li>
        </ol>
      </div>
      <div class="course-level">
        <h3>Electivas</h3>
        <ol>
          <li>Introducción a la Liturgia</li>
          <li>Predicación</li>
          <li>La Palabra de Dios y la Predicación</li>
          <li>La Oración de Alabanza y la Palabra de Dios en el Grupo de Oración</li>
          <li>La Evangelización y Predicación I</li>
          <li>La Evangelización y Predicación II</li>
        </ol>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Equipo</span>
      <h2>Encargadas de la Escuela</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Juana De Jesús</h4><p class="role">Directora EFL</p></div>
      <div class="team-card"><h4>Massiel Reynoso</h4><p class="role">Subdirectora</p></div>
    </div>
    <div class="contact-block">
      <span class="eyebrow">Contacto de la Escuela</span>
      <a class="contact-phone" href="https://wa.me/18622647885" target="_blank" rel="noopener">{PHONE_ICON} 862-264-7885</a>
      <p class="contact-sub">Escríbenos por WhatsApp para inscripciones y dudas sobre los cursos</p>
      <a class="contact-email" href="mailto:eflrcc@gmail.com">eflrcc@gmail.com</a>
    </div>
  </div>
</section>
''' + footer(root=R) + TAIL

with open("ministerios/escuela-formacion-lideres.html", "w", encoding="utf-8") as f:
    f.write(html)
print("EFL page bytes:", len(html.encode("utf-8")))
