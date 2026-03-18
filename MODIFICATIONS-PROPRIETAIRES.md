# Modifications structurelles — proprietaires.html (SolarGlobe)

## Résumé des modifications

Corrections structurelles appliquées aux 15 slides de la présentation SolarGlobe, sans refonte visuelle. Objectif : layout robuste, espacements uniformes, prévention des débordements.

---

## 1. Éléments CSS modifiés

### Nouveau bloc `.sg-slide-inner` (layout flex)

```css
.sg-slide-inner {
  display: flex;
  flex-direction: column;
  min-height: 100%;
  gap: clamp(1rem, 2vh, 2rem);
}
.sg-slide-inner > header { flex-shrink: 0; }
.sg-slide-inner > main {
  flex: 1;
  display: flex;
  align-items: center;
  min-height: 0;
  overflow: hidden;
}
.sg-slide-inner > footer {
  flex-shrink: 0;
  padding-bottom: clamp(1.2rem, 2.5vh, 2.4rem);
}
```

### `.slide` — overflow

- Ajout de `overflow: hidden` sur `.slide` pour éviter tout débordement.

### Remplacement layout

- **Avant** : `grid grid-rows-[auto_1fr_auto]`
- **Après** : `sg-slide-inner` (flex vertical)

### Espacements uniformisés

- **Gap vertical** : `clamp(1rem, 2vh, 2rem)` entre header, main et footer
- **Padding footer** : `clamp(1.2rem, 2.5vh, 2.4rem)` en bas
- Suppression des `pb-8`, `pb-10`, `pb-12` redondants sur les conteneurs

---

## 2. Micro-ajustements (slides 4, 6, 7)

### Slide 4 — Prix de l’électricité

- Card : `py-8` → `py-6`
- Grid texte + graph : `gap-10` → `gap-6`
- Colonne texte : `space-y-5` → `space-y-4`
- Canvas : `h-[360px]` → `h-[min(340px,32vh)]` pour éviter les débordements sur petits écrans

### Slide 6 — Vrais problèmes du marché

- Card : `py-7` → `py-6`
- Grid : `gap-4` → `gap-3`
- Liste : `mt-3 space-y-3` → `mt-2 space-y-2`
- Positionnement : `mt-4` → `mt-3`

### Slide 7 — Méthode Solarglobe

- Card : `py-8` → `py-6`
- Grid : `gap-8` → `gap-6`
- Blocs étapes : `flex gap-5` → `flex gap-4`

---

## 3. Scripts

### Animations

- **État actuel** : système déjà optimisé
- Pas de boucles `requestAnimationFrame` continues
- Animations déclenchées uniquement via `showSlide(index)` → `playSlideAnim(index)`
- Utilisation de `setTimeout` pour les séquences, avec `ANIM_TOKEN` pour annuler les animations en cours

Aucune modification des scripts d’animation.

---

## 4. Autres corrections

- Correction de la balise `<nav>` dupliquée dans le header

---

## 5. Validation des 15 slides

| Slide | Structure | Layout | Animations |
|-------|-----------|--------|------------|
| 00 | Intro | `flex flex-col` (inchangée) | — |
| 01 | Rendez-vous | `sg-slide-inner` | ✓ |
| 02 | SolarGlobe / Bureau | `sg-slide-inner` | ✓ |
| 03 | Pourquoi le solaire | `sg-slide-inner` | ✓ |
| 04 | Prix électricité | `sg-slide-inner` + micro-ajustements | ✓ |
| 05 | 4 risques | `sg-slide-inner` | ✓ |
| 06 | Vrais problèmes | `sg-slide-inner` + micro-ajustements | ✓ |
| 07 | Méthode Solarglobe | `sg-slide-inner` + micro-ajustements | ✓ |
| 08 | Notre solution | `sg-slide-inner` | ✓ |
| 09 | Produit | `sg-slide-inner` | ✓ |
| 10 | Processus | `sg-slide-inner` | ✓ |
| 11 | Primes | `sg-slide-inner` | ✓ |
| 12 | Vendeur / Acheteur | `sg-slide-inner` | ✓ |
| 13 | Suite | `sg-slide-inner` | ✓ |
| 14 | Cadre final | `sg-slide-inner` | ✓ |

---

## 6. Garde-fous respectés

- Pas de conteneur scrollable
- Pas de boîte centrale ajoutée
- Fond image fullscreen conservé
- Contenu texte inchangé
- Animations conservées
- Navigation inchangée

---

## 7. Tests à effectuer

Vérifier le rendu sur :

- 13 pouces
- 16 pouces
- 27 pouces
- 30 pouces

Sur chaque slide : pas de débordement, pas de superposition, pas de scroll.
