/**
 * AUDIT DE VÉRITÉ — Scroll Reveal /le-solaire/
 * Exécute la page et capture l'état réel (fichiers chargés, console, DOM)
 * Usage: node scripts/audit-scroll-reveal.js
 * Prérequis: serveur local sur http://localhost:3000 (npx serve -p 3000)
 */
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const SITE_ROOT = path.resolve(__dirname, '..');
const BASE_URL = process.env.AUDIT_URL || 'http://localhost:3000';
const PAGE_URL = BASE_URL + '/le-solaire/';

async function runAudit() {
  const report = {
    timestamp: new Date().toISOString(),
    pageUrl: PAGE_URL,
    filesLoaded: [],
    networkRequests: [],
    consoleLogs: [],
    consoleErrors: [],
    consoleWarnings: [],
    sectionsFound: 0,
    revealsFound: 0,
    revealsWithVisibleClass: 0,
    revealsWithoutVisibleClass: [],
    elementsOK: [],
    elementsKO: [],
    testVeriteResult: null,
    headerLoaded: false,
    scriptTiming: null
  };

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 800 } });
  
  const page = await context.newPage();

  // Capturer les requêtes réseau
  page.on('request', req => {
    const url = req.url();
    if (url.includes('sg-scroll-reveal') || url.includes('sg-animations') || 
        url.includes('le-solaire') || url.includes('header') || url.includes('footer')) {
      report.networkRequests.push({ type: req.resourceType(), url });
    }
  });

  page.on('response', async res => {
    const url = res.url();
    const status = res.status();
    if (url.includes('sg-scroll-reveal') || url.includes('sg-animations')) {
      report.filesLoaded.push({ url, status, ok: res.ok() });
    }
  });

  // Capturer la console
  page.on('console', msg => {
    const text = msg.text();
    const type = msg.type();
    if (type === 'error') report.consoleErrors.push(text);
    else if (type === 'warning') report.consoleWarnings.push(text);
    else if (text.includes('sg-scroll-reveal') || text.includes('sections') || text.includes('reveals')) {
      report.consoleLogs.push(text);
    }
  });

  try {
    const startTime = Date.now();
    await page.goto(PAGE_URL, { waitUntil: 'networkidle', timeout: 15000 });
    report.scriptTiming = { loadMs: Date.now() - startTime };

    // État à 500ms (AVANT fallback 800ms) — fenêtre où éléments peuvent rester invisibles
    await page.waitForTimeout(500);
    const state500ms = await page.evaluate(() => {
      const reveals = document.querySelectorAll('.sg-reveal, .sg-reveal-card');
      let withoutVisible = 0;
      reveals.forEach(el => {
        if (!el.classList.contains('sg-reveal-visible')) withoutVisible++;
      });
      return { total: reveals.length, withoutVisible };
    });
    report.stateAt500ms = state500ms;

    // Attendre les fallbacks (800ms + 1200ms) et le header async
    await page.waitForTimeout(2000);

    // Récupérer les comptages réels
    const counts = await page.evaluate(() => {
      const reveals = document.querySelectorAll('.sg-reveal, .sg-reveal-card');
      const sections = document.querySelectorAll('.sg-section, .sg-section-editorial');
      const withVisible = document.querySelectorAll('.sg-reveal-visible');
      const revealsWithoutVisible = [];
      reveals.forEach((el, i) => {
        if (!el.classList.contains('sg-reveal-visible')) {
          const rect = el.getBoundingClientRect();
          const style = window.getComputedStyle(el);
          revealsWithoutVisible.push({
            index: i,
            tag: el.tagName,
            classes: el.className,
            rectTop: Math.round(rect.top),
            innerHeight: window.innerHeight,
            opacity: style.opacity,
            visibility: style.visibility,
            display: style.display,
            transform: style.transform
          });
        }
      });
      return {
        sectionsCount: sections.length,
        revealsCount: reveals.length,
        withVisibleCount: document.querySelectorAll('.sg-reveal.sg-reveal-visible, .sg-reveal-card.sg-reveal-visible').length,
        revealsWithoutVisible,
        headerPlaceholder: document.getElementById('header-placeholder')?.innerHTML?.length || 0
      };
    });

    report.sectionsFound = counts.sectionsCount;
    report.revealsFound = counts.revealsCount;
    report.revealsWithVisibleClass = counts.withVisibleCount;
    report.revealsWithoutVisibleClass = counts.revealsWithoutVisible;
    report.headerLoaded = counts.headerPlaceholder > 100;

    // Exemple élément OK et KO
    if (counts.revealsWithoutVisible.length > 0) {
      report.elementsKO = counts.revealsWithoutVisible.slice(0, 3);
    }
    const okSample = await page.evaluate(() => {
      const visible = document.querySelector('.sg-reveal.sg-reveal-visible, .sg-reveal-card.sg-reveal-visible');
      if (!visible) return null;
      const style = window.getComputedStyle(visible);
      return { tag: visible.tagName, classes: visible.className, opacity: style.opacity };
    });
    report.elementsOK = okSample;

    // TEST DE VÉRITÉ
    await page.evaluate(() => {
      document.querySelectorAll('.sg-reveal, .sg-reveal-card').forEach(el => el.classList.add('sg-reveal-visible'));
    });
    await page.waitForTimeout(500);

    const afterTest = await page.evaluate(() => {
      const reveals = document.querySelectorAll('.sg-reveal, .sg-reveal-card');
      let stillInvisible = 0;
      reveals.forEach(el => {
        const style = window.getComputedStyle(el);
        if (parseFloat(style.opacity) < 0.5) stillInvisible++;
      });
      return { total: reveals.length, stillInvisible };
    });

    report.testVeriteResult = afterTest;

  } catch (err) {
    report.error = err.message;
  } finally {
    await browser.close();
  }

  return report;
}

runAudit().then(report => {
  const outputPath = path.join(SITE_ROOT, 'docs', 'AUDIT_VERITE_SCROLL_REVEAL.md');
  const md = `# AUDIT DE VÉRITÉ — SCROLL REVEAL /le-solaire/

**Date :** ${report.timestamp}
**URL testée :** ${report.pageUrl}

---

## 1. FICHIERS RÉELLEMENT CHARGÉS

${report.filesLoaded.length ? report.filesLoaded.map(f => `- ${f.url} — Status: ${f.status} ${f.ok ? '✅' : '❌'}`).join('\n') : '- Aucun fichier scroll-reveal/animation capturé (page file://)'}

### Requêtes réseau pertinentes
${report.networkRequests.map(r => `- [${r.type}] ${r.url}`).join('\n') || '- N/A (page file://)'}

---

## 2. ERREURS ET LOGS CONSOLE

### Erreurs
${report.consoleErrors.length ? report.consoleErrors.map(e => `- ${e}`).join('\n') : '- Aucune erreur'}

### Warnings
${report.consoleWarnings.length ? report.consoleWarnings.map(w => `- ${w}`).join('\n') : '- Aucun warning'}

### Logs scroll-reveal
${report.consoleLogs.length ? report.consoleLogs.map(l => `- ${l}`).join('\n') : '- Aucun log scroll-reveal capturé'}

---

## 3. NOMBRES RÉELS

| Métrique | Valeur |
|----------|--------|
| Sections trouvées | ${report.sectionsFound} |
| Reveals trouvés | ${report.revealsFound} |
| Reveals avec sg-reveal-visible | ${report.revealsWithVisibleClass} |
| Reveals SANS sg-reveal-visible | ${report.revealsWithoutVisibleClass?.length || 0} |
| Header chargé (async) | ${report.headerLoaded ? 'Oui' : 'Non'} |
| Temps chargement | ${report.scriptTiming?.loadMs || 'N/A'} ms |
| **À 500ms** (avant fallback 800ms) | ${report.stateAt500ms?.withoutVisible ?? 'N/A'} reveals SANS sg-reveal-visible |

---

## 4. EXEMPLE ÉLÉMENT OK

${report.elementsOK ? JSON.stringify(report.elementsOK, null, 2) : 'Aucun'}

---

## 5. EXEMPLES ÉLÉMENTS KO (sans sg-reveal-visible après 2s)

${report.elementsKO?.length ? report.elementsKO.map((e, i) => `
### Élément KO #${i + 1}
- Tag: \`${e.tag}\`
- Classes: \`${e.classes}\`
- rect.top: ${e.rectTop} (viewport: ${e.innerHeight})
- opacity: ${e.opacity}
- visibility: ${e.visibility}
- display: ${e.display}
- transform: ${e.transform}
`).join('\n') : 'Aucun élément KO'}

---

## 6. TEST DE VÉRITÉ

Après \`document.querySelectorAll('.sg-reveal, .sg-reveal-card').forEach(el => el.classList.add('sg-reveal-visible'))\` :

| Résultat | Valeur |
|----------|--------|
| Total reveals | ${report.testVeriteResult?.total || 'N/A'} |
| Restés invisibles (opacity < 0.5) | ${report.testVeriteResult?.stillInvisible ?? 'N/A'} |

**Interprétation :**
- Si tout réapparaît (stillInvisible = 0) → **Problème JS / déclenchement**
- Si certains restent invisibles → **Problème CSS / structure / override**

---

## 7. DIAGNOSTIC

${report.error ? `**Erreur exécution :** ${report.error}` : ''}

### Cause probable
${report.testVeriteResult?.stillInvisible > 0 
  ? '**CSS / override** — Des éléments restent invisibles même avec la classe sg-reveal-visible. Vérifier les règles CSS qui overrident opacity/visibility/display.'
  : report.stateAt500ms?.withoutVisible > 0
    ? '**JS / timing** — Entre le chargement et 800ms, des éléments restent invisibles. Fenêtre de ~500-800ms où le contenu peut paraître cassé avant le fallback.'
    : report.revealsWithoutVisibleClass?.length > 0
      ? '**JS / déclenchement** — Le script ne pose pas la classe à temps. Problème de timing, observer, ou fallback.'
      : '**Système fonctionnel** — Tous les éléments reçoivent sg-reveal-visible (après fallbacks).'}

### Vérification contenu chargé vs repo
Les fichiers servis par le serveur local proviennent du répertoire du projet. En production, vérifier qu'aucun cache CDN/serveur ne sert une ancienne version de sg-scroll-reveal.js ou sg-animations.css.
`;

  fs.writeFileSync(outputPath, md, 'utf8');
  console.log('Rapport écrit:', outputPath);
  console.log(JSON.stringify(report, null, 2));
});
