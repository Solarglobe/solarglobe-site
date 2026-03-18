/**
 * SOLARGLOBE COUNTER PREMIUM
 * Un seul IntersectionObserver pour tous les .sg-counter
 */
(function () {
  'use strict';

  var SELECTOR = '.sg-counter';

  function animateCounter(el) {
    var target = parseInt(el.innerText.replace(/\D/g, ''), 10);
    if (isNaN(target)) return;

    var count = 0;
    var duration = 1500;
    var startTime = null;

    function update(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      count = Math.round(target * progress);
      el.innerText = count.toLocaleString('fr-FR');
      if (progress < 1) {
        requestAnimationFrame(update);
      } else {
        el.innerText = target.toLocaleString('fr-FR');
      }
    }

    requestAnimationFrame(update);
  }

  function init() {
    var elements = document.querySelectorAll(SELECTOR);
    if (!elements.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animateCounter(entry.target);
          observer.unobserve(entry.target);
        });
      },
      {
        threshold: 0.2,
        rootMargin: '0px 0px -10% 0px'
      }
    );

    elements.forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
