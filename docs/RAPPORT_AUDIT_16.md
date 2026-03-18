# Rapport d'audit – Prompts 16A, 16B, 16C

## 16A – Audit contenu et enrichissement (900 mots min)

### Objectif
Vérifier que les 9 pages migrées contiennent au minimum 900 mots et une structure complète : Introduction, Comprendre, Fonctionnement, Avantages, FAQ.

### Corrections appliquées

| Page | Avant | Après | Statut |
|------|-------|-------|--------|
| /le-solaire/autoconsommation-solaire/ | ~380 | ~900+ | ✅ Enrichi |
| /le-solaire/aides-panneaux-solaires/ | ~280 | ~900+ | ✅ Enrichi |
| /le-solaire/rentabilite-panneaux-solaires/ | ~260 | ~900+ | ✅ Enrichi |
| /le-solaire/rendement-panneaux-solaires/ | ~180 | ~900+ | ✅ Enrichi |
| /produits/panneaux-solaires/ | ~320 | ~900+ | ✅ Enrichi |
| /produits/onduleurs/ | ~200 | ~900+ | ✅ Enrichi |
| /produits/batteries-solaires/ | ~220 | ~900+ | ✅ Enrichi |
| /notre-methode/etude-solaire/ | ~180 | ~900+ | ✅ Enrichi |
| /notre-methode/installation/ | ~150 | ~900+ | ✅ Enrichi |

### Sections ajoutées par page
- **Comprendre le sujet** : explications pédagogiques
- **Fonctionnement** : détails techniques et pratiques
- **Avantages** : listes à puces avec `.sg-list-premium`
- **FAQ** : 2 à 5 questions supplémentaires par page avec `.sg-faq`

### Classes utilisées
- `.sg-section`, `.sg-container`, `.sg-section-title`
- `.sg-list-premium`, `.sg-faq`, `.sg-faq-item`, `.sg-faq-question`, `.sg-faq-answer`

---

## 16B – Correction des liens internes /seo/

### Objectif
Remplacer les liens vers `/seo/` par les nouvelles URLs dans `/le-solaire/*`, `/produits/*`, `/notre-methode/*` uniquement. **Ne pas modifier les pages dans `/seo/`.**

### Mapping des remplacements
| Ancien lien | Nouveau lien |
|-------------|--------------|
| /seo/panneaux-solaires | /produits/panneaux-solaires/ |
| /seo/batteries-solaires | /produits/batteries-solaires/ |
| /seo/onduleurs-solaires | /produits/onduleurs/ |
| /seo/autoconsommation-solaire | /le-solaire/autoconsommation-solaire/ |
| /seo/aides-financements | /le-solaire/aides-panneaux-solaires/ |

### Rapport
- **Pages impactées** : index.html (racine), produits/index.html
- **Liens corrigés** : 5 liens par page (cartes thématiques)
- **Pages non modifiées** : /seo/villes/* (conformément à la consigne)

---

## 16C – Vérification des canonical SEO

### Objectif
Chaque page doit contenir :
```html
<link rel="canonical" href="https://www.solarglobe.fr/.../" />
```
avec URL complète et slash final.

### Rapport
- **Canonical ajoutés** : 9 pages (le-solaire, produits, notre-methode)
- **Canonical corrigés** : 0
- **Pages conformes** : 9/9

### Détail des canonical
| Page | Canonical |
|------|-----------|
| le-solaire/autoconsommation-solaire.html | https://www.solarglobe.fr/le-solaire/autoconsommation-solaire/ |
| le-solaire/aides-panneaux-solaires.html | https://www.solarglobe.fr/le-solaire/aides-panneaux-solaires/ |
| le-solaire/rentabilite-panneaux-solaires.html | https://www.solarglobe.fr/le-solaire/rentabilite-panneaux-solaires/ |
| le-solaire/rendement-panneaux-solaires.html | https://www.solarglobe.fr/le-solaire/rendement-panneaux-solaires/ |
| produits/panneaux-solaires.html | https://www.solarglobe.fr/produits/panneaux-solaires/ |
| produits/onduleurs.html | https://www.solarglobe.fr/produits/onduleurs/ |
| produits/batteries-solaires.html | https://www.solarglobe.fr/produits/batteries-solaires/ |
| notre-methode/etude-solaire.html | https://www.solarglobe.fr/notre-methode/etude-solaire/ |
| notre-methode/installation.html | https://www.solarglobe.fr/notre-methode/installation/ |

---

## Synthèse
- **16A** : 9 pages enrichies à 900+ mots avec structure complète
- **16B** : Liens /seo/ corrigés dans index et produits (hors /seo/)
- **16C** : 9 canonical conformes

**Suite** : Prompts 17, 18, 19, 20 pour consolidation SEO.
