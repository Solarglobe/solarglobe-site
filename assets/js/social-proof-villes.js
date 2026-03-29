/**
 * Preuve sociale pages locales panneaux-solaires-* — fragment components/social-proof-villes.html
 * + testimonials.data.js / testimonials-section.js (même logique que l’accueil et l’étude gratuite).
 */
document.addEventListener('DOMContentLoaded', function () {
  var root = document.getElementById('sg-local-social-proof-placeholder');
  if (!root) return;

  function loadScript(src, onload) {
    var sel = 'script[src="' + src + '"]';
    if (document.querySelector(sel)) {
      if (onload) onload();
      return;
    }
    var s = document.createElement('script');
    s.src = src;
    s.onload = function () {
      if (onload) onload();
    };
    s.onerror = function () {
      console.error('social-proof-villes: échec chargement', src);
    };
    document.body.appendChild(s);
  }

  function mount() {
    var grid = document.getElementById('sg-villes-testimonials-mount');
    if (grid && window.SG_TestimonialsSection) {
      window.SG_TestimonialsSection.mountGrid(grid, { mode: 'short', maxCards: 6 });
    }
  }

  fetch('/components/social-proof-villes.html?v=1')
    .then(function (r) {
      if (!r.ok) throw new Error(r.status);
      return r.text();
    })
    .then(function (html) {
      root.innerHTML = html;
      loadScript('/assets/js/testimonials.data.js?v=1', function () {
        loadScript('/assets/js/testimonials-section.js?v=1', mount);
      });
    })
    .catch(function (e) {
      console.error('social-proof-villes:', e);
    });
});
