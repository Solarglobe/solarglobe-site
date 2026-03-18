# DIAGNOSTIC COMPLET — SYSTÈME SCROLL REVEAL
## Page /le-solaire/

**Date :** 14 mars 2025  
**Objectif :** Analyse exhaustive du système actuel avant toute correction. Comprendre pourquoi le comportement est devenu incohérent (éléments invisibles, script inactif).

---

# 1. VÉRIFICATION DU CHARGEMENT DU SCRIPT

## 1.1 Présence et ordre de chargement

| Fichier | Ligne | Chargé ? | Ordre |
|---------|-------|----------|-------|
| `/assets/js/header.js` | 839 | ✅ Oui | 1 |
| `/assets/js/footer.js` | 896 | ✅ Oui | 2 |
| `/assets/js/sg-scroll-reveal.js` | 897 | ✅ Oui | 3 |
| `/assets/js/sg-counter.js` | 898 | ✅ Oui | 4 |

**Conclusion :** Le script `sg-scroll-reveal.js` est bien présent et chargé en fin de body, après le DOM principal. L'ordre est correct : scroll-reveal avant sg-counter.

## 1.2 Point d'exécution

Le script utilise une IIFE qui s'exécute :
- Si `document.readyState === 'loading'` → écoute `DOMContentLoaded`
- Sinon → exécution immédiate (`run()`)

**Risque potentiel :** Si `header.js` ou `footer.js` injecte du contenu de manière asynchrone (fetch, etc.), le DOM peut changer après l'exécution du scroll-reveal. Les sections et éléments seraient déjà scannés à ce moment-là.

## 1.3 Logs console

Le script contient un `console.log` conditionnel (lignes 57-59) :
```javascript
if (typeof console !== 'undefined' && console.log) {
  console.log('sg-scroll-reveal: section observed', section);
}
```
Chaque section observée devrait afficher ce log. **Si aucun log n'apparaît**, soit `sections.length === 0`, soit aucune section ne contient `.sg-reveal` ou `.sg-reveal-card`.

---

# 2. ANALYSE DU SCRIPT sg-scroll-reveal.js

## 2.1 Architecture globale

| Constante | Valeur | Rôle |
|-----------|--------|------|
| `SECTION_SELECTOR` | `.sg-section, .sg-section-editorial` | Sections observées |
| `REVEAL_SELECTOR` | `.sg-reveal` | Éléments reveal standard |
| `REVEAL_CARD_SELECTOR` | `.sg-reveal-card` | Cartes |
| `ALL_REVEAL_SELECTOR` | `.sg-reveal, .sg-reveal-card` | Tous les éléments animables |
| `VISIBLE_CLASS` | `sg-reveal-visible` | Classe ajoutée pour afficher |
| `STAGGER_MS` | 90 | Délai entre chaque élément (ms) |

## 2.2 Flux d'exécution

1. **`run()`** → appelle `initHero()` puis `init()`
2. **`initHero()`** → cible `.sg-hero-premium`, trouve kicker, title, subtitle, cta, ajoute `sg-reveal-visible` avec stagger 180 ms
3. **`init()`** :
   - Récupère toutes les sections `.sg-section` ou `.sg-section-editorial`
   - Si aucune section → **return immédiat** (script inactif pour le contenu principal)
   - Crée un `IntersectionObserver`
   - Pour chaque section contenant au moins un `.sg-reveal` ou `.sg-reveal-card` → `observer.observe(section)`
   - Appelle `revealElementsInView()` — révèle les éléments déjà visibles
   - `setTimeout(1500)` — fallback : après 1,5 s, ajoute `sg-reveal-visible` à tous les éléments qui ne l'ont pas

## 2.3 Fonctionnement de l'IntersectionObserver

```javascript
{
  threshold: 0.35,
  rootMargin: '0px 0px -25% 0px'
}
```

- **threshold 0.35** : 35 % de la section doit être visible pour déclencher
- **rootMargin -25%** : la zone de détection est réduite de 25 % en bas du viewport (seul le haut 75 % compte)

**Condition bloquante (ligne 43) :**
```javascript
if (window.scrollY < 120) return;
```

Si cette condition est vraie, `animateSection()` n'est **jamais** appelé et la section n'est **pas** `unobserve`. La section reste observée mais ne s'anime pas via l'observer.

## 2.4 Détection des sections

Seules les sections qui contiennent au moins un `.sg-reveal` ou `.sg-reveal-card` sont observées. La page utilise uniquement `.sg-section` (pas `.sg-section-editorial`).

## 2.5 Hero vs sections

| Zone | Classe HTML | Géré par | Sélecteur script |
|------|-------------|----------|-------------------|
| Hero | `sg-hero-reveal` | `initHero()` | `.sg-hero-kicker`, `.sg-hero-title`, etc. |
| Sections | `sg-reveal`, `sg-reveal-card` | `init()` + Observer | `ALL_REVEAL_SELECTOR` |

Le hero utilise `sg-hero-reveal` (non inclus dans `ALL_REVEAL_SELECTOR`). Il est traité séparément.

## 2.6 Fonctions de secours

- **`revealElementsInView()`** : parcourt tous les `.sg-reveal` et `.sg-reveal-card`, si `rect.top < window.innerHeight` → ajoute `sg-reveal-visible`
- **`setTimeout(1500)`** : ajoute `sg-reveal-visible` à tout élément qui ne l'a pas

**Théoriquement**, aucun élément ne devrait rester invisible au-delà de 1,5 s grâce au fallback.

---

# 3. INVENTAIRE DES ÉLÉMENTS DANS LE DOM

## 3.1 Comptage par type

| Type | Nombre | Sections concernées |
|------|--------|---------------------|
| `.sg-hero-reveal` | 4 | Hero uniquement |
| `.sg-reveal` | 52 | Toutes les sections |
| `.sg-reveal-card` | 13 | Production (3), Guides solaire (6), Guides expertise (4) |
| **Total animables (hors hero)** | **65** | 13 sections |

## 3.2 Répartition par section

| Section | .sg-reveal | .sg-reveal-card | Total |
|--------|------------|-----------------|-------|
| Rentabilité | 8 | 0 | 8 |
| Durabilité | 5 | 0 | 5 |
| Contexte | 5 | 0 | 5 |
| Fonctionnement | 5 | 0 | 5 |
| Production | 5 | 3 | 8 |
| Étude | 5 | 0 | 5 |
| Dimensionnement | 5 | 0 | 5 |
| Bureau d'étude | 4 | 0 | 4 |
| Guides solaire | 5 | 6 | 11 |
| Guides expertise | 4 | 4 | 8 |
| Avantages | 5 | 0 | 5 |
| FAQ | 5 | 0 | 5 |
| Éligibilité | 5 | 0 | 5 |

## 3.3 Éléments potentiellement bloqués

Tous les éléments `.sg-reveal` et `.sg-reveal-card` ont `opacity: 0` par défaut (CSS). Ils ne deviennent visibles que si `sg-reveal-visible` est ajouté.

**Scénarios où ils peuvent rester invisibles :**
1. Le script ne s'exécute pas (erreur JS avant)
2. `init()` retourne car `sections.length === 0`
3. `revealElementsInView()` ne les atteint pas (hors viewport)
4. L'IntersectionObserver ne déclenche pas (condition `scrollY < 120` ou intersection jamais atteinte)
5. Le fallback `setTimeout(1500)` ne s'exécute pas (erreur entre-temps)

---

# 4. ANALYSE DE L'INTERSECTION OBSERVER

## 4.1 Configuration

| Paramètre | Valeur | Effet |
|-----------|--------|-------|
| `threshold` | 0.35 | 35 % de la section visible |
| `rootMargin` | `0px 0px -25% 0px` | Zone utile = haut 75 % du viewport |

## 4.2 Condition `scrollY < 120`

**Problème majeur :** Cette condition empêche toute animation au chargement et dans les premiers 120 px de scroll.

**Conséquences :**
- **Première section visible au chargement** : si l'utilisateur n'a pas scrollé 120 px, l'observer déclenche mais `animateSection()` n'est pas appelé. Les éléments dépendent alors de `revealElementsInView()` ou du fallback 1500 ms.
- **Sections en bas de page** : quand l'utilisateur scroll pour les voir, `scrollY` est généralement > 120. Donc pas de blocage dans ce cas.
- **Cas problématique** : écran très grand (ex. 4K), première section visible sans scroll. `revealElementsInView()` peut la révéler. Mais si la section est partiellement visible (ex. bas du viewport), certains éléments ont `rect.top > innerHeight` et ne sont pas révélés. L'observer déclenche avec `scrollY < 120` → pas d'animation. Ces éléments attendent le fallback 1500 ms.

## 4.3 Sections jamais observées ?

Toutes les sections avec `.sg-section` et contenant au moins un `.sg-reveal` ou `.sg-reveal-card` sont observées. Aucune section de la page n'est exclue par le sélecteur.

**Exception :** La section `.sg-cta-editorial` (CTA final) n'a pas la classe `.sg-section` et ne contient pas de `.sg-reveal`. Elle n'est pas concernée par le scroll reveal.

## 4.4 Combinaison threshold + rootMargin

Avec `rootMargin: -25%` en bas, une section doit avoir 35 % de sa surface dans le **haut 75 %** du viewport pour déclencher. Une section qui n'apparaît que dans le bas 25 % de l'écran ne déclenchera jamais l'observer.

---

# 5. ANALYSE DU CSS (sg-animations.css)

## 5.1 État initial et visible

| Classe | État initial | État visible |
|-------|--------------|--------------|
| `.sg-reveal` | `opacity: 0`, `translateY(24px)` | `opacity: 1`, `transform: none` |
| `.sg-reveal-card` | `opacity: 0`, `translateY(32px) scale(0.98)` | idem |
| `.sg-hero-reveal` | `opacity: 0`, `translateY(20px)` | via `.sg-reveal-visible` |

## 5.2 Transitions

- `.sg-reveal` : 0,65 s (opacity, transform)
- `.sg-reveal-card` : 0,75 s
- `.sg-hero-reveal` : 0,8 s

**Pas de blur** dans le CSS actuel (contrairement à l'audit précédent qui mentionnait un blur supprimé depuis).

## 5.3 Reduced motion

Sous `prefers-reduced-motion: reduce`, tous les éléments passent directement à `opacity: 1` et `transform: none`. Aucun blocage possible dans ce mode.

## 5.4 Éléments bloqués en opacity: 0

Un élément reste en `opacity: 0` tant qu'il n'a pas la classe `sg-reveal-visible`. Si le script ne l'ajoute jamais, l'élément reste invisible.

---

# 6. CONFLITS POTENTIELS

## 6.1 sg-counter.js

- Utilise son propre `IntersectionObserver` (threshold 0.2, rootMargin -10 %)
- Les `.sg-counter` sont souvent **à l'intérieur** de `.sg-reveal`
- Pas de conflit direct sur `opacity` ou `transform` : le compteur anime son texte, le parent gère l'apparition
- Le compteur peut démarrer avant que le parent soit visible si les seuils diffèrent

## 6.2 Scripts inline (FAQ)

Le script FAQ (lignes 1339-1350) fait un `toggle('hidden')` et modifie le `transform` de l'icône. Aucun impact sur `.sg-reveal` ou `.sg-reveal-card`.

## 6.3 CSS design system / editorial

Aucune règle ne cible `.sg-reveal`, `.sg-reveal-card` ou `.sg-reveal-visible`. Pas de conflit identifié.

## 6.4 Header / footer

`header.js` et `footer.js` chargent du contenu dynamique. Si le header modifie la hauteur de la page après le chargement, les `getBoundingClientRect()` utilisés à l'init peuvent être obsolètes. Mais `revealElementsInView()` et l'observer s'exécutent au chargement ; les recalculs de layout se font ensuite. Le fallback 1500 ms reste la dernière chance pour les éléments non révélés.

---

# 7. DIAGNOSTIC FINAL

## 7.1 État réel du système scroll reveal

| Aspect | État |
|--------|------|
| Script chargé | ✅ Oui |
| Script exécuté | ✅ Oui (sauf erreur avant) |
| Sections observées | ✅ 13 sections avec éléments reveal |
| Hero | ✅ Traité par `initHero()` |
| Fallback 1500 ms | ✅ Présent |

## 7.2 Pourquoi certains éléments ne s'affichent plus

1. **Condition `scrollY < 120`**  
   Bloque l'animation au chargement et dans les 120 premiers pixels. Les éléments visibles au chargement dépendent de `revealElementsInView()` ou du fallback.

2. **`revealElementsInView()` limité au viewport**  
   Seuls les éléments avec `rect.top < window.innerHeight` sont révélés. Sur un hero de 78 vh, la première section peut être en dessous ; ses éléments ne sont pas révélés par cette fonction.

3. **Threshold + rootMargin stricts**  
   Une section doit avoir 35 % de sa surface dans le haut 75 % du viewport. Sections en bas d'écran ou partiellement visibles peuvent ne jamais déclencher l'observer.

4. **Dépendance au fallback 1500 ms**  
   Beaucoup d'éléments peuvent ne s'afficher qu’après 1,5 s, sans animation de scroll, ce qui donne une impression de script peu actif.

## 7.3 Le script est-il réellement actif ?

Oui, s'il n'y a pas d'erreur JavaScript avant son exécution. Pour vérifier :
- Ouvrir la console
- Chercher les logs `sg-scroll-reveal: section observed`
- Si aucun log → soit pas de sections, soit pas d’éléments reveal dans les sections

## 7.4 Sections jamais observées ?

Non. Toutes les sections `.sg-section` contenant des `.sg-reveal` ou `.sg-reveal-card` sont observées.

## 7.5 Éléments bloqués en invisible ?

Théoriquement non, grâce au fallback 1500 ms. Sauf si :
- Erreur JS avant ou pendant l’exécution
- `init()` quitte à cause de `!sections.length`
- Problème de chemin (ex. site servi depuis un sous-dossier, script non chargé)

## 7.6 Ce qui casse le fonctionnement actuel

| Cause | Impact |
|-------|--------|
| **`scrollY < 120`** | Pas d’animation au chargement ; première section et contenu visible sans scroll dépendent de `revealElementsInView()` ou du fallback |
| **rootMargin -25 %** | Zone de détection réduite ; sections en bas du viewport peuvent ne jamais déclencher |
| **threshold 0.35** | Exige 35 % de section visible ; déclenchement plus tardif |
| **Fallback 1500 ms** | Beaucoup d’éléments n’apparaissent qu’après 1,5 s, sans effet de scroll, d’où l’impression de script peu actif |
| **Hero avec `sg-hero-reveal`** | Cohérent avec `initHero()` ; pas de bug identifié |

---

# SYNTHÈSE

Le système scroll reveal est **techniquement en place** mais **mal calibré** :

1. La condition `scrollY < 120` empêche les animations au chargement et au début du scroll.
2. La combinaison threshold 0.35 + rootMargin -25 % rend le déclenchement tardif et parfois absent.
3. Une grande partie des apparitions repose sur le fallback 1500 ms, ce qui donne une impression de script peu réactif.
4. Aucun conflit majeur n’a été trouvé avec les autres scripts ou le CSS.

**Recommandation prioritaire pour la correction :** Revoir ou supprimer la condition `scrollY < 120` et ajuster threshold/rootMargin pour un déclenchement plus précoce et plus fiable.
