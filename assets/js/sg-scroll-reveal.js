/**
 * SOLARGLOBE SCROLL REVEAL PREMIUM
 * Animation par section — stagger automatique
 * Inspiré Apple, Stripe, Vercel, Linear
 */
(function () {
  'use strict';

  var SECTION_SELECTOR = '.sg-section, .sg-section-editorial';
  var REVEAL_SELECTOR = '.sg-reveal';
  var REVEAL_CARD_SELECTOR = '.sg-reveal-card';
  var ALL_REVEAL_SELECTOR = '.sg-reveal, .sg-reveal-card';
  var VISIBLE_CLASS = 'sg-reveal-visible';
  var STAGGER_MS = 220;

  function animateSection(section) {
    var elements = section.querySelectorAll(ALL_REVEAL_SELECTOR);
    if (!elements.length) return;

    elements.forEach(function (el, index) {
      // sécurité : éviter les éléments bloqués invisibles
      if (el.classList.contains(VISIBLE_CLASS)) return;

      setTimeout(function () {
        el.classList.add(VISIBLE_CLASS);
      }, index * STAGGER_MS);
    });
  }

  function init() {
    var sections = document.querySelectorAll(SECTION_SELECTOR);
    if (!sections.length) return;

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          animateSection(entry.target);
          observer.unobserve(entry.target);
        });
      },
      {
        threshold: 0.3,
        rootMargin: '0px 0px -10% 0px'
      }
    );

    sections.forEach(function (section) {
      if (section.querySelectorAll(ALL_REVEAL_SELECTOR).length > 0) {
        observer.observe(section);
      }
    });
  }

  function initHero() {
    var hero = document.querySelector('.sg-hero-premium') || document.querySelector('.sg-hero-solaire');
    if (!hero) return;

    var reveals = hero.querySelectorAll('.sg-hero-reveal');
    if (reveals.length) {
      reveals.forEach(function (el, i) {
        setTimeout(function () {
          el.classList.add('sg-reveal-visible');
        }, i * 220);
      });
      return;
    }

    var kicker = hero.querySelector('.sg-hero-kicker');
    var title = hero.querySelector('.sg-hero-title');
    var subtitle = hero.querySelector('.sg-hero-subtitle');
    var cta = hero.querySelector('.sg-hero-cta');

    [kicker, title, subtitle, cta].filter(Boolean).forEach(function (el, i) {
      setTimeout(function () {
        el.classList.add('sg-reveal-visible');
      }, i * 300);
    });
  }

  function run() {
    initHero();
    init();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
