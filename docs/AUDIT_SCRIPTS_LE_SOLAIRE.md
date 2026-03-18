# AUDIT COMPLET DES SCRIPTS — PAGE /le-solaire/index.html

**Date :** 14 mars 2025  
**Objectif :** Analyse technique des scripts JavaScript liés aux scénarios et animations.

---

## 1. INVENTAIRE DES SCRIPTS CHARGÉS

### 1.1 Ordre de chargement

| Ordre | Source | Rôle |
|-------|--------|------|
| 1 | GTM (inline head) | Google Tag Manager — analytics |
| 2 | cdn.tailwindcss.com | Framework CSS utility |
| 3 | tailwind.config (inline) | Configuration Tailwind |
| 4 | `/assets/js/header.js` | Injection du header, menu mobile, navigation active |
| 5 | `/assets/js/footer.js` | Injection du footer |
| 6 | `/assets/js/sg-animations.js` | Système d'animation au scroll (IntersectionObserver) |
| 7 | Script inline `.sg-counter` | Compteurs animés (40000, 25, 900, etc.) |
| 8 | Script inline FAQ | Accordéon FAQ (toggle hidden, rotation icône) |
| 9 | JSON-LD (4 blocs) | Données structurées SEO |

### 1.2 Fichiers non chargés sur cette page

- Aucun script d'animation scroll externe (GSAP, AOS, etc.)
- Pas de script CTA spécifique
- Pas de script hero spécifique

---

## 2. ANALYSE DÉTAILLÉE DE sg-animations.js

### 2.1 Sélecteur et classes

```javascript
SELECTOR = '.sg-fade-up, .sg-fade-left, .sg-fade-right, .sg-zoom-in, .sg-reveal-text, .sg-card-rise, .sg-image-reveal, .sg-guides-grid'
VISIBLE_CLASS = 'sg-animate-visible'
```

### 2.2 IntersectionObserver — Configuration

| Paramètre | Valeur | Effet |
|-----------|--------|-------|
| **threshold** | 0.25 | L'élément doit être visible à 25 % pour déclencher |
| **rootMargin** | `0px 0px -20% 0px` | Zone du bas du viewport exclue (20 %) — déclenchement quand l'élément entre dans le haut 80 % de l'écran |

### 2.3 Logique de traitement

1. **Éléments `.sg-card-rise` dans `.sg-guides-grid`** : exclus de l'observation individuelle (ligne 29-31)
2. **Conteneur `.sg-guides-grid`** : observé ; au déclenchement → `animateCardsSequential()` qui ajoute `sg-animate-visible` à chaque `.sg-card-rise` avec un délai de **340 ms** entre chaque carte
3. **Tous les autres éléments** : observés individuellement ; au déclenchement → ajout direct de `sg-animate-visible`

### 2.4 Points positifs

- Utilisation d'IntersectionObserver (performant)
- `unobserve()` après déclenchement (pas de re-déclenchement)
- Cascade réelle pour les cartes dans `sg-guides-grid`
- Init au `DOMContentLoaded` ou immédiate si DOM déjà prêt

### 2.5 Problèmes identifiés

| Problème | Détail |
|----------|--------|
| **sg-delay ignoré dans sg-guides-grid** | Les cartes ont `sg-delay-1` à `sg-delay-5` mais le script utilise un délai fixe de 340 ms. Les classes CSS `sg-delay-*` s'ajoutent à la transition, ce qui peut créer des délais cumulés très longs (ex. carte 4 : 1020 ms + 1200 ms = 2,2 s avant le début de l'animation) |
| **Pas de stagger pour les éléments non-cartes** | Dans une section, kicker, titre, intro, paragraphes, colonnes sont tous déclenchés en même temps. Les `sg-delay-1`, `sg-delay-2` créent une cascade via CSS, mais tous reçoivent la classe au même instant |
| **Classes inutilisées** | `.sg-zoom-in` et `.sg-image-reveal` sont dans le sélecteur mais **aucun élément** de la page ne les utilise |
| **Première section visible au chargement** | Avec un hero ~78vh, la section « Rentabilité » peut être déjà dans le viewport. L'IntersectionObserver déclenche immédiatement au premier frame → animation dès le chargement, pas au scroll |

---

## 3. ÉLÉMENTS ANIMÉS DANS LE DOM

### 3.1 Répartition par type

| Classe | Nombre | Exemples |
|--------|--------|----------|
| **sg-fade-up** | ~25 | Séparateurs, kickers, titres |
| **sg-fade-left** | ~6 | Kickers, colonnes texte |
| **sg-fade-right** | ~8 | Intros, colonnes image |
| **sg-reveal-text** | ~35 | Paragraphes, intros |
| **sg-card-rise** | ~14 | 3 cartes Production + 6 guides + 3 packs |
| **sg-zoom-in** | 0 | Non utilisé |
| **sg-image-reveal** | 0 | Non utilisé |
| **sg-guides-grid** | 2 | Conteneurs des grilles de cartes |

### 3.2 Détection par le script

- Tous les éléments avec les classes du sélecteur sont bien détectés
- Les `.sg-card-rise` dans `.sg-guides-grid` sont exclus de l'observation individuelle (comportement voulu)
- Aucun élément animé n'est oublié

### 3.3 Éléments potentiellement visibles avant animation

- **Section Rentabilité** : première section sous le hero ; selon la hauteur d'écran, peut être visible au chargement
- **Séparateur sgsep00** : juste sous le hero, souvent visible immédiatement
- Avec `rootMargin: -20%` en bas, le déclenchement se fait quand l'élément atteint le haut 80 % du viewport → les éléments du haut de page peuvent être déclenchés dès le chargement

---

## 4. SÉQUENCES D'ANIMATION

### 4.1 Comportement actuel

| Contexte | Comportement |
|----------|--------------|
| **Section type** (ex. Rentabilité) | Kicker, titre, intro, paragraphes, colonnes : tous reçoivent `sg-animate-visible` au même moment. La cascade vient uniquement des `sg-delay-*` (300, 600, 900 ms…) en CSS |
| **Cartes Production** (3 kWc, 6 kWc, 9 kWc) | Observées individuellement. Comme elles sont dans la même zone, elles se déclenchent ensemble → les 3 reçoivent la classe en même temps. Les `sg-delay-1`, `sg-delay-2`, `sg-delay-3` créent une cascade correcte |
| **Grille Guides** (6 cartes) | `animateCardsSequential` : délai 0, 340, 680, 1020, 1360, 1700 ms. Cascade réelle côté JS |
| **Grille Packs** (3 cartes) | Même logique, sans `sg-delay` sur les cartes → cascade propre |

### 4.2 Problèmes de séquence

| Problème | Impact |
|----------|--------|
| **Pas de stagger par section** | Tous les éléments d'une section s'animent en parallèle (avec décalage CSS uniquement). Pas de notion de « section entière » qui s'anime de haut en bas |
| **Cartes Production** | Pas de conteneur parent observé ; chaque carte est observée seule. Si la section est visible, les 3 cartes se déclenchent ensemble. Les délais CSS fonctionnent, mais une logique type `sg-guides-grid` serait plus cohérente |
| **Délais cumulés dans sg-guides-grid** | Script (340 ms × index) + `sg-delay-*` (300–1500 ms) → les cartes 4, 5, 6 peuvent commencer très tard |

---

## 5. PROBLÈMES CONNUS

### 5.1 Animations au chargement

- **Oui** : la section Rentabilité et le premier séparateur sont souvent visibles au chargement
- L'IntersectionObserver déclenche dès que l'élément est dans la zone (threshold 25 %, rootMargin -20 %)
- Conséquence : animations immédiates au lieu d’être liées au scroll

### 5.2 Animations trop rapides

- Durée CSS : 1,4 s (`--sg-anim-duration`)
- Les délais `sg-delay` (300–1500 ms) peuvent donner une impression de lenteur sur les derniers éléments d’une section

### 5.3 Éléments déjà visibles

- Non : les éléments ont `opacity: 0` au chargement (sg-animations.css)
- Ils ne deviennent visibles qu’après ajout de `sg-animate-visible`

### 5.4 Cartes en bloc

- **Cartes Production** : déclenchées ensemble (même zone), cascade via CSS uniquement
- **Grilles Guides** : cascade réelle via `animateCardsSequential` ✅

### 5.5 Éléments sans animation

- **Hero** : pas de classe d’animation (choix assumé)
- **CTA inline** : pas d’animation
- **Boutons** : pas d’animation d’entrée
- **Section « Guides photovoltaïques »** (2e grille) : kicker, titre, intro sans classes d’animation (ligne 1167–1169)

---

## 6. SCRIPTS INLINE — ANALYSE

### 6.1 Script sg-counter

**Rôle :** Animation des chiffres (40000, 25, 900, 1200, etc.) au scroll.

**Problème majeur :** création d’**un IntersectionObserver par élément** `.sg-counter`.

- 14 éléments `.sg-counter` → 14 observers
- Chaque observer observe un seul élément
- Recommandation : un seul observer pour tous les `.sg-counter`

**Autre point :** `obs.disconnect()` après le premier déclenchement — correct pour éviter les re-déclenchements.

### 6.2 Script FAQ

**Rôle :** Accordéon (toggle `hidden`, `aria-expanded`, rotation de l’icône).

- Implémentation simple et correcte
- Pas de conflit avec les animations

---

## 7. PERFORMANCES

### 7.1 IntersectionObserver

| Script | Nombre d'observers | Éléments observés |
|--------|--------------------|-------------------|
| sg-animations.js | 1 | ~90 éléments (après filtrage) |
| sg-counter (inline) | 14 | 1 chacun |

**Total : 15 IntersectionObserver** pour la page.

### 7.2 Poids JS

- ~2,5 Ko (sg-animations.js)
- Header/Footer : chargement asynchrone de composants
- Pas de librairie d’animation lourde

### 7.3 Risques

| Risque | Niveau | Commentaire |
|--------|--------|-------------|
| Lag au scroll | Faible | Un seul observer pour les animations, pas de calcul lourd |
| Répétition d’animations | Nul | `unobserve()` après déclenchement |
| Multiples observers | Moyen | 14 observers pour les compteurs — à regrouper |

---

## 8. SYNTHÈSE DES PROBLÈMES

### Critiques

1. **14 IntersectionObserver pour les compteurs** — à remplacer par un seul observer partagé
2. **Première section déclenchée au chargement** — animations immédiates au lieu d’être liées au scroll
3. **Section « Guides photovoltaïques »** — kicker, titre, intro sans animation

### Modérés

4. **Délais cumulés** dans `sg-guides-grid` (script + `sg-delay`) — cartes 4–6 très retardées
5. **Cartes Production** — pas de stagger côté JS, uniquement CSS
6. **Classes inutilisées** — `sg-zoom-in`, `sg-image-reveal` dans le sélecteur mais absentes du DOM

### Mineurs

7. **Pas de stagger par section** — tous les enfants d’une section déclenchés en même temps
8. **Hero sans animation** — choix de design, pas un bug

---

## 9. OPTIMISATIONS POSSIBLES

### 9.1 Priorité haute

1. **Regrouper les observers des compteurs** : un seul IntersectionObserver pour tous les `.sg-counter`
2. **Ajuster le déclenchement initial** : `rootMargin` ou `threshold` pour éviter que la première section se déclenche au chargement (ex. `rootMargin: '0px 0px -30% 0px'` ou délai minimal avant la première observation)
3. **Ajouter les classes d’animation** sur la section « Guides photovoltaïques » (kicker, titre, intro)

### 9.2 Priorité moyenne

4. **Stagger par section** : observer un conteneur parent (ex. `.sg-section`) et déclencher les enfants avec des délais progressifs
5. **Cartes Production** : utiliser un conteneur parent (type `sg-guides-grid`) pour une cascade cohérente
6. **Simplifier les délais dans sg-guides-grid** : soit retirer les `sg-delay` des cartes, soit adapter le délai du script (ex. 200 ms au lieu de 340 ms)

### 9.3 Priorité basse

7. **Nettoyer le sélecteur** : retirer `sg-zoom-in` et `sg-image-reveal` s’ils ne sont pas utilisés
8. **Documenter** le système (README ou commentaires dans le code)

---

## 10. RECOMMANDATIONS DE REFACTOR

### 10.1 sg-animations.js

- Ajouter une option pour retarder le premier check (éviter le déclenchement au chargement)
- Introduire un mode « stagger par section » pour les blocs `.sg-section`
- Créer un conteneur dédié pour les cartes Production (ex. `.sg-cards-stagger`) avec la même logique que `sg-guides-grid`

### 10.2 Script sg-counter

- Extraire dans un fichier `/assets/js/sg-counter.js`
- Utiliser un seul IntersectionObserver pour tous les `.sg-counter`
- Gérer `prefers-reduced-motion` (affichage direct sans animation)

### 10.3 Cohérence

- Définir une règle : toutes les sections éditoriales ont kicker + titre + intro animés
- Uniformiser le traitement des grilles de cartes (Production, Guides, Packs)

---

## ANNEXE — Éléments animés par section

| Section | Éléments animés |
|---------|-----------------|
| Rentabilité | Divider, kicker, titre, intro, 2 paragraphes, sg-fade-left, sg-fade-right, sg-counter (3) |
| Durée de vie | Divider, kicker, titre, intro, 6 paragraphes |
| Contexte | Divider, kicker, titre, intro, 2 paragraphes |
| Fonctionnement | Divider, kicker, titre, intro, sg-fade-left, sg-fade-right |
| Production | Divider, kicker, titre, intro, 2 paragraphes, 3 cartes sg-card-rise, sg-counter (6) |
| Étude | Divider, kicker, titre, intro, sg-fade-left, sg-fade-right |
| Dimensionnement | Divider, kicker, titre, intro, sg-fade-left, sg-fade-right |
| Bureau d'étude | Divider, kicker, titre, intro, 2 paragraphes |
| Comprendre le solaire | Divider, kicker, titre, intro, sg-guides-grid (6 cartes) |
| Guides expertise | Kicker/titre/intro SANS animation, sg-guides-grid (3 cartes) |
| Avantages | Divider, kicker, titre, intro |
| FAQ | Divider, kicker, titre, intro |
| Éligibilité | Divider, kicker, titre, intro, paragraphes |
| CTA final | Aucune animation |
