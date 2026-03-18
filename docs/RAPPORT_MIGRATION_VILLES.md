# Rapport de migration – Pages villes

**Date** : 13 mars 2025  
**Pages cibles** : `/panneaux-solaires-[ville]/` (36 pages)  
**Pages sources** : `seo/villes/[ville].html` (36 pages)

---

## 1. Résumé

Les 36 pages `/panneaux-solaires-[ville]` ont été enrichies avec un contenu crédible et des liens internes pertinents. Les anciennes pages `seo/villes/` n'ont **pas** été supprimées. Les redirections seront mises en place plus tard.

---

## 2. Analyse des anciennes pages villes

### Contenu identifié (sources seo/villes/)

| Type | Élément | Décision |
|------|---------|----------|
| **Utile** | « De plus en plus de foyers passent à l'énergie solaire » | Réécrit et intégré |
| **Utile** | « Installateurs certifiés RGE QualiPV » | Intégré dans l'introduction |
| **À supprimer** | Paragraphe keyword stuffing (liste de 12+ mots-clés) | Non migré |
| **À supprimer** | Bloc « Autres villes proches » (liens vers autres villes) | Non migré |
| **À supprimer** | Bloc « Nos expertises solaires » (liens /seo/) | Remplacé par liens vers pages piliers |
| **À supprimer** | Liens internes artificiels (../autoconsommation-solaire, etc.) | Remplacés par URLs canoniques |

### Contenu des anciennes pages

Les pages `seo/villes/` étaient des templates quasi identiques avec :
- Une phrase de keyword stuffing : « En combinant panneaux solaires, autoconsommation solaire, batteries solaires, onduleurs solaires... »
- Aucune description spécifique de la ville
- Aucun contexte énergétique local détaillé
- Aucun exemple de projet photovoltaïque

---

## 3. Contenu migré et enrichi

### Introduction locale

**Avant** : « À [ville] et dans [région], de plus en plus de foyers font le choix du photovoltaïque... »

**Après** :
- Mention des **maisons individuelles** et de l'installation en autoconsommation
- **Contexte énergétique** : hausse des tarifs, intérêt de produire sa propre électricité
- **Région** et ensoleillement
- Lien vers `/le-solaire/autoconsommation-solaire/`
- Lien vers `/notre-methode/etude-solaire/`
- Mention des installateurs RGE QualiPV
- Correction « SolarGlobe » → « Solarglobe »

### Projet solaire type

- Lien vers `/le-solaire/` et `/le-solaire/rentabilite-panneaux-solaires/`
- Précision sur la **vente du surplus** (0,04 €/kWh)
- Conservation des 3 cartes : maison individuelle, autoconsommation, batterie

### Étude solaire

- Lien vers `/etude-gratuite/`
- Liste `.sg-list-premium` enrichie :
  - Analyse de toiture (orientation, inclinaison, ombrages)
  - Dimensionnement (puissance kWc)
  - Simulation de production (kWh/an)
  - Rentabilité (économies, temps de retour)
  - Aides (prime, TVA, revente)

### FAQ locale

- 3 questions conservées (rentabilité, puissance, coût)
- **2 questions ajoutées** :
  - « Qui installe les panneaux solaires à [ville] ? »
  - « Faut-il un permis de construire pour des panneaux à [ville] ? »
- Mise à jour TVA 10 % → 5,5 %
- Liens vers `/etude-gratuite/` dans les réponses

---

## 4. Liens internes intégrés

| Lien | Emplacement |
|------|-------------|
| `/le-solaire/` | Section Projet solaire |
| `/le-solaire/autoconsommation-solaire/` | Introduction |
| `/le-solaire/rentabilite-panneaux-solaires/` | Section Projet solaire |
| `/notre-methode/etude-solaire/` | Introduction |
| `/etude-gratuite/` | Introduction, Étude solaire, FAQ, CTA |

---

## 5. Contenu supprimé (non migré)

| Élément | Raison |
|---------|--------|
| Paragraphe keyword stuffing | Phrases artificielles, répétitions SEO |
| Bloc « Autres villes proches » | Listes de villes répétées, pratique SEO ancienne |
| Bloc « Nos expertises solaires » | Liens vers /seo/, structure obsolète |
| Liens relatifs (../autoconsommation-solaire) | URLs incorrectes |

---

## 6. Pages villes enrichies

Les 36 pages suivantes ont été régénérées avec le template enrichi :

Reims, Beauvais, Argenteuil, Meaux, Chelles, Noisy-le-Grand, Melun, Fontainebleau, Versailles, Saint-Denis, Aulnay-sous-Bois, Drancy, Sarcelles, Cergy, Pontoise, Nanterre, Colombes, Boulogne-Billancourt, Issy-les-Moulineaux, Ivry-sur-Seine, Vitry-sur-Seine, Créteil, Saint-Maur-des-Fossés, Choisy-le-Roi, Évry, Corbeil-Essonnes, Palaiseau, Antony, Massy, Rambouillet, Chartres, Orléans, Amiens, Compiègne, Soissons, Laon.

---

## 7. Structure conservée

- Hero ville
- Introduction locale
- Projet solaire type
- Étude solaire
- FAQ locale
- CTA

---

## 8. Design system

Classes utilisées : `.sg-section`, `.sg-container`, `.sg-section-title`, `.sg-card`, `.sg-list-premium`, `.sg-faq`, `.sg-faq-item`, `.sg-cta`.

---

## 9. SEO conservé

- **H1** : « Installer des panneaux solaires à [VILLE] »
- **Title** : « Panneaux solaires à [ville] | Étude solaire et installation photovoltaïque »
- **Meta description** : conservée
- **Canonical** : conservé
- **Robots** : index, follow
- **Schema.org** : BreadcrumbList, LocalBusiness, FAQPage

---

## 10. Correspondance anciennes / nouvelles pages

Les anciennes pages `seo/villes/` utilisent des slugs différents de certaines nouvelles. Villes communes : meaux, fontainebleau, massy, argenteuil, compiegne, beauvais, reims, orleans, etc. Les nouvelles pages couvrent 36 villes ; les anciennes en couvrent 36 autres (lagny-sur-marne, provins, sens, etc.). La migration a porté sur l'enrichissement du **template des nouvelles pages**, et non sur une correspondance ville par ville avec les anciennes.

---

## 11. Résultat

Les pages `/panneaux-solaires-[ville]` sont désormais :

- **Des pages locales crédibles** avec introduction contextualisée
- **Des pages SEO propres** sans keyword stuffing ni blocs villes
- **Des pages utiles** avec FAQ enrichie et liens internes pertinents

Les anciennes pages `seo/villes/` restent en ligne. Les redirections pourront être configurées ultérieurement.
