# Rapport – Refonte complète du hub /produits/ (PROMPT 4B)

**Date :** 16 mars 2025  
**Fichier modifié :** `produits/index.html`  
**Objectif :** Transformer la page en vrai hub produits efficace, clair, premium, rapide et orienté navigation.

---

## 1. Scripts supprimés

| Élément | Statut |
|--------|--------|
| GSAP (cdnjs.cloudflare.com) | ✅ Supprimé |
| ScrollTrigger (cdnjs.cloudflare.com) | ✅ Supprimé |
| Script IntersectionObserver / reveal cascade | ✅ Supprimé |
| Script filtres `.chip-filter` | ✅ Supprimé (filtres supprimés) |
| Script GSAP `gsap.utils.toArray('.reveal')` | ✅ Supprimé |
| Script reveal `#etudes-types` | ✅ Supprimé (section inexistante) |

**Scripts conservés :**
- GTM (Google Tag Manager)
- `header.js`
- `footer.js`
- Script FAQ (toggle `.sg-faq-item`)

---

## 2. Styles supprimés

| Style | Statut |
|-------|--------|
| `.reveal`, `.reveal.is-visible` | ✅ Supprimé |
| `.product-card.reveal`, `.product-card.reveal:not(.is-visible)` | ✅ Supprimé |
| `#etudes-types` (tous les styles) | ✅ Supprimé |
| `#comparatif-express` (tous les styles) | ✅ Supprimé |
| `.gsap-cta::after` (pulsation) | ✅ Supprimé |
| `.partner-logo` | ✅ Supprimé |
| `@keyframes pulseGold` (dupliqué) | ✅ Supprimé |
| `.no-scrollbar` | ✅ Supprimé |
| `.drop-shadow-gold` | ✅ Supprimé |

**Styles conservés :**
- `body.menu-open { overflow: hidden }`
- `.shadow-gold` (utilisé si besoin)

---

## 3. Séparateurs (sg-transition-block)

| Avant | Après |
|-------|-------|
| 5+ séparateurs | **2 séparateurs** |

**Emplacements conservés :**
1. Après l’introduction hub (avant les catégories)
2. Avant la FAQ (avant le CTA final)

---

## 4. Sections supprimées ou réduites

| Section | Action |
|---------|--------|
| `#etudes-types` | ✅ Supprimée (n’existait pas dans le DOM) |
| `#comparatif-express` | ✅ Supprimée (n’existait pas) |
| Filtres « Filtrer par » (boutons) | ✅ Supprimés |
| `#pilotage-shelly` (6 cartes Shelly) | ✅ Réduite en bloc résumé (titre + texte court + 1 CTA) |
| `#garanties` (timeline lourde) | ✅ Simplifiée en 3 cartes (25 ans, 15 ans, 10 ans) |
| `#faq-produits` (5 questions) | ✅ Réduite à 3 questions |
| « Découvrez tout sur l’énergie solaire » (12 liens) | ✅ Remplacée par « Accéder directement à la bonne page » (4 liens premium) |
| Grille 36 villes | ✅ Supprimée |

---

## 5. Nouvelles sections ajoutées

| Section | Description |
|---------|-------------|
| **Introduction hub courte** | Titre « Choisir les bons équipements pour son installation solaire » + 2 paragraphes orientés SEO |
| **Liens rapides par besoin** | 4 grands liens : panneaux, micro-onduleurs vs onduleur, batteries, étude gratuite |
| **Pilotage Shelly (résumé)** | Bloc court avec titre, texte et CTA vers étude gratuite |

---

## 6. Structure finale du hub (ordre)

1. **Hero** – H1 « Nos produits solaires haut de gamme », sous-titre, 3 visuels (panneaux, micro-onduleur, batterie), CTA principal + CTA secondaire vers `#categories-produits`
2. **Introduction hub courte** – Choisir les bons équipements, 4 familles
3. **Catégories produits** (4 cartes) – Panneaux, onduleurs, micro-onduleurs, batteries (titre, mini-texte, 3 points clés, CTA « Découvrir »)
4. **Comment choisir votre système** – Assistant simplifié (4 cartes étapes + bloc matériel SolarGlobe)
5. **Pourquoi SolarGlobe sélectionne ces technologies** – 4 colonnes : performance, fiabilité, garanties, compatibilité
6. **Liens rapides vers les sous-pages** – 4 grands liens par besoin
7. **Pilotage Shelly** – Bloc résumé
8. **Garanties** – 3 cartes (25 ans, 15 ans, 10 ans)
9. **FAQ courte** – 3 questions
10. **CTA final**

---

## 7. Liens vers les 4 sous-pages vérifiés

| Page | URL | Statut |
|------|-----|--------|
| Panneaux solaires | `/produits/panneaux-solaires/` | ✅ OK |
| Onduleurs | `/produits/onduleurs/` | ✅ OK |
| Micro-onduleurs | `/produits/micro-onduleurs/` | ✅ OK |
| Batteries solaires | `/produits/batteries-solaires/` | ✅ OK |

---

## 8. Schema.org corrigé

| Ancienne URL | Nouvelle URL |
|--------------|--------------|
| `https://www.solarglobe.fr/nos-produits` | `https://www.solarglobe.fr/produits/` |
| `@id` WebPage | `https://www.solarglobe.fr/produits/#webpage` |
| `@id` BreadcrumbList | `https://www.solarglobe.fr/produits/#breadcrumb` |
| `@id` ItemList | `https://www.solarglobe.fr/produits/#itemlist` |
| Breadcrumb item 2 | `https://www.solarglobe.fr/produits/` |
| ItemList | 4 items (panneaux, onduleurs, micro-onduleurs, batteries) avec URLs correctes |

**Schema supprimés :** ItemList détaillé avec 6 produits (LONGi, Dualsun, ATMOCE…) – remplacé par une liste des 4 catégories du hub.

---

## 9. Hero – modifications

| Élément | Avant | Après |
|--------|-------|-------|
| H1 | « Nos produits solaires haut de gamme » | Conservé |
| Sous-titre | « Des équipements sélectionnés pour leur performance… » | « Panneaux solaires, onduleurs, micro-onduleurs et batteries : découvrez les technologies… » |
| CTA principal | « Démarrer mon étude gratuite » | « Demander mon étude gratuite » → `/etude-gratuite/` |
| CTA secondaire | « Voir nos produits » → `/produits/panneaux-solaires/` | « Explorer les équipements » → `#categories-produits` |

---

## 10. Assistant choix – modifications

| Élément | Avant | Après |
|---------|-------|-------|
| Filtres « Filtrer par » | 4 boutons (Sans batterie, Avec batterie, 3/6/9 kWc, Ombres) | ✅ Supprimés |
| Carte puissance | → `/etude-gratuite/` | ✅ Conservé |
| Carte sans batterie | → `/etude-gratuite/` | → `/produits/micro-onduleurs/` |
| Carte avec batterie | → `/etude-gratuite/` | → `/produits/batteries-solaires/` |
| Carte ombres | → `/etude-gratuite/` | → `/produits/micro-onduleurs/` |
| Bloc matériel SolarGlobe | CTA → `/etude-gratuite/` | Liens vers panneaux et micro-onduleurs + CTA étude |

---

## 11. Résumé des gains

- **Performance :** suppression de GSAP (~100 Ko) et ScrollTrigger (~30 Ko)
- **Lisibilité :** structure claire, 4 familles visibles en un coup d’œil
- **Navigation :** liens directs vers les 4 sous-pages et vers l’étude gratuite
- **Maintenance :** suppression du code mort (#etudes-types, #comparatif-express)
- **Design :** 2 séparateurs, pas d’animations lourdes, transitions CSS légères

---

*Rapport généré à l’issue de la refonte PROMPT 4B.*
