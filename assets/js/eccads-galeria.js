// Lightbox simple para la galería de fotos ECCADS 2026 — sin dependencias externas
(function () {
  var items = Array.prototype.slice.call(document.querySelectorAll('.gallery-item'));
  if (!items.length) return;

  var overlay = document.createElement('div');
  overlay.className = 'lightbox-overlay';
  overlay.innerHTML =
    '<button class="lightbox-close" aria-label="Cerrar">&times;</button>' +
    '<button class="lightbox-prev" aria-label="Foto anterior">&#10094;</button>' +
    '<img class="lightbox-img" alt="">' +
    '<button class="lightbox-next" aria-label="Foto siguiente">&#10095;</button>' +
    '<div class="lightbox-count"></div>';
  document.body.appendChild(overlay);

  var imgEl = overlay.querySelector('.lightbox-img');
  var countEl = overlay.querySelector('.lightbox-count');
  var current = 0;

  function open(index) {
    current = index;
    show();
    overlay.classList.add('is-open');
    document.body.style.overflow = 'hidden';
  }
  function close() {
    overlay.classList.remove('is-open');
    document.body.style.overflow = '';
  }
  function show() {
    var full = items[current].getAttribute('href');
    var alt = items[current].querySelector('img').getAttribute('alt') || '';
    imgEl.setAttribute('src', full);
    imgEl.setAttribute('alt', alt);
    countEl.textContent = (current + 1) + ' / ' + items.length;
  }
  function next() { current = (current + 1) % items.length; show(); }
  function prev() { current = (current - 1 + items.length) % items.length; show(); }

  items.forEach(function (link, i) {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      open(i);
    });
  });

  overlay.querySelector('.lightbox-close').addEventListener('click', close);
  overlay.querySelector('.lightbox-next').addEventListener('click', next);
  overlay.querySelector('.lightbox-prev').addEventListener('click', prev);
  overlay.addEventListener('click', function (e) {
    if (e.target === overlay) close();
  });
  document.addEventListener('keydown', function (e) {
    if (!overlay.classList.contains('is-open')) return;
    if (e.key === 'Escape') close();
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
  });
})();
