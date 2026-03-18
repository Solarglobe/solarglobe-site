# Rapport de fusion – Autoconsommation solaire

**Date** : 13 mars 2025  
**Page cible** : `/le-solaire/autoconsommation-solaire.html`  
**Pages sources** : `autonomie-solaire.html`, `seo/autoconsommation-solaire.html`, `seo/energie-solaire-maison.html`

---

## 1. Résumé

La page pilier `/le-solaire/autoconsommation-solaire` a été enrichie et réorganisée en fusionnant le contenu utile des trois pages sources. La structure imposée en 8 sections a été respectée. Les pages sources n'ont **pas** été supprimées (redirections prévues plus tard).

---

## 2. Sections migrées

| Section | Source(s) | Statut |
|---------|-----------|--------|
| **1. Introduction** | autonomie-solaire, seo/autoconsommation-solaire, seo/energie-solaire-maison | Fusionnée et réécrite |
| **2. Comprendre l'autoconsommation solaire** | seo/autoconsommation-solaire, page cible existante | Enrichie (production, consommation directe, vente surplus) |
| **3. Comment fonctionne une installation** | autonomie-solaire, seo/energie-solaire-maison | Nouvelle section (panneaux, onduleurs, tableau, gestion) |
| **4. Peut-on devenir autonome ?** | autonomie-solaire (notion autonomie vs autoconsommation) | Nouvelle section créée |
| **5. Le rôle des batteries** | autonomie-solaire, seo/autoconsommation-solaire, page cible | Enrichie (stockage, optimisation, cas d'usage) |
| **6. L'autoconsommation est-elle rentable ?** | autonomie-solaire, seo/autoconsommation-solaire, seo/energie-solaire-maison | Enrichie (coût, économies, ROI, aides) |
| **7. Comment maximiser l'autoconsommation** | seo/autoconsommation-solaire, page cible | Réorganisée avec `.sg-list-premium` |
| **8. FAQ** | Page cible existante | Enrichie (6 questions au lieu de 5) |

---

## 3. Contenu supprimé

| Élément | Raison |
|---------|--------|
| **Blocs villes SEO** (36 villes) | Présents sur seo/autoconsommation-solaire et seo/energie-solaire-maison – non intégrés (éviter duplications SEO) |
| **Grilles de liens internes** vers pages /seo/ | Liens obsolètes ou redondants – remplacés par liens vers pages principales |
| **Section « Avantages »** en cartes | Contenu fusionné dans l'introduction et les sections thématiques |
| **Section « Aides financières »** dédiée | Contenu fusionné dans la section « Rentabilité » |
| **Mentions CITE (crédit d'impôt)** | Potentiellement obsolète – conservée uniquement TVA réduite et prime |
| **Répétitions** « Solarglobe vous accompagne » | Simplifiées, intégrées naturellement |
| **Phrases artificielles** type « Ne laissez pas passer cette opportunité » | Supprimées |
| **Références produits trop commerciales** (LONGI, DualSun, ATMOCE) | Conservées de manière naturelle dans les sections techniques |

---

## 4. Contenu réécrit

| Bloc | Modifications |
|------|---------------|
| **Introduction** | Regroupement des 3 intros sources, clarification principe / contexte / intérêt |
| **Comprendre l'autoconsommation** | Bloc pédagogique structuré (production, consommation directe, vente surplus) |
| **Fonctionnement installation** | Passage en liste avec composants (panneaux, onduleurs, tableau, gestion) |
| **Autonomie vs autoconsommation** | Nouvelle section explicative sur les limites réelles et le rôle du réseau |
| **Batteries** | Ajout des cas d'usage (absent la journée, consommation soir, coupure) |
| **Rentabilité** | Structuration en sous-blocs (coût, économies, temps de retour, aides) |
| **Maximiser l'autoconsommation** | Utilisation de `.sg-list-premium` avec 4 leviers (dimensionnement, pilotage, batteries, domotique) |
| **FAQ** | 6 questions : Qu'est-ce que l'autoconsommation ? Peut-on être autonome ? Faut-il une batterie ? Quelle puissance ? Rentabilité ? Tarif surplus |

---

## 5. Sections ajoutées

- **Section 4 : Peut-on devenir autonome en électricité ?** – Différence autoconsommation / autonomie, limites réelles, rôle du réseau
- **Bloc pédagogique** dans « Comprendre l'autoconsommation » – Production photovoltaïque, consommation directe, vente du surplus
- **Détail des composants** dans « Comment fonctionne une installation » – Panneaux, onduleurs, tableau électrique, gestion de l'énergie

---

## 6. Liens internes intégrés

| Lien | Emplacement |
|------|-------------|
| `/produits/panneaux-solaires/` | Introduction, section fonctionnement |
| `/produits/onduleurs/` | Section fonctionnement |
| `/produits/batteries-solaires/` | Section batteries (2 occurrences) |
| `/notre-methode/etude-solaire/` | Comprendre, fonctionnement, FAQ |
| `/notre-methode/installation/` | Section fonctionnement |
| `/etude-gratuite/` | Maximiser l'autoconsommation, FAQ, CTA |

---

## 7. Design system

Classes utilisées conformément aux spécifications :

- `.sg-section`
- `.sg-container`
- `.sg-section-title`
- `.sg-section-subtitle`
- `.sg-card` (non utilisée dans cette version – contenu en listes)
- `.sg-list-premium` / `.sg-list-premium-dark`
- `.sg-faq` / `.sg-faq-item`
- `.sg-cta` / `.sg-cta-dark`

---

## 8. SEO conservé

- **Title** : Autoconsommation solaire – Solarglobe
- **Meta description** : Enrichie pour refléter le contenu complet
- **Canonical** : https://www.solarglobe.fr/le-solaire/autoconsommation-solaire/
- **Robots** : index, follow

---

## 9. Actions non réalisées (comme demandé)

- Aucune page source supprimée
- Aucune redirection mise en place

---

## 10. Résultat

La page `/le-solaire/autoconsommation-solaire` est désormais :

- **Une page pilier complète** couvrant l’ensemble du sujet
- **La référence du site** sur l’autoconsommation solaire
- **Claire pour les utilisateurs** avec une structure en 8 sections
- **Solide pour le SEO** avec contenu unique, liens internes pertinents et absence de duplications

Les pages `autonomie-solaire.html`, `seo/autoconsommation-solaire.html` et `seo/energie-solaire-maison.html` restent en ligne temporairement.
