# Rapport de refonte – Hub « Le solaire »

**Date** : 13 mars 2025  
**Page concernée** : `/le-solaire/`

---

## 1. Résumé

La page hub « Le solaire » a été entièrement refaite pour en faire un hub central SolarGlobe : pédagogique, premium et orienté navigation SEO vers les pages expertise.

---

## 2. Modifications réalisées

### 2.1 Hero

| Élément | Avant | Après |
|--------|-------|-------|
| **H1** | Le solaire | Le solaire photovoltaïque : comprendre, produire et économiser |
| **Sous-titre** | Comprendre l'énergie photovoltaïque... | Le solaire photovoltaïque permet aux particuliers de produire leur propre électricité... + SolarGlobe accompagne votre projet de A à Z |
| **CTA principal** | Démarrer mon étude gratuite | Faire mon étude solaire gratuite |
| **Lien CTA** | /etude-gratuite/ | /etude-gratuite/ |

### 2.2 Introduction hub

Nouvelle section « Pourquoi le solaire se développe » :
- Développement du solaire en France
- Intérêt des particuliers (économies, hausses tarifaires, valorisation)
- Importance de bien comprendre avant d'installer

### 2.3 Section 1 : Comment fonctionne le solaire

- **H2** : Comment fonctionne une installation solaire photovoltaïque
- **H3** : Production d'électricité solaire, Autoconsommation, Revente du surplus
- Illustration : schéma installation photovoltaïque (placeholder)

### 2.4 Section 2 : Rentabilité

- **H2** : Les panneaux solaires sont-ils rentables ?
- Contenu : coût, économies, durée de retour
- Lien vers `/rentabilite-solaire/`
- Graphique SVG : évolution économies sur 25 ans

### 2.5 Section 3 : Étude solaire

- **H2** : Pourquoi une étude solaire est indispensable
- Contenu : orientation, inclinaison, ombrage, consommation
- Lien vers `/etude-solaire/`
- Image : analyse toiture solaire (placeholder)

### 2.6 Section 4 : Dimensionnement

- **H2** : Combien de panneaux solaires faut-il pour une maison
- Contenu : puissance, surface, consommation
- Lien vers `/dimensionnement-photovoltaique/`
- Image : calpinage panneaux (placeholder)

### 2.7 Section 5 : Bureau d'étude

- **H2** : Le rôle du bureau d'étude photovoltaïque
- Contenu : analyse technique, simulation, optimisation
- Lien vers `/bureau-etude-photovoltaique/`

### 2.8 Section visuelle premium

Cartes avec image, texte et bouton :
- Étude solaire → /etude-solaire/
- Rentabilité solaire → /rentabilite-solaire/
- Dimensionnement photovoltaïque → /dimensionnement-photovoltaique/
- Bureau d'étude photovoltaïque → /bureau-etude-photovoltaique/

+ Liens vers autoconsommation et rentabilité panneaux

### 2.9 FAQ solaire

5 questions :
- Les panneaux solaires fonctionnent-ils en hiver ?
- Combien coûte une installation solaire ?
- Combien de panneaux pour une maison ?
- Les panneaux solaires sont-ils rentables ?
- Qu'est-ce que l'autoconsommation solaire ?

### 2.10 CTA final

- **Titre** : Votre maison est-elle adaptée au solaire ?
- **Texte** : Une étude solaire permet de connaître précisément...
- **Bouton** : Demander mon étude gratuite → /etude-gratuite/

---

## 3. Images à ajouter

Créer le dossier `/assets/images/le-solaire/` et y placer les images suivantes (format WebP, < 150 KB) :

| Fichier | Alt suggéré | Usage |
|---------|-------------|-------|
| schema-installation.webp | Schéma installation photovoltaïque : panneaux, onduleur, compteur et autoconsommation | Section 1 |
| analyse-toiture.webp | Analyse toiture solaire : orientation, inclinaison et potentiel photovoltaïque | Section 3 |
| calpinage-panneaux.webp | Calpinage panneaux solaires sur toiture maison | Section 4 |
| etude-solaire-card.webp | Étude solaire maison et potentiel toiture | Carte premium |
| rentabilite-card.webp | Rentabilité panneaux solaires et retour sur investissement | Carte premium |
| dimensionnement-card.webp | Dimensionnement installation panneaux solaires maison | Carte premium |
| bureau-etude-card.webp | Bureau d'étude photovoltaïque analyse toiture | Carte premium |

**Fallback** : En l'absence d'images, des placeholders (zones grises + icônes) s'affichent automatiquement.

---

## 4. SEO

- **Title** : Le solaire photovoltaïque : comprendre, produire et économiser | Solarglobe
- **Meta description** : Hub pédagogique sur le solaire photovoltaïque...
- **Schema.org** : BreadcrumbList, WebPage, FAQPage
- **Maillage interne** : 8 liens vers pages expertise + sous-pages le-solaire

---

## 5. Design system

Classes utilisées : `.sg-hero-premium`, `.sg-section`, `.sg-container`, `.sg-section-title`, `.sg-card`, `.sg-faq`, `.sg-cta`, `.sg-btn-primary`, `.sg-btn-outline`, `.text-gold`, `.sg-section-subtitle`.

Structure HTML, header et footer inchangés. Responsive conservé.

---

## 6. Résultat

La page `/le-solaire/` est désormais :

- **Hub SEO** : point d'entrée vers toutes les pages expertise
- **Pédagogique** : explications claires sur le fonctionnement, la rentabilité, l'étude, le dimensionnement
- **Premium** : cartes visuelles, graphique, structure soignée
- **Navigation** : liens vers étude solaire, rentabilité, dimensionnement, bureau d'étude, autoconsommation
