/**
 * Solarglobe — scroll reveal .ps-reveal (global)
 * Contenu visible par défaut (CSS) ; animation uniquement avec js-enabled + .ps-animate.
 * Les blocs déjà dans la fenêtre au chargement restent visibles (pas de flash masqué).
 */
(function () {
  'use strict';

  var ROOT = document.documentElement;
  var REDUCED = '(prefers-reduced-motion: reduce)';

  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia(REDUCED).matches;
  }

  function isRoughlyInViewport(el) {
    var rect = el.getBoundingClientRect();
    var vh = window.innerHeight || document.documentElement.clientHeight || 0;
    return rect.top < vh * 0.92 && rect.bottom > 0;
  }

  function boot() {
    if (prefersReducedMotion()) return;

    var els = document.querySelectorAll('.ps-reveal, .sg-reveal');
    if (!els.length) return;

    var toObserve = [];

    function markRevealed(el) {
      el.classList.add('ps-visible');
      el.classList.add('visible');
    }

    els.forEach(function (el) {
      if (el.classList.contains('ps-visible') || el.classList.contains('visible')) return;
      if (isRoughlyInViewport(el)) {
        markRevealed(el);
      } else {
        el.classList.add('ps-animate');
        toObserve.push(el);
      }
    });

    if (!toObserve.length) return;

    var io = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (!e.isIntersecting) return;
          e.target.classList.add('ps-visible');
          e.target.classList.add('visible');
          io.unobserve(e.target);
        });
      },
      { rootMargin: '0px 0px -8% 0px', threshold: 0.05 }
    );

    toObserve.forEach(function (el) {
      io.observe(el);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
