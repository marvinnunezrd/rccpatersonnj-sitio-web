(function(){
  var slides = document.querySelectorAll('.hero-bg-slide');
  if (slides.length) {
    var i = 0;
    setInterval(function(){
      slides[i].classList.remove('is-active', 'is-first');
      i = (i + 1) % slides.length;
      slides[i].classList.add('is-active');
    }, 3000);
  }
})();
