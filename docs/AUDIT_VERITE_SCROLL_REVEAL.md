# AUDIT DE VÉRITÉ — SCROLL REVEAL /le-solaire/

**Date :** 2026-03-14T00:05:36.617Z
**URL testée :** http://localhost:3000/le-solaire/

---

## 1. FICHIERS RÉELLEMENT CHARGÉS

- http://localhost:3000/assets/css/sg-animations.css — Status: 200 ✅
- http://localhost:3000/assets/js/sg-scroll-reveal.js — Status: 200 ✅

### Requêtes réseau pertinentes
- [document] http://localhost:3000/le-solaire/
- [stylesheet] http://localhost:3000/assets/css/le-solaire-editorial.css
- [stylesheet] http://localhost:3000/assets/css/sg-animations.css
- [stylesheet] http://localhost:3000/assets/css/header-common.css
- [stylesheet] http://localhost:3000/assets/css/footer-common.css
- [script] http://localhost:3000/assets/js/header.js
- [script] http://localhost:3000/assets/js/footer.js
- [script] http://localhost:3000/assets/js/sg-scroll-reveal.js
- [fetch] http://localhost:3000/components/header.html
- [fetch] http://localhost:3000/components/footer.html
- [fetch] http://localhost:3000/components/header
- [fetch] http://localhost:3000/components/footer
- [fetch] https://region1.google-analytics.com/g/collect?v=2&tid=G-V9BGEJKQKZ&gtm=45je63c0h2v9227073979z89227056579za20gzb9227056579zd9227056579&_p=1773446736794&gcd=13l3l3l2l1l1&npa=1&dma_cps=a&dma=1&cid=689121203.1773446737&ul=fr&sr=1280x800&uaa=x86&uab=64&uafvl=Not%253AA-Brand%3B99.0.0.0%7CHeadlessChrome%3B145.0.7632.6%7CChromium%3B145.0.7632.6&uamb=0&uam=&uap=Windows&uapv=19.0.0&uaw=0&are=1&frm=0&pscdl=noapi&_s=1&tag_exp=103116026~103200004~115938466~115938468~116024733~117484252&sid=1773446737&sct=1&seg=0&dl=http%3A%2F%2Flocalhost%2Fle-solaire%2F&dt=Le%20solaire%20photovolta%C3%AFque%20%3A%20comprendre%2C%20produire%20et%20%C3%A9conomiser%20%7C%20Solarglobe&en=page_view&_fv=1&_nsi=1&_ss=1&tfd=511
- [fetch] https://www.google.com/ccm/collect?frm=0&en=page_view&dl=http%3A%2F%2Flocalhost%3A3000%2Fle-solaire%2F&scrsrc=www.googletagmanager.com&rnd=142497607.1773446737&dt=Le%20solaire%20photovolta%C3%AFque%20%3A%20comprendre%2C%20produire%20et%20%C3%A9conomiser%20%7C%20Solarglobe&auid=45156639.1773446737&navt=n&npa=1&gtm=45be63b1v9227074345za200zd9227074345xec&gcd=13l3l3l2l1l1&dma_cps=a&dma=1&tag_exp=103116026~103200004~115616986~115938466~115938469~116024733~117484252&apve=1&apvf=f&apvc=1&tids=AW-17462997481&tid=AW-17462997481&tft=1773446737314&tfd=536

---

## 2. ERREURS ET LOGS CONSOLE

### Erreurs
- Aucune erreur

### Warnings
- cdn.tailwindcss.com should not be used in production. To use Tailwind CSS in production, install it as a PostCSS plugin or use the Tailwind CLI: https://tailwindcss.com/docs/installation

### Logs scroll-reveal
- sg-scroll-reveal: loaded
- sg-scroll-reveal: sections found 13
- sg-scroll-reveal: reveals found 67
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node
- sg-scroll-reveal: section observed JSHandle@node

---

## 3. NOMBRES RÉELS

| Métrique | Valeur |
|----------|--------|
| Sections trouvées | 13 |
| Reveals trouvés | 67 |
| Reveals avec sg-reveal-visible | 67 |
| Reveals SANS sg-reveal-visible | 0 |
| Header chargé (async) | Oui |
| Temps chargement | 1112 ms |
| **À 500ms** (avant fallback 800ms) | 0 reveals SANS sg-reveal-visible |

---

## 4. EXEMPLE ÉLÉMENT OK

{
  "tag": "SPAN",
  "classes": "sg-section-kicker sg-reveal sg-reveal-visible",
  "opacity": "1"
}

---

## 5. EXEMPLES ÉLÉMENTS KO (sans sg-reveal-visible après 2s)

Aucun élément KO

---

## 6. TEST DE VÉRITÉ

Après `document.querySelectorAll('.sg-reveal, .sg-reveal-card').forEach(el => el.classList.add('sg-reveal-visible'))` :

| Résultat | Valeur |
|----------|--------|
| Total reveals | 67 |
| Restés invisibles (opacity < 0.5) | 0 |

**Interprétation :**
- Si tout réapparaît (stillInvisible = 0) → **Problème JS / déclenchement**
- Si certains restent invisibles → **Problème CSS / structure / override**

---

## 7. DIAGNOSTIC



### Cause probable
**Système fonctionnel** — Tous les éléments reçoivent sg-reveal-visible (après fallbacks).

### Vérification contenu chargé vs repo
Les fichiers servis par le serveur local proviennent du répertoire du projet. En production, vérifier qu'aucun cache CDN/serveur ne sert une ancienne version de sg-scroll-reveal.js ou sg-animations.css.

**Version repo actuelle (sg-scroll-reveal.js) :**
- Contient : `sg-scroll-reveal: loaded`, `sections found`, `reveals found`
- Fallbacks : 800ms et 1200ms
- Pas de condition `scrollY < 120`
- threshold: 0.15, rootMargin: -10%

---

## 8. VÉRIFICATION EN PRODUCTION

Si le problème persiste sur https://www.solarglobe.fr/le-solaire/ :

1. **DevTools > Network** : Vérifier que `sg-scroll-reveal.js` et `sg-animations.css` sont chargés (200)
2. **DevTools > Sources** : Ouvrir `sg-scroll-reveal.js` et chercher `sg-scroll-reveal: loaded` — si absent, une ancienne version est servie
3. **Console** : Les logs doivent afficher "sections found 13", "reveals found 67"
4. **Test de vérité** : Exécuter dans la console :
   `document.querySelectorAll('.sg-reveal, .sg-reveal-card').forEach(el => el.classList.add('sg-reveal-visible'))`
   - Si tout réapparaît → problème de déclenchement JS (timing, cache)
   - Si certains restent invisibles → problème CSS ou override

---

## 9. RÉSUMÉ FACTUEL

| Vérification | Résultat localhost |
|--------------|-------------------|
| HTML servi | le-solaire/index.html |
| JS scroll-reveal chargé | ✅ /assets/js/sg-scroll-reveal.js (200) |
| CSS animations chargé | ✅ /assets/css/sg-animations.css (200) |
| Erreurs console | Aucune |
| Sections trouvées | 13 |
| Reveals trouvés | 67 |
| Éléments avec sg-reveal-visible (après 2s) | 67/67 |
| Éléments sans classe à 500ms | 0 |
| Test de vérité (opacity après ajout manuel) | 0 invisibles |
| Header injecté (async) | Oui |

**Conclusion locale :** Le système fonctionne correctement sur localhost. Si le problème persiste en production, la cause est probablement : cache, chemin différent, ou environnement (CDN, minification, etc.).
