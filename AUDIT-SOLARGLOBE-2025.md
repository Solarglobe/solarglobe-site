# Audit complet du site SolarGlobe

**Date :** 12 mars 2025  
**Périmètre :** Toutes les pages publiques SAUF `partenaires.html` et `proprietaires.html`

---

## Carte du site actuel

```
Accueil (index.html)
├── Qui sommes-nous
├── Votre projet de A à Z
├── Produits
├── FAQ
├── Blog
├── Contact
├── Étude solaire gratuite (tunnel de conversion principal)
│
├── Page de présentation (hub pro, protégée par token)
│
├── Pages utilitaires
│   ├── Merci (post-soumission)
│   ├── Aides financières (article blog)
│   ├── Choisir puissance solaire
│   ├── Autonomie solaire
│   ├── Rendement panneaux
│   └── Contrat apporteur d'affaires
│
├── Pages légales
│   ├── Mentions légales
│   ├── Politique de confidentialité
│   ├── Cookies
│   └── C.G.V
│
└── Silo SEO (/seo/)
    ├── 12 pages thématiques (panneaux, autoconsommation, batteries, etc.)
    └── 36 pages villes (/seo/villes/)
```

---

# 1️⃣ Analyse globale UX / structure

## Ce qui fonctionne bien

- **Navigation principale cohérente** : Header identique sur les pages principales (Accueil, Qui sommes-nous, Projet A→Z, Produits, FAQ, Blog, Contact)
- **Tunnel de conversion clair** : Étude gratuite → Merci, avec CTA bien positionnés
- **Hiérarchie logique** : Accueil → Découverte (Qui sommes-nous, Projet A→Z) → Produits → Conversion (Étude gratuite, Contact)
- **Maillage interne riche** : Bloc SEO en bas d’accueil avec liens vers pages thématiques et villes
- **Lien actif dans le menu** : Script qui met en évidence la page courante (text-gold)

## Problèmes identifiés

### Pages inutiles ou mal positionnées

| Problème | Détail |
|----------|--------|
| **Page de présentation** | Protégée par token/mot de passe, lien "Espace pro" en "+" dans le header. Peu visible et peu compréhensible pour un visiteur. |
| **Duplication etude-solaire-gratuite** | Existe en `/etude-solaire-gratuite` ET `/seo/etude-solaire-gratuite` → risque de cannibalisation SEO. |
| **Aides financières vs aides-financements** | `aides-financieres.html` (article blog) et `seo/aides-financements.html` (page SEO) : confusion possible. |

### Liens cassés / erreurs

| Lien | Page source | Problème |
|------|-------------|----------|
| `contact-fondateur` | qui-sommes-nous.html | **Page inexistante** – lien "Rencontrer les fondateurs" |
| `pourquoi-solarglobe` | index.html (lien certification) | Devrait être `#pourquoi-solarglobe` (ancre sur la même page) |
| `aides-panneaux-solaires` | Toutes les pages villes SEO | **Page inexistante** – doit pointer vers `aides-financements` |
| `lisle-adam` | Pages SEO | **Typo** – le dossier s’appelle `l-isle-adam` |
| `/assets/img/logos/` | qui-sommes-nous.html | Chemins possibles : `assets/images/` ou `assets/img/` – à vérifier |

### Incohérences de navigation

- **C.G.V** : Liens footer vers `/C.G.V` alors que le fichier est `C.G.V.html` (URL peut varier selon la config serveur)
- **Lien Espace pro** : `page-de-presentation.html` en absolu, alors que les autres liens sont relatifs sans `.html`
- **votre-projet-de-a-a-z** : CTA "Étude gratuite" pointe vers `/contact` au lieu de `etude-solaire-gratuite`

### Structure idéale recommandée

```
Niveau 1 - Conversion
├── Accueil
├── Étude gratuite (landing principale)
└── Contact

Niveau 2 - Découverte / Confiance
├── Qui sommes-nous
├── Votre projet de A à Z
├── Produits
└── FAQ

Niveau 3 - Contenu
├── Blog (liste + articles)
└── Silo SEO (thématiques + villes)

Niveau 4 - Utilitaires
├── Merci
├── Mentions légales, CGV, Cookies, Politique confidentialité
└── Page de présentation (pro, noindex)
```

**Recommandations :**
1. Créer une page `contact` ou une section dédiée "Rencontrer les fondateurs" et corriger le lien `contact-fondateur`
2. Corriger `pourquoi-solarglobe` → `#pourquoi-solarglobe`
3. Remplacer tous les liens `aides-panneaux-solaires` par `aides-financements`
4. Corriger `lisle-adam` → `l-isle-adam` dans toutes les pages SEO
5. Unifier les URLs (avec ou sans `.html`, cohérence www/non-www)

---

# 2️⃣ Analyse du design et CSS

## Ce qui fonctionne bien

- **Charte visuelle** : Noir (#0D0D0D, #101010) + or (#C39847) cohérent
- **Typographie** : Montserrat utilisée de façon homogène
- **Séparateurs dorés** : `border-t-2 border-gold` récurrent, bonne cohérence
- **Cartes premium** : `.gold-card`, `.why-card` avec bordures et ombres dorées
- **Responsive** : Breakpoints md/lg utilisés, menu burger sur mobile
- **Animations** : GSAP, ScrollTrigger, effets au scroll maîtrisés

## Problèmes identifiés

### Incohérences CSS

| Problème | Détail |
|----------|--------|
| **Styles dupliqués** | Chaque page redéfinit `.shadow-gold`, `.drop-shadow-gold`, `.gold-card`, animations. Aucun fichier CSS commun. |
| **Tailwind CDN** | Chargé sur chaque page sans purge → CSS non optimisé, poids inutile |
| **Contact** | Icônes réseaux sociaux vides (commentaires `<!-- svg -->` sans contenu) |
| **Page de présentation** | Design très minimal, pas de header/footer commun |
| **Contrat apporteur** | Design totalement différent (fond clair, Arial) – hors charte |
| **Mentions légales** | Faute "Pierre Currie" au lieu de "Pierre Curie" (ou vérifier l’orthographe exacte) |

### Problèmes de layout

- **Index** : Lien `pourquoi-solarglobe` sans `#` ne mène nulle part (section id="pourquoi-solarglobe" sur la même page)
- **Grille villes** : Liens en `block text-center` sans style hover cohérent sur toutes les pages
- **Densité** : Page d’accueil très longue (~1500 lignes) – beaucoup de scroll avant le footer

### Recommandations design

1. **Créer un fichier CSS commun** (`assets/css/solarglobe.css`) avec variables et classes réutilisables
2. **Compiler Tailwind** en production avec purge pour réduire le poids
3. **Compléter les icônes** réseaux sociaux sur la page Contact
4. **Harmoniser** le contrat apporteur (optionnel : garder format document mais appliquer la charte)
5. **Réduire la longueur** de l’accueil : regrouper certaines sections ou ajouter des ancres de navigation

---

# 3️⃣ Analyse du contenu

## Ce qui fonctionne bien

- **Positionnement clair** : "Bureau d’études solaire indépendant" bien mis en avant
- **Argumentaire différenciant** : "Nous ne vendons pas des panneaux, nous concevons des projets"
- **Tableau comparatif** : SolarGlobe vs installateur classique – efficace
- **Preuves** : RGE, QualiPV, garanties 25 ans, packs tarifaires
- **Ton professionnel** : Transparence, sans promesses excessives

## Problèmes identifiés

### Encodage UTF-8

- **contact.html** : `â€"`, `Ã©`, `dÃ©diÃ©` dans title et meta – encodage incorrect
- **etude-solaire-gratuite.html** : `Ã‰tude`, `Ã©`, `dÃ©faut` – idem
- **votre-projet-de-a-a-z.html** : `Ã `, `Ã©`, `â€"` – idem
- **Plusieurs pages** : Caractères mal encodés dans les meta et titres

### Contenus à améliorer

| Page | Problème |
|------|----------|
| **Pages villes** | Paragraphe bourré de mots-clés : "En combinant panneaux solaires, autoconsommation solaire, batteries solaires, onduleurs solaires..." – lourd et peu naturel |
| **SEO** | Certaines pages génériques (ex. panneaux-solaires) : contenu correct mais peu différenciant |
| **Blog** | À vérifier : articles récents, qualité, fréquence |
| **FAQ** | Contenu riche, bien structuré – point fort |

### Recommandations rédactionnelles

1. **Corriger l’encodage** : S’assurer que tous les fichiers sont en UTF-8 sans BOM et que les serveurs envoient le bon charset
2. **Réécrire les paragraphes villes** : Texte plus naturel, moins de répétition de mots-clés
3. **Renforcer l’expertise** : Chiffres, témoignages, cas clients si possible
4. **Uniformiser** : "SolarGlobe" vs "Solarglobe" – choisir une graphie

---

# 4️⃣ Analyse SEO complète

## Ce qui fonctionne bien

- **Balises** : meta title, description, canonical présentes sur la plupart des pages
- **Open Graph / Twitter** : Configurés sur les pages principales
- **Schema.org** : LocalBusiness, WebSite, BreadcrumbList sur plusieurs pages
- **Structure H1** : Une seule H1 par page en général
- **Maillage interne** : Bloc SEO riche sur l’accueil, liens entre pages thématiques

## Problèmes identifiés

### Structure et balises

| Problème | Détail |
|----------|--------|
| **Canonical** | Incohérence : `solarglobe.fr` vs `www.solarglobe.fr` selon les pages |
| **Meta descriptions** | Certaines trop longues ou trop courtes ; à optimiser pour 150–160 caractères |
| **Duplication** | `etude-solaire-gratuite` (racine) et `seo/etude-solaire-gratuite` → risque de cannibalisation |
| **Page de présentation** | `noindex, nofollow` – cohérent pour une page protégée |

### URLs et structure

| Problème | Détail |
|----------|--------|
| **C.G.V** | URL avec majuscules et points – peu recommandé |
| **Profondeur** | Pages villes à 3 niveaux (/seo/villes/troyes) – acceptable |
| **Pages orphelines** | `contrat-apporteur-solarglobe.html` peu ou pas liée |
| **aides-financieres** | Article blog à la racine – pourrait être dans /blog/ |

### Pages SEO

| Problème | Détail |
|----------|--------|
| **aides-panneaux-solaires** | Liens partout – page n’existe pas (rediriger vers aides-financements) |
| **Contenu villes** | Trop optimisé, risque de pénalité |
| **Headers** | Bonne hiérarchie H1 > H2 > H3 sur les pages thématiques |

### Stratégie SEO recommandée

1. **Unifier le domaine** : `www.solarglobe.fr` partout (canonical, OG, liens)
2. **Fusionner ou rediriger** : `seo/etude-solaire-gratuite` → redirection 301 vers `/etude-solaire-gratuite`
3. **Renommer C.G.V** : `cgv` ou `conditions-generales-vente`
4. **Créer aides-panneaux-solaires** OU remplacer tous les liens par aides-financements
5. **Structurer le blog** : `/blog/aides-financieres` pour les articles
6. **Lier** le contrat apporteur depuis une page dédiée (ex. partenaires) si pertinent

---

# 5️⃣ Analyse SEO pour les IA (LLM SEO)

## État actuel

- **Schema.org** : LocalBusiness, Organization, Service – bien structurés
- **Contenu expert** : FAQ détaillée, pages thématiques avec explications
- **Données structurées** : BreadcrumbList, AboutPage sur certaines pages

## Ce qui manque pour être cité par les IA

| Élément | Recommandation |
|--------|----------------|
| **FAQPage schema** | Ajouter un schéma FAQPage sur la page FAQ pour les rich results |
| **Article schema** | Sur les articles blog (BlogPosting) |
| **HowTo schema** | Sur "Votre projet de A à Z" (étapes) |
| **Contenu de référence** | Guides longs, chiffres, études – format "source fiable" |
| **Page "À propos" dédiée** | Renforcer la page Qui sommes-nous avec historique, chiffres clés |
| **Données chiffrées** | "X projets réalisés", "Y kW installés" – à afficher clairement |

## Recommandations LLM SEO

1. **Ajouter FAQPage** sur faq.html
2. **Ajouter HowTo** sur votre-projet-de-a-a-z.html
3. **Créer une page "Chiffres clés"** ou section dédiée avec données vérifiables
4. **Rédiger des guides** (PDF ou pages) : "Guide autoconsommation 2025", "Calcul rentabilité"
5. **Citer des sources** officielles (ADEME, Enedis) pour renforcer l’autorité

---

# 6️⃣ Analyse technique

## Performance

| Élément | État |
|--------|------|
| **Tailwind CDN** | Non optimisé, CSS complet chargé |
| **GSAP** | Chargé 2 fois sur index.html (lignes 69–70 et 1150–1151) |
| **Images** | Format AVIF utilisé – bon choix |
| **Fonts** | Google Fonts avec display=swap – correct |
| **Scripts** | Plusieurs scripts inline, pas de lazy loading systématique |

## Structure HTML

- **Validité** : À vérifier (balises fermées, attributs)
- **Accessibilité** : `aria-label` sur certains liens, `focus-visible` sur quelques pages
- **Sémantique** : Usage de `<main>`, `<section>`, `<article>` – correct

## Problèmes techniques

| Problème | Détail |
|----------|--------|
| **GSAP dupliqué** | index.html charge GSAP deux fois |
| **Modales produits** | Script dupliqué (ouverture/fermeture) dans index.html |
| **GTM noscript** | C.G.V.html : `ns.html?id=` au lieu de `ns.html?id=` (typo possible) |
| **Cookie banner** | Présent sur plusieurs pages avec code dupliqué |
| **Pas de sitemap** | Aucun sitemap.xml visible dans l’arborescence |

## Recommandations techniques

1. **Supprimer le chargement double** de GSAP sur index.html
2. **Extraire** le cookie banner et le menu dans des composants inclus
3. **Générer un sitemap.xml** pour toutes les pages indexables
4. **Vérifier** les chemins d’assets (`/assets/images/` vs `assets/images/`)
5. **Tester** l’accessibilité (WCAG 2.1 niveau AA) avec un outil type axe DevTools

---

# 7️⃣ Conclusion

## 1. Résumé des problèmes majeurs

| Priorité | Problème |
|----------|----------|
| **P0** | Liens cassés : `contact-fondateur`, `aides-panneaux-solaires`, `lisle-adam` |
| **P0** | Encodage UTF-8 sur contact, etude-solaire-gratuite, votre-projet-de-a-a-z |
| **P0** | Lien `pourquoi-solarglobe` sans ancre `#` |
| **P1** | Duplication SEO etude-solaire-gratuite (racine vs /seo/) |
| **P1** | Incohérence canonical (www vs non-www) |
| **P1** | GSAP chargé deux fois sur index |
| **P2** | Page de présentation peu intégrée |
| **P2** | Contenu villes trop optimisé |
| **P2** | Absence de sitemap.xml |

## 2. Améliorations prioritaires (P0–P1)

1. Corriger tous les liens cassés (contact-fondateur, aides-panneaux-solaires, lisle-adam, pourquoi-solarglobe)
2. Corriger l’encodage UTF-8 sur les pages concernées
3. Mettre en place une redirection 301 de `seo/etude-solaire-gratuite` vers `etude-solaire-gratuite`
4. Unifier les canonical sur `www.solarglobe.fr`
5. Supprimer le chargement en double de GSAP
6. Vérifier et corriger les chemins des logos dans qui-sommes-nous (`/assets/img/logos/`)

## 3. Améliorations secondaires (P2)

1. Créer un fichier CSS commun et optimiser Tailwind
2. Ajouter FAQPage et HowTo schema
3. Générer un sitemap.xml
4. Réécrire les paragraphes des pages villes
5. Harmoniser le design du contrat apporteur
6. Compléter les icônes réseaux sur la page Contact

## 4. Roadmap d’optimisation

```
Phase 1 - Corrections critiques (1–2 jours)
├── Liens cassés
├── Encodage UTF-8
├── Lien pourquoi-solarglobe
└── GSAP dupliqué

Phase 2 - SEO (3–5 jours)
├── Redirection etude-solaire-gratuite
├── Unification canonical
├── Sitemap.xml
└── Correction aides-panneaux-solaires / lisle-adam

Phase 3 - UX / Design (1–2 semaines)
├── CSS commun
├── Icônes Contact
├── Vérification chemins assets
└── Page contact-fondateur ou section dédiée

Phase 4 - Premium / LLM (2–4 semaines)
├── Schema FAQPage, HowTo
├── Réécriture contenu villes
├── Guides et contenu expert
└── Optimisation performance (Tailwind compilé)
```

---

*Audit réalisé le 12 mars 2025. Document à conserver et à mettre à jour après chaque phase d’optimisation.*
