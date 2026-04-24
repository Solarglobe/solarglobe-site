/**
 * SOLARGLOBE — animations scroll (reveal unifié)
 * Un seul IntersectionObserver pour tous les éléments observés.
 * .sg-reveal + .sg-visible (état visible)
 * Anciennes classes : .sg-fade-up, etc. + .sg-animate-visible
 * Page étude financière : .reveal, .fade-up, .slide-*, .zoom-image + .reveal-visible
 */
(function () {
  'use strict';

  var SELECTOR =
    '.sg-reveal, .reveal, .fade-up, .slide-left, .slide-right, .zoom-image, .sg-fade-up, .sg-fade-left, .sg-fade-right, .sg-zoom-in, .sg-reveal-text, .sg-card-rise, .sg-image-reveal, .sg-guides-grid';
  var CLASS_VISIBLE_REVEAL = 'sg-visible';
  var CLASS_VISIBLE_LEGACY = 'sg-animate-visible';
  var CLASS_REVEAL_VISIBLE = 'reveal-visible';

  function prefersReducedMotion() {
    return window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function setRevealedClass(el) {
    if (el.classList.contains('sg-reveal')) {
      el.classList.add(CLASS_VISIBLE_REVEAL);
      return;
    }
    if (
      el.matches &&
      el.matches('.reveal, .fade-up, .slide-left, .slide-right, .zoom-image')
    ) {
      el.classList.add(CLASS_REVEAL_VISIBLE);
      return;
    }
    el.classList.add(CLASS_VISIBLE_LEGACY);
  }

  function revealAllReducedMotion() {
    var all = document.querySelectorAll(SELECTOR);
    var i;
    for (i = 0; i < all.length; i++) {
      setRevealedClass(all[i]);
    }
    var grids = document.querySelectorAll('.sg-guides-grid');
    for (var g = 0; g < grids.length; g++) {
      var cards = grids[g].querySelectorAll('.sg-card-rise');
      for (var c = 0; c < cards.length; c++) {
        cards[c].classList.add(CLASS_VISIBLE_LEGACY);
      }
    }
  }

  function animateCardsSequential(container, observer) {
    var cards = container.querySelectorAll('.sg-card-rise');
    var c;
    for (c = 0; c < cards.length; c++) {
      (function (idx) {
        window.setTimeout(function () {
          cards[idx].classList.add(CLASS_VISIBLE_LEGACY);
        }, idx * 340);
      })(c);
    }
    observer.unobserve(container);
  }

  function init() {
    if (prefersReducedMotion()) {
      revealAllReducedMotion();
      return;
    }

    var elements = document.querySelectorAll(SELECTOR);
    if (!elements.length) return;

    var toObserve = [];
    for (var k = 0; k < elements.length; k++) {
      var el = elements[k];
      if (el.classList.contains('sg-card-rise') && el.closest('.sg-guides-grid')) {
        continue;
      }
      toObserve.push(el);
    }

    var observer = new IntersectionObserver(
      function (entries) {
        for (var i = 0; i < entries.length; i++) {
          var entry = entries[i];
          if (!entry.isIntersecting) continue;
          if (entry.target.classList.contains('sg-guides-grid')) {
            animateCardsSequential(entry.target, observer);
          } else {
            setRevealedClass(entry.target);
            observer.unobserve(entry.target);
          }
        }
      },
      {
        threshold: 0.2,
        rootMargin: '0px 0px -10% 0px'
      }
    );

    for (var j = 0; j < toObserve.length; j++) {
      observer.observe(toObserve[j]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
