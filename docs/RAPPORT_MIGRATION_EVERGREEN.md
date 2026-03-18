# Rapport de migration – Contenus evergreen vers pages piliers

## Objectif
Migrer les anciens contenus blog evergreen vers les pages piliers du silo `/le-solaire/` pour renforcer les pages stratégiques, éviter les duplications SEO et centraliser les contenus pédagogiques.

## Mapping réalisé

| Source (blog) | Cible (piliers) | Statut |
|---------------|-----------------|--------|
| choisir-puissance-solaire.html | /le-solaire/puissance-installation-solaire/ | ✅ Migré |
| autonomie-solaire.html | /le-solaire/autoconsommation-solaire/ | ✅ Migré |
| rendement-panneaux.html | /le-solaire/rendement-panneaux-solaires/ | ✅ Migré |
| aides-financieres.html | /le-solaire/aides-panneaux-solaires/ | ✅ Migré |

**Important** : Les anciennes pages blog n'ont pas été supprimées. La suppression et les redirections seront réalisées dans les étapes ultérieures.

---

## 1. puissance-installation-solaire

### Contenu migré
- **Introduction** : Méthode de dimensionnement (taux d'autoconsommation 55–75 %)
- **Comprendre** : 5 étapes de la méthode Solarglobe (profil conso, autoconsommation, toiture, puissance, ROI)
- **Fonctionnement** : Profils 6 kWc vs 9 kWc (2 cartes sg-card)
- **Surface** : Tableau puissance / nb panneaux / surface utile (6 kWc, 9 kWc)
- **Usages** : PAC, ECS, borne EV
- **Production** : Tableau production annuelle et autoconsommation visée
- **Avantages et limites** : Faut-il une batterie ?
- **FAQ** : 3 questions (6 vs 9 kWc, nb panneaux, maximiser autoconsommation)

### Contenu supprimé (non migré)
- Sommaire / table des matières
- Bloc « Articles liés » (liens vers autres articles blog)
- Chips, date de publication, temps de lecture
- Styles spécifiques (card, callout, figure)
- Schema.org BlogPosting

### Liens internes ajoutés
- /produits/panneaux-solaires/
- /produits/batteries-solaires/
- /notre-methode/etude-solaire/
- /etude-gratuite/

### SEO conservé
- title, meta description, canonical, robots index follow

---

## 2. autoconsommation-solaire

### Contenu migré (enrichissement)
- **Introduction** : Contexte énergétique, autonomie accessible
- **Nouvelle section** : Produire avec des panneaux haut de gamme (LONGi Hi-MO X6, DualSun Flash 500)
- **Section batteries** : Stockage ATMOCE, micro-onduleurs, autonomie réelle
- **Nouvelle section** : L'autoconsommation est-elle rentable ? (70–100 % conso, 8–12 ans amortissement)

### Contenu supprimé
- Aucun (enrichissement uniquement)

### Liens internes ajoutés
- /produits/panneaux-solaires/
- /produits/onduleurs/
- /produits/batteries-solaires/
- /notre-methode/etude-solaire/

---

## 3. rendement-panneaux-solaires

### Contenu migré
- **Comprendre** : Rendement catalogue vs conditions réelles
- **Fonctionnement** : Tableau inclinaison (0–10°, ~30–35°, >40°) avec contexte et remarques
- **Ombrage** : Masques, micro-onduleurs, stratégie (élagage, décalage)
- **Qualité matériel** : Rendement nominal, électronique de puissance, fixation, température
- **Optimisation** : 5 leviers (étude, implantation, matériel, pilotage conso, suivi)

### Contenu supprimé
- Images (schema-orientation, schema-ombrage, schema-temperature) – non migrées (assets blog)
- Bloc « Articles liés »

### Liens internes ajoutés
- /produits/panneaux-solaires/
- /produits/onduleurs/
- /notre-methode/etude-solaire/

---

## 4. aides-panneaux-solaires

### Contenu migré
- **Prime** : Barème 2025 complet (≤3, >3–9, >9–36, >36–100 kWc) avec montants et modes de versement
- **Vente surplus** : 0,04 €/kWh, exemple chiffré (3 kWc, 50 % autoconsommation)
- **TVA** : Réduction 5,5 % / 10 % selon période, ≤ 9 kWc
- **Fiscalité** : Exonération ≤ 3 kWc, micro-BIC > 3 kWc
- **Faut-il compter sur les aides ?** : Vrai levier = autoconsommation, pas les aides
- **FAQ** : Prime versée immédiatement ? MaPrimeRénov' photovoltaïque ?

### Contenu supprimé
- Bloc « Optimiser votre projet » (méthode Solarglobe) – partiellement intégré dans « Faut-il compter »
- Transparence Solarglobe (TVA vs modules bas carbone) – jugé trop commercial
- Exemples packs 6 kWc / 9 kWc avec prix

### Liens internes ajoutés
- /le-solaire/autoconsommation-solaire/
- /produits/panneaux-solaires/
- /produits/onduleurs/
- /produits/batteries-solaires/
- /notre-methode/etude-solaire/
- /notre-methode/installation/

---

## Structure respectée

Chaque page cible respecte :
- **Introduction**
- **Comprendre le sujet**
- **Comment cela fonctionne**
- **Avantages et limites**
- **Questions fréquentes (FAQ)** – 4 à 6 questions max

Classes utilisées : `.sg-section`, `.sg-container`, `.sg-section-title`, `.sg-section-subtitle`, `.sg-card`, `.sg-list-premium`, `.sg-faq`, `.sg-faq-item`, `.sg-faq-question`, `.sg-faq-answer`

---

## Synthèse

| Page pilier | Sections migrées | Tableaux | FAQ |
|-------------|------------------|----------|-----|
| puissance-installation-solaire | 7 | 2 | 3 |
| autoconsommation-solaire | 3 (enrichissement) | 0 | 0 (existantes) |
| rendement-panneaux-solaires | 4 | 1 | 0 (existantes) |
| aides-panneaux-solaires | 5 | 1 | +2 |

**Pages renforcées** : 4  
**Pages sources conservées** : 4 (choisir-puissance-solaire, autonomie-solaire, rendement-panneaux, aides-financieres)  
**SEO existant** : Conservé (title, meta, canonical, robots)
