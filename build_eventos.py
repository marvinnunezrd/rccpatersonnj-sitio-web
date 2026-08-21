import sys, os
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
    "url": "{SITE_URL}/eventos/encuentro-regional-2026.html"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{"@type": "Question", "name": "¿Cuándo es el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm."}}}},
    {{"@type": "Question", "name": "¿Dónde es el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "En la Parroquia Our Lady of Libera, 5808 John F Kennedy Blvd, West New York, NJ 07093."}}}},
    {{"@type": "Question", "name": "¿Cuánto cuesta la entrada al Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "La donación es de $30 e incluye el almuerzo."}}}},
    {{"@type": "Question", "name": "¿Habrá cuidado de niños en el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "No, el flyer oficial indica que no habrá cuidado de niños en este encuentro."}}}},
    {{"@type": "Question", "name": "¿Quién organiza el Encuentro Regional 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "Lo organiza la Renovación Carismática Católica Región 2 (Estados Unidos y Canadá), con la participación de Su Excelencia Pedro Bismarck Chau (Obispo Auxiliar de Newark), Mons. Joseph Malagreca, Mary Cruz y el Ministerio de Música Aroma de Cristo."}}}},
    {{"@type": "Question", "name": "¿Cómo me inscribo o pido más información del Encuentro Regional 2026?",
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
    <div class="breadcrumb"><a href="{R}index.html">Inicio</a> / <a href="{R}index.html#eventos">Eventos</a> / Encuentro Regional 2026</div>
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
    <p style="max-width:760px;margin:0 auto 18px;">El <strong>Encuentro Regional 2026 — Llamados a la Santidad</strong> es el encuentro anual de la <strong>Renovación Carismática Católica Región 2 (Estados Unidos y Canadá)</strong>, un día completo de oración, formación y alabanza junto a hermanos de toda la región. Se celebrará el <strong>sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm</strong>, en la <strong>Parroquia Our Lady of Libera</strong>, en West New York, NJ.</p>
    <p style="max-width:760px;margin:0 auto;">La Renovación Carismática Católica de la Diócesis de Paterson invita a toda su comunidad — grupos de oración, ministerios y líderes — a participar de este encuentro regional, viviendo juntos el mismo llamado a la santidad que compartimos como Iglesia.</p>
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
        <h3>¿Cuándo es el Encuentro Regional 2026?</h3>
        <p>El sábado 26 de septiembre de 2026, de 9:00 am a 6:00 pm.</p>
      </div>
      <div class="faq-item">
        <h3>¿Dónde es el Encuentro Regional 2026?</h3>
        <p>En la Parroquia Our Lady of Libera, 5808 John F Kennedy Blvd, West New York, NJ 07093.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cuánto cuesta la entrada?</h3>
        <p>La donación es de $30 e incluye el almuerzo.</p>
      </div>
      <div class="faq-item">
        <h3>¿Habrá cuidado de niños?</h3>
        <p>No, el flyer oficial indica que no habrá cuidado de niños en este encuentro.</p>
      </div>
      <div class="faq-item">
        <h3>¿Quién organiza el Encuentro Regional 2026?</h3>
        <p>Lo organiza la Renovación Carismática Católica Región 2 (Estados Unidos y Canadá), con la participación de Su Excelencia Pedro Bismarck Chau (Obispo Auxiliar de Newark), Mons. Joseph Malagreca, Mary Cruz y el Ministerio de Música "Aroma de Cristo".</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo me inscribo o pido más información?</h3>
        <p>Puedes comunicarte con Leybi Lima, Mary Paguay, Maria de la Cruz o Lissette Escobar — sus números están en la sección de contacto de esta página.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="{R}index.html#eventos">&larr; Volver a la agenda de eventos</a>
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
    {{"@type": "Question", "name": "¿Cuándo es la Gran Asamblea Diocesana de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm."}}}},
    {{"@type": "Question", "name": "¿Dónde es la Gran Asamblea Diocesana de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "En el Salón Principal de la Escuela Santa Teresita, 765 14th Avenue, Paterson, NJ 07504."}}}},
    {{"@type": "Question", "name": "¿Quién predica en la Gran Asamblea de septiembre 2026?",
      "acceptedAnswer": {{"@type": "Answer", "text": "El Diácono José Luis Abreu, quien dirigirá la predicación y la Exposición del Santísimo. En la música participa Marvin Núñez."}}}},
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
    <div class="breadcrumb"><a href="{R}index.html">Inicio</a> / <a href="{R}index.html#eventos">Eventos</a> / Gran Asamblea Diocesana</div>
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
    <p style="max-width:760px;margin:0 auto 18px;">La <strong>Gran Asamblea Diocesana</strong> reúne a toda la Renovación Carismática Católica de la Diócesis de Paterson en un mismo lugar: un domingo de predicación, adoración y Exposición del Santísimo, bajo el tema <strong>"Alma Sana, Corazón Libre"</strong>. Se celebrará el <strong>domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm</strong>, en el <strong>Salón Principal de la Escuela Santa Teresita</strong>, en Paterson, NJ.</p>
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
        <h3>¿Cuándo es la Gran Asamblea Diocesana de septiembre 2026?</h3>
        <p>El domingo 20 de septiembre de 2026, de 2:30 pm a 6:00 pm.</p>
      </div>
      <div class="faq-item">
        <h3>¿Dónde es?</h3>
        <p>En el Salón Principal de la Escuela Santa Teresita, 765 14th Avenue, Paterson, NJ 07504.</p>
      </div>
      <div class="faq-item">
        <h3>¿Quién predica?</h3>
        <p>El Diácono José Luis Abreu, quien dirigirá la predicación y la Exposición del Santísimo. En la música participa Marvin Núñez.</p>
      </div>
      <div class="faq-item">
        <h3>¿Cómo obtengo más información?</h3>
        <p>Puedes llamar al 862-271-4805.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-navy" style="text-align:center;padding-top:50px;padding-bottom:60px;">
  <a class="btn btn-outline" href="{R}index.html#eventos">&larr; Volver a la agenda de eventos</a>
</section>
''' + footer(root=R) + f'''
<script src="{R}assets/js/lightbox.js"></script>
''' + TAIL

filename = "eventos/gran-asamblea-septiembre-2026.html"
with open(filename, "w", encoding="utf-8") as f:
    f.write(html)
print(filename, len(html.encode("utf-8")), "bytes")
