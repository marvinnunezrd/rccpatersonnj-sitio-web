import sys, os, json
sys.path.insert(0, ".")
from common import head, footer, TAIL, SOCIAL_ICONS, SITE_URL

R = "../"
PHONE_ICON = SOCIAL_ICONS['phone']

os.makedirs("eventos", exist_ok=True)

# ---------- ENCUENTRO REGIONAL 2026 — LLAMADOS A LA SANTIDAD ----------

EVENT_JSONLD = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Encuentro Regional 2026 — Llamados a la Santidad",
  "startDate": "2026-09-26T09:00:00-04:00",
  "endDate": "2026-09-26T18:00:00-04:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {{
    "@type": "Place",
    "name": "Parroquia Our Lady of Libera",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "5808 John F Kennedy Blvd",
      "addressLocality": "West New York",
      "addressRegion": "NJ",
      "postalCode": "07093",
      "addressCountry": "US"
    }}
  }},
  "image": ["{SITE_URL}/assets/img/eventos/encuentro-regional-2026-og.jpg"],
  "description": "Encuentro Regional 2026 de la Renovación Carismática Católica Región 2 (Estados Unidos y Canadá), con el tema 'Llamados a la Santidad'. Sábado 26 de septiembre de 2026, 9:00 am a 6:00 pm, en la Parroquia Our Lady of Libera, West New York, NJ.",
  "organizer": {{
    "@type": "Organization",
    "name": "Renovación Carismática Católica Región 2 (Estados Unidos y Canadá)",
    "url": "{SITE_URL}"
  }},
  "performer": [
    {{"@type": "PerformingGroup", "name": "Ministerio de Música Aroma de Cristo"}}
  ],
  "offers": {{
    "@type": "Offer",
    "price": "30",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "url": "{SITE_URL}/eventos/encuentro-regional-2026"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "¿Cuándo fue el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm."}}}},
    {{"@type": "Question", "name": "¿Dónde fue el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "En la Parroquia Our Lady of Libera, 5808 John F Kennedy Blvd, West New York, NJ 07093."}}}},
    {{"@type": "Question", "name": "¿Cuánto cuesta la entrada al Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "La donación es de $30 e incluye el almuerzo."}}}},
    {{"@type": "Question", "name": "¿Hubo cuidado de niños en el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "No, el encuentro no contó con servicio de cuidado de niños."}}}},
    {{"@type": "Question", "name": "¿Quién organiza el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Lo organiza la Renovación Carismática Católica Región 2 (Estados Unidos y Canadá), con la participación de Su Excelencia Pedro Bismarck Chau (Obispo Auxiliar de Newark), Mons. Joseph Malagreca, Mary Cruz y el Ministerio de Música Aroma de Cristo."}}}},
    {{"@type": "Question", "name": "¿Cómo pido más información sobre el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Puedes comunicarte con Leybi Lima al (347) 681-1815, Mary Paguay al (917) 790-9528, Maria de la Cruz al (646) 852-2739, o Lissette Escobar al 1 (903) 903-0230."}}}}
  ]
}}
</script>'''

html = head(
    "Encuentro Regional 2026 — Llamados a la Santidad | RCC Región 2",
    "Encuentro Regional 2026 de la RCC Región 2: 'Llamados a la Santidad'. Sábado 26 de septiembre, Our Lady of Libera, West New York, NJ. Info y detalles aquí.",
    root=R, path="eventos/encuentro-regional-2026.html",
    og_image="assets/img/eventos/encuentro-regional-2026-og.jpg",
    extra=EVENT_JSONLD
) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/#eventos">Eventos</a> / Encuentro Regional 2026</div>
    <span class="event-tag event-tag--done">Realizado · 26 sep 2026</span>
    <span class="hero-edition">Renovación Carismática Católica Región 2</span>
    <h1>Encuentro Regional 2026</h1>
    <p class="lema">Llamados a la Santidad</p>
    <p class="subtitle">Sábado 26 de septiembre de 2026 · 9:00 am – 6:00 pm · Parroquia Our Lady of Libera, West New York, NJ</p>
    <a class="hero-flyer gallery-item" href="{R}assets/img/eventos/encuentro-regional-2026-flyer.webp">
      <img src="{R}assets/img/eventos/encuentro-regional-2026-thumb.webp" alt="Flyer oficial del Encuentro Regional 2026 — Llamados a la Santidad" width="420" height="560">
    </a>
    <p class="hero-flyer-caption">Toca el flyer para verlo completo</p>
  </div>
</header>

<section class="info-strip">
  <div class="container">
    <div class="info-item">
      <div class="icon">📅</div>
      <h3>Fecha</h3>
      <p>Sábado 26 de septiembre de 2026</p>
    </div>
    <div class="info-item">
      <div class="icon">🕑</div>
      <h3>Horario</h3>
      <p>9:00 am – 6:00 pm</p>
    </div>
    <div class="info-item">
      <div class="icon">💵</div>
      <h3>Donación</h3>
      <p>$30 · incluye almuerzo</p>
    </div>
    <div class="info-item">
      <div class="icon">ℹ️</div>
      <h3>Importante</h3>
      <p>No habrá cuidado de niños</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Sobre el encuentro</span>
      <h2>Un mismo llamado, toda una región reunida</h2>
    </div>
    <p style="max-width:760px;margin:0 auto 18px;">El <strong>Encuentro Regional 2026 — Llamados a la Santidad</strong> fue el encuentro anual de la <strong>Renovación Carismática Católica Región 2 (Estados Unidos y Canadá)</strong>, un día completo de oración, formación y alabanza junto a hermanos de toda la región. Se celebró el <strong>sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm</strong>, en la <strong>Parroquia Our Lady of Libera</strong>, en West New York, NJ.</p>
    <p style="max-width:760px;margin:0 auto;">La Renovación Carismática Católica de la Diócesis de Paterson participó con toda su comunidad — grupos de oración, ministerios y líderes — en este encuentro regional, viviendo juntos el mismo llamado a la santidad que compartimos como Iglesia.</p>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Invitados especiales</span>
      <h2>Quiénes nos acompañan</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Su Excelencia Pedro Bismarck Chau</h4><p class="role">Obispo Auxiliar de Newark</p></div>
      <div class="team-card"><h4>Mons. Joseph Malagreca</h4><p class="role">Director Espiritual CNSH</p></div>
      <div class="team-card"><h4>Mary Cruz</h4><p class="role">Miembro CNSH</p></div>
      <div class="team-card"><h4>Ministerio de Música "Aroma de Cristo"</h4><p class="role">Alabanza y adoración</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Ubicación</span>
      <h2>Cómo llegar</h2>
    </div>
    <div class="location-card">
      <svg class="pin-icon-lg" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10c0 5.4 6.9 11.1 7.2 11.4a1.2 1.2 0 0 0 1.6 0C13.1 21.1 20 15.4 20 10c0-4.4-3.6-8-8-8zm0 10.8A2.8 2.8 0 1 1 12 7.2a2.8 2.8 0 0 1 0 5.6z"/></svg>
      <h3>Parroquia Our Lady of Libera</h3>
      <p class="address">5808 John F Kennedy Blvd<br>West New York, NJ 07093</p>
      <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&query=5808+John+F+Kennedy+Blvd%2C+West+New+York%2C+NJ+07093" target="_blank" rel="noopener">Ver en Google Maps →</a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Contacto e información</span>
      <h2>¿Tienes preguntas?</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Leybi Lima</h4><a class="phone" href="https://wa.me/13476811815" target="_blank" rel="noopener">{PHONE_ICON} (347) 681-1815</a></div>
      <div class="team-card"><h4>Mary Paguay</h4><a class="phone" href="https://wa.me/19177909528" target="_blank" rel="noopener">{PHONE_ICON} (917) 790-9528</a></div>
      <div class="team-card"><h4>Maria de la Cruz</h4><a class="phone" href="https://wa.me/16468522739" target="_blank" rel="noopener">{PHONE_ICON} (646) 852-2739</a></div>
      <div class="team-card"><h4>Lissette Escobar</h4><a class="phone" href="https://wa.me/19039030230" target="_blank" rel="noopener">{PHONE_ICON} 1 (903) 903-0230</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2>Todo lo que debes saber</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <h3>¿Cuándo fue el Encuentro Regional 2026?</h3>
        <p>El sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm.</p>
      </div>
      <div class="faq-item">
        <h3>¿Dónde fue el Encuentro Regional 2026?</h3>
        <p>En la Parroquia Our Lady of Libera, 5808 John F Kennedy Blvd, West New York, NJ 07093.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cuánto cuesta la entrada?</h3>
        <p>La donación es de $30 e incluye el almuerzo.</p>
      </div>
      <div class="faq-item">
        <h3>¿Hubo cuidado de niños?</h3>
        <p>No, el encuentro no contó con servicio de cuidado de niños.</p>
      </div>
      <div class="faq-item">
        <h3>¿Quién organiza el Encuentro Regional 2026?</h3>
        <p>Lo organiza la Renovación Carismática Católica Región 2 (Estados Unidos y Canadá), con la participación de Su Excelencia Pedro Bismarck Chau (Obispo Auxiliar de Newark), Mons. Joseph Malagreca, Mary Cruz y el Ministerio de Música "Aroma de Cristo".</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo pido más información?</h3>
        <p>Puedes comunicarte con Leybi Lima, Mary Paguay, Maria de la Cruz o Lissette Escobar — sus números están en la sección de contacto de esta página.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="/#eventos">&larr; Volver a la agenda de eventos</a>
</section>
''' + footer(root=R) + f'''
<script src="{R}assets/js/lightbox.js"></script>
''' + TAIL

filename = "eventos/encuentro-regional-2026.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
print(filename, len(html.encode("utf-8")), "bytes")

# ---------- GRAN ASAMBLEA DIOCESANA — SEPTIEMBRE 2026 ----------

ASAMBLEA_JSONLD = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Gran Asamblea Diocesana — Septiembre 2026",
  "startDate": "2026-09-20T14:30:00-04:00",
  "endDate": "2026-09-20T18:00:00-04:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {{
    "@type": "Place",
    "name": "Salón Principal de la Escuela Santa Teresita",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "765 14th Avenue",
      "addressLocality": "Paterson",
      "addressRegion": "NJ",
      "postalCode": "07504",
      "addressCountry": "US"
    }}
  }},
  "image": ["{SITE_URL}/assets/img/eventos/gran-asamblea-sep-2026-og.jpg"],
  "description": "Gran Asamblea Diocesana de la Renovación Carismática Católica de la Diócesis de Paterson. Domingo 20 de septiembre de 2026, 2:30 pm a 6:00 pm, en el Salón Principal de la Escuela Santa Teresita, Paterson, NJ. Predicación y Exposición del Santísimo: Diácono José Luis Abreu. Tema: 'Alma Sana, Corazón Libre'.",
  "organizer": {{
    "@type": "Organization",
    "name": "Renovación Carismática Católica — Diócesis de Paterson",
    "url": "{SITE_URL}"
  }},
  "performer": [
    {{"@type": "Person", "name": "Diácono José Luis Abreu"}},
    {{"@type": "Person", "name": "Marvin Núñez"}}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "¿Cuándo fue la Gran Asamblea Diocesana de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm."}}}},
    {{"@type": "Question", "name": "¿Dónde fue la Gran Asamblea Diocesana de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "En el Salón Principal de la Escuela Santa Teresita, 765 14th Avenue, Paterson, NJ 07504."}}}},
    {{"@type": "Question", "name": "¿Quién predicó en la Gran Asamblea de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El Diácono José Luis Abreu, quien dirigió la predicación y la Exposición del Santísimo. En la música participó Marvin Núñez."}}}},
    {{"@type": "Question", "name": "¿Cómo obtengo más información sobre la Gran Asamblea de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Puedes llamar al 862-271-4805."}}}}
  ]
}}
</script>'''

html = head(
    "Gran Asamblea Diocesana — Septiembre 2026 | RCC Paterson NJ",
    "Gran Asamblea Diocesana RCC Paterson: 'Alma Sana, Corazón Libre'. Domingo 20 sept., Escuela Santa Teresita, Paterson NJ. Predica Diácono José Luis Abreu.",
    root=R, path="eventos/gran-asamblea-septiembre-2026.html",
    og_image="assets/img/eventos/gran-asamblea-sep-2026-og.jpg",
    extra=ASAMBLEA_JSONLD
) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/#eventos">Eventos</a> / Gran Asamblea Diocesana</div>
    <span class="event-tag event-tag--done">Realizado · 20 sep 2026</span>
    <span class="hero-edition">Renovación Carismática Católica — Diócesis de Paterson</span>
    <h1>Gran Asamblea Diocesana</h1>
    <p class="lema">Alma Sana, Corazón Libre</p>
    <p class="subtitle">Domingo 20 de septiembre de 2026 · 2:30 pm – 6:00 pm · Salón Principal, Escuela Santa Teresita, Paterson, NJ</p>
    <a class="hero-flyer gallery-item" href="{R}assets/img/eventos/gran-asamblea-sep-2026-flyer.webp">
      <img src="{R}assets/img/eventos/gran-asamblea-sep-2026-thumb.webp" alt="Flyer oficial de la Gran Asamblea Diocesana — Septiembre 2026" width="420" height="553">
    </a>
    <p class="hero-flyer-caption">Toca el flyer para verlo completo</p>
  </div>
</header>

<section class="info-strip">
  <div class="container">
    <div class="info-item">
      <div class="icon">📅</div>
      <h3>Fecha</h3>
      <p>Domingo 20 de septiembre de 2026</p>
    </div>
    <div class="info-item">
      <div class="icon">🕑</div>
      <h3>Horario</h3>
      <p>2:30 pm – 6:00 pm</p>
    </div>
    <div class="info-item">
      <div class="icon">📖</div>
      <h3>Predicación</h3>
      <p>Diácono José Luis Abreu</p>
    </div>
    <div class="info-item">
      <div class="icon">🎵</div>
      <h3>Música</h3>
      <p>Marvin Núñez</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Sobre la asamblea</span>
      <h2>Alma sana, corazón libre</h2>
    </div>
    <p style="max-width:760px;margin:0 auto 18px;">La <strong>Gran Asamblea Diocesana</strong> reúne a toda la Renovación Carismática Católica de la Diócesis de Paterson en un mismo lugar: un domingo de predicación, adoración y Exposición del Santísimo, bajo el tema <strong>"Alma Sana, Corazón Libre"</strong>. Se celebró el <strong>domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm</strong>, en el <strong>Salón Principal de la Escuela Santa Teresita</strong>, en Paterson, NJ.</p>
    <p style="max-width:760px;margin:0 auto;font-style:italic;">"Entren, inclinémonos para adorar; doblemos la rodilla ante el Señor que nos creó." — Salmo 95,6</p>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Quiénes nos acompañan</span>
      <h2>Predicación y música</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><h4>Diácono José Luis Abreu</h4><p class="role">Predicación y Exposición del Santísimo</p></div>
      <div class="team-card"><h4>Marvin Núñez</h4><p class="role">En la Música</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Ubicación</span>
      <h2>Cómo llegar</h2>
    </div>
    <div class="location-card">
      <svg class="pin-icon-lg" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10c0 5.4 6.9 11.1 7.2 11.4a1.2 1.2 0 0 0 1.6 0C13.1 21.1 20 15.4 20 10c0-4.4-3.6-8-8-8zm0 10.8A2.8 2.8 0 1 1 12 7.2a2.8 2.8 0 0 1 0 5.6z"/></svg>
      <h3>Escuela Santa Teresita — Salón Principal</h3>
      <p class="address">765 14th Avenue<br>Paterson, NJ 07504</p>
      <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&query=765+14th+Avenue%2C+Paterson%2C+NJ+07504" target="_blank" rel="noopener">Ver en Google Maps →</a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Contacto e información</span>
      <h2>¿Tienes preguntas?</h2>
    </div>
    <div class="team-grid" style="max-width:340px;margin:0 auto;">
      <div class="team-card"><h4>Información</h4><a class="phone" href="https://wa.me/18622714805" target="_blank" rel="noopener">{PHONE_ICON} 862-271-4805</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Otros formatos del flyer</span>
      <h2>Descarga la versión que prefieras</h2>
    </div>
    <div class="download-grid">
      <a class="download-card" href="{R}assets/img/eventos/gran-asamblea-sep-2026-alt.webp" download>
        <img src="{R}assets/img/eventos/gran-asamblea-sep-2026-alt-thumb.webp" alt="Flyer alterno vertical — Gran Asamblea Diocesana Septiembre 2026" width="260" height="428">
        <h4>Versión vertical alterna</h4>
        <p>Descargar imagen</p>
      </a>
      <a class="download-card" href="{R}assets/img/eventos/gran-asamblea-sep-2026-banner.webp" download>
        <img src="{R}assets/img/eventos/gran-asamblea-sep-2026-banner-thumb.webp" alt="Flyer horizontal — Gran Asamblea Diocesana Septiembre 2026" width="300" height="168">
        <h4>Versión horizontal (banner)</h4>
        <p>Descargar imagen</p>
      </a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2>Todo lo que debes saber</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <h3>¿Cuándo fue la Gran Asamblea Diocesana de septiembre 2026?</h3>
        <p>El domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm.</p>
      </div>
      <div class="faq-item">
        <h3>¿Dónde es?</h3>
        <p>En el Salón Principal de la Escuela Santa Teresita, 765 14th Avenue, Paterson, NJ 07504.</p>
      </div>
      <div class="faq-item">
        <h3>¿Quién predica?</h3>
        <p>El Diácono José Luis Abreu, quien dirigió la predicación y la Exposición del Santísimo. En la música participó Marvin Núñez.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo obtengo más información?</h3>
        <p>Puedes llamar al 862-271-4805.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="/#eventos">&larr; Volver a la agenda de eventos</a>
</section>
''' + footer(root=R) + f'''
<script src="{R}assets/js/lightbox.js"></script>
''' + TAIL

filename = "eventos/gran-asamblea-septiembre-2026.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
print(filename, len(html.encode("utf-8")), "bytes")

# ---------- CONGRESO DE SANACIÓN Y LIBERACIÓN — ALMA SANA, CORAZÓN LIBRE (24-25 OCT 2026) ----------
# Agregado 2026-10-09. Datos confirmados por Marvin con el flyer oficial y el
# calendario "Eventos Publicos RCCPatersonNJ" (evento confirmado 20 sep 2026).

CONGRESO_SLUG = "congreso-sanacion-liberacion-2026"

# Programa público (fuente: agenda oficial, oct 2026). Solo lo que ve el
# asistente: SIN lectores, ujieres, moderadores, servidores, logística ni rifa.
# (hora, actividad, tema, cita, predica)
CONGRESO_PROGRAMA = [
  ("Sábado 24 de octubre", "2026-10-24", [
    ("8:35 am",  "Santo Rosario", "", "", ""),
    ("9:05 am",  "Bienvenida", "", "", ""),
    ("9:15 am",  "Avivamiento musical", "", "", "Los Hijos del Padre"),
    ("9:25 am",  "Oraciones de intervención: Espíritu Santo y alabanzas", "", "", ""),
    ("10:00 am", "Santa Misa — Tema I", "Alma Sana, Corazón Libre", "2 Cor 3,17", "Rev. Alexis Coffi"),
    ("11:30 am", "Tema II", "¡Jesús Sana lo que el Alma Esconde!", "Salmo 147,3", "Osvaldo Fernández"),
    ("12:45 pm", "Almuerzo", "", "", ""),
    ("1:30 pm",  "Avivamiento", "", "", "Los Hijos del Padre"),
    ("1:50 pm",  "Tema III", "¡Perdona, Suelta y Deja que Dios te Sane!", "Efesios 4,31-32", "Osvaldo Fernández"),
    ("3:10 pm",  "Tema IV", "¡Levántate, Dios Renueva los Corazones Abatidos!", "Isaías 61,1-3 · Ezequiel 36,26", "Osvaldo Fernández"),
    ("4:15 pm",  "Clausura del primer día", "", "", ""),
  ]),
  ("Domingo 25 de octubre", "2026-10-25", [
    ("3:00 pm", "Coronilla de la Divina Misericordia", "", "", ""),
    ("3:10 pm", "Bienvenida", "", "", ""),
    ("3:15 pm", "Avivamiento", "", "", "Los Hijos del Padre"),
    ("3:25 pm", "Oraciones de intervención: Espíritu Santo y alabanzas", "", "", ""),
    ("3:40 pm", "Tema V", "¡El Espíritu Santo Rompe las Cadenas!", "2 Cor 3,17 · Romanos 8,1-2", "Osvaldo Fernández"),
    ("4:30 pm", "Tema VI", "¡Ante Jesús Eucaristía, Toda Alma se Libera!", "Juan 8,36", "Rev. Yasid Salas"),
    ("5:15 pm", "Exposición del Santísimo y oración final", "", "", "Rev. Yasid Salas y Osvaldo Fernández"),
    ("6:15 pm", "Clausura del Congreso", "", "", ""),
  ]),
]

def _iso(fecha, hora):
    hm, ap = hora.split()
    h, m = map(int, hm.split(":"))
    if ap == "pm" and h != 12: h += 12
    return f"{fecha}T{h:02d}:{m:02d}:00-04:00"

_CONGRESO_PLACE = {"@type": "Place", "name": "Gimnasio de la Parroquia St. Gerard",
  "address": {"@type": "PostalAddress", "streetAddress": "501 West Broadway", "addressLocality": "Paterson",
              "addressRegion": "NJ", "postalCode": "07522", "addressCountry": "US"}}
_sub = []
for _dia, _fecha, _items in CONGRESO_PROGRAMA:
    for _h, _act, _tema, _cita, _quien in _items:
        if not (_tema or "Santísimo" in _act):
            continue
        _ev = {"@type": "Event", "name": f"{_act}: {_tema}" if _tema else _act,
               "startDate": _iso(_fecha, _h), "location": _CONGRESO_PLACE,
               "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode"}
        if _cita: _ev["description"] = f"Cita bíblica: {_cita}"
        if _quien: _ev["performer"] = [{"@type": "Person", "name": n.strip()} for n in _quien.split(" y ")]
        _sub.append(_ev)
CONGRESO_SUBEVENTS = json.dumps(_sub, ensure_ascii=False, indent=2)

CONGRESO_JSONLD = f'''<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Event",
  "name": "Congreso de Sanación y Liberación — Alma Sana, Corazón Libre",
  "startDate": "2026-10-24T08:30:00-04:00",
  "endDate": "2026-10-25T18:30:00-04:00",
  "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
  "eventStatus": "https://schema.org/EventScheduled",
  "location": {json.dumps(_CONGRESO_PLACE, ensure_ascii=False)},
  "image": ["{SITE_URL}/assets/img/eventos/congreso-sanacion-2026-og.jpg"],
  "description": "Congreso de Sanación y Liberación 'Alma Sana, Corazón Libre' (2 Corintios 3:17) de la Renovación Carismática Católica de la Diócesis de Paterson. Sábado 24 de octubre de 2026, 8:30 am a 4:30 pm, y domingo 25 de octubre, 3:00 pm a 6:30 pm, en el Gimnasio de la Parroquia St. Gerard, 501 West Broadway, Paterson, NJ. Predican el Padre Alexis Coffi, Osvaldo Fernández y el Padre Yasid Salas. Música: Los Hijos Del Padre.",
  "offers": {{
    "@type": "Offer",
    "price": "35",
    "priceCurrency": "USD",
    "description": "Donativo (almuerzo incluido)",
    "availability": "https://schema.org/InStock",
    "url": "{SITE_URL}/eventos/{CONGRESO_SLUG}"
  }},
  "organizer": {{
    "@type": "Organization",
    "name": "Renovación Carismática Católica — Diócesis de Paterson",
    "url": "{SITE_URL}"
  }},
  "performer": [
    {{"@type": "Person", "name": "Padre Alexis Coffi"}},
    {{"@type": "Person", "name": "Osvaldo Fernández"}},
    {{"@type": "Person", "name": "Padre Yasid Salas"}},
    {{"@type": "MusicGroup", "name": "Los Hijos Del Padre"}}
  ],
  "subEvent": {CONGRESO_SUBEVENTS}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "¿Cuándo es el Congreso de Sanación y Liberación 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El sábado 24 de octubre de 2026, de 8:30 am a 4:30 pm, y el domingo 25 de octubre, de 3:00 pm a 6:30 pm."}}}},
    {{"@type": "Question", "name": "¿A qué hora debo llegar al Congreso?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El sábado el Santo Rosario inicia a las 8:35 am; el domingo, la Coronilla de la Divina Misericordia inicia a las 3:00 pm."}}}},
    {{"@type": "Question", "name": "¿Dónde es el Congreso de Sanación y Liberación?",
      "acceptedAnswer": {{"@type": "Answer", "text": "En el Gimnasio de la Parroquia St. Gerard, 501 West Broadway, Paterson, NJ 07522."}}}},
    {{"@type": "Question", "name": "¿Cuánto cuesta el Congreso?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Donativo de $35, con almuerzo incluido."}}}},
    {{"@type": "Question", "name": "¿Quién predica en el Congreso?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El Padre Alexis Coffi, Osvaldo Fernández y el Padre Yasid Salas. La música está a cargo de Los Hijos Del Padre."}}}},
    {{"@type": "Question", "name": "¿Habrá cuidado de niños?",
      "acceptedAnswer": {{"@type": "Answer", "text": "No. En este Congreso no habrá servicio de cuidado de niños."}}}},
    {{"@type": "Question", "name": "¿Cómo obtengo más información?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Puedes llamar o escribir por WhatsApp al +1 862-271-4805."}}}}
  ]
}}
</script>'''

CONGRESO_STYLE = '''<style>
.prog-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:26px;max-width:var(--max-width);margin:0 auto;align-items:start;}
@media (max-width:860px){.prog-grid{grid-template-columns:1fr;}}
.prog-day{background:var(--ivory);border-radius:14px;padding:26px 24px;box-shadow:0 10px 26px rgba(0,0,0,.18);}
.prog-day h3{color:var(--navy);text-align:center;margin:0 0 4px;}
.prog-day .prog-sub{text-align:center;font-size:.78rem;letter-spacing:.12em;text-transform:uppercase;color:var(--wine);font-weight:700;margin:0 0 16px;}
.prog-row{display:grid;grid-template-columns:78px 1fr;gap:12px;padding:11px 0;border-top:1px solid rgba(8,43,76,.1);}
.prog-time{font-weight:700;color:var(--wine);font-size:.86rem;}
.prog-act{color:var(--navy);font-weight:600;font-size:.93rem;}
.prog-tema{display:block;font-style:italic;color:#3c3630;font-size:.9rem;margin-top:2px;}
.prog-cita{display:block;color:#8a6410;font-size:.8rem;margin-top:2px;}
.prog-quien{display:block;color:#3c3630;font-size:.82rem;margin-top:2px;}
.prog-row.is-key .prog-act{color:var(--wine);}
.prog-cta{text-align:center;margin-top:30px;}
.video-grid{display:flex;gap:28px;justify-content:center;flex-wrap:wrap;}
.video-card{width:300px;max-width:100%;text-align:center;}
.video-card video{width:100%;height:auto;aspect-ratio:9/16;border-radius:14px;background:#000;box-shadow:0 14px 34px rgba(5,27,50,.25);display:block;}
.video-card h4{color:var(--navy);margin:14px 0 2px;}
.video-card p{font-size:.85rem;color:#6b5f4a;margin:0;}
.team-card .team-photo{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:10px;margin-bottom:14px;}
</style>'''

def _prog_day(dia, fecha, items, n):
    rows = []
    for h, act, tema, cita, quien in items:
        key = " is-key" if tema else ""
        extra = ""
        if tema: extra += f'<span class="prog-tema">“{tema}”</span>'
        if cita: extra += f'<span class="prog-cita">{cita}</span>'
        if quien: extra += f'<span class="prog-quien">{quien}</span>'
        rows.append(f'<div class="prog-row{key}"><div class="prog-time">{h}</div><div><span class="prog-act">{act}</span>{extra}</div></div>')
    return f'''<div class="prog-day"><h3>{dia}</h3><p class="prog-sub">Día {n} de 2</p>{"".join(rows)}</div>'''

CONGRESO_PROG_HTML = "\n      ".join(_prog_day(d, f, it, i + 1) for i, (d, f, it) in enumerate(CONGRESO_PROGRAMA))

# Archivo .ics para "Agregar a mi calendario" (ambos días, horario oficial del flyer)
_ics = "\r\n".join([
  "BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//RCC Paterson NJ//Congreso 2026//ES", "CALSCALE:GREGORIAN", "METHOD:PUBLISH",
  "BEGIN:VEVENT", "UID:congreso-2026-dia1@rccpatersonnj.com", "DTSTAMP:20261017T120000Z",
  "DTSTART:20261024T123000Z", "DTEND:20261024T203000Z",
  "SUMMARY:Congreso de Sanación y Liberación — Día 1",
  "LOCATION:Gimnasio de la Parroquia St. Gerard\\, 501 West Broadway\\, Paterson\\, NJ 07522",
  "DESCRIPTION:Alma Sana\\, Corazón Libre. Santo Rosario 8:35 am. Programa: https://rccpatersonnj.com/eventos/congreso-sanacion-liberacion-2026",
  "URL:https://rccpatersonnj.com/eventos/congreso-sanacion-liberacion-2026", "END:VEVENT",
  "BEGIN:VEVENT", "UID:congreso-2026-dia2@rccpatersonnj.com", "DTSTAMP:20261017T120000Z",
  "DTSTART:20261025T190000Z", "DTEND:20261025T223000Z",
  "SUMMARY:Congreso de Sanación y Liberación — Día 2",
  "LOCATION:Gimnasio de la Parroquia St. Gerard\\, 501 West Broadway\\, Paterson\\, NJ 07522",
  "DESCRIPTION:Alma Sana\\, Corazón Libre. Coronilla de la Divina Misericordia 3:00 pm. Programa: https://rccpatersonnj.com/eventos/congreso-sanacion-liberacion-2026",
  "URL:https://rccpatersonnj.com/eventos/congreso-sanacion-liberacion-2026", "END:VEVENT",
  "END:VCALENDAR", ""])
with open(f"eventos/{CONGRESO_SLUG}.ics", "w", encoding="utf-8", newline="") as f:
    f.write(_ics)

html = head(
    "Congreso de Sanación y Liberación 2026 — Alma Sana, Corazón Libre | RCC Paterson NJ",
    "Congreso de Sanación y Liberación 'Alma Sana, Corazón Libre'. 24 y 25 de octubre de 2026, Parroquia St. Gerard, Paterson NJ. Programa, predicadores, videos y donativo de $35 con almuerzo incluido.",
    root=R, path=f"eventos/{CONGRESO_SLUG}.html",
    og_image="assets/img/eventos/congreso-sanacion-2026-og.jpg",
    extra=CONGRESO_JSONLD + CONGRESO_STYLE
) + f'''
<header class="hero-sub">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/#eventos">Eventos</a> / Congreso de Sanación y Liberación</div>
    <span class="hero-edition">Renovación Carismática Católica — Diócesis de Paterson</span>
    <h1>Congreso de Sanación y Liberación</h1>
    <p class="lema">Alma Sana, Corazón Libre</p>
    <p class="subtitle">Sábado 24 y domingo 25 de octubre de 2026 · Gimnasio de la Parroquia St. Gerard, Paterson, NJ</p>
    <a class="hero-flyer gallery-item" href="{R}assets/img/eventos/congreso-sanacion-2026-flyer.webp">
      <img src="{R}assets/img/eventos/congreso-sanacion-2026-thumb.webp" alt="Flyer oficial del Congreso de Sanación y Liberación — Alma Sana, Corazón Libre" width="420" height="525">
    </a>
    <p class="hero-flyer-caption">Toca el flyer para verlo completo</p>
    <p style="margin-top:14px;"><a class="btn btn-outline" href="#programa">Ver el programa ↓</a></p>
  </div>
</header>

<section class="info-strip">
  <div class="container">
    <div class="info-item">
      <div class="icon">📅</div>
      <h3>Sábado 24 de octubre</h3>
      <p>8:30 am – 4:30 pm</p>
    </div>
    <div class="info-item">
      <div class="icon">📅</div>
      <h3>Domingo 25 de octubre</h3>
      <p>3:00 pm – 6:30 pm</p>
    </div>
    <div class="info-item">
      <div class="icon">🎟️</div>
      <h3>Donativo</h3>
      <p>$35 · almuerzo incluido</p>
    </div>
    <div class="info-item">
      <div class="icon">🎵</div>
      <h3>Música</h3>
      <p>Los Hijos Del Padre</p>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Sobre el congreso</span>
      <h2>Alma sana, corazón libre</h2>
    </div>
    <p style="max-width:760px;margin:0 auto 18px;">El <strong>Congreso de Sanación y Liberación</strong> de la Renovación Carismática Católica de la Diócesis de Paterson es un fin de semana de oración, Eucaristía, predicación y alabanza, para dejar que el Señor sane las heridas del alma y nos devuelva la libertad de los hijos de Dios. Se celebrará el <strong>sábado 24 de octubre de 2026, de 8:30 am a 4:30 pm</strong>, y el <strong>domingo 25 de octubre, de 3:00 pm a 6:30 pm</strong>, en el <strong>Gimnasio de la Parroquia St. Gerard</strong>, en Paterson, NJ.</p>
    <p style="max-width:760px;margin:0 auto;font-style:italic;">"Donde está el Espíritu del Señor, allí hay libertad." — 2 Corintios 3,17</p>
  </div>
</section>

<section class="bg-navy" id="programa">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Programa</span>
      <h2>Dos días de sanación y libertad</h2>
      <p>Seis temas de predicación, Santa Misa, alabanza y Exposición del Santísimo.</p>
    </div>
    <div class="prog-grid">
      {CONGRESO_PROG_HTML}
    </div>
    <div class="prog-cta">
      <a class="btn btn-primary" href="{R}eventos/{CONGRESO_SLUG}.ics" download>📅 Agregar a mi calendario</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Videos de invitación</span>
      <h2>Te invitamos personalmente</h2>
    </div>
    <div class="video-grid">
      <div class="video-card">
        <video controls playsinline preload="none" poster="{R}assets/img/eventos/congreso-2026-reel-teresa-poster.webp" width="720" height="1280">
          <source src="{R}assets/video/eventos/congreso-2026-reel-teresa.mp4" type="video/mp4">
        </video>
        <h4>Teresa Amparo</h4>
        <p>Invitación al Congreso</p>
      </div>
      <div class="video-card">
        <video controls playsinline preload="none" poster="{R}assets/img/eventos/congreso-2026-reel-osvaldo-poster.webp" width="720" height="1280">
          <source src="{R}assets/video/eventos/congreso-2026-reel-osvaldo.mp4" type="video/mp4">
        </video>
        <h4>Osvaldo Fernández</h4>
        <p>Invitación al Congreso</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Quiénes nos acompañan</span>
      <h2>Predicación y música</h2>
    </div>
    <div class="team-grid">
      <div class="team-card"><img class="team-photo" src="{R}assets/img/eventos/congreso-2026-padre-alexis-coffi.webp" alt="Padre Alexis Coffi" width="480" height="600" loading="lazy"><h4>Padre Alexis Coffi</h4><p class="role">Santa Misa · Tema I</p></div>
      <div class="team-card"><img class="team-photo" src="{R}assets/img/eventos/congreso-2026-osvaldo-fernandez.webp" alt="Osvaldo Fernández, predicador" width="480" height="600" loading="lazy"><h4>Osvaldo Fernández</h4><p class="role">Predicación · Temas II a V</p></div>
      <div class="team-card"><img class="team-photo" src="{R}assets/img/eventos/congreso-2026-padre-yasid-salas.webp" alt="Padre Yasid Salas" width="480" height="600" loading="lazy"><h4>Padre Yasid Salas</h4><p class="role">Tema VI · Exposición del Santísimo</p></div>
      <div class="team-card"><img class="team-photo" src="{R}assets/img/musica-los-hijos-del-padre.webp" alt="Ministerio de música Los Hijos Del Padre" loading="lazy"><h4>Los Hijos Del Padre</h4><p class="role">Ministerio de Música</p></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Ubicación</span>
      <h2>Cómo llegar</h2>
    </div>
    <div class="location-card">
      <svg class="pin-icon-lg" viewBox="0 0 24 24"><path d="M12 2C7.6 2 4 5.6 4 10c0 5.4 6.9 11.1 7.2 11.4a1.2 1.2 0 0 0 1.6 0C13.1 21.1 20 15.4 20 10c0-4.4-3.6-8-8-8zm0 10.8A2.8 2.8 0 1 1 12 7.2a2.8 2.8 0 0 1 0 5.6z"/></svg>
      <h3>Parroquia St. Gerard — Gimnasio</h3>
      <p class="address">501 West Broadway<br>Paterson, NJ 07522</p>
      <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&query=501+West+Broadway%2C+Paterson%2C+NJ+07522" target="_blank" rel="noopener">Ver en Google Maps →</a>
    </div>
  </div>
</section>

<section class="bg-navy">
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Contacto e información</span>
      <h2>¿Tienes preguntas?</h2>
    </div>
    <div class="team-grid" style="max-width:340px;margin:0 auto;">
      <div class="team-card"><h4>Información</h4><a class="phone" href="https://wa.me/18622714805" target="_blank" rel="noopener">{PHONE_ICON} +1 862-271-4805</a></div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-title">
      <span class="eyebrow">Preguntas frecuentes</span>
      <h2>Todo lo que debes saber</h2>
    </div>
    <div class="faq-list">
      <div class="faq-item">
        <h3>¿Cuándo es el Congreso?</h3>
        <p>El sábado 24 de octubre de 2026, de 8:30 am a 4:30 pm, y el domingo 25 de octubre, de 3:00 pm a 6:30 pm.</p>
      </div>
      <div class="faq-item">
        <h3>¿A qué hora debo llegar?</h3>
        <p>El sábado el Santo Rosario inicia a las 8:35 am; el domingo, la Coronilla de la Divina Misericordia inicia a las 3:00 pm. Te recomendamos llegar unos minutos antes.</p>
      </div>
      <div class="faq-item">
        <h3>¿Dónde es?</h3>
        <p>En el Gimnasio de la Parroquia St. Gerard, 501 West Broadway, Paterson, NJ 07522.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cuánto cuesta?</h3>
        <p>Donativo de $35, con almuerzo incluido.</p>
      </div>
      <div class="faq-item">
        <h3>¿Habrá cuidado de niños?</h3>
        <p>No. En este Congreso no habrá servicio de cuidado de niños.</p>
      </div>
      <div class="faq-item">
        <h3>¿Habrá venta de artículos religiosos?</h3>
        <p>Sí, habrá venta de objetos religiosos durante el Congreso.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo obtengo más información?</h3>
        <p>Puedes llamar o escribir por WhatsApp al +1 862-271-4805.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="/#eventos">&larr; Volver a la agenda de eventos</a>
</section>
''' + footer(root=R) + f'''
<script src="{R}assets/js/lightbox.js"></script>
''' + TAIL

filename = f"eventos/{CONGRESO_SLUG}.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
print(filename, len(html.encode("utf-8")), "bytes")


# ---------- ÁGAPE NAVIDEÑO DIOCESANO (5 DIC 2026) ----------
# Evento PRIVADO. URL corta /agape/ (QR del flyer). noindex.
# Los detalles (fecha, hora, lugar, flyer) NO están en este repo público:
# viven en ../Privado-Sitio-Web/agape/ y se publican CIFRADOS con el PIN
# (AES-256-GCM, clave PBKDF2-SHA256). El PIN nunca se escribe en archivos:
# se pasa en la variable de entorno AGAPE_PIN al generar (ver LEEME de esa carpeta).
# Sin AGAPE_PIN, este bloque NO toca agape/index.html.

import base64, json, secrets as _secrets
PRIV_AGAPE = os.path.join("..", "Privado-Sitio-Web", "agape")
AGAPE_ITER = 600000

AGAPE_STYLE = '''<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Great+Vibes&display=swap" rel="stylesheet">
<style>
.agape-hero{position:relative;overflow:hidden;text-align:center;color:var(--ivory);padding:70px 0 0;
  background:
    radial-gradient(1.5px 1.5px at 12% 18%,#fff 60%,transparent 61%),
    radial-gradient(1px 1px at 28% 32%,#fff 60%,transparent 61%),
    radial-gradient(1.5px 1.5px at 72% 14%,#fff 60%,transparent 61%),
    radial-gradient(1px 1px at 86% 36%,#fff 60%,transparent 61%),
    radial-gradient(1px 1px at 58% 26%,#fff 60%,transparent 61%),
    radial-gradient(1.5px 1.5px at 40% 9%,#fff 60%,transparent 61%),
    radial-gradient(1px 1px at 92% 58%,#fff 60%,transparent 61%),
    radial-gradient(1px 1px at 6% 52%,#fff 60%,transparent 61%),
    linear-gradient(180deg,#0B1D3F 0%,#1B2452 38%,#3A1E46 66%,#5A1424 100%);}
.agape-hero .breadcrumb{color:rgba(255,243,214,.7);}
.agape-hero .breadcrumb a{color:var(--gold-light);}
.agape-shield{width:104px;margin:18px auto 14px;filter:drop-shadow(0 8px 20px rgba(0,0,0,.45));}
.agape-org{font-family:'Cormorant Garamond',serif;letter-spacing:.32em;text-transform:uppercase;color:var(--gold-light);font-size:1rem;margin:0;}
.agape-dio{font-family:'Cormorant Garamond',serif;font-style:italic;color:rgba(255,243,214,.85);margin:2px 0 6px;font-size:1.05rem;}
.agape-title{font-family:'Great Vibes',cursive;font-weight:400;font-size:clamp(4.2rem,15vw,8rem);line-height:1;margin:6px 0 0;letter-spacing:0;
  background:linear-gradient(180deg,#F8DD8E 0%,#D9A12E 55%,#A8741A 100%);-webkit-background-clip:text;background-clip:text;color:transparent;}
.agape-sub{font-family:'Cormorant Garamond',serif;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-light);font-size:clamp(1.2rem,4.4vw,2rem);margin:0 0 6px;}
.agape-star{width:120px;height:120px;margin:10px auto 0;position:relative;}
.agape-star::before{content:"";position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle,rgba(255,236,170,.75) 0%,rgba(255,220,130,.25) 35%,transparent 70%);}
.agape-star::after{content:"";position:absolute;left:50%;top:50%;width:84px;height:84px;transform:translate(-50%,-50%);background:#FFF6D8;
  clip-path:polygon(50% 0,56% 44%,100% 50%,56% 56%,50% 100%,44% 56%,0 50%,44% 44%);}
.agape-nativity{display:block;width:100%;max-width:900px;margin:-6px auto 0;}
.agape-date{background:linear-gradient(180deg,#5A1424 0%,#4A0F1E 100%);color:var(--ivory);text-align:center;padding:34px 0 40px;}
.agape-date .d{font-family:'Cormorant Garamond',serif;font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:clamp(1.5rem,5vw,2.4rem);margin:0;}
.agape-date .h{font-family:'Cormorant Garamond',serif;color:var(--gold-light);font-size:clamp(1.3rem,4vw,1.8rem);margin:4px 0;}
.agape-date .l{font-family:'Cormorant Garamond',serif;font-size:clamp(1.1rem,3.6vw,1.45rem);margin:0;}
.agape-prelim{display:inline-block;margin-top:18px;border:1px solid rgba(242,203,105,.5);color:var(--gold-light);border-radius:999px;padding:6px 16px;font-size:.74rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;}
.agape-script{font-family:'Great Vibes',cursive;font-weight:400;color:var(--wine);font-size:clamp(2.4rem,8vw,3.4rem);letter-spacing:0;margin:0 0 4px;}
.bg-navy .agape-script{color:var(--gold-light);}
.agape-highlights{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px;max-width:960px;margin:0 auto;}
.agape-hl{text-align:center;border:1px solid rgba(217,161,46,.35);border-radius:14px;padding:28px 20px;background:rgba(255,255,255,.04);}
.agape-hl .k{font-size:.74rem;letter-spacing:.14em;text-transform:uppercase;font-weight:700;color:var(--gold);margin:0 0 8px;}
.agape-hl .v{font-family:'Cormorant Garamond',serif;font-size:1.45rem;color:var(--ivory);margin:0;line-height:1.25;}
.agape-flyer-link.gallery-item{aspect-ratio:auto;width:300px;max-width:100%;margin:0 auto 8px;border:2px solid var(--gold);border-radius:12px;box-shadow:0 20px 50px rgba(5,27,50,.3);}
.agape-flyer-link.gallery-item img{width:100%;height:auto;object-fit:unset;}
.agape-lock{max-width:560px;margin:0 auto;text-align:center;background:#fff;border:1px solid rgba(217,161,46,.45);border-radius:16px;padding:34px 26px;box-shadow:0 14px 34px rgba(5,27,50,.12);}
.agape-lock .ico{font-size:2rem;margin-bottom:6px;}
.agape-lock h3{color:var(--navy);}
.agape-lock p{color:#3c3630;font-size:.95rem;}
.agape-pin{display:flex;gap:10px;justify-content:center;margin:18px 0 8px;}
.agape-pin span{width:46px;height:56px;border:1.5px solid rgba(8,43,76,.25);border-radius:10px;background:var(--ivory);}
.agape-lock .soon{display:inline-block;margin-top:10px;font-size:.76rem;letter-spacing:.12em;text-transform:uppercase;font-weight:700;color:var(--wine);}
.agape-gate{background:linear-gradient(180deg,#5A1424 0%,#4A0F1E 100%);color:var(--ivory);text-align:center;padding:40px 0 48px;}
.agape-gate p{margin:0 auto 6px;max-width:520px;}
.agape-gate form{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:18px auto 6px;}
.agape-gate input{width:180px;font-size:1.6rem;letter-spacing:.5em;text-align:center;padding:10px 6px 10px 18px;border-radius:10px;border:1.5px solid var(--gold);background:rgba(255,255,255,.95);color:var(--navy);font-family:var(--font-body);}
.agape-gate .msg{min-height:1.4em;color:var(--gold-light);font-size:.9rem;margin-top:8px;}
.agape-gate .small{font-size:.8rem;color:rgba(255,243,214,.7);}
</style>'''

AGAPE_NATIVITY = '''<svg class="agape-nativity" viewBox="0 0 900 210" aria-hidden="true" preserveAspectRatio="xMidYMax meet">
  <g fill="#1A1430">
    <path d="M0 190 Q450 150 900 190 L900 210 L0 210 Z"/>
    <path d="M95 182 l6-110 q-30 6-46 22 q18-22 44-26 q-26-10-50-4 q26-12 52 0 q-6-22-24-34 q24 12 30 32 q14-22 40-26 q-24 12-32 30 q26-4 46 10 q-26-8-46 0 q24 10 34 30 q-20-18-42-22 l-4 98z"/>
    <path d="M790 182 l6-104 q-30 6-46 22 q18-22 44-26 q-26-10-50-4 q26-12 52 0 q-6-22-24-34 q24 12 30 32 q14-22 40-26 q-24 12-32 30 q26-4 46 10 q-26-8-46 0 q24 10 34 30 q-20-18-42-22 l-4 92z"/>
    <path d="M300 92 L450 30 L600 92 L588 98 L580 94 L580 180 L568 180 L568 96 L332 96 L332 180 L320 180 L320 94 L312 98 Z"/>
    <path d="M190 182 q2-34 16-40 q-10-14 0-24 q14-6 18 8 q2 10-6 16 q16 8 16 40 z"/>
    <path d="M232 182 q0-40 14-48 l-4-16 l8 6 l4-10 l4 10 l8-6 l-4 16 q14 8 14 48 z"/>
    <path d="M384 182 q-2-44 22-58 q-10-10-6-24 q10-12 24-4 q10 10 2 26 q20 18 16 60 z"/>
    <path d="M426 170 h48 l-6 14 h-36 z"/>
    <path d="M492 182 q-4-56 14-74 q-6-12 4-22 q14-8 22 4 q4 12-6 20 q18 22 14 72 z"/>
    <path d="M640 182 q4-26 30-30 q10-18 30-14 l6-14 l6 8 q10 4 6 14 l-6 4 q18 10 10 32 l-6 0 q0-12-8-18 q-24 2-40 0 q-10 8-10 18 z"/>
  </g>
  <g fill="none" stroke="#E7C266" stroke-width="2" opacity=".85">
    <circle cx="420" cy="112" r="15"/><circle cx="516" cy="96" r="15"/>
  </g>
  <ellipse cx="450" cy="168" rx="20" ry="7" fill="#FFF0B8" opacity=".9"/>
  <line x1="450" y1="0" x2="450" y2="160" stroke="#FFF0B8" stroke-width="1.2" opacity=".55"/>
</svg>'''


def _agape_encrypt(plaintext, pin):
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.ciphers.aead import AESGCM
    salt = _secrets.token_bytes(16); iv = _secrets.token_bytes(12)
    key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=AGAPE_ITER).derive(pin.encode())
    ct = AESGCM(key).encrypt(iv, plaintext.encode("utf-8"), None)
    b64 = lambda b: base64.b64encode(b).decode()
    return {"s": b64(salt), "i": b64(iv), "c": b64(ct), "n": AGAPE_ITER}

def _data_uri(path, mime="image/webp"):
    with open(path, "rb") as fh:
        return f"data:{mime};base64," + base64.b64encode(fh.read()).decode()

AGAPE_GATE_JS = r"""<script>
(function(){
  var P = window.AGAPE_PAYLOAD;
  var form = document.getElementById('agape-form'), input = document.getElementById('agape-pin'),
      msg = document.getElementById('agape-msg'), gate = document.getElementById('agape-gate'),
      box = document.getElementById('agape-privado');
  function b(s){ return Uint8Array.from(atob(s), function(c){ return c.charCodeAt(0); }); }
  async function open(pin){
    var base = await crypto.subtle.importKey('raw', new TextEncoder().encode(pin), 'PBKDF2', false, ['deriveKey']);
    var key = await crypto.subtle.deriveKey({name:'PBKDF2', salt:b(P.s), iterations:P.n, hash:'SHA-256'}, base,
                                            {name:'AES-GCM', length:256}, false, ['decrypt']);
    var pt = await crypto.subtle.decrypt({name:'AES-GCM', iv:b(P.i)}, key, b(P.c));
    box.innerHTML = new TextDecoder().decode(pt);
    gate.style.display = 'none'; box.hidden = false;
    var sc = document.createElement('script'); sc.src = '../assets/js/lightbox.js'; document.body.appendChild(sc);
    try { sessionStorage.setItem('agape-pin', pin); } catch(e) {}
  }
  form.addEventListener('submit', function(e){
    e.preventDefault();
    var pin = (input.value || '').replace(/\D/g, '');
    if (pin.length < 4) { msg.textContent = 'Escribe el PIN completo.'; return; }
    msg.textContent = 'Verificando…';
    open(pin).then(function(){ msg.textContent = ''; }).catch(function(){
      msg.textContent = 'PIN incorrecto. Revisa tu invitación.'; input.select();
    });
  });
  try { var saved = sessionStorage.getItem('agape-pin'); if (saved) open(saved).catch(function(){}); } catch(e) {}
})();
</script>"""

_agape_pin = os.environ.get("AGAPE_PIN", "").strip()
if not _agape_pin:
    print("AVISO: AGAPE_PIN no definido -> agape/index.html NO se regeneró.")
elif not os.path.isdir(PRIV_AGAPE):
    print("AVISO: falta la carpeta privada", PRIV_AGAPE, "-> agape/index.html NO se regeneró.")
else:
    with open(os.path.join(PRIV_AGAPE, "contenido.html"), encoding="utf-8") as fh:
        privado = fh.read()
    privado = privado.replace("{FLYER_THUMB}", _data_uri(os.path.join(PRIV_AGAPE, "agape-2026-thumb.webp")))
    privado = privado.replace("{FLYER_FULL}", _data_uri(os.path.join(PRIV_AGAPE, "agape-2026-flyer.webp")))
    payload = json.dumps(_agape_encrypt(privado, _agape_pin))

    html = head(
        "Ágape Navideño Diocesano | RCC Paterson NJ",
        "Encuentro privado de la Renovación Carismática Católica de la Diócesis de Paterson para el Equipo Diocesano y los servidores de los grupos de oración. Acceso con PIN de invitación.",
        root=R, path="agape/index.html",
        og_image="assets/img/eventos/agape-2026-og.jpg",
        og_description="Encuentro privado para el Equipo Diocesano y los servidores de los grupos de oración. Ingresa con el PIN de tu invitación.",
        extra=AGAPE_STYLE
    ) + f"""
<header class="agape-hero">
  <div class="container">
    <div class="breadcrumb"><a href="/">Inicio</a> / <a href="/#eventos">Eventos</a> / Ágape Navideño</div>
    <img class="agape-shield" src="{R}assets/img/escudo-rcc-oficial.webp" alt="Escudo oficial de la Renovación Carismática Católica — Diócesis de Paterson" width="420" height="420">
    <p class="agape-org">Renovación Carismática Católica</p>
    <p class="agape-dio">Diócesis de Paterson</p>
    <h1 class="agape-title">Ágape</h1>
    <p class="agape-sub">Navideño Diocesano</p>
    <div class="agape-star"></div>
  </div>
  {AGAPE_NATIVITY}
</header>

<section class="agape-gate" id="agape-gate">
  <div class="container">
    <p style="font-size:1.6rem;">🔒</p>
    <p><strong>Encuentro privado</strong> para el Equipo Diocesano y los servidores de los grupos de oración.</p>
    <p class="small">Ingresa el PIN que recibiste con tu invitación para ver los detalles y registrarte.</p>
    <form id="agape-form" autocomplete="off">
      <input id="agape-pin" type="password" inputmode="numeric" pattern="[0-9]*" maxlength="6" aria-label="PIN de invitación" placeholder="••••">
      <button class="btn btn-outline" type="submit">Entrar</button>
    </form>
    <p class="msg" id="agape-msg" role="status"></p>
  </div>
</section>

<div id="agape-privado" hidden></div>

<section style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-primary" href="/#eventos">&larr; Volver a la agenda de eventos</a>
</section>
""" + footer(root=R) + f"""
<script>window.AGAPE_PAYLOAD = {payload};</script>
{AGAPE_GATE_JS}
""" + TAIL

    os.makedirs("agape", exist_ok=True)
    with open("agape/index.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("agape/index.html", len(html.encode("utf-8")), "bytes (contenido cifrado)")
