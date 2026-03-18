# Squelette HTML de référence — SolarGlobe

**Source :** index.html (page d'accueil)

## Structure globale

```
<!DOCTYPE html>
<html lang="fr">
<head>
  [GTM] [Meta] [Favicon] [Fonts] [Tailwind] [Styles]
</head>
<body class="bg-black">

  <!-- GTM noscript -->
  <!-- NAV (header fixe) -->
  <!-- Overlay mobile -->
  <!-- Menu mobile -->
  <!-- Scripts (burger + lien actif) -->

  <!-- Hero / Page-header (variable selon page) -->
  <!-- Main content -->
  <!-- Sections -->
  <!-- CTA éventuel -->
  <!-- Footer -->

</body>
</html>
```

## Zones identifiées

| Zone | Élément | Rôle |
|------|---------|------|
| **Topbar** | — | Aucune dans l'index |
| **Header** | `<nav id="main-nav">` | Navigation fixe, logo, menu desktop, CTA, burger |
| **Navigation desktop** | `<ul class="hidden md:flex">` | Liens + lien PRO + icônes réseaux |
| **Navigation mobile** | `<div id="mobile-menu">` | Menu déroulant + overlay |
| **Hero / Page-header** | Variable | Titre H1, intro, CTA (accueil = hero split, autres = section) |
| **Main content** | `<main>` ou sections | Contenu principal |
| **Sections** | `<section>` | Blocs de contenu |
| **CTA** | Liens/boutons | Appels à l'action |
| **Footer** | `<footer>` | 5 colonnes + réseaux + légal |

## Composants à répliquer

### 1. Head
- GTM, meta charset, viewport
- Tailwind + config gold
- Favicon, fonts Montserrat

### 2. Nav (référence index)
- Logo → index
- Liens : Accueil, Qui sommes-nous, Votre projet A→Z, Produits, FAQ, Blog, Contact
- Lien PRO (Espace professionnel)
- Icônes réseaux (Facebook, Instagram, LinkedIn)
- CTA « Étude gratuite »
- Burger mobile

### 3. Overlay + Menu mobile
- Overlay `#mobile-overlay` (z-120)
- Menu `#mobile-menu` (z-130)
- Script toggle

### 4. Script lien actif
- Détection URL courante
- Classe `text-gold` sur lien actif

### 5. Footer (référence faq)
- 5 colonnes : Solarglobe, Navigation, Énergie solaire, (liens), Zones
- Icônes réseaux
- Mentions légales, Confidentialité, Cookies, CGV
