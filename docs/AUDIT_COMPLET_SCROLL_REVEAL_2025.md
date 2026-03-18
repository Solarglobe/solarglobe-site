# AUDIT COMPLET — SYSTÈME SCROLL REVEAL
## Page /le-solaire/ — Analyse exhaustive

**Date :** 14 mars 2025  
**Objectif :** Identifier exactement pourquoi les animations partent trop tôt, trop vite, et pourquoi certaines corrections cassent l'affichage.

---

# 1. LISTE EXHAUSTIVE DES FICHIERS IMPLIQUÉS

## Fichiers HTML
| Chemin | Rôle |
|--------|------|
| `le-solaire/index.html` | Page principale — structure hero, sections, ordre DOM, scripts |

## Fichiers CSS (ordre de chargement)
| Chemin | Rôle |
|--------|------|
| `assets/css/solarglobe-design-system.css` | Design system global — pas de règles reveal |
| `assets/css/le-solaire-editorial.css` | Styles éditoriaux — hero, sections, CTA — pas de .sg-reveal |
| `assets/css/sg-animations.css` | **Règles reveal** — .sg-reveal, .sg-reveal-card, .sg-hero-reveal |
| `assets/css/header-common.css` | Header fixe 72px, body padding-top 72px |
| `assets/css/footer-common.css` | Footer — pas d'impact reveal |

## Fichiers JS (ordre de chargement)
| Chemin | Rôle |
|--------|------|
| `assets/js/header.js` | Injecte header via fetch — DOMContentLoaded |
| `assets/js/footer.js` | Injecte footer via fetch — DOMContentLoaded |
| `assets/js/sg-scroll-reveal.js` | **Script reveal** — hero + sections |
| `assets/js/sg-counter.js` | Compteurs animés — IntersectionObserver séparé |

## Autres pages utilisant le système
| Page | sg-scroll-reveal.js | sg-animations.css |
|------|---------------------|-------------------|
| `le-solaire/index.html` | ✅ Oui | ✅ Oui |
| Autres pages du site | ❌ Non | ❌ Non |

**Conclusion :** Le système scroll reveal est utilisé **uniquement** sur `/le-solaire/`. Aucune autre page ne partage ce système.

---

# 2. CARTOGRAPHIE PRÉCISE DU SYSTÈME ACTUEL

## A. État initial masqué (qui cache les éléments)

| Fichier | Classe | Règles |
|---------|--------|--------|
| `sg-animations.css` | `.sg-reveal` | `opacity: 0`, `transform: translateY(24px)`, `transition: 0.65s` |
| `sg-animations.css` | `.sg-reveal-card` | `opacity: 0`, `transform: translateY(32px) scale(0.98)`, `transition: 0.75s` |
| `sg-animations.css` | `.sg-hero-reveal` | `opacity: 0`, `transform: translateY(20px)`, `transition: 0.8s` |

**Aucun autre fichier** ne définit opacity/transform sur ces classes. Les éléments sont invisibles par défaut tant que `sg-reveal-visible` n'est pas ajouté.

## B. Révélation du hero

| Fichier | Fonction | Mécanisme |
|---------|----------|-----------|
| `sg-scroll-reveal.js` | `initHero()` | Trouve kicker, title, subtitle, cta dans `.sg-hero-premium` → ajoute `sg-reveal-visible` avec délais 0, 300, 600, 900 ms |

**Déclenchement :** Au chargement (DOMContentLoaded), immédiatement. Pas d'IntersectionObserver pour le hero.

## C. Révélation des sections

| Fichier | Mécanisme | Déclenchement |
|---------|-----------|---------------|
| `sg-scroll-reveal.js` | `animateSection(sections[0])` | **Synchrone au init** — première section animée immédiatement |
| `sg-scroll-reveal.js` | IntersectionObserver | Sections 2 à 13 — quand 25% visible dans zone (viewport - 10% bas) |

**Paramètres observer actuels :**
- `threshold: 0.25`
- `rootMargin: '0px 0px -10% 0px'`

## D. Transitions CSS réelles (vitesse perçue)

| Classe | transition-duration | transition-timing |
|--------|---------------------|-------------------|
| `.sg-reveal` | **0.65s** | cubic-bezier(0.22, 1, 0.36, 1) |
| `.sg-reveal-card` | **0.75s** | cubic-bezier(0.22, 1, 0.36, 1) |
| `.sg-hero-reveal` | **0.8s** | cubic-bezier(0.22, 1, 0.36, 1) |

**Stagger JS (délai entre chaque élément) :**
- Sections : `STAGGER_MS = 180` → 0, 180, 360, 540… ms
- Hero : `i * 300` → 0, 300, 600, 900 ms

---

# 3. STRUCTURE EXACTE DU DOM

## Hero (bloc 1)
```
section.sg-hero-premium.sg-hero-solaire
  margin-top: -72px (remonte sous header)
  min-height: 78vh (desktop)
  ├── .sg-hero-bg
  ├── .sg-hero-content
  │   └── .sg-hero-inner
  │       ├── span.sg-hero-kicker.sg-hero-reveal
  │       ├── h1.sg-hero-title.sg-hero-reveal
  │       ├── p.sg-hero-subtitle.sg-hero-reveal
  │       └── div.sg-hero-cta.sg-hero-reveal
```

**Hauteur perçue :** 78vh ≈ 624px (viewport 800px). Le hero occupe la quasi-totalité de l'écran au chargement.

## Header fixe
- `position: fixed`, `height: 72px`, `z-index: 1000`
- `body { padding-top: 72px }`
- `#header-placeholder { min-height: 72px }`
- Hero : `margin-top: -72px` pour compenser et remonter sous le header

**Impact :** Le viewport "utile" pour l'IntersectionObserver est la zone visible. Le header fixe ne modifie pas le calcul d'intersection (root = viewport par défaut). Mais le hero avec margin-top négatif peut créer une zone de chevauchement visuel.

## Première section (Rentabilité)
- `section.sg-section.sg-section-dark`
- Premier enfant : `sg-section-divider` (margin 90px)
- Contient 8 éléments `.sg-reveal` (kicker, title, intro, bloc texte, 2 divs, etc.)

**Position au chargement :** Juste sous le hero. Sur un viewport 800px, la première section commence vers 624px + padding. Elle peut être partiellement visible (bas du viewport) ou totalement sous le fold selon la hauteur d'écran.

---

# 4. DIAGNOSTIC DES CAUSES

## 4.1 Cause du "trop tôt"

| Cause | Fichier | Ligne / Mécanisme | Gravité |
|-------|---------|-------------------|---------|
| **animateSection(sections[0]) synchrone** | sg-scroll-reveal.js | 33-36 | **CRITIQUE** |
| **IntersectionObserver threshold 0.25** | sg-scroll-reveal.js | 53 | **IMPORTANTE** |
| **rootMargin -10%** | sg-scroll-reveal.js | 54 | **SECONDAIRE** |

**Explication :**
1. **animateSection(sections[0])** est appelé **dès l'init**, avant même que l'utilisateur ait scrollé. La première section (Rentabilité) s'anime au chargement, pas au scroll. C'est une "sécurité" ajoutée pour garantir l'affichage, mais elle court-circuite le comportement "reveal au scroll".
2. **threshold 0.25** : une section déclenche quand 25% est visible. Pour une section partiellement en bas du viewport, 25% peut être atteint très tôt (avant que l'utilisateur ait vraiment "scrollé vers" la section).
3. **rootMargin -10%** : rétrécit la zone de 10% en bas. Cela retarde légèrement le déclenchement par rapport à un rootMargin 0. Pas la cause principale du "trop tôt".

## 4.2 Cause du "trop rapide"

| Cause | Fichier | Valeur actuelle | Gravité |
|-------|---------|-----------------|---------|
| **transition CSS courte** | sg-animations.css | 0.65s / 0.75s / 0.8s | **IMPORTANTE** |
| **Stagger 180ms** | sg-scroll-reveal.js | STAGGER_MS = 180 | **SECONDAIRE** |
| **Hero 300ms** | sg-scroll-reveal.js | i * 300 | **SECONDAIRE** |

**Explication :**
1. Les transitions CSS (0.65s à 0.8s) sont relativement courtes. Une transition à 1s ou 1.2s donnerait une impression plus "premium" et moins précipitée.
2. Le stagger 180ms entre chaque élément : pour une section avec 8 éléments, le dernier commence à 1260ms. Combiné à une transition de 0.65s, l'animation totale d'une section ≈ 1.9s. C'est déjà long, mais la **vitesse perçue** de chaque élément individuel est dictée par la transition CSS (0.65s).
3. Le hero : 4 éléments à 0, 300, 600, 900 ms. Chaque élément met 0.8s pour apparaître. La cascade est rapide.

## 4.3 Cause du "ça casse l'affichage"

| Cause | Fichier | Mécanisme | Gravité |
|-------|---------|-----------|---------|
| **animateSection sécurité `if (contains VISIBLE) return`** | sg-scroll-reveal.js | 22-23 | **CRITIQUE** |
| **Suppression des fallbacks** | (historique) | revealElementsInView + setTimeout supprimés | **CRITIQUE** |
| **Double appel animateSection(sections[0])** | sg-scroll-reveal.js | init + observer | **SECONDAIRE** |

**Explication :**
1. **Sécurité `if (el.classList.contains(VISIBLE_CLASS)) return`** : Si un élément a déjà la classe, on ne programme pas le setTimeout. En soi, c'est correct. Mais le **problème** : quand `animateSection(sections[0])` est appelé au init, on programme les setTimeouts. Si pour une raison quelconque (race condition, ordre d'exécution) l'IntersectionObserver appelle `animateSection` sur une section **avant** que le init ait fini, ou si une section n'est jamais observée (bug), les éléments sans classe restent invisibles. **Sans fallback**, il n'y a plus de filet de sécurité. Les corrections qui ont supprimé revealElementsInView et les setTimeout ont créé un risque : si une section n'est jamais déclenchée par l'observer, ses éléments restent invisibles.
2. **Sections 2 à 13** : dépendent uniquement de l'IntersectionObserver. Si threshold/rootMargin sont trop stricts, ou si une section est mal détectée (layout, viewport), elle peut ne jamais déclencher. **Sans fallback = bloc invisible**.
3. **Double appel** : sections[0] est animée par animateSection(sections[0]) au init ET potentiellement par l'observer (car elle est visible). La sécurité `if (contains VISIBLE) return` évite les doublons, mais l'ordre d'exécution peut créer des cas limites.

## 4.4 Cause spécifique du bloc 1 / hero

| Cause | Fichier | Mécanisme | Gravité |
|-------|---------|-----------|---------|
| **initHero() exécuté en premier** | sg-scroll-reveal.js | run() → initHero() puis init() | **SECONDAIRE** |
| **Hero non observé par IntersectionObserver** | sg-scroll-reveal.js | Hero = .sg-hero-premium, pas .sg-section | **N/A** |
| **Header injecté après DOMContentLoaded** | header.js | fetch async | **IMPORTANTE** |

**Explication :**
1. Le hero est traité par `initHero()` qui s'exécute immédiatement. Il n'est pas concerné par l'observer. **Stable** tant qu'on ne touche pas à initHero.
2. **Header async** : header.js écoute DOMContentLoaded, fait un fetch, puis injecte le HTML. Le scroll-reveal écoute aussi DOMContentLoaded et s'exécute. **Ordre réel** : DOMContentLoaded → header fetch lancé + scroll-reveal run(). Le header peut être injecté **après** que le scroll-reveal ait scanné le DOM. Le header-placeholder a une min-height 72px, donc l'espace est réservé. Mais le **layout** peut changer quand le header est injecté (si le header a une hauteur différente, ou si le fetch échoue et le placeholder reste vide). Le hero avec margin-top -72px suppose un header de 72px. Si le header n'est pas encore là, le calcul peut être faux. **Risque** : sur connexion lente, le header arrive tard, le hero peut "sauter" visuellement.
3. **Instabilité selon modifications** : les corrections successives ont ajouté/supprimé animateSection(sections[0]), modifié le stagger, ajouté la sécurité. Chaque changement affecte **sections[0]** (première section) qui est juste sous le hero. Si on supprime animateSection(sections[0]), la première section dépend de l'observer. Si elle est visible au chargement, l'observer devrait déclencher. Mais si threshold/rootMargin font qu'elle n'intersecte pas assez, elle reste invisible. **C'est pourquoi** animateSection(sections[0]) a été ajouté comme "sécurité" — mais cela crée le "trop tôt".

---

# 5. NIVEAU DE GRAVITÉ PAR CAUSE

| Cause | Gravité | Impact |
|-------|---------|--------|
| animateSection(sections[0]) synchrone | **CRITIQUE** | Première section s'anime au chargement, pas au scroll |
| Suppression fallbacks (revealElementsInView, setTimeout) | **CRITIQUE** | Sections 2-13 peuvent rester invisibles si observer ne déclenche pas |
| Sécurité `if (contains VISIBLE) return` | **IMPORTANTE** | Peut empêcher une ré-animation si appelée dans un ordre inattendu (edge case) |
| threshold 0.25 | **IMPORTANTE** | Déclenchement relativement tôt |
| transition CSS 0.65s-0.8s | **IMPORTANTE** | Animations perçues comme rapides |
| Header injecté async | **IMPORTANTE** | Peut créer instabilité layout hero sur connexion lente |
| rootMargin -10% | **SECONDAIRE** | Impact modéré |
| Stagger 180ms / Hero 300ms | **SECONDAIRE** | Ajustable pour affiner |

---

# 6. PLAN DE CORRECTION MINIMAL ET SÛR

## Principe
- **Reveal plus tardif** : ne pas animer la première section au chargement
- **Reveal plus lent** : augmenter les durées CSS et/ou stagger
- **Affichage jamais cassé** : conserver un filet de sécurité
- **Hero stable** : ne pas toucher à initHero

## Ordre des corrections

### Étape 1 — Sécuriser l'affichage (priorité absolue)
**Fichier :** `assets/js/sg-scroll-reveal.js`

**Action :** Réintroduire un fallback minimal, exécuté après un délai suffisant (ex. 2500ms), qui ajoute `sg-reveal-visible` à tout élément qui ne l'a pas.

**Raison :** Garantir qu'aucune section ne reste invisible si l'observer ne déclenche pas (layout, viewport, edge cases).

**Ne pas toucher :** IntersectionObserver, initHero, structure init().

---

### Étape 2 — Rendre le reveal plus tardif
**Fichier :** `assets/js/sg-scroll-reveal.js`

**Action 2a :** Supprimer l'appel `animateSection(sections[0])` au init. La première section sera animée uniquement par l'observer quand elle entrera dans la zone.

**Action 2b :** Augmenter le threshold à 0.3 ou 0.35 pour que les sections déclenchent plus tard (quand l'utilisateur a vraiment scrollé vers elles).

**Risque :** Si la première section est visible au chargement et que threshold 0.3 n'est pas atteint (section trop grande, peu visible), elle pourrait ne pas déclencher. Le fallback de l'étape 1 compense.

---

### Étape 3 — Ralentir les animations
**Fichier :** `assets/css/sg-animations.css`

**Action :** Augmenter les transition-duration :
- `.sg-reveal` : 0.65s → 0.85s ou 0.9s
- `.sg-reveal-card` : 0.75s → 0.9s ou 1s
- `.sg-hero-reveal` : 0.8s → 1s (optionnel, hero déjà au chargement)

**Fichier :** `assets/js/sg-scroll-reveal.js`

**Action :** Augmenter STAGGER_MS : 180 → 220 ou 250. Et/ou hero : 300 → 350 ou 400.

**Ne pas toucher :** La logique de l'IntersectionObserver, les sélecteurs, initHero.

---

### Étape 4 — Vérifier la sécurité animateSection
**Fichier :** `assets/js/sg-scroll-reveal.js`

**Action :** La condition `if (el.classList.contains(VISIBLE_CLASS)) return` est correcte pour éviter les doublons. **La conserver**. Elle n'est pas la cause du "ça casse" — c'est l'absence de fallback qui l'est.

---

## Ce qu'il ne faut surtout pas toucher

| Élément | Raison |
|---------|--------|
| **initHero()** | Hero stable, animation au chargement voulue |
| **Structure DOM** | Risque de régression sur toute la page |
| **Sélecteurs** (.sg-section, .sg-reveal, etc.) | Cohérence avec le HTML |
| **header.js / footer.js** | Hors scope, pourrait casser le site |
| **sg-animations.css — règles reduced-motion** | Accessibilité |
| **Ordre de chargement des scripts** | Dépendances |

---

## Correction minimale pour objectifs

| Objectif | Correction minimale |
|----------|---------------------|
| Reveal plus tardif | Supprimer animateSection(sections[0]), augmenter threshold à 0.3 |
| Reveal plus lent | transition 0.65s→0.85s, STAGGER_MS 180→220 |
| Affichage jamais cassé | Fallback setTimeout 2500ms qui ajoute sg-reveal-visible à tous |
| Hero stable | Ne pas modifier initHero |

---

# 7. RÉSUMÉ DES DÉPENDANCES CROISÉES

| Conflit potentiel | Analyse |
|-------------------|---------|
| CSS initial + JS reveal | Pas de conflit. Le CSS met opacity:0, le JS ajoute la classe. |
| Hero script + section script | Séparés. initHero pour hero, init pour sections. Pas d'interférence. |
| threshold + rootMargin + layout | rootMargin -10% réduit la zone. Avec hero 78vh, la première section peut être en bas du viewport. threshold 0.25 peut être atteint. |
| transition CSS + stagger JS | Le stagger décale le **début** de chaque animation. La **durée** est en CSS. Les deux contribuent à la vitesse perçue. |
| Sticky header + viewport | Le header fixed 72px n'est pas dans le root de l'observer. Le viewport = zone visible. Pas de conflit direct. |
| sg-counter.js | IntersectionObserver séparé. Les .sg-counter sont dans des .sg-reveal. Le parent s'anime, le compteur aussi. Pas de conflit. |
| Mobile vs desktop | Mêmes règles. Le hero a min-height: auto en 480px. Les sections ont moins d'éléments visibles. Comportement identique. |

---

# 8. RÈGLES QUI PEUVENT LAISSER DES ÉLÉMENTS INVISIBLES

| Règle | Fichier | Condition |
|-------|---------|-----------|
| `.sg-reveal { opacity: 0 }` | sg-animations.css | État par défaut. Sans sg-reveal-visible, reste invisible. |
| `.sg-reveal-card { opacity: 0 }` | sg-animations.css | Idem. |
| `.sg-hero-reveal { opacity: 0 }` | sg-animations.css | Idem. initHero ajoute la classe. |
| `@media (prefers-reduced-motion)` | sg-animations.css | Force opacity: 1. **Pas de blocage** dans ce mode. |

**Conclusion :** Si le JS n'ajoute jamais `sg-reveal-visible`, les éléments restent invisibles. Le seul filet actuel est `animateSection(sections[0])` pour la première section. Les sections 2-13 n'ont **aucun fallback**.

---

# 9. ORDRE DE CHARGEMENT RÉEL DES SCRIPTS

```
1. header.js (déclenche fetch sur DOMContentLoaded)
2. footer.js (déclenche fetch sur DOMContentLoaded)
3. sg-scroll-reveal.js (s'exécute sur DOMContentLoaded ou immédiatement)
4. sg-counter.js (s'exécute sur DOMContentLoaded ou immédiatement)
```

Tous écoutent DOMContentLoaded. L'ordre d'exécution suit l'ordre des balises script. Le header et footer lancent des fetch asynchrones ; le scroll-reveal s'exécute sans attendre. Le DOM est prêt (sections, hero), mais le header peut ne pas être encore injecté.

---

# 10. SYNTHÈSE FINALE

## Causes racines identifiées

1. **Trop tôt** : `animateSection(sections[0])` au init + threshold 0.25
2. **Trop rapide** : transition CSS 0.65-0.8s + stagger 180ms
3. **Ça casse** : suppression des fallbacks (revealElementsInView, setTimeout) sans filet de sécurité
4. **Hero instable** : header injecté en async peut modifier le layout après le reveal

## Fichiers à modifier (plan validé)

| Fichier | Modifications |
|---------|---------------|
| `assets/js/sg-scroll-reveal.js` | Fallback 2500ms, supprimer animateSection(sections[0]), threshold 0.3, STAGGER_MS 220 |
| `assets/css/sg-animations.css` | transition 0.65s→0.85s, 0.75s→0.9s |

## Fichiers à ne pas modifier

- `le-solaire/index.html` (structure)
- `assets/css/le-solaire-editorial.css`
- `assets/css/header-common.css`
- `assets/js/header.js`
- `assets/js/footer.js`
- `assets/js/sg-counter.js`

---

**AUDIT TERMINÉ**

**AUCUNE MODIFICATION APPLIQUÉE**

En attente de votre feu vert pour procéder aux corrections.
