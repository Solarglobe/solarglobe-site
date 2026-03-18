# AUDIT TECHNIQUE COMPLET – PAGE /produits/

**Date :** 16 mars 2025  
**Fichier analysé :** `produits/index.html`  
**Objectif :** Rapport détaillé sans modification de code

---

## 1 — STRUCTURE HTML ACTUELLE

### Liste des blocs principaux (ordre d'apparition)

| # | Nom du bloc | ID / Classe principale | Type de contenu | Fonction UX |
|---|-------------|------------------------|----------------|-------------|
| 1 | **Hero Produits** | `#hero-produits`, `.sg-hero-premium` | Titre H1, sous-titre, badges (Étude•Devis•Démarches•Pose•Suivi), 3 images produits (panneaux / micro-onduleur / batterie), 2 CTA | Introduction page, accroche visuelle |
| 2 | **Introduction équipements** | `.sg-section`, `.sg-section-dark` | H2 « Nos équipements photovoltaïques », paragraphe intro | Contexte général |
| 3 | **Hub technologies** | `.sg-section`, grille 4 cartes | 4 liens : Panneaux solaires / Onduleurs / Micro-onduleurs / Batteries solaires | Navigation vers sous-pages produits |
| 4 | **Bandeau transition** | `.sg-transition-block` | Ligne décorative | Séparation visuelle |
| 5 | **Assistant choix système** | `#assistant-choix` | Titre, filtres visuels (non fonctionnels), 4 cartes étapes (Puissance / Sans batterie / Avec batterie / Ombres), encadré matériel sélectionné, CTA | Aide à la décision utilisateur |
| 6 | **Listing produits** | `#listing-produits` | Filtres (Tous / Panneaux / Micro-onduleurs / Coffrets / Batteries / Aides financières), 6 cartes produits (LONGi, Dualsun, ATMOCE M-Combiner, ATMOCE Micro-onduleur, ATMOCE Batterie, EcoFlow), CTA expert | Catalogue produits avec filtrage |
| 7 | **Études types économies** | `#etudes-types` | 4 cartes scénarios (Cas #0 à #3) avec économies annuelles, hypothèses, CTA « Estimer mes économies » | Démonstration rentabilité |
| 8 | **Pilotage Shelly** | `#pilotage-shelly` | Titre, 6 scénarios (batterie charge/décharge, chauffe-eau, climatisation, chauffage, borne recharge), CTA | Présentation optimisation autoconsommation |
| 9 | **Garanties** | `#garanties` | Titre, engagements (25 ans panneaux, 25 ans micro-onduleurs, 15 ans batteries), timeline, CTA | Réassurance qualité |
| 10 | **FAQ Produits** | `#faq-produits` | 5 questions/réponses (économies, Shelly, aides, météo, fournisseur) | Réponses aux objections |
| 11 | **Bloc SEO – Accès rapide** | `.sg-section` | Grille 12 liens thématiques + grille 36 villes | Maillage interne SEO |
| 12 | **Pourquoi équipements premium** | `.sg-section` | H2 + paragraphe | Contexte qualité |
| 13 | **FAQ Hub** | `.sg-section`, `.sg-faq` | 3 questions accordéon (marques, micro-onduleurs, batterie) | Questions équipements |
| 14 | **CTA final** | `.sg-cta`, `.sg-cta-dark` | Titre, paragraphe, bouton « Demander mon étude gratuite » | Conversion |

### Liens d’ancrage cassés (à corriger)

- `#bloc-tarifs` : référencé 3 fois (assistant choix) — **section absente**
- `#aides-financements` : référencé par le filtre « Aides financières » — **section absente**
- `#cta-final` : référencé 2 fois (Shelly, Garanties) — **section absente**
- `#comparatif-express` : référencé 6 fois (cartes produits) — **section absente**

---

## 2 — CLASSIFICATION DES BLOCS

| Bloc | Statut recommandé | Destination |
|------|-------------------|-------------|
| Hero Produits | **CONSERVER DANS HUB** | `/produits/` |
| Introduction équipements | **CONSERVER DANS HUB** | `/produits/` |
| Hub technologies | **CONSERVER DANS HUB** | `/produits/` |
| Bandeau transition | **CONSERVER DANS HUB** | `/produits/` |
| Assistant choix système | **CONSERVER DANS HUB** | `/produits/` |
| Listing produits | **DÉPLACER VERS PAGES PRODUITS** | Panneaux → `/produits/panneaux-solaires/`, Micro-onduleurs → `/produits/micro-onduleurs/`, Onduleurs/Coffrets → `/produits/onduleurs/`, Batteries → `/produits/batteries-solaires/` |
| Études types économies | **DÉPLACER VERS PAGE SEO** | `/rentabilite-solaire/` (simulation rentabilité) |
| Pilotage Shelly | **À SIMPLIFIER** ou **DÉPLACER** | Option : garder résumé dans hub, détailler sur page dédiée ou `/le-solaire/autoconsommation-solaire/` |
| Garanties | **CONSERVER DANS HUB** ou **À SIMPLIFIER** | Hub ou page dédiée |
| FAQ Produits | **CONSERVER DANS HUB** | `/produits/` |
| Bloc SEO – Accès rapide | **CONSERVER DANS HUB** | `/produits/` |
| Pourquoi équipements premium | **CONSERVER DANS HUB** | `/produits/` |
| FAQ Hub | **CONSERVER DANS HUB** | `/produits/` |
| CTA final | **CONSERVER DANS HUB** | `/produits/` |

---

## 3 — ANALYSE DES SCRIPTS

| Script | Source | Poids estimé | Utilité | Nécessaire ? | Remplaçable par CSS ? |
|--------|--------|--------------|---------|--------------|------------------------|
| **Google Tag Manager** | Inline | ~2 KB | Analytics, tracking | Oui (business) | Non |
| **Tailwind CSS** | CDN cdn.tailwindcss.com | ~300 KB (runtime) | Styles utilitaires | Oui | Non |
| **GSAP** | CDN cdnjs.cloudflare.com (gsap.min.js) | ~60 KB | Animations | À évaluer | Partiellement |
| **ScrollTrigger** | CDN cdnjs.cloudflare.com | ~25 KB | Animations au scroll | À évaluer | Partiellement |
| **header.js** | /assets/js/header.js | ~2 KB | Injection header, menu mobile | Oui | Non |
| **footer.js** | /assets/js/footer.js | ~0,5 KB | Injection footer | Oui | Non |
| **Script inline – filtres** | Inline | ~0,5 KB | Filtrage cartes par catégorie | Oui | Non |
| **Script inline – reveal cascade** | Inline | ~2 KB | IntersectionObserver + classes `.reveal` | Oui | Partiellement (IntersectionObserver + CSS) |
| **Script inline – GSAP ScrollTrigger** | Inline | ~1 KB | Animations `.reveal` (desktop) | À simplifier | Oui (CSS + IntersectionObserver) |
| **Script inline – FAQ toggle** | Inline | ~0,3 KB | Accordéon FAQ | Oui | Non |
| **Script inline – #etudes-types reveal** | Inline | ~0,5 KB | Reveal spécifique section études | Redondant | Oui (fusionner avec cascade) |

### Scripts non chargés sur /produits/

- `sg-scroll-reveal.js` : **non utilisé** (page utilise GSAP + scripts inline)
- `sg-animations.js` : **non utilisé**
- `sg-counter.js` : **non utilisé**

### Recommandations scripts

1. **GSAP + ScrollTrigger** : ~85 KB — lourd pour des animations reveal. Remplacer par **IntersectionObserver + transitions CSS** (gain ~80 KB).
2. **Doublon animations** : 3 systèmes coexistants (GSAP ScrollTrigger, script cascade inline, script #etudes-types). Unifier sur **IntersectionObserver + CSS**.
3. **Corriger les ancres** : `#bloc-tarifs`, `#aides-financements`, `#cta-final`, `#comparatif-express` pointent vers des sections inexistantes.

---

## 4 — ANALYSE DES ANIMATIONS

| Animation | Type | Implémentation | Performance | Impact UX | Recommandation |
|-----------|------|-----------------|-------------|-----------|----------------|
| **Reveal au scroll** | Apparition progressive | `.reveal` + GSAP ScrollTrigger + script cascade | Moyenne (GSAP lourd) | Bon | Remplacer par IntersectionObserver + `transition` CSS |
| **Product-card reveal** | Cascade cartes | `transition-delay` progressif (360 ms × index) | Correct | Bon | Conserver logique, simplifier déclencheur |
| **Hover cartes produits** | Scale + rotation | `group-hover:scale-105`, `group-hover:rotate-[.5deg]` | Bon | Bon | Conserver |
| **Hover CTA** | Scale | `hover:scale-[1.02]` | Bon | Bon | Conserver |
| **Pulse gold (gsap-cta)** | Pulsation bordure | `@keyframes pulseGold` | Bon | Moyen | Optionnel, peut simplifier |
| **Partner-logo hover** | Scale + filter | `transform: scale(1.08)`, `filter` | Bon | Bon | Conserver |
| **Blur + translateY** | Effet reveal | `filter: blur(10px)`, `translateY(50px)` | Moyen (blur coûteux) | Bon | Réduire blur ou le supprimer sur mobile |
| **ScrollTrigger scrub** | Animation liée au scroll | GSAP `scrub: true` | Lourd | Moyen | Supprimer, garder reveal simple |

### Problèmes identifiés

- **Durées longues** : `transition-duration: 2.8s` et `3.2s` pour `.reveal` — ralentit la perception de chargement.
- **will-change** : Présent sur `.reveal` — correct, mais à limiter aux éléments réellement animés.
- **prefers-reduced-motion** : Géré correctement (lignes 143–151, 1699–1711).

---

## 5 — ANALYSE DES IMAGES

| Chemin | Type | Usage | Statut |
|--------|------|-------|--------|
| `/assets/images/produits/panneaux-hero.avif` | Hero | Hero produits (panneaux) | **CONSERVER** |
| `/assets/images/produits/micro-onduleur-hero.avif` | Hero | Hero produits (micro-onduleur) | **CONSERVER** |
| `/assets/images/produits/batterie-hero.avif` | Hero | Hero produits (batterie) | **CONSERVER** |
| `/assets/images/produits/longi-x10-explorer.avif` | Produit | Carte LONGi | **CONSERVER** – déplacer vers panneaux-solaires |
| `/assets/images/produits/dualsun-flash-500.avif` | Produit | Carte Dualsun | **CONSERVER** – déplacer vers panneaux-solaires |
| `/assets/images/produits/m-combiner-atmoce.avif` | Produit | Carte ATMOCE M-Combiner | **CONSERVER** – déplacer vers onduleurs |
| `/assets/images/produits/micro-onduleur-atmoce-mi500.avif` | Produit | Carte ATMOCE Micro-onduleur | **CONSERVER** – déplacer vers micro-onduleurs |
| `/assets/images/produits/batterie-atmoce-7kwh.avif` | Produit | Carte ATMOCE Batterie | **CONSERVER** – déplacer vers batteries-solaires |
| `/assets/images/produits/ecoflow-batterie-onduleur.avif` | Produit | Carte EcoFlow | **CONSERVER** – déplacer vers batteries-solaires |
| `/assets/images/logo/longi.avif` | Logo | Carte LONGi | **CONSERVER** |
| `/assets/images/logo/dualsun.avif` | Logo | Carte Dualsun | **CONSERVER** |
| `/assets/images/logo/atmoce.avif` | Logo | Cartes ATMOCE | **CONSERVER** |
| `/assets/images/logo/ecoflow.avif` | Logo | Carte EcoFlow | **CONSERVER** |
| `/assets/images/shelly/batterie-charge.avif` | Illustration | Scénario Shelly | **CONSERVER** |
| `/assets/images/shelly/batterie-decharge.avif` | Illustration | Scénario Shelly | **CONSERVER** |
| `/assets/images/shelly/chauffe-eau.avif` | Illustration | Scénario Shelly | **CONSERVER** |
| `/assets/images/shelly/climatisation.avif` | Illustration | Scénario Shelly | **CONSERVER** |
| `/assets/images/shelly/chauffage.avif` | Illustration | Scénario Shelly | **CONSERVER** |
| `/assets/images/shelly/borne-recharge.avif` | Illustration | Scénario Shelly | **CONSERVER** |

**Format** : AVIF — bon pour la performance.  
**Priorité** : Conserver toutes les images existantes.

---

## 6 — ANALYSE SEO

### Structure des titres

| Niveau | Contenu | Statut |
|--------|---------|--------|
| H1 | « Nos produits solaires haut de gamme » | Correct |
| H2 | « Nos équipements photovoltaïques », « Explorez nos équipements », « Quel système pour votre maison ? », etc. | Correct |
| H3 | Sous-titres sections, cartes | Correct |

### Meta & balises

- **Title** : « Nos Produits – Solarglobe | Panneaux solaires premium » — correct
- **Meta description** : Présente et pertinente
- **Canonical** : `https://www.solarglobe.fr/produits/` — correct
- **Open Graph / Twitter Card** : Configurés
- **Robots** : `index, follow`

### Maillage interne

- Liens vers `/produits/panneaux-solaires/`, `/produits/onduleurs/`, `/produits/micro-onduleurs/`, `/produits/batteries-solaires/` — correct
- Bloc SEO : 12 liens thématiques + 36 villes — bon maillage

### Schema.org

- **WebPage** : Présent (URL à corriger : `nos-produits` → `produits`)
- **BreadcrumbList** : Présent (même correction URL)
- **ItemList** + **Product** : 6 produits listés — correct
- **FAQPage** : Présent (3 questions FAQ Hub)
- **LocalBusiness** : Présent

### Points à améliorer

1. **Schema.org** : URLs `nos-produits` incohérentes avec l’URL réelle `produits`.
2. **Schema Product** : Images référencent `.jpg` (ex. `longi-himo6.jpg`) alors que le site utilise `.avif`.
3. **Schema Product** : Nom « LONGi Hi-MO 6 Artist » alors que le contenu affiche « LONGi Hi-MO 10 Explorer ».

---

## 7 — STRUCTURE CIBLE

### Structure future du hub /produits/

```
/produits/ (hub allégé)
├── Hero Produits
├── Introduction équipements
├── Hub technologies (4 cartes)
├── Assistant choix système
├── [Optionnel : aperçu 1–2 produits par catégorie avec lien « Voir tout »]
├── Pilotage Shelly (version courte ou lien)
├── Garanties (version courte)
├── FAQ Produits
├── Bloc SEO – Accès rapide
├── FAQ Hub
└── CTA étude gratuite
```

### Pages produits (contenu déplacé)

| Page | Contenu à recevoir |
|------|--------------------|
| `/produits/panneaux-solaires/` | Cartes LONGi, Dualsun + listing détaillé |
| `/produits/micro-onduleurs/` | Carte ATMOCE Micro-onduleur + listing |
| `/produits/onduleurs/` | Carte ATMOCE M-Combiner + coffrets |
| `/produits/batteries-solaires/` | Cartes ATMOCE Batterie, EcoFlow + listing |

### Page SEO rentabilité

| Page | Contenu à recevoir |
|------|--------------------|
| `/rentabilite-solaire/` | Section « Études types économies » (4 scénarios Cas #0 à #3) |

---

## 8 — RÉSUMÉ DES ACTIONS RECOMMANDÉES

### Priorité haute

1. Corriger les ancres cassées : `#bloc-tarifs`, `#aides-financements`, `#cta-final`, `#comparatif-express` (créer les sections ou rediriger vers des sections existantes).
2. Mettre à jour les Schema.org (URLs, noms produits, chemins images).
3. Remplacer GSAP + ScrollTrigger par IntersectionObserver + CSS pour les animations reveal.

### Priorité moyenne

4. Déplacer le listing produits vers les sous-pages par catégorie.
5. Déplacer la section « Études types économies » vers `/rentabilite-solaire/`.
6. Unifier les scripts d’animation (supprimer les doublons).

### Priorité basse

7. Réduire les durées d’animation (2,8 s → 1–1,5 s).
8. Simplifier ou déplacer la section Pilotage Shelly si la page reste trop longue.

---

**Fin du rapport – Aucune modification de code effectuée.**
