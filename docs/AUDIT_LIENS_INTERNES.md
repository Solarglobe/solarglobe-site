# Audit exhaustif des liens internes — SolarGlobe (repo statique)

**Date :** 2026-03-20  
**Périmètre :** fichiers présents dans le dépôt uniquement (pas de test HTTP en production).  
**Méthode :** inventaire `**/*.html` (hors `node_modules`), extraction des `<a href>`, résolution vers chemins disque sous la racine du site, lecture de `vercel.json` et `.htaccess`.

---

## A. Inventaire des fichiers / routes réelles

| Catégorie | Détail factuel |
|-----------|----------------|
| Fichiers HTML recensés | **114** fichiers `.html` sous la racine du projet |
| Modèle dominant | Dossier + `index.html` (ex. `contact/index.html` → URL canonique attendue `/contact/`) |
| Fichiers `.html` à la racine | `index.html`, `partenaires.html`, `contrat-apporteur-solarglobe.html`, `C.G.V.html`, `autonomie-solaire.html`, `choisir-puissance-solaire.html`, `rendement-panneaux.html`, `aides-financieres.html`, `google8216ab55dcee3d13.html`, `_header-global.html` |
| Pages locales | Préfixe `panneaux-solaires-*/index.html` (villes + départements + région Île-de-France) |
| SEO piliers | `seo/*/index.html` — **pas** de fichiers `seo/<slug>.html` dans le repo |
| `le-solaire` | Sous-dossiers avec `index.html` uniquement (pas de `le-solaire/<page>.html`) |
| Doublons structurels | `bureau-etude-photovoltaique/index.html` **et** `pages-expertise/bureau-etude-photovoltaique/index.html` ; idem `dimensionnement-photovoltaique`, `rentabilite-solaire`, `etude-solaire` — **deux arborescences parallèles** ; aucune occurrence de `href="/pages-expertise/` dans le grep HTML (les doublons sont surtout un risque SEO / maintenance, pas un lien mort) |

**Convention cible (Vercel — `vercel.json`)**  
- `"trailingSlash": true`  
- `"cleanUrls": true`  

**Apache (`.htaccess`)**  
- `DirectoryIndex index.html`  
- Réécritures `le-solaire/`, `notre-methode/`, `produits/`, `seo/` vers `…/$1.html` **si** fichier/répertoire physique absent — or les `seo/*.html` **n’existent pas** : en pratique ce sont surtout les **répertoires** `seo/<slug>/` qui servent `index.html`.  
- **Risque hébergeur :** URL sans slash final selon la config exacte du serveur (voir section G.3).

---

## B. Inventaire des liens internes (`<a href>`)

| Métrique | Valeur |
|----------|--------|
| Liens internes analysés (hors `mailto:`, `tel:`, `#`, `http(s)` externes) | **1870** |
| Résolus vers un **fichier existant** sur le disque | **1870** |
| **Aucun** `<a href>` interne ne pointe vers un chemin inexistant dans le repo | **0 lien `<a>` cassé fichier** |

*Exclusions : liens externes, ancres seules, mailto/tel. Les PDF sous `/assets/.../*.pdf` ont été vérifiés comme fichiers présents (ex. fiches techniques produits).*

---

## C. Croisement liens ↔ fichiers (synthèse)

- **Statut technique global des `<a>` internes :** **OK** (fichier cible présent).  
- **Statut sémantique / UX :** plusieurs liens du bloc géographique de l’accueil envoient vers une **page hub** (département ou grande ville) alors que le libellé est une **autre commune** — ce n’est pas une 404 mais une **incohérence contenu ↔ URL** (voir §4 et tableau critique sémantique).  
- **Hors `<a>` :** le JSON-LD `SearchAction` de `index.html` référence `https://www.solarglobe.fr/recherche?q=…` — **aucune** route `recherche/` ou fichier équivalent dans le repo → **“lien logique” mort** pour un moteur qui exécuterait l’action (voir §2).

---

## D. Priorité — page d’accueil (`index.html`)

### État actuel de la zone (post-refonte récente)

La capture utilisateur mentionnait **trois** boutons (« Découvrez l’énergie solaire », « Nos zones d’intervention », « Nos installations solaires par ville »). **Dans le repo actuel**, il n’y a plus que **deux** boutons :

1. **Découvrez l’énergie solaire** → panneau thématique (produits, le-solaire, seo rentabilité, étude gratuite).  
2. **Villes, départements & région** → pilules départements IDF + grille de communes + lien vers la page régionale.

Le panneau **« Nos installations solaires par ville »** a été **fusionné/supprimé** ; les villes qui n’y figuraient que là (ex. Versailles, Cergy, Melun, Nanterre, Créteil) sont **intégrées** dans la grille unique.

### Audit item par item (grille + pilules)

Tous les `href` de cette section **résolvent** vers un `…/index.html` existant.  
**Problèmes restants (sémantique / gravité) :**

| Libellé affiché | `href` | Fichier servi | Problème | Gravité |
|-----------------|--------|---------------|----------|---------|
| **Montmorency** | `/panneaux-solaires-val-doise/` | `panneaux-solaires-val-doise/index.html` | **Erreur géographique :** Montmorency est en **Hauts-de-Seine (92)**, pas Val-d’Oise. | **Élevée** (contrefait la zone d’intervention) |
| Lagny-sur-Marne, Provins | `/panneaux-solaires-seine-et-marne/` | dept 77 | Hub département acceptable si assumé ; pas une page « Lagny ». | Moyenne (SEO/UX) |
| Étampes, Dourdan | `/panneaux-solaires-essonne/` | dept 91 | Idem | Moyenne |
| L’Isle-Adam, Magny-en-Vexin | `/panneaux-solaires-val-doise/` | dept 95 | Cohérent | Basse |
| Senlis | `/panneaux-solaires-beauvais/` | Oise — hub | Acceptable comme proxy | Moyenne |
| Nogent-sur-Oise | `/panneaux-solaires-compiegne/` | Oise — hub | Acceptable | Moyenne |
| Saint-Quentin | `/panneaux-solaires-laon/` | Aisne — autre ville | Hub discutable | Moyenne |
| Château-Thierry | `/panneaux-solaires-soissons/` | Aisne | Hub discutable | Moyenne |
| Épernay, Châlons, Vitry-le-François | `/panneaux-solaires-reims/` | Marne | Hub « Grand Est » | Moyenne |
| Troyes, Romilly, Sainte-Savine, Bar-sur-Seine | `/panneaux-solaires-reims/` | Aube / voisinage | **Très discutable** géographiquement (Troyes ≠ Reims) | **Élevée** pour Troyes |
| Sens | `/panneaux-solaires-orleans/` | Yonne vs Loiret | Très large géographiquement | Moyenne |
| Auxerre, Joigny, Migennes | `/panneaux-solaires-chartres/` | Yonne vs Eure-et-Loir | Très large | Moyenne |
| Montargis, Gien, Olivet | `/panneaux-solaires-orleans/` | Loiret | Cohérent comme hub 45 | Basse |
| Évry-Courcouronnes | `/panneaux-solaires-evry/` | `panneaux-solaires-evry/index.html` | Libellé officiel vs slug `evry` — **OK** techniquement | Basse |

---

## E. Footer global (`components/footer.html`)

| Lien | Cible résolue | Statut fichier |
|------|---------------|----------------|
| `/`, `/le-solaire/`, `/notre-methode/`, `/qui-sommes-nous/`, `/contact/`, `/produits/`, `/faq/`, `/blog/`, `/etude-gratuite/` | `*/index.html` | OK |
| `/seo/…/` (6 entrées) | `seo/*/index.html` | OK |
| `/mentions-legales/`, `/politique-de-confidentialite/`, `/cookies/`, `/cgv/` | OK | OK |

**Remarque :** le footer charge via `fetch("/components/footer.html")` — la **ressource** `components/footer.html` existe ; ce n’est pas un lien `<a>` mais une dépendance runtime.

---

## F. Normalisation du routing statique

| Source | Règle |
|--------|--------|
| **Vercel** | `trailingSlash: true` + `cleanUrls` → URLs canoniques de type `/chemin/` |
| **Liens dans le HTML** | Très majoritairement **slash final** sur les pages « dossier » |
| **Fichiers seuls** | Ex. `/mentions légales` servies par dossier ; `C.G.V.html` à la racine coexiste avec `cgv/index.html` → **double accès possible** selon hébergeur (risque doublon, pas traité comme lien mort dans les `<a>` du footer qui pointent vers `/cgv/`) |
| **`.htaccess`** | Réécritures vers `*.html` pour certains segments si pas de fichier/dossier — alignement à vérifier sur **Apache** pour URLs **sans** slash final |

---

## G. Rapport final (5 blocs demandés)

### 1. Résumé exécutif

- **Liens internes `<a>` scannés :** 1870  
- **Valides (fichier cible présent) :** 1870  
- **Cassés (fichier absent) :** **0**  
- **À risque :** (a) **JSON-LD** `SearchAction` → `/recherche` inexistante ; (b) **incohérences sémantiques** grille accueil (dont **Montmorency** / **Troyes**…) ; (c) **Apache** si servi sans équivalent Vercel pour URLs sans `/` ; (d) **doublons** `pages-expertise/` vs racine.  
- **Cause principale des plaintes utilisateur antérieures :** faux liens en `<span>` — **corrigé** dans la version actuelle du repo (tout est `<a>` avec cible existante).

### 2. « Liens cassés » critiques

**Aucun `<a href>` interne ne mène à un fichier absent.**

| Type | Source | Cible | Problème exact | Correctif logique recommandé |
|------|--------|-------|----------------|------------------------------|
| JSON-LD (pas un `<a>`) | `index.html` | `https://www.solarglobe.fr/recherche?q={search_term_string}` | Aucune page `recherche` dans le repo | Retirer le bloc `SearchAction` ou créer une vraie page recherche ; sinon Google peut indexer une action invalide |
| Sémantique | `index.html` | Montmorency → `val-doise` | Mauvais département | Pointer vers `/panneaux-solaires-hauts-de-seine/` ou page ville dédiée si créée |
| Sémantique | `index.html` | Troyes → `reims` | Hub trop éloigné / autre région cognitive | Page Aube dédiée, ou `/etude-gratuite/`, ou retirer le libellé précis |

### 3. Liens à risque / incohérences de convention

- **Trailing slash :** aligné avec Vercel sur la plupart des pages ; vérifier cas marginaux sur Apache sans slash.  
- **Pas de `seo/foo.html` :** uniquement `seo/foo/index.html` — les règles `.htaccess` « vers .html » sont potentiellement **redondantes ou trompeuses** si mal comprises en maintenance.  
- **Doublons contenu :** `pages-expertise/*` vs pages racine — pas de lien mort, risque **SEO duplicate**.  
- **Fichiers racine orphelins** (`rendement-panneaux.html`, etc.) vs URLs propres `/blog/...` — à cartographier si des anciens liens pointent encore vers eux (hors périmètre grep `<a>` ici).

### 4. Focus page d’accueil (aligné capture / état repo)

- **Troisième bouton** de la capture : **n’existe plus** dans le HTML actuel ; remplacé par une section unifiée.  
- **Tous les href** du bloc local **existent** sur disque.  
- **À corriger en priorité :** libellé **Montmorency** + pertinence **Troyes / Aube** → **Reims**.  
- Le reste est une **stratégie de hubs** (département ou grande ville) : à documenter en légende pour l’utilisateur (« page département ») plutôt que liste de villes trompeuse.

### 5. Plan de correction recommandé (sans implémentation ici)

1. **Corriger** le couple **Montmorency** → URL **Hauts-de-Seine** (ou page ville future).  
2. **Revoir** les hubs **Aube / Yonne** (Troyes, Sens, Auxerre…) : page dédiée, lien étude gratuite, ou libellé explicite « zone X — en savoir plus ».  
3. **Nettoyer** le **JSON-LD** `SearchAction` si pas de moteur de recherche.  
4. **Décider** d’une **convention unique** documentée (`/chemin/` partout + comportement Apache mirror de Vercel).  
5. **Audit secondaire** (optionnel) : `link rel="canonical"`, `src` images, `fetch()` vers `components/*.html` en 404 sur certains hébergeurs mal configurés.  
6. **Décider du sort** de `pages-expertise/` (redirect 301 vers canoniques ou suppression).

---

*Script utilisé pour les chiffres : `scripts/audit_internal_links.py` — sortie brute : `scripts/_audit_links_output.txt`.*
