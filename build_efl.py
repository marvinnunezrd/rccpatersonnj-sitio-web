import sys
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']
WA_ICON = SOCIAL_ICONS['wa']

# Estilo local para las tarjetas de formador de la nueva sección "Cursos
# Activos Ahora Mismo" (Clase Alpha y Clase ETA). Reutiliza .details-list
# (ya pensado para fondo navy) para el calendario de cada formador; solo se
# agrega la tarjeta en sí y la foto circular. Agregado 2026-09-22.
#
# Recalibración de color 2026-09-22: la sección "Próximo taller" pasa de
# fondo navy a fondo claro (para alternar con "Clases semanales", que se
# queda navy), así que .flyer-details necesita sus propias reglas con id
# #proximo-taller. Las .faculty-card, en cambio, ahora viven sobre fondo
# navy y se rediseñan como tarjetas claras (blanco/crema) para contrastar,
# siguiendo el mismo patrón de .team-card en fondo .bg-navy.
EFL_STYLE = '''<style>
.faculty-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:32px;max-width:var(--max-width);margin:0 auto;align-items:start;}
.faculty-card{background:var(--ivory);border:1px solid rgba(0,0,0,.06);border-radius:14px;padding:32px 28px;box-shadow:0 10px 26px rgba(0,0,0,.18);}
.faculty-card .faculty-photo{width:120px;height:120px;border-radius:50%;overflow:hidden;margin:0 auto 18px;border:3px solid var(--gold);box-shadow:0 8px 20px rgba(0,0,0,.15);}
.faculty-card .faculty-photo img{width:100%;height:100%;object-fit:cover;display:block;}
.faculty-card .faculty-track{display:block;text-align:center;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;color:var(--wine);font-weight:700;margin-bottom:8px;}
.faculty-card h3{text-align:center;color:var(--navy);font-family:var(--font-title);font-size:1.3rem;margin:0 0 2px;}
.faculty-card .faculty-role{text-align:center;font-size:.76rem;color:var(--red);font-weight:700;text-transform:uppercase;letter-spacing:.03em;margin-bottom:16px;}
.faculty-card .faculty-bio{font-size:.88rem;color:#3c3630;line-height:1.65;margin-bottom:20px;text-align:justify;}
.faculty-card .faculty-bio strong{color:var(--navy);}
.faculty-card .details-list .label{color:#8a7a55;font-weight:700;}
.faculty-card .details-list .value{color:var(--navy);}
.faculty-card .details-list li{border-bottom:1px solid rgba(0,0,0,.08);}
.faculty-enroll-cta{text-align:center;max-width:520px;margin:44px auto 0;padding-top:34px;border-top:1px solid rgba(217,161,46,.25);}
.faculty-enroll-cta .eyebrow{display:block;margin-bottom:10px;}
.faculty-enroll-cta p{font-size:.92rem;color:rgba(255,243,214,.8);margin:0 0 20px;}
#proximo-taller .flyer-details h3{color:var(--navy);}
#proximo-taller .flyer-details .detail-line{color:#3c3630;}
#proximo-taller .flyer-details .detail-line strong{color:var(--wine);}
</style>'''

html = head(
  "Escuela de Formación de Líderes — RCC Paterson NJ",
  "Escuela de Formación de Líderes (EFL) de la Renovación Carismática Católica de la Diócesis de Paterson. Inscripciones abiertas al Módulo 4.",
  root=R,
  path="ministerios/escuela-formacion-lideres.html",
  og_image="assets/img/ministerios/escuela-formacion-lideres-og.jpg",
  extra=EFL_STYLE
) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/#ministerios">Ministerios</a> / Escuela de Formación de Líderes</div>
    <img class="hero-shield-sm" src="{R}assets/img/escudo-efl.webp" alt="Logo Escuela de Formación de Líderes" width="560" height="560">
    <h1>Escuela de Formación de Líderes</h1>
    <p class="subtitle">Formando servidores que lideran desde el servicio, como Jesús.</p>
  </div>
</header>

<section id="proximo-taller" style="padding-top:56px;">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Próximo taller</span>
      <h2>Talleres de Formación Nacional</h2>
      <p>Módulo 4: Grupos de Oración — en comunión con el Comité Nacional de Servicio Hispano (CNSH).</p>
    </div>
    <div class="flyer-block">
      <img src="{R}assets/img/modulo-4-flyer.webp" alt="Flyer Módulo 4: Grupos de Oración — Talleres de Formación Nacional, RCC Paterson NJ" width="1024" height="1536">
      <div class="flyer-details">
        <h3>Módulo 4 — Grupos de Oración</h3>
        <p class="detail-line"><strong>Instructor</strong> Juan De La Rosa, Instructor de Formación Nacional</p>
        <p class="detail-line"><strong>Viernes</strong> 2 de octubre, 2026 — 7:00 pm – 9:30 pm</p>
        <p class="detail-line"><strong>Sábado</strong> 3 de octubre, 2026 — 8:30 am – 5:30 pm</p>
        <p class="detail-line"><strong>Lugar</strong> Salón Parroquial, Escuela Sta. Teresita — 765 14th Ave, Paterson, NJ 07504</p>
        <p class="detail-line"><strong>Donación</strong> $30 (incluye desayuno y almuerzo)</p>
        <p class="detail-line"><strong>Info</strong> <a href="https://wa.me/18622647885" target="_blank" rel="noopener" style="color:var(--wine);">862-264-7885 (WhatsApp) →</a></p>
        <div style="margin-top:22px;">
          <a class="btn btn-primary" href="https://docs.google.com/forms/d/e/1FAIpQLSc4Bcl6dMDr8Fw4jNe8nhwONLmG1qfJqn7XYCEmh6HuPJWSrQ/viewform?usp=header" target="_blank" rel="noopener">Inscribirme al Módulo 4 →</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Clases semanales</span>
      <h2>Cursos Activos Ahora Mismo</h2>
      <p>Además del taller nacional, la Escuela ofrece dos clases continuas cada semana — Alpha y ETA — cada una con su propio formador y su propio calendario de cursos.</p>
    </div>
    <div class="faculty-grid">
      <div class="faculty-card">
        <div class="faculty-photo">
          <img src="{R}assets/img/ministerios/jose-cordero-formador-eta.webp" alt="José Cordero, formador de la Clase ETA" width="480" height="480">
        </div>
        <span class="faculty-track">Clase ETA &middot; lunes, 7:30 – 9:30 pm</span>
        <h3>José Cordero</h3>
        <p class="faculty-role">Formador</p>
        <p class="faculty-bio"><strong>José Cordero</strong> llega a la Escuela con una trayectoria de más de dos décadas dedicada a la formación en la fe. Tiene una Maestría en Estudios Religiosos y Pastoral por la <strong>Universidad de Fordham</strong> — universidad católica jesuita de <strong>Nueva York</strong> — y cuenta además con estudios en Educación y en Música. Formado también en el <strong>Instituto de Estudios Religiosos y Pastorales del Centro Católico Carismático de Nueva York</strong>, ha servido como catequista, predicador y músico en distintas parroquias del área metropolitana, y hoy acompaña procesos de formación de fe en la <strong>Diócesis de Rockville Centre</strong>. Es además educador de profesión, vinculado al sistema de escuelas públicas de <strong>Nueva York</strong>.</p>
        <ul class="details-list">
          <li><span class="label">Curso activo</span><span class="value">Introducción a la Liturgia — 14 sept. al 12 oct.</span></li>
          <li><span class="label">Próximo curso</span><span class="value">Predicación — 19 oct. al 16 nov.</span></li>
          <li><span class="label">Costo</span><span class="value">$75 por curso (5 clases)</span></li>
        </ul>
      </div>
      <div class="faculty-card">
        <div class="faculty-photo">
          <img src="{R}assets/img/ministerios/nector-garcia-formador-alpha.webp" alt="Néctor García, formador de la Clase Alpha" width="480" height="480">
        </div>
        <span class="faculty-track">Clase Alpha &middot; viernes, 7:30 – 9:30 pm</span>
        <h3>Néctor García</h3>
        <p class="faculty-role">Formador</p>
        <ul class="details-list">
          <li><span class="label">Curso activo</span><span class="value">La Moral y el Cristiano — 18 sept. al 16 oct.</span></li>
          <li><span class="label">Próximo curso</span><span class="value">Los Sacramentos y Liturgia — 23 oct. al 20 nov.</span></li>
          <li><span class="label">Costo</span><span class="value">$75 por curso (5 clases)</span></li>
        </ul>
      </div>
    </div>
    <div class="faculty-enroll-cta">
      <span class="eyebrow">¿Te sientes llamado a formarte?</span>
      <p>Para inscribirte en la Clase Alpha o la Clase ETA, comunícate directamente con la Escuela.</p>
      <a class="wa-cta-btn" href="https://wa.me/18622647885" target="_blank" rel="noopener">{WA_ICON}<span>Escríbenos por WhatsApp</span></a>
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
      <p>Programa oficial de la Escuela de Formación de Líderes.</p>
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
