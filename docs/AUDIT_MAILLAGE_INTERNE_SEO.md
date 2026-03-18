# AUDIT MAILLAGE INTERNE SEO — SolarGlobe (VERSION HARDCORE 100%)

**Date :** 18 mars 2025  
**Périmètre :** 165 fichiers HTML — audit exhaustif  
**Base :** https://www.solarglobe.fr/  
**Règle :** Audit uniquement — aucune correction

---

## A. PAGES INDEXABLES AUDITÉES

### Liste complète (sitemap + structure fichiers + canonical)

| Catégorie | Nombre | Exemples |
|-----------|--------|----------|
| Accueil | 1 | `/` |
| Étude gratuite / Contact | 2 | `/etude-gratuite/`, `/contact/` |
| Produits | 5 | `/produits/`, `/produits/panneaux-solaires/`, etc. |
| Le solaire | 7 | `/le-solaire/`, `/le-solaire/autoconsommation-solaire/`, etc. |
| Notre méthode | 8 | `/notre-methode/`, `/notre-methode/etude-solaire/`, `/notre-methode/dimensionnement/`, `/notre-methode/demarches-administratives/`, `/notre-methode/suivi/`, etc. |
| Pages expertise (canonical) | 4 | `/rentabilite-solaire/`, `/etude-solaire/`, `/dimensionnement-photovoltaique/`, `/bureau-etude-photovoltaique/` |
| SEO thématiques | 12 | `/seo/panneaux-solaires/`, `/seo/autoconsommation-solaire/`, etc. |
| SEO villes | 36 | `/seo/villes/argenteuil/`, `/seo/villes/meaux/`, etc. |
| Panneaux par ville | 36 | `/panneaux-solaires-amiens/`, `/panneaux-solaires-meaux/`, etc. |
| Blog | 5 | `/blog/`, `/blog/autonomie-solaire/`, etc. |
| FAQ / Légal | 5 | `/faq/`, `/mentions-legales/`, `/cookies/`, `/cgv/`, `/politique-de-confidentialite/` |

**Total : ~113 URLs indexables** (sitemap)

### Pages non indexables ou doublons

| Page | Statut |
|------|--------|
| `pages-expertise/*.html` | Canonical vers URLs racine (`/rentabilite-solaire/`, etc.) — dupliquées |
| `seo/etude-solaire-gratuite.html` | Canonical vers `/etude-gratuite/` — redirige via JS |
| `qui-sommes-nous.html` | Redirige 301 vers `/notre-methode/` |
| `partenaires.html` | `noindex, nofollow` — exclue du maillage SEO |

---

## B. LIENS INTERNES AUDITÉS

### Répartition par type

| Type | Nombre estimé | Source |
|------|---------------|--------|
| Header (composant partagé) | ~25 | components/header.html |
| Footer (composant partagé) | ~15 | components/footer.html |
| Index home | ~50 | index.html |
| Pages SEO thématiques | ~50/page × 12 | seo/*.html |
| Pages SEO villes | ~20/page × 36 | seo/villes/*.html |
| Panneaux par ville | ~15/page × 36 | panneaux-solaires-xxx/index.html |
| Blog, méthode, produits, etc. | Variable | Autres pages |

**Total : plusieurs milliers de liens internes** (header/footer répétés sur toutes les pages)

---

## C. LIENS CASSÉS

| Source | Lien brut | URL résolue | Raison |
|--------|-----------|-------------|--------|
| **index.html** (ligne 1493) | `href="/qui-sommes-nous/"` | `/qui-sommes-nous/` | **404** — Aucune redirection ni rewrite pour `/qui-sommes-nous/` dans _redirects. Seul `/qui-sommes-nous.html` redirige vers `/notre-methode/`. |
| **qui-sommes-nous.html** (ligne 696) | `href="/qui-sommes-nous"` | `/qui-sommes-nous` | Même page (sans slash) — page redirige vers notre-methode, lien circulaire |
| **etude-solaire-gratuite.html** (ligne 143, 191) | `href="etude-solaire-gratuite"` | Relatif → résolution variable | Lien relatif sans slash — risque selon contexte |
| **etude-solaire-gratuite.html** (ligne 114) | `href="qui-sommes-nous"` | Relatif | Lien relatif — résout vers URL incorrecte depuis etude-solaire-gratuite |

---

## D. LIENS NON CANONIQUES

| Source | Destination actuelle | Destination canonique attendue |
|--------|----------------------|-------------------------------|
| **components/header.html** (lignes 25, 112) | `/pages-expertise/rentabilite-solaire/` | `/rentabilite-solaire/` |
| **components/header.html** (lignes 44, 121) | `/qui-sommes-nous.html` | `/notre-methode/` |
| **index.html** (ligne 1493) | `/qui-sommes-nous/` | `/notre-methode/` |
| **qui-sommes-nous.html** (lignes 702, 721) | `/etude-solaire-gratuite`, `/seo/etude-solaire-gratuite` | `/etude-gratuite/` |
| **etude-solaire-gratuite.html** (lignes 388, 407) | `/etude-solaire-gratuite`, `/seo/etude-solaire-gratuite` | `/etude-gratuite/` |

---

## E. LIENS RELATIFS OU FORMATS NON CONFORMES

| Source | Lien concerné | Type d'écart |
|--------|---------------|--------------|
| **seo/autoconsommation-solaire.html** | `href="panneaux-solaires"` (lignes 74, 126) | Relatif, sans slash final |
| **seo/autoconsommation-solaire.html** | `href="batteries-solaires"` (ligne 119) | Relatif, sans slash final |
| **seo/autoconsommation-solaire.html** | `href="onduleurs-solaires"` (ligne 126) | Relatif, sans slash final |
| **seo/aides-financements.html** | `href="panneaux-solaires"` (lignes 66, 105) | Relatif, sans slash final |
| **seo/aides-financements.html** | `href="onduleurs-solaires"` (ligne 105) | Relatif, sans slash final |
| **components/header.html** | `href="/qui-sommes-nous.html"` | Extension .html dans lien public |
| **seo/*.html** (8 fichiers) | `href="../assets/images/favicon.ico"` | Relatif pour favicon (hors SEO mais incohérent) |

**Résolution des relatifs SEO :**  
Depuis `seo/autoconsommation-solaire.html`, `href="panneaux-solaires"` résout vers `/seo/panneaux-solaires` (sans slash). La rewrite Netlify `/seo/panneaux-solaires/` → `panneaux-solaires.html` peut ne pas matcher `/seo/panneaux-solaires` sans slash → **risque 404 ou comportement variable**.

---

## F. PAGES ORPHELINES OU SOUS-MAILLÉES

| Page / Groupe | Niveau de criticité | Détail |
|---------------|--------------------|--------|
| **36 pages panneaux-solaires-xxx** | **Moyen** | Aucun lien depuis header, footer, index, ni pages SEO. Accessibles uniquement via sitemap et moteurs. Non intégrées au maillage interne. |
| **seo/etude-solaire-gratuite** | Faible | Canonical vers /etude-gratuite/, peu de liens directs (redirection JS) |
| **Pages notre-methode** (demarches-administratives, suivi) | Faible | Liées uniquement via menu header — maillage correct |

---

## G. PROBLÈMES D'ANCRES

| Page | Ancre | Statut |
|------|-------|--------|
| faq/index.html | `#installation`, `#rentabilite`, `#autoconsommation`, `#batteries`, `#administratif` | OK — IDs présents |
| blog/* | `#intro`, `#mythe-realite`, etc. | OK |
| pages-expertise/rentabilite-solaire.html | `#rentabilite-intro` | OK |
| **partenaires.html** | **13× `href="#"`** | Liens non fonctionnels — navigation slides (page noindex, impact SEO limité) |

---

## H. PROBLÈMES DANS HEADER / FOOTER / COMPOSANTS PARTAGÉS

| Composant | Erreur | Impact |
|-----------|--------|--------|
| **header.html** | `href="/qui-sommes-nous.html"` — URL non canonique, redirige 301 | Toutes les pages : lien vers redirection au lieu de destination finale |
| **header.html** | `href="/pages-expertise/rentabilite-solaire/"` — URL non canonique | Canonical de la page cible = `/rentabilite-solaire/`. Maillage pousse une mauvaise version. |
| **footer.html** | Liens SEO conformes | OK |
| **header.html** | "Dimensionnement photovoltaïque" → `/notre-methode/dimensionnement/` | Cohérent (page méthode, pas page expertise) |

---

## I. INCOHÉRENCES SITEMAP / CANONICAL / MAILLAGE

| Détail | Gravité |
|--------|----------|
| **Sitemap** liste `/etude-gratuite/` mais **etude-solaire-gratuite.html** a canonical `https://www.solarglobe.fr/etude-solaire-gratuite` (sans slash) | Confusion d’URLs — plusieurs variantes pour la même page |
| **Header** pointe vers `/pages-expertise/rentabilite-solaire/` alors que **sitemap** et **canonical** = `/rentabilite-solaire/` | Maillage incohérent avec sitemap |
| **36 pages panneaux-solaires-xxx** dans sitemap mais **jamais liées** depuis le site | Pages orphelines côté maillage |
| **seo/etude-solaire-gratuite** dans _redirects (rewrite 200) mais canonical = `/etude-gratuite/` | Duplication potentielle si des liens pointent vers /seo/etude-solaire-gratuite/ |

---

## J. CHAÎNES SEO CASSÉES

| Parcours testé | Étape cassée | Impact |
|----------------|--------------|--------|
| Home → "Découvrir notre histoire" (index) | Clic sur `/qui-sommes-nous/` | **404** — chaîne rompue |
| Home → Header "Qui sommes-nous" | Clic sur `/qui-sommes-nous.html` | Redirige 301 vers notre-methode — fonctionne mais non canonique |
| Home → Header "Rentabilité solaire" | Clic sur `/pages-expertise/rentabilite-solaire/` | Page s’affiche mais canonical = `/rentabilite-solaire/` — dilution de signaux |
| Home → page service → étude gratuite | OK | |
| Home → SEO thématique → ville → autre ville | OK | |
| Ville → thématique SEO → étude gratuite | OK | |
| Index → Panneaux par ville | **Absent** | Aucun lien vers panneaux-solaires-xxx |

---

## K. PATTERNS STRUCTURELS DANGEREUX

| Pattern | Fichiers concernés | Gravité |
|---------|-------------------|---------|
| **Liens relatifs** sans slash dans contenu SEO | seo/autoconsommation-solaire.html, seo/aides-financements.html | Moyenne |
| **Liens .html** dans navigation globale | components/header.html (qui-sommes-nous) | Moyenne |
| **Liens vers URL non canonique** | header → pages-expertise/rentabilite-solaire | Moyenne |
| **Lien 404** dans zone visible | index.html → qui-sommes-nous/ | **Haute** |
| **Favicon relatif** | 8 fichiers seo/*.html | Faible (hors SEO) |
| **Pages orphelines** (sitemap mais pas de liens) | 36 panneaux-solaires-xxx | Moyenne |

---

## L. VERDICT FINAL

# MAILLAGE SEO ENCORE DÉFAILLANT ❌

### Synthèse

| Type | Nombre |
|------|--------|
| **Problèmes bloquants** | 1 (lien 404 `/qui-sommes-nous/` dans index) |
| **Problèmes importants** | 4 (liens non canoniques header, liens relatifs seo/*, pages orphelines) |
| **Problèmes mineurs** | 3 (lien .html, favicon relatifs, ancres # sur partenaires) |

### Raisons du verdict

1. **Lien cassé** : `/qui-sommes-nous/` dans index.html → 404.
2. **Liens non canoniques** : header pointe vers `/pages-expertise/rentabilite-solaire/` et `/qui-sommes-nous.html` au lieu des canoniques.
3. **Liens relatifs** : `panneaux-solaires`, `batteries-solaires`, `onduleurs-solaires` dans seo/*.html — non conformes au standard absolu + slash final.
4. **Pages orphelines** : 36 pages panneaux-solaires-xxx sans lien depuis la navigation.
5. **Incohérence sitemap/maillage** : header pousse une URL non canonique pour la rentabilité solaire.

### Actions recommandées (à titre indicatif — aucune correction appliquée)

1. Remplacer `href="/qui-sommes-nous/"` par `href="/notre-methode/"` dans index.html.
2. Remplacer `href="/qui-sommes-nous.html"` par `href="/notre-methode/"` dans components/header.html.
3. Remplacer `href="/pages-expertise/rentabilite-solaire/"` par `href="/rentabilite-solaire/"` dans components/header.html.
4. Remplacer les liens relatifs dans seo/autoconsommation-solaire.html et seo/aides-financements.html par `/seo/panneaux-solaires/`, `/seo/batteries-solaires/`, `/seo/onduleurs-solaires/`.
5. Ajouter des liens vers les pages panneaux-solaires-xxx depuis l’index ou une section dédiée.
6. Corriger les liens etude-solaire-gratuite / qui-sommes-nous dans etude-solaire-gratuite.html et qui-sommes-nous.html pour pointer vers les canoniques.

---

*Rapport généré par audit exhaustif — aucun correctif automatique appliqué.*
