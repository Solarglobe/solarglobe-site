(function () {
  'use strict';
  const KEY = 'solarglobe_consent_v2';
  const MAX_AGE = 180 * 24 * 60 * 60 * 1000;
  const denied = { analytics_storage: 'denied', ad_storage: 'denied', ad_user_data: 'denied', ad_personalization: 'denied' };
  window.dataLayer = window.dataLayer || [];
  window.gtag = window.gtag || function () { window.dataLayer.push(arguments); };
  window.gtag('consent', 'default', denied);
  let choice = null;
  try {
    const saved = JSON.parse(localStorage.getItem(KEY));
    if (saved && saved.version === 2 && typeof saved.analytics === 'boolean' && typeof saved.marketing === 'boolean' && saved.time <= Date.now() && Date.now() - saved.time < MAX_AGE) choice = saved;
    // An old acceptance did not expose granular choices or an expiry. Ask again.
    localStorage.removeItem('solarglobe_cookie_consent');
    localStorage.removeItem('SolarGlobe_cookie_consent');
  } catch (_) { /* Storage may be disabled; consent remains denied. */ }

  function apply(value) {
    window.gtag('consent', 'update', {
      analytics_storage: value.analytics ? 'granted' : 'denied',
      ad_storage: value.marketing ? 'granted' : 'denied',
      ad_user_data: value.marketing ? 'granted' : 'denied',
      ad_personalization: value.marketing ? 'granted' : 'denied'
    });
    // Load categories separately: the previous GTM container fired custom Meta
    // and Ads HTML tags on every pageview, regardless of granular consent.
    if ((value.analytics || value.marketing) && !document.getElementById('sg-google-tag')) {
      const script = document.createElement('script');
      script.id = 'sg-google-tag'; script.async = true;
      script.src = 'https://www.googletagmanager.com/gtag/js?id=' + (value.analytics ? 'G-V9BGEJKQKZ' : 'AW-17462997481');
      document.head.appendChild(script);
      window.gtag('js', new Date());
    }
    if (value.analytics && !document.documentElement.hasAttribute('data-sg-analytics')) {
      document.documentElement.setAttribute('data-sg-analytics', 'true');
      window.gtag('config', 'G-V9BGEJKQKZ');
    }
    if (value.marketing && !document.documentElement.hasAttribute('data-sg-marketing')) {
      document.documentElement.setAttribute('data-sg-marketing', 'true');
      window.gtag('config', 'AW-17462997481');
      window.fbq = window.fbq || function () {
        if (window.fbq.callMethod) window.fbq.callMethod.apply(window.fbq, arguments);
        else window.fbq.queue.push(arguments);
      };
      window.fbq.queue = window.fbq.queue || []; window.fbq.loaded = true; window.fbq.version = '2.0';
      window._fbq = window._fbq || window.fbq;
      const meta = document.createElement('script'); meta.async = true; meta.id = 'sg-meta-tag';
      meta.src = 'https://connect.facebook.net/en_US/fbevents.js'; document.head.appendChild(meta);
      window.fbq('consent', 'grant'); window.fbq('init', '772633518785475'); window.fbq('track', 'PageView');
    }
    window.dataLayer.push({ event: 'sg_consent_update', analytics_consent: value.analytics, marketing_consent: value.marketing });
  }
  if (choice) apply(choice);

  function clearCookies(value) {
    const domains = ['', location.hostname, '.' + location.hostname];
    const parts = location.hostname.split('.');
    if (parts.length > 2) domains.push('.' + parts.slice(-2).join('.'));
    document.cookie.split(';').forEach(function (entry) {
      const name = entry.split('=')[0].trim();
      const analytics = /^(_ga|_gid|_gat)/.test(name);
      const marketing = /^(_gcl_|_gac_|_fbp$|_fbc$)/.test(name);
      if ((analytics && !value.analytics) || (marketing && !value.marketing)) {
        domains.forEach(function (domain) {
          document.cookie = name + '=; Max-Age=0; path=/' + (domain ? '; domain=' + domain : '') + '; SameSite=Lax';
        });
      }
    });
  }

  function mount() {
    const link = document.createElement('link'); link.rel = 'stylesheet'; link.href = '/assets/css/consent.css'; document.head.appendChild(link);
    const banner = document.createElement('section');
    banner.id = 'sg-consent-banner'; banner.setAttribute('aria-label', 'Choix des cookies'); banner.hidden = !!choice;
    banner.innerHTML = '<div class="sg-consent-inner"><div><strong>Vos choix de confidentialité</strong><p>Avec votre accord, nous utilisons des traceurs de mesure d’audience et de publicité. Vous pouvez refuser ou choisir par catégorie. <a href="/cookies/">En savoir plus</a></p></div><div class="sg-consent-actions"><button type="button" data-consent="reject">Tout refuser</button><button type="button" data-consent="settings">Personnaliser</button><button type="button" data-consent="accept">Tout accepter</button></div></div>';
    const dialog = document.createElement('dialog'); dialog.id = 'sg-consent-dialog'; dialog.setAttribute('aria-labelledby', 'sg-consent-title');
    dialog.innerHTML = '<h2 id="sg-consent-title">Préférences cookies</h2><p>Les préférences nécessaires au fonctionnement sont toujours actives. Les autres catégories sont facultatives.</p><label><input type="checkbox" checked disabled> Nécessaires</label><label><input type="checkbox" id="sg-consent-analytics"> Mesure d’audience</label><label><input type="checkbox" id="sg-consent-marketing"> Publicité et personnalisation publicitaire</label><p>Votre choix est conservé pendant 6 mois. Vous pouvez le modifier à tout moment.</p><div class="sg-consent-actions"><button type="button" data-consent="reject">Tout refuser</button><button type="button" data-consent="save">Enregistrer mes choix</button><button type="button" data-consent="close">Fermer</button></div>';
    const manage = document.createElement('button'); manage.type = 'button'; manage.id = 'sg-consent-manage'; manage.textContent = 'Gestion des cookies';
    document.body.append(banner, dialog, manage);
    let opener = null;
    function open() {
      opener = document.activeElement;
      dialog.querySelector('#sg-consent-analytics').checked = !!(choice && choice.analytics);
      dialog.querySelector('#sg-consent-marketing').checked = !!(choice && choice.marketing);
      dialog.showModal();
    }
    function save(analytics, marketing) {
      const previous = choice;
      choice = { version: 2, analytics: analytics, marketing: marketing, time: Date.now() };
      try { localStorage.setItem(KEY, JSON.stringify(choice)); } catch (_) {}
      apply(choice); clearCookies(choice); banner.hidden = true;
      if (!marketing && window.fbq) window.fbq('consent', 'revoke');
      if (dialog.open) dialog.close();
      // Unload already-running third-party tags when a category is withdrawn.
      if (previous && ((previous.analytics && !analytics) || (previous.marketing && !marketing))) location.reload();
    }
    manage.addEventListener('click', open);
    document.addEventListener('click', function (event) {
      const button = event.target.closest('[data-consent]');
      if (!button) return;
      switch (button.dataset.consent) {
        case 'settings': open(); break;
        case 'accept': save(true, true); break;
        case 'reject': save(false, false); break;
        case 'save': save(dialog.querySelector('#sg-consent-analytics').checked, dialog.querySelector('#sg-consent-marketing').checked); break;
        case 'close': dialog.close(); break;
      }
    });
    dialog.addEventListener('close', function () { if (opener) opener.focus(); });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
