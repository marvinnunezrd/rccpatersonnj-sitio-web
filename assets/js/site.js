(function(){
  var slides = document.querySelectorAll('.hero-bg-slide');
  if (!slides.length) return;
  var i = 0;

  function startCarousel(){
    setInterval(function(){
      slides[i].classList.remove('is-active', 'is-first');
      i = (i + 1) % slides.length;
      slides[i].classList.add('is-active');
    }, 3000);
  }

  // No arrancar el temporizador del carrusel hasta que la primera imagen
  // (la que cuenta para el LCP) haya terminado de cargar. En conexiones
  // lentas, si los 3s del temporizador se cumplen antes de que esa imagen
  // termine de descargarse, se le quita "is-active" a la primera slide sin
  // que el usuario llegue a verla, y el navegador termina "persiguiendo"
  // una imagen tras otra -- disparando el LCP muy por encima de lo real.
  // Con este guard, en conexiones lentas la primera imagen simplemente se
  // queda más tiempo en pantalla antes de que arranque la rotación.
  var match = /url\(["']?([^"')]+)["']?\)/.exec(slides[0].style.backgroundImage);
  var started = false;
  function safeStart(){
    if (started) return;
    started = true;
    startCarousel();
  }
  if (match) {
    var img = new Image();
    img.onload = safeStart;
    img.onerror = safeStart;
    img.src = match[1];
  } else {
    safeStart();
  }
  setTimeout(safeStart, 5000); // resguardo por si 'load' nunca dispara
})();
