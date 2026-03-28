/**
 * SOLARGLOBE ANIMATIONS PREMIUM
 * IntersectionObserver — déclenche sg-animate-visible au scroll
 * Cascade réelle pour les cartes (sg-guides-grid)
 */
(function () {
  'use strict';

  var SELECTOR = '.sg-fade-up, .sg-fade-left, .sg-fade-right, .sg-zoom-in, .sg-reveal-text, .sg-card-rise, .sg-image-reveal, .sg-guides-grid';
  var VISIBLE_CLASS = 'sg-animate-visible';

  function animateCardsSequential(container) {
    var cards = container.querySelectorAll('.sg-card-rise');
    for (var c = 0; c < cards.length; c++) {
      (function (idx) {
        setTimeout(function () {
          cards[idx].classList.add(VISIBLE_CLASS);
        }, idx * 340);
      })(c);
    }
  }

  function init() {
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
            animateCardsSequential(entry.target);
          } else {
            entry.target.classList.add(VISIBLE_CLASS);
          }
          observer.unobserve(entry.target);
        }
      },
      {
        threshold: 0.25,
        rootMargin: '0px 0px -20% 0px'
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
