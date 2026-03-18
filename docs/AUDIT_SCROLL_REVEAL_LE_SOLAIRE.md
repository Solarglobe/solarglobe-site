# AUDIT COMPLET — SYSTÈME SCROLL REVEAL
## Page /le-solaire/index.html

**Date :** 14 mars 2025  
**Objectif :** Diagnostic technique et visuel précis du système d'animation scroll reveal. Comprendre pourquoi le rendu reste en dessous d'un niveau Apple / Stripe / Vercel.

---

# 1. INVENTAIRE DES SCRIPTS ET CSS QUI IMPACTENT LE SCROLL

## 1.1 Scripts chargés

| Fichier | Chargé ? | Rôle |
|---------|----------|------|
| `/assets/js/sg-scroll-reveal.js` | ✅ Oui | Script principal — IntersectionObserver, stagger, hero |
| `/assets/js/sg-counter.js` | ✅ Oui | Compteurs animés — IntersectionObserver séparé |
| `/assets/js/sg-animations.js` | ❌ Non | **Non chargé** — ancien système remplacé |

**Conclusion :** Pas de conflit avec l'ancien système. `sg-animations.js` n'est plus référencé.

## 1.2 CSS impactant les animations

| Fichier | Impact |
|---------|--------|
| `/assets/css/sg-animations.css` | **Principal** — `.sg-reveal`, `.sg-reveal-card`, `.sg-hero-reveal`, transitions, blur |
| `/assets/css/le-solaire-editorial.css` | Styles hero (blur décoratif ::before/::after), guides, sections — **pas de conflit direct** |
| `/assets/css/solarglobe-design-system.css` | Transitions génériques — **pas de conflit** |
| **Inline dans index.html** | `.sg-counter`, `.sg-counter-running`, `.sg-card-premium`, `.sg-img-premium-wrap`, `.sg-section-divider` |

**Point critique :** Le `.sg-section-divider::after` (inline index.html, lignes 573-587) utilise `filter: blur(18px)` pour un halo décoratif. Ce blur est **statique** et ne participe pas au reveal, mais peut créer une confusion visuelle si le divider est animé avec `.sg-reveal` (qui a lui aussi un blur).

## 1.3 Scripts inline pouvant perturber

| Script | Rôle | Conflit potentiel ? |
|--------|------|---------------------|
| FAQ (lignes 1339-1350) | Toggle `.hidden` sur les réponses, `transform` sur l'icône | **Non** — aucun impact sur reveal |
| Compteurs | Via `sg-counter.js` externe | **Oui** — potentiel (voir § 2.2) |

---

# 2. PROBLÈMES TECHNIQUES RÉELS IDENTIFIÉS

## 2.1 IntersectionObserver — Configuration actuelle

```javascript
threshold: 0.35
rootMargin: '0px 0px -25% 0px'
```

**Analyse :**

- **Threshold 0.35** : L'animation se déclenche quand 35 % de la section est visible. Avec un viewport réduit de 25 % en bas (`rootMargin`), la zone effective est plus stricte. Le déclenchement est **correct** pour un effet "section au centre".
- **Condition `scrollY < 120`** : Empêche l'animation au chargement. **Problème** : La première section (Rentabilité) ne s'anime **jamais** si l'utilisateur ne scroll pas au moins 120 px. Si l'utilisateur scroll légèrement puis revient en haut, la section peut rester non animée.

**Sections observées :** `.sg-section`, `.sg-section-editorial`, `.sg-guides-grid`, `.sg-card-grid`

- `.sg-guides-grid` et `.sg-card-grid` sont **enfants** de `.sg-section`. Ils sont observés en double. Quand la section parente déclenche, tout est animé. Quand la grille déclenche à son tour (élément plus petit), `animateSection` est rappelé sur des éléments déjà visibles — pas de bug, mais **redondance**.

## 2.2 Blur — Problème majeur

**CSS actuel :**
```css
.sg-reveal {
  filter: blur(6px);
  transition: filter 0.9s cubic-bezier(0.22, 1, 0.36, 1);
}
.sg-reveal-visible {
  filter: none;
}
```

**Diagnostic :**

1. **6 px de blur sur du texte** : Sur du texte de taille courante (14–18 px), 6 px de blur est **très fort**. Le texte devient illisible au début de l'animation.
2. **Durée 900 ms** : Le blur reste pendant toute la transition. Avec l'easing `cubic-bezier(0.22, 1, 0.36, 1)` (ease-out), la progression est rapide au début et lente à la fin. Le blur reste **perceptible longtemps** en fin de transition.
3. **Pas de transition dédiée** : Opacity, transform et filter partagent la même durée et le même easing. Le blur ne se retire pas plus vite que le reste. L'œil perçoit le texte comme "flou longtemps" avant d'être net.
4. **Effet "brouillard"** : Sur les paragraphes, titres et intro, le blur crée une impression de "brouillard" ou de "nettoyage" progressif plutôt qu'une apparition nette — **pas premium**.

**Référence Apple/Stripe/Vercel :** Ces sites utilisent rarement du blur sur le texte. Ils privilégient opacity + translateY. Le blur sur le texte est **vulgaire** et peu lisible.

## 2.3 Stagger — Surcharge et uniformité

**Configuration :** `STAGGER_MS = 120` — délai = `index * 120 ms`

**Comptage par section (éléments `.sg-reveal` + `.sg-reveal-card`) :**

| Section | Nb éléments | Dernier élément à | Durée totale anim |
|---------|-------------|-------------------|-------------------|
| Rentabilité | 10 | 1080 ms | ~2 s |
| Durabilité | 10 | 1080 ms | ~2 s |
| Contexte | 7 | 720 ms | ~1,6 s |
| Fonctionnement | 7 | 720 ms | ~1,6 s |
| Production | 9 | 960 ms | ~1,9 s |
| Étude | 8 | 840 ms | ~1,7 s |
| Dimensionnement | 8 | 840 ms | ~1,7 s |
| Bureau d'étude | 7 | 720 ms | ~1,6 s |
| **Guides solaire** | **10** | **1080 ms** | **~2 s** |
| Guides expertise | 9 | 960 ms | ~1,9 s |
| Avantages | 7 | 720 ms | ~1,6 s |
| FAQ | 4 | 360 ms | ~1,3 s |
| Éligibilité | 7 | 720 ms | ~1,6 s |

**Problèmes :**

1. **Trop d'éléments animés** : 10 éléments par section (Rentabilité, Durabilité, Guides) = 10 × 120 ms = 1,2 s de stagger uniquement. Le dernier élément commence à 1,08 s et met encore 0,9 s pour finir → **2 s** de cascade. C'est trop long.
2. **Uniformité** : Tout le monde utilise le même stagger (120 ms). Pas de hiérarchie (titre vs paragraphe vs carte). Pas de variation par type de contenu.
3. **Paragraphes animés un par un** : Section Durabilité = 6 paragraphes animés séparément. Effet de "machine à écrire" ou de "défilement" qui donne une impression **moll** et **répétitive**.
4. **Ordre DOM = ordre visuel** : Le stagger suit l'ordre du DOM. Les dividers, kickers, titres, intros, paragraphes, images, cartes sont tous traités de la même façon. Pas de regroupement logique (ex. titre + intro ensemble, puis bloc texte).

## 2.4 Durée et easing

**Durées :**

- `.sg-reveal` : 0,9 s
- `.sg-reveal-card` : 0,9 s
- `.sg-hero-reveal` : 0,8 s

**Easing :** `cubic-bezier(0.22, 1, 0.36, 1)` — ease-out.

**Analyse :**

- 0,9 s est **long** pour une apparition. Apple/Stripe restent souvent entre 0,5 et 0,7 s.
- L'ease-out donne une fin de mouvement lente — peut accentuer l'impression de "moll".
- Pas de variation : texte, images et cartes ont la même durée.

## 2.5 Conflit potentiel Compteurs / Reveal

Les `.sg-counter` sont **à l'intérieur** de paragraphes `.sg-reveal` :

```html
<p class="sg-reveal">...plus de <span class="sg-counter">40000</span> €...</p>
```

- Le paragraphe s'anime (opacity, blur, translateY).
- Le compteur a son propre IntersectionObserver (`sg-counter.js`) avec `threshold: 0.2`, `rootMargin: '0px 0px -10% 0px'`.
- Le compteur peut se déclencher **avant** ou **pendant** l'animation du paragraphe. Si le paragraphe est encore flou, le compteur qui défile peut paraître bizarre.

**Verdict :** Conflit mineur mais possible. Le compteur n'a pas de `scrollY` minimum, donc il peut démarrer au chargement si le paragraphe est visible.

## 2.6 Hero — Animation au chargement

**Configuration :** Cascade 0, 180, 360, 540 ms (4 éléments).

**CSS :** `.sg-hero-reveal` — `opacity: 0`, `translateY(20px)`, **pas de blur**.

**Analyse :** Le hero est correct : pas de blur, délais cohérents. C'est la partie la plus propre du système.

---

# 3. PROBLÈMES VISUELS / UX RÉELS IDENTIFIÉS

## 3.1 Blur — Jugement visuel

| Critère | Verdict |
|---------|---------|
| Trop flou | **Oui** — 6 px sur du texte est excessif |
| Trop long | **Oui** — 900 ms de blur visible |
| Mal géré | **Oui** — même timing que opacity/transform, pas de courbe dédiée |
| Effet "brouillard" | **Oui** — texte qui "se nettoie" plutôt qu'il "apparaît" |
| Premium ? | **Non** — Apple/Stripe n'utilisent pas de blur sur le texte |

**Conclusion :** Le blur sur le texte est le **principal** facteur de "pas premium" et de "reste flou trop longtemps".

## 3.2 Stagger — Jugement visuel

| Critère | Verdict |
|---------|---------|
| Trop uniforme | **Oui** — même timing partout |
| Trop long | **Oui** — 10 éléments × 120 ms = 1,2 s de stagger |
| Mal hiérarchisé | **Oui** — titre, intro, paragraphes traités pareil |
| "Moll" | **Oui** — cascade trop lente |
| "Template" | **Oui** — effet générique |

**Conclusion :** Le stagger est **trop systématique** et **trop long**. Pas de hiérarchie visuelle.

## 3.3 Sections — Diagnostic par section

| Section | Problème principal |
|---------|-------------------|
| **Rentabilité** | 10 éléments, dont 2 blocs (div) + paragraphes. Blur sur tout. Durée totale ~2 s. |
| **Durabilité** | 6 paragraphes animés un par un — effet "machine à écrire" ou "défilement lent". |
| **Guides solaire** | 6 cartes + header + divider. 10 éléments. Blur sur kicker/titre/intro, cartes sans blur. |
| **Production** | 3 cartes + texte. Cartes sans blur. Texte avec blur. |
| **FAQ** | 4 éléments seulement. Plus équilibré. |

**Sections problématiques :**

- **Durabilité** : 6 paragraphes animés séparément = trop répétitif.
- **Rentabilité, Guides** : 10 éléments = trop chargé.
- **Toutes les sections texte** : Blur sur les paragraphes = illisible au début.

## 3.4 État intermédiaire visible

Pendant la transition (0 → 900 ms), l'élément est dans un état intermédiaire :

- Opacity : 0 → 1
- Transform : 24 px → 0
- Filter : blur(6 px) → none

À 450 ms, on a environ : opacity ~0,5, translateY ~12 px, blur ~3 px. Le texte est **semi-transparent, décalé et flou**. Cet état intermédiaire est **visible trop longtemps** et donne une impression de "flou persistant".

## 3.5 Comparaison Apple / Stripe / Vercel

| Critère | Solarglobe actuel | Références premium |
|---------|-------------------|-------------------|
| Blur sur texte | Oui, 6 px | Non ou très léger |
| Durée | 900 ms | 500–700 ms |
| Stagger | 120 ms uniforme | Variable, hiérarchisé |
| Nb éléments animés | Jusqu'à 10 par section | 3–5 max |
| Paragraphes | Un par un | Bloc ou groupe |
| Easing | Ease-out | Souvent ease-out ou custom |

**Conclusion :** Le système actuel est **trop chargé**, **trop uniforme** et **trop flou** par rapport aux références.

---

# 4. RECOMMANDATIONS DE CORRECTION PRIORISÉES

## 4.1 À corriger en priorité

1. **Supprimer le blur sur `.sg-reveal`**  
   - Garder opacity + translateY uniquement.  
   - Impact immédiat sur la lisibilité et la perception "premium".

2. **Réduire la durée des transitions**  
   - Passer de 900 ms à 600–700 ms pour `.sg-reveal` et `.sg-reveal-card`.  
   - Raccourcir le temps pendant lequel l’état intermédiaire est visible.

3. **Limiter le nombre d’éléments animés par section**  
   - Ne pas animer chaque paragraphe individuellement.  
   - Grouper : titre + intro + bloc texte (1 seul élément) + image + cartes.  
   - Ou animer uniquement : kicker, titre, intro, puis 1 bloc pour le contenu.

## 4.2 À recalibrer

1. **Stagger**  
   - Réduire : 80–100 ms au lieu de 120 ms.  
   - Ou varier : titre 0 ms, intro 80 ms, contenu 160 ms, image 240 ms, cartes 320 ms + 80 ms entre chaque carte.

2. **Hiérarchie**  
   - Titres : durée plus courte (0,6 s).  
   - Paragraphes/blocs : 0,7 s.  
   - Cartes : 0,8 s (effet plus marqué).

3. **Sections surchargées**  
   - Durabilité : regrouper les 6 paragraphes en 1 ou 2 blocs.  
   - Rentabilité, Guides : réduire à 5–6 éléments animés max.

## 4.3 À simplifier

1. **Observation redondante**  
   - Ne plus observer `.sg-guides-grid` et `.sg-card-grid` séparément.  
   - Garder uniquement `.sg-section` et `.sg-section-editorial`.

2. **Uniformité**  
   - Ne pas appliquer le même traitement à tous les types de contenu.  
   - Différencier : titres, texte, images, cartes.

## 4.4 À rendre plus premium

1. **Pas de blur sur le texte** — alignement avec Apple/Stripe/Vercel.
2. **Transitions plus courtes** — 600–700 ms.
3. **Stagger hiérarchisé** — pas le même délai pour tout.
4. **Moins d’éléments animés** — 3–5 par section au lieu de 10.
5. **Regrouper le contenu** — blocs plutôt que paragraphes isolés.

---

# SYNTHÈSE — CE QUI REND LE REVEAL "PAS OUF"

| Cause | Impact |
|-------|--------|
| **Blur 6 px sur texte** | Texte illisible au début, impression de "brouillard" |
| **Durée 900 ms** | Transitions trop longues, état intermédiaire trop visible |
| **Stagger 120 ms × 10 éléments** | Cascade trop longue (~2 s), effet "moll" |
| **Trop d’éléments animés** | Sections surchargées, pas de hiérarchie |
| **Paragraphes un par un** | Répétitif, "template" |
| **Uniformité totale** | Pas de variation, pas de hiérarchie visuelle |

**Conclusion :** Le système est techniquement correct mais **mal calibré** pour un rendu premium. Le blur sur le texte et la surcharge d’animations sont les deux principaux freins à un niveau Apple/Stripe/Vercel.
