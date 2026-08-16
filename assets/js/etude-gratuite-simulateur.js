/**
 * Simulateur étude gratuite - Solarglobe
 * Moteur isolé, CRM-ready, maintenable
 */
(function () {
  'use strict';

  const CONFIG = {
    apiKey: '332e9049494d42e09da67425057cf1b2',
    autocompleteUrl: 'https://api.geoapify.com/v1/geocode/autocomplete',
    debounceMs: 220,
    formAction: 'https://formsubmit.co/direction.solarglobe@gmail.com',
    formNext: '/merci/',
    stepVideos: [
      '/assets/videos/step1-carte.mp4',
      '/assets/videos/step2-maison.mp4',
      '/assets/videos/step3-orientation.mp4',
      '/assets/videos/step4-inclinaison.mp4',
      '/assets/videos/step5-ombres.mp4',
      '/assets/videos/step6-panneaux.mp4',
      '/assets/videos/step7-success.mp4'
    ],
    images: {
      longi: '/assets/images/final-longi.webp',
      aiko: '/assets/images/logo/aiko-logo.png'
    }
  };

  let state = {
    address: null,
    lat: null,
    lon: null,
    surface: 30,
    orientation: 'sud',
    inclinaison: 30,
    obstacles: 'non',
    panneaux: 'longi',
    estimation: null,
    contact: {
      nom: '',
      prenom: '',
      email: '',
      telephone: ''
    }
  };

  function computeEstimation(s) {
    const surface = Math.max(10, Math.min(120, Number(s.surface) || 30));
    let kwc = surface / 5;
    kwc = Math.max(2, Math.min(12, kwc));
    kwc = Math.round(kwc * 10) / 10;

    const orientMap = {
      sud: 1.0,
      'sud-est': 0.9,
      'sud-ouest': 0.9,
      est: 0.8,
      ouest: 0.8,
      'nord-est': 0.7,
      'nord-ouest': 0.7,
      nord: 0.6,
      plat: 0.85
    };
    const coefOrientation = orientMap[s.orientation] ?? 1.0;

    const incl = Number(s.inclinaison) || 30;
    let coefInclinaison = 0.75;
    if (incl >= 20 && incl <= 40) coefInclinaison = 1.0;
    else if ((incl >= 10 && incl < 20) || (incl > 40 && incl <= 50)) coefInclinaison = 0.9;

    const obstacleMap = { non: 1.0, incertain: 0.9, oui: 0.75 };
    const coefOmbrage = obstacleMap[s.obstacles] ?? 1.0;

    let production = kwc * 1100 * coefOrientation * coefInclinaison * coefOmbrage;
    production = Math.round(production / 100) * 100;
    production = Math.max(0, production);

    let economies = production * 0.22 * 0.7;
    economies = Math.round(economies / 50) * 50;
    economies = Math.max(0, economies);

    return { kwc, production, economies };
  }

  let currentStep = 0;
  let debounceTimer = null;
  let root = null;

  const STEP_LABELS = [
    'Adresse du projet',
    'Surface de toiture disponible',
    'Orientation du toit',
    'Inclinaison de la toiture',
    'Ombres et obstacles',
    'Technologie étudiée',
    'Vos coordonnées'
  ];

  const STEP_SUBTITLES = [
    'Adresse utilisée uniquement pour analyser le potentiel solaire de votre toiture.',
    'À titre indicatif : une maison individuelle dispose généralement de 30 à 50 m² exploitables.',
    'Même une orientation imparfaite peut être optimisée par un bon dimensionnement.',
    'Une inclinaison comprise entre 25° et 35° est généralement optimale en France.',
    'Les ombres peuvent être prises en compte lors du dimensionnement de l\'installation.',
    'Les deux technologies sont compatibles avec une installation performante et durable.',
    ''
  ];

  const steps = [
    {
      id: 'address',
      render: () => `
        <div class="sim-field">
          <span class="sim-label">Commencez à taper votre adresse</span>
          <div class="sim-autocomplete-wrap">
            <input id="etude-address-input" type="text" class="sim-input"
              placeholder="Ex : 8 avenue des Champs-Élysées, Paris"
              autocomplete="off" aria-autocomplete="list" aria-controls="etude-suggestions" />
            <div id="etude-suggestions" class="sim-suggestions" style="display:none;" role="listbox"></div>
          </div>
          <button id="etude-gps-btn" type="button" class="sim-gps-btn">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
              <path d="M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8zm9.94 3h-2.02a8.06 8.06 0 0 0-1.65-3.97l1.43-1.43a.996.996 0 1 0-1.41-1.41l-1.43 1.43A8.06 8.06 0 0 0 13 2.08V.06a1 1 0 1 0-2 0v2.02a8.06 8.06 0 0 0-3.97 1.65L5.6 2.3a.996.996 0 1 0-1.41 1.41l1.43 1.43A8.06 8.06 0 0 0 2.08 11H.06a1 1 0 1 0 0 2h2.02a8.06 8.06 0 0 0 1.65 3.97l-1.43 1.43a.996.996 0 1 0 1.41 1.41l1.43-1.43A8.06 8.06 0 0 0 11 21.92v2.02a1 1 0 1 0 2 0v-2.02a8.06 8.06 0 0 0 3.97-1.65l1.43 1.43a.996.996 0 1 0 1.41-1.41l-1.43-1.43A8.06 8.06 0 0 0 21.92 13h2.02a1 1 0 1 0 0-2z"/>
            </svg>
            Localiser automatiquement
          </button>
          <p id="etude-gps-msg" class="sim-gps-msg" style="display:none;"></p>
        </div>
      `,
      onMount: initAddressStep
    },
    {
      id: 'surface',
      render: () => `
        <div class="sim-field">
          <span class="sim-label">Surface exploitable (m²)</span>
          <input id="etude-surface-slider" type="range" min="10" max="120" value="${state.surface}"
            class="sim-slider" />
          <span id="etude-surface-value" class="sim-slider-value">${state.surface} m²</span>
        </div>
      `,
      onMount: initSurfaceStep
    },
    {
      id: 'orientation',
      render: () => `
        <div class="sim-choice-grid sim-choice-grid--3">
          <button type="button" class="sim-choice-btn" data-orient="sud">Sud</button>
          <button type="button" class="sim-choice-btn" data-orient="sud-est">Sud-Est</button>
          <button type="button" class="sim-choice-btn" data-orient="sud-ouest">Sud-Ouest</button>
          <button type="button" class="sim-choice-btn" data-orient="est">Est</button>
          <button type="button" class="sim-choice-btn" data-orient="ouest">Ouest</button>
          <button type="button" class="sim-choice-btn" data-orient="nord-est">Nord-Est</button>
          <button type="button" class="sim-choice-btn" data-orient="nord-ouest">Nord-Ouest</button>
          <button type="button" class="sim-choice-btn" data-orient="nord">Nord</button>
          <button type="button" class="sim-choice-btn" data-orient="plat">Toit plat</button>
        </div>
      `,
      onMount: initOrientationStep
    },
    {
      id: 'inclinaison',
      render: () => {
        const disabled = state.orientation === 'plat';
        const val = disabled ? 0 : state.inclinaison;
        return `
        <div class="sim-field">
          <span class="sim-label">Inclinaison de la toiture</span>
          <input id="etude-inclinaison-slider" type="range" min="0" max="45" step="1" value="${val}"
            class="sim-slider" ${disabled ? 'disabled' : ''} />
          <span id="etude-inclinaison-value" class="sim-slider-value">${val === 0 ? 'Toit plat' : val + '°'}</span>
        </div>
      `;
    },
    onMount: initInclinaisonStep
    },
    {
      id: 'obstacles',
      render: () => `
        <div class="sim-choice-grid sim-choice-grid--3">
          <button type="button" class="sim-choice-btn" data-ombre="non">Non</button>
          <button type="button" class="sim-choice-btn" data-ombre="oui">Oui</button>
          <button type="button" class="sim-choice-btn" data-ombre="incertain">Je ne sais pas</button>
        </div>
      `,
      onMount: initObstaclesStep
    },
    {
      id: 'panneaux',
      render: () => `
        <div class="sim-choice-grid sim-choice-grid--2">
          <button type="button" class="sim-choice-btn" data-pan="longi">Longi Hi-MO 10 Explorer</button>
          <button type="button" class="sim-choice-btn" data-pan="aiko">Aiko Neostar 2S+</button>
        </div>
      `,
      onMount: initPanneauxStep
    },
    {
      id: 'contact',
      render: () => {
        const est = computeEstimation(state);
        state.estimation = est;
        const orientLabels = { sud: 'Sud', 'sud-est': 'Sud-Est', 'sud-ouest': 'Sud-Ouest', est: 'Est', ouest: 'Ouest', 'nord-est': 'Nord-Est', 'nord-ouest': 'Nord-Ouest', nord: 'Nord', plat: 'Toit plat' };
        const ombreLabels = { non: 'Aucune', incertain: 'Légères', oui: 'Importantes' };
        const orient = orientLabels[state.orientation] || state.orientation;
        const ombres = ombreLabels[state.obstacles] || state.obstacles;
        const incl = state.orientation === 'plat' ? 'Toit plat' : state.inclinaison + '°';
        const economies20 = Math.round((est.economies * 20) / 100) * 100;
        return `
        <div id="etude-result-block" class="sim-result">
          <div class="sim-result__header">
            <h3 class="sim-result__title">Votre étude solaire est prête</h3>
            <p class="sim-result__subtitle">Voici une estimation indicative basée sur votre toiture et votre configuration. Elle sera affinée avec SolarGlobe selon votre consommation et vos usages.</p>
          </div>
          <p class="sim-result__hook">Production annuelle estimée : <strong>${est.production.toLocaleString('fr-FR')} kWh</strong></p>
          <div class="sim-result__grid">
            <div class="sim-result__summary">
              <h4 class="sim-result__card-title">Résumé du projet</h4>
              <ul class="sim-result__list">
                <li><span class="sim-result__label">Surface utilisée</span> <span class="sim-result__value">${state.surface} m²</span></li>
                <li><span class="sim-result__label">Orientation</span> <span class="sim-result__value">${orient}</span></li>
                <li><span class="sim-result__label">Inclinaison</span> <span class="sim-result__value">${incl}</span></li>
                <li><span class="sim-result__label">Ensoleillement</span> <span class="sim-result__value">${ombres}</span></li>
              </ul>
            </div>
            <div class="sim-result__projection">
              <h4 class="sim-result__card-title">Estimation</h4>
              <div class="sim-result__stat">
                <span class="sim-result__stat-value">${est.kwc}</span>
                <span class="sim-result__stat-unit">kWc</span>
                <span class="sim-result__stat-label">Puissance estimée</span>
              </div>
              <div class="sim-result__stat">
                <span class="sim-result__stat-value">${est.production.toLocaleString('fr-FR')}</span>
                <span class="sim-result__stat-unit">kWh/an</span>
                <span class="sim-result__stat-label">Production annuelle</span>
              </div>
              <div class="sim-result__stat sim-result__stat--highlight">
                <span class="sim-result__stat-value">${est.economies.toLocaleString('fr-FR')} €</span>
                <span class="sim-result__stat-unit">d'économies annuelles indicatives</span>
                <span class="sim-result__stat-sublabel">Projection indicative sur 20 ans : ${economies20.toLocaleString('fr-FR')} €</span>
              </div>
            </div>
          </div>
          <div class="sim-result__projection-future">
            <p>Cette projection dépendra de votre consommation, de l'autoconsommation réelle, de la production et de l'évolution du prix de l'électricité.</p>
          </div>
          <div class="sim-result__benefits">
            <ul class="sim-result__benefits-list">
              <li>Réduction possible de votre facture</li>
              <li>Valorisation de votre bien</li>
              <li>Scénario comparé face à l'évolution du prix de l'électricité</li>
              <li>Projet optimisé selon votre toiture</li>
            </ul>
          </div>
          <div class="sim-result__cta">
            <div class="sim-result__form-intro">
              <h4 class="sim-result__form-intro-title">Finalisez votre étude personnalisée</h4>
              <p class="sim-result__form-intro-text">SolarGlobe analyse votre projet en détail et vous transmet une étude adaptée à votre maison.</p>
              <p class="sim-result__form-intro-sub">Sans engagement — réponse sous 24 à 48h</p>
            </div>
            <form id="etude-contact-form" class="sim-result__form" action="${CONFIG.formAction}" method="POST" autocomplete="off" novalidate>
              <input type="hidden" name="_subject" value="Nouvelle demande d'étude solaire via le simulateur Solarglobe" />
              <input type="hidden" name="_template" value="table" />
              <input type="hidden" name="_captcha" value="false" />
              <input type="hidden" name="_next" value="${CONFIG.formNext}" />
              <input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off" />
              <div class="sim-form-grid">
                <div class="sim-field">
                  <label class="sim-label" for="form-prenom">Prénom</label>
                  <input id="form-prenom" required name="prenom" type="text" placeholder="Votre prénom" class="sim-input" autocomplete="given-name" />
                  <span class="sim-form-error" id="err-prenom" role="alert"></span>
                </div>
                <div class="sim-field">
                  <label class="sim-label" for="form-nom">Nom</label>
                  <input id="form-nom" required name="nom" type="text" placeholder="Votre nom" class="sim-input" autocomplete="family-name" />
                  <span class="sim-form-error" id="err-nom" role="alert"></span>
                </div>
                <div class="sim-field">
                  <label class="sim-label" for="form-email">Email</label>
                  <input id="form-email" required name="email" type="email" placeholder="votre@email.fr" class="sim-input" autocomplete="email" />
                  <span class="sim-form-error" id="err-email" role="alert"></span>
                </div>
                <div class="sim-field">
                  <label class="sim-label" for="form-tel">Téléphone</label>
                  <input id="form-tel" required name="tel" type="tel" placeholder="06 12 34 56 78" class="sim-input" autocomplete="tel" />
                  <span class="sim-form-error" id="err-tel" role="alert"></span>
                </div>
              </div>
              <ul class="sim-result__form-reassurance">
                <li>Vos données restent confidentielles</li>
                <li>Aucun démarchage abusif</li>
                <li>Étude gratuite et sans engagement</li>
              </ul>
              <p class="sim-result__form-rgpd">
                En soumettant ce formulaire, vous acceptez d'être recontacté dans le cadre de votre étude solaire.
                <a href="/politique-de-confidentialite/" class="sim-result__form-rgpd-link" target="_blank" rel="noopener">Politique de confidentialité</a>
              </p>
              <input type="hidden" name="Adresse" id="formAdresse" />
              <input type="hidden" name="Latitude" id="formLat" />
              <input type="hidden" name="Longitude" id="formLon" />
              <input type="hidden" name="Surface" id="formSurface" />
              <input type="hidden" name="Orientation" id="formOrientation" />
              <input type="hidden" name="Inclinaison" id="formInclinaison" />
              <input type="hidden" name="Obstacles" id="formObstacles" />
              <input type="hidden" name="Panneaux" id="formPanneaux" />
              <div class="sim-result__submit-wrap">
                <button type="submit" class="sim-result__submit" id="etude-form-submit" disabled>
                  <span class="sim-result__submit-text">Faire vérifier mon projet solaire</span>
                  <span class="sim-result__submit-loader" aria-hidden="true"></span>
                </button>
                <p class="sim-result__submit-hint">Réponse sous 24 à 48h</p>
              </div>
            </form>
          </div>
        </div>
      `;
      },
      onMount: initContactStep
    }
  ];

  function syncFormFinal() {
    const form = root.querySelector('#etude-contact-form');
    if (!form) return;
    const set = (id, val) => {
      const el = form.querySelector('#' + id);
      if (el) el.value = val !== null && val !== undefined ? String(val) : '';
    };
    set('formAdresse', state.address);
    set('formLat', state.lat);
    set('formLon', state.lon);
    set('formSurface', state.surface);
    set('formOrientation', state.orientation);
    set('formInclinaison', state.inclinaison);
    set('formObstacles', state.obstacles);
    set('formPanneaux', state.panneaux);
  }

  function updateIllustration(stepIdx) {
    const videoEl = root.querySelector('#etude-sim-video');
    const fallbackEl = root.querySelector('#etude-sim-fallback');
    if (!videoEl) return;
    const src = CONFIG.stepVideos[stepIdx] || CONFIG.stepVideos[0];
    videoEl.src = src;
    videoEl.style.display = 'block';
    if (fallbackEl) fallbackEl.style.display = 'none';
    videoEl.onerror = function () {
      videoEl.style.display = 'none';
      if (fallbackEl) fallbackEl.style.display = 'flex';
    };
    videoEl.load().catch(function () {});
    videoEl.play().catch(function () {});
  }

  function renderStep() {
    if (!root) return;
    const progressEl = root.querySelector('#sim-progress');
    const stepEl = root.querySelector('#sim-step');
    const navEl = root.querySelector('#sim-nav');
    const bottomEl = root.querySelector('#simulator-bottom');
    if (!progressEl || !stepEl || !navEl) return;

    const percent = Math.round(((currentStep + 1) / steps.length) * 100);
    progressEl.innerHTML = `
      <div class="etude-sim__progress-label">Votre projet</div>
      <div class="etude-sim__progress-step" aria-live="polite">Étape ${currentStep + 1} sur ${steps.length}</div>
      <div class="etude-sim__progress-bar">
        <div class="etude-sim__progress-fill" style="width:${percent}%"></div>
      </div>
      <p class="etude-sim__reassurance">Données confidentielles · aucune revente · sans engagement</p>
    `;

    const step = steps[currentStep];
    if (!step) return;
    const isContactStep = currentStep === steps.length - 1;

    if (isContactStep && bottomEl) {
      bottomEl.innerHTML = step.render();
      bottomEl.hidden = false;
      bottomEl.removeAttribute('aria-hidden');
      stepEl.innerHTML = `
        <div class="sim-step-ui">
          <div class="sim-step-header">
            <h3 class="sim-step-title">Vos coordonnées</h3>
            <p class="sim-step-sub">Votre étude est prête. Remplissez le formulaire ci-dessous pour recevoir votre étude personnalisée.</p>
          </div>
        </div>
      `;
    } else {
      if (bottomEl) {
        bottomEl.innerHTML = '';
        bottomEl.hidden = true;
        bottomEl.setAttribute('aria-hidden', 'true');
      }
      const sub = STEP_SUBTITLES[currentStep] || '';
      stepEl.innerHTML = `
        <div class="sim-step-ui">
          <div class="sim-step-header">
            <h3 class="sim-step-title">${STEP_LABELS[currentStep]}</h3>
            ${sub ? `<p class="sim-step-sub">${sub}</p>` : ''}
          </div>
          <div class="sim-step-body">${step.render()}</div>
        </div>
      `;
    }

    navEl.innerHTML = `
      ${currentStep > 0 ? '<button id="etude-prev-btn" type="button" class="etude-sim__btn etude-sim__btn--prev">Retour</button>' : '<span></span>'}
      ${currentStep < steps.length - 1 ? '<button id="etude-next-btn" type="button" class="etude-sim__btn etude-sim__btn--next">Continuer</button>' : '<span></span>'}
    `;

    step.onMount && step.onMount();

    const nextBtn = root.querySelector('#etude-next-btn');
    const prevBtn = root.querySelector('#etude-prev-btn');
    if (nextBtn) nextBtn.addEventListener('click', nextStep);
    if (prevBtn) prevBtn.addEventListener('click', prevStep);

    updateIllustration(currentStep);

    if (window.dataLayer) {
      window.dataLayer.push({
        event: 'simulateur_step_view',
        step_index: currentStep + 1,
        step_label: STEP_LABELS[currentStep]
      });
    }
  }

  function nextStep() {
    if (currentStep < steps.length - 1) {
      currentStep++;
      renderStep();
    }
  }

  function prevStep() {
    if (currentStep > 0) {
      currentStep--;
      renderStep();
    }
  }

  function initAddressStep() {
    const input = root.querySelector('#etude-address-input');
    const suggestionsBox = root.querySelector('#etude-suggestions');
    const gpsBtn = root.querySelector('#etude-gps-btn');
    const gpsMsg = root.querySelector('#etude-gps-msg');
    if (!input || !suggestionsBox) return;

    input.focus();

    input.addEventListener('input', () => {
      const query = input.value.trim();
      clearTimeout(debounceTimer);
      suggestionsBox.style.display = 'none';
      suggestionsBox.innerHTML = '';

      if (query.length < 3) return;

      debounceTimer = setTimeout(async () => {
        try {
          const url = `${CONFIG.autocompleteUrl}?text=${encodeURIComponent(query)}&lang=fr&limit=6&format=json&apiKey=${CONFIG.apiKey}`;
          const res = await fetch(url);
          if (!res.ok) return;
          const dataApi = await res.json();
          const results = dataApi?.results || [];
          if (!results.length) return;

          results.forEach((item) => {
            const div = document.createElement('div');
            div.className = 'sim-suggestion';
            div.textContent = item.formatted || '';
            div.setAttribute('role', 'option');
            div.addEventListener('mousedown', (e) => {
              e.preventDefault();
              input.value = item.formatted || '';
              state.address = item.formatted || '';
              state.lat = item.lat ?? item.properties?.lat ?? null;
              state.lon = item.lon ?? item.properties?.lon ?? null;
              suggestionsBox.style.display = 'none';
              suggestionsBox.innerHTML = '';
              updateIllustration(currentStep);
            });
            suggestionsBox.appendChild(div);
          });
          suggestionsBox.style.display = 'block';
        } catch (err) {
          suggestionsBox.style.display = 'none';
        }
      }, CONFIG.debounceMs);
    });

    document.addEventListener('mousedown', (e) => {
      if (!suggestionsBox.contains(e.target) && e.target !== input) {
        suggestionsBox.style.display = 'none';
      }
    });

    if (gpsBtn && gpsMsg) {
      gpsBtn.addEventListener('click', () => {
        if (!navigator.geolocation) {
          gpsMsg.textContent = 'La géolocalisation n\'est pas supportée par votre navigateur.';
          gpsMsg.className = 'sim-gps-msg sim-gps-msg--error';
          gpsMsg.style.display = 'block';
          return;
        }
        gpsMsg.style.display = 'none';
        navigator.geolocation.getCurrentPosition(
          (pos) => {
            state.lat = pos.coords.latitude;
            state.lon = pos.coords.longitude;
            input.value = `Coordonnées détectées (${state.lat.toFixed(4)}, ${state.lon.toFixed(4)})`;
            state.address = 'Localisation GPS';
            gpsMsg.textContent = 'Position détectée.';
            gpsMsg.className = 'sim-gps-msg sim-gps-msg--success';
            gpsMsg.style.display = 'block';
            updateIllustration(currentStep);
          },
          () => {
            gpsMsg.textContent = 'Impossible de détecter la position. Vérifiez les autorisations ou saisissez votre adresse manuellement.';
            gpsMsg.className = 'sim-gps-msg sim-gps-msg--error';
            gpsMsg.style.display = 'block';
          },
          { enableHighAccuracy: false, timeout: 5000 }
        );
      });
    }
  }

  function initSurfaceStep() {
    const slider = root.querySelector('#etude-surface-slider');
    const valueText = root.querySelector('#etude-surface-value');
    if (!slider || !valueText) return;
    slider.addEventListener('input', () => {
      const v = parseInt(slider.value, 10);
      state.surface = v;
      valueText.textContent = v + ' m²';
    });
    slider.focus();
  }

  function initOrientationStep() {
    root.querySelectorAll('.sim-choice-btn[data-orient]').forEach((b) => {
      b.addEventListener('click', () => {
        state.orientation = b.getAttribute('data-orient');
        nextStep();
      });
    });
  }

  function initInclinaisonStep() {
    const slider = root.querySelector('#etude-inclinaison-slider');
    const valueText = root.querySelector('#etude-inclinaison-value');
    if (!slider || !valueText) return;
    if (state.orientation === 'plat') {
      state.inclinaison = 0;
    }
    slider.addEventListener('input', () => {
      const v = parseInt(slider.value, 10);
      state.inclinaison = v;
      valueText.textContent = v === 0 ? 'Toit plat' : v + '°';
    });
    slider.focus();
  }

  function initObstaclesStep() {
    root.querySelectorAll('.sim-choice-btn[data-ombre]').forEach((b) => {
      b.addEventListener('click', () => {
        state.obstacles = b.getAttribute('data-ombre');
        nextStep();
      });
    });
  }

  function initPanneauxStep() {
    root.querySelectorAll('.sim-choice-btn[data-pan]').forEach((b) => {
      b.addEventListener('click', () => {
        state.panneaux = b.getAttribute('data-pan');
        nextStep();
      });
    });
  }

  function isValidEmail(val) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(String(val).trim());
  }

  function updateFormSubmitState() {
    const form = root.querySelector('#etude-contact-form');
    const btn = root.querySelector('#etude-form-submit');
    if (!form || !btn) return;
    const prenom = (form.querySelector('[name="prenom"]') || {}).value.trim();
    const nom = (form.querySelector('[name="nom"]') || {}).value.trim();
    const email = (form.querySelector('[name="email"]') || {}).value.trim();
    const tel = (form.querySelector('[name="tel"]') || {}).value.trim();
    const allFilled = prenom && nom && email && tel && isValidEmail(email);
    btn.disabled = !allFilled;
  }

  function showFieldError(id, msg) {
    const el = root.querySelector('#err-' + id);
    const input = root.querySelector('#form-' + id);
    if (el) el.textContent = msg || '';
    if (input) input.classList.toggle('sim-input--error', !!msg);
  }

  function validateForm() {
    let valid = true;
    const form = root.querySelector('#etude-contact-form');
    if (!form) return false;
    const prenom = (form.querySelector('[name="prenom"]') || {}).value.trim();
    const nom = (form.querySelector('[name="nom"]') || {}).value.trim();
    const email = (form.querySelector('[name="email"]') || {}).value.trim();
    const tel = (form.querySelector('[name="tel"]') || {}).value.trim();

    showFieldError('prenom', '');
    showFieldError('nom', '');
    showFieldError('email', '');
    showFieldError('tel', '');

    if (!prenom) {
      showFieldError('prenom', 'Merci de renseigner votre prénom');
      valid = false;
    }
    if (!nom) {
      showFieldError('nom', 'Merci de renseigner votre nom');
      valid = false;
    }
    if (!email) {
      showFieldError('email', 'Merci de renseigner votre email');
      valid = false;
    } else if (!isValidEmail(email)) {
      showFieldError('email', 'Veuillez saisir une adresse email valide');
      valid = false;
    }
    if (!tel) {
      showFieldError('tel', 'Merci de renseigner votre téléphone');
      valid = false;
    }
    return valid;
  }

  function initContactStep() {
    syncFormFinal();
    const form = root.querySelector('#etude-contact-form');
    if (!form) return;

    const inputs = form.querySelectorAll('.sim-input');
    const btn = root.querySelector('#etude-form-submit');

    inputs.forEach((inp) => {
      inp.addEventListener('input', () => {
        showFieldError(inp.id.replace('form-', ''), '');
        updateFormSubmitState();
      });
      inp.addEventListener('blur', () => {
        const id = inp.id.replace('form-', '');
        const val = inp.value.trim();
        if (val && id === 'email' && !isValidEmail(val)) {
          showFieldError(id, 'Veuillez saisir une adresse email valide');
        } else if (!val && inp.hasAttribute('required')) {
          showFieldError(id, '');
        }
      });
    });

    form.addEventListener('submit', (e) => {
      syncFormFinal();
      if (btn && btn.classList.contains('sim-result__submit--loading')) {
        e.preventDefault();
        return;
      }
      if (!validateForm()) {
        e.preventDefault();
        return;
      }
      if (btn) {
        btn.disabled = true;
        btn.classList.add('sim-result__submit--loading');
      }
    });

    updateFormSubmitState();
  }

  function initEtudeGratuiteSimulateur() {
    console.log('SIMULATEUR INIT OK');
    root = document.getElementById('etude-app');
    if (!root) {
      console.error('SIMULATEUR: #etude-app introuvable');
      return;
    }

    const mediaEl = root.querySelector('.simulator-media');
    const progressEl = root.querySelector('#sim-progress');
    const stepEl = root.querySelector('#sim-step');
    const navEl = root.querySelector('#sim-nav');
    if (!mediaEl || !progressEl || !stepEl || !navEl) {
      console.error('SIMULATEUR: éléments manquants', { mediaEl: !!mediaEl, progressEl: !!progressEl, stepEl: !!stepEl, navEl: !!navEl });
      return;
    }

    mediaEl.innerHTML = `
      <video id="etude-sim-video" autoplay muted loop playsinline preload="metadata"
        style="max-height:340px;">
      </video>
      <div id="etude-sim-fallback" class="etude-sim__media-fallback" style="display:none;">Illustration</div>
    `;

    currentStep = 0;
    renderStep();
  }

  window.initEtudeGratuiteSimulateur = initEtudeGratuiteSimulateur;

  function run() {
    if (document.getElementById('etude-app') && typeof initEtudeGratuiteSimulateur === 'function') {
      initEtudeGratuiteSimulateur();
    }
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run);
  } else {
    run();
  }
})();
