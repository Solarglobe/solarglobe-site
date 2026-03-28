/**
 * TestimonialsSection — rendu des témoignages Google (données : testimonials.data.js).
 * Modes : short (accueil, 6 max · featured), full (tous les avis avec texte), banner (bandeau).
 */
(function (w) {
  'use strict';

  var STAR_PATH =
    'M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z';

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function starsHtml(rating) {
    var n = Math.min(5, Math.max(0, Math.round(Number(rating) || 0)));
    var i;
    var out =
      '<div class="sg-testimonial__stars" role="img" aria-label="' +
      esc(String(n) + ' sur 5') +
      '">';
    for (i = 0; i < 5; i++) {
      out +=
        '<svg class="sg-testimonial__star' +
        (i < n ? ' sg-testimonial__star--on' : '') +
        '" viewBox="0 0 24 24" aria-hidden="true"><path d="' +
        STAR_PATH +
        '"/></svg>';
    }
    return out + '</div>';
  }

  function formatDate(iso) {
    if (!iso) return '';
    var d = new Date(iso);
    if (isNaN(d.getTime())) return '';
    return d.toLocaleDateString('fr-FR', { month: 'long', year: 'numeric' });
  }

  function getTextReviews(data) {
    if (!data || !data.items) return [];
    return data.items.filter(function (i) {
      return (
        !i.counterOnly &&
        i.visible !== false &&
        typeof i.shortText === 'string' &&
        i.shortText.trim().length > 0
      );
    });
  }

  function cardHtml(t, mode) {
    var showLong = mode === 'full' && t.longText && t.longText.trim() !== t.shortText.trim();
    var dateLabel = formatDate(t.date);
    var meta = (dateLabel ? dateLabel + ' · ' : '') + esc(t.source || 'Google');

    var body =
      '<article class="sg-testimonial-card" role="listitem">' +
      '<blockquote class="sg-testimonial-card__quote"><p>«&nbsp;' +
      esc(t.shortText) +
      '&nbsp;»</p></blockquote>';

    if (showLong) {
      body +=
        '<p class="sg-testimonial-card__long">' + esc(t.longText) + '</p>';
    }

    body +=
      '<footer class="sg-testimonial-card__footer">' +
      starsHtml(t.rating) +
      '<div class="sg-testimonial-card__by">' +
      '<cite class="sg-testimonial-card__cite">' +
      esc(t.displayName || t.name) +
      '</cite>' +
      '<span class="sg-testimonial-card__meta">' +
      meta +
      '</span>' +
      '</div></footer></article>';

    return body;
  }

  function mountGrid(container, options) {
    var data = w.SG_TESTIMONIALS_DATA;
    if (!container || !data) return;

    var mode = (options && options.mode) || 'short';
    var maxCards = (options && options.maxCards) || 6;
    var list = getTextReviews(data);

    if (mode === 'short') {
      var feat = list.filter(function (i) {
        return i.featured;
      });
      list = feat.length ? feat : list;
      list = list.slice(0, maxCards);
    }

    container.innerHTML = list.map(function (t) {
      return cardHtml(t, mode);
    }).join('');
  }

  function mountBanner(container) {
    var data = w.SG_TESTIMONIALS_DATA;
    if (!container || !data) return;
    var n = data.googleTotalReviewCount || getTextReviews(data).length;
    var maps = data.googleMapsUrl || '#';
    container.innerHTML =
      '<p class="sg-testimonials-banner__text">' +
      '<span class="sg-testimonials-banner__score">5/5</span> sur Google' +
      ' · <strong>' +
      esc(String(n)) +
      ' avis</strong> clients' +
      ' · <a class="sg-testimonials-banner__link" href="' +
      esc(maps) +
      '" target="_blank" rel="noopener noreferrer">Voir sur Google</a>' +
      '</p>';
  }

  w.SG_TestimonialsSection = {
    mountGrid: mountGrid,
    mountBanner: mountBanner,

    initHomeSection: function () {
      var el = document.getElementById('sg-testimonials-grid-mount');
      if (el) mountGrid(el, { mode: 'short', maxCards: 6 });
    },

    initFullSection: function (mountId) {
      var el = document.getElementById(mountId || 'sg-testimonials-grid-mount');
      if (el) mountGrid(el, { mode: 'full' });
    },

    initBanner: function (mountId) {
      var el = document.getElementById(mountId || 'sg-testimonials-banner-mount');
      if (el) mountBanner(el);
    }
  };
})(typeof window !== 'undefined' ? window : this);
