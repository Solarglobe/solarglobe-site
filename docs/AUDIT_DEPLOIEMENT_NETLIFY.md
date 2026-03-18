# AUDIT DÉPLOIEMENT NETLIFY — SOLARGLOBE

**Date :** 18 mars 2025  
**Objectif :** Déterminer si le site est prêt à être déployé sur Netlify.

---

## 1. TYPE DE PROJET

| Critère | Résultat |
|---------|----------|
| **Type** | **Projet statique** (HTML/CSS/JS simple) |
| Build (Vite, React, etc.) | ❌ Aucun |
| `package.json` à la racine | ❌ Absent |
| `vite.config` / `webpack` | ❌ Absent |

Le dossier `scripts/` contient un `package.json` pour Playwright (audits) — **non utilisé pour le site**.

---

## 2. CONFIGURATION DÉPLOIEMENT

| Paramètre | Valeur |
|-----------|--------|
| **Dossier racine du site** | **Racine du projet** (`.` ou `/`) |
| **Commande de build** | Aucune |
| **Dossier de sortie** | N/A (site statique direct) |

**Configuration Netlify recommandée :**
- **Publish directory :** `.` (ou laisser vide)
- **Build command :** (vide)
- **Base directory :** (vide)

---

## 3. FONCTIONNEMENT EN LOCAL

### ✅ Points OK
- Structure HTML cohérente
- Header/footer chargés dynamiquement via `fetch` (`/components/header.html`, `/assets/js/footer.js`)
- `_redirects` Netlify présent et bien structuré
- Liens internes en chemins relatifs ou absolus depuis la racine (`/`)
- Pas de PHP, pas de backend

### ❌ Problèmes critiques

#### A. Images manquantes
**Aucune image réelle dans le projet.** Le dossier `assets/images/` ne contient que :
- `solaire/schema-energie-premium.svg`
- `solaire/IMAGES_A_AJOUTER.txt`

**Images référencées mais absentes (liste non exhaustive) :**
- `favicon.png`, `favicon.ico`, `og-image.jpg`
- `logo-solarglobe-rect.png`, `logo-rge.png`, `logo-rge.avif`
- `accueil/hero-solarglobe.avif`, `accueil/visuel-energie-waouh-fullblack.avif`
- `accueil/bloctarifs/*.avif`, `accueil/bloc6-cta2.avif`
- `partenaire/maison-photovoltaique.webp`, `partenaire/maison_produit.webp`
- `produits/*.avif` (longi, atmoce, etc.)
- `logo/*.avif` (longi, dualsun, atmoce, isypv, domos)
- `qui-sommes-nous.webp`, `projetaaz/duo-benoit-nicolas.webp`
- `og/og-a-propos.jpg`, `icons/apple-touch-icon.png`
- `ton-visuel.jpg`, `simulateur-poster.jpg`, `final-dualsun.webp`, `final-longi.webp`, `cta-unique.webp`

**Impact :** Toutes les pages afficheront des images cassées (icônes 404).

#### B. Vidéos manquantes
Le dossier `assets/videos/` est **vide**. Le simulateur d’étude gratuite référence :
- `step1-carte.mp4`, `step2-maison.mp4`, `step3-orientation.mp4`, etc.

**Impact :** Les étapes du simulateur n’afficheront pas les vidéos.

#### C. Formulaire de contact non fonctionnel
**Fichier :** `contact/index.html`

Le formulaire n’a **ni `action` ni `method`** et **aucun JavaScript** pour gérer l’envoi. Au clic sur « Envoyer ma demande », la page se recharge sans envoyer de données.

**À faire :** Brancher sur FormSubmit.co (comme `etude-solaire-gratuite.html`) ou un autre service compatible Netlify.

---

## 4. POINTS CRITIQUES NETLIFY

| Critère | Statut |
|---------|--------|
| Chemins relatifs / absolus depuis racine | ✅ OK (`/assets/...`, `/contact/`, etc.) |
| Chemins type `C:\...` ou `file://` | ✅ Aucun dans le site (uniquement dans `scripts/` et `node_modules`) |
| PHP / accès serveur | ✅ Aucun |
| Formulaires | ⚠️ **Contact : non fonctionnel** — Étude gratuite : OK (FormSubmit.co) |

---

## 5. FICHIERS NETLIFY

| Fichier | Présent | Remarque |
|---------|---------|----------|
| `_redirects` | ✅ | Redirections 301 et réécritures 200 correctes |
| `netlify.toml` | ❌ | Optionnel ; la racine et `_redirects` suffisent |

---

## 6. LIENS ET ROUTAGE

- `page-de-presentation.html` : ✅ Existe (lien logo header)
- Redirections legacy → canoniques : ✅ Configurées
- Réécritures `/le-solaire/`, `/notre-methode/`, `/seo/` : ✅ Configurées

---

## 7. CONCLUSION

### ❌ PAS PRÊT À DÉPLOYER

**Blocages principaux :**

1. **Images manquantes** — Toutes les images du site (logo, favicon, visuels, produits, etc.) sont absentes. Le site sera visuellement cassé.
2. **Vidéos manquantes** — Le simulateur d’étude gratuite ne pourra pas afficher les vidéos d’étapes.
3. **Formulaire de contact inopérant** — Les demandes de contact ne sont pas envoyées.

**Actions avant déploiement :**

| Priorité | Action |
|----------|--------|
| 1 | Ajouter toutes les images dans `assets/images/` (logo, favicon, og-image, visuels, produits, etc.) |
| 2 | Ajouter les vidéos du simulateur dans `assets/videos/` ou retirer/adapter les références |
| 3 | Connecter le formulaire de contact à FormSubmit.co (ou équivalent) |

**Une fois ces points traités :** le site sera techniquement déployable sur Netlify en mode statique, sans build.

---

*Audit réalisé le 18 mars 2025.*
