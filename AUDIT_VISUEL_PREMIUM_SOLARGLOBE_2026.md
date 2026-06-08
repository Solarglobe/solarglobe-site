# Audit visuel premium — SolarGlobe

Audit purement visuel et d'effets. Aucune modification appliquée au site. Objectif : passer du niveau actuel à un rendu 95/100.

**Note visuelle actuelle estimée : 80 / 100.**

Le socle est sérieux : direction artistique cohérente (noir + or), animations GSAP au scroll avec respect de `prefers-reduced-motion`, halos radiaux, vignettages, hero en split asymétrique, favicon et balises OG en place, focus visible sur le CTA principal. Ce n'est pas un site générique. Ce qui le retient sous le seuil premium, ce sont sept plafonds précis, listés ci-dessous par ordre d'impact visuel.

---

## Ce qui est déjà bon (à ne pas casser)

- Palette mono-accent disciplinée : un seul or (#C39847) comme couleur signature, pas de second accent qui parasite.
- Hero en split 2/5 – 3/5 : asymétrie maîtrisée, kicker à filet doré, image avec zoom lent (6 s) + vignettage + halo. C'est la zone la plus aboutie du site.
- Reveals échelonnés (`hero-ani`, GSAP au scroll) avec état final forcé quand l'animation est désactivée : robuste.
- Glassmorphism utilisé avec parcimonie et à propos (pills de hero, badge RGE) plutôt qu'en décor partout.
- Accessibilité de base présente : `:focus-visible`, `aria-labelledby`, breadcrumb sémantique.

---

## Les 7 plafonds qui empêchent le 95/100

### 1. Typographie — le plus gros levier (actuel ~6/10)

C'est ici que se joue l'essentiel de l'écart perçu entre « bien fait » et « premium ».

- **Montserrat partout.** Le site tourne entièrement sur Montserrat (poids 400 à 800 chargés). Montserrat est un grotesque géométrique très répandu, sans signature. Un bureau d'étude qui se positionne comme tiers de confiance haut de gamme gagnerait énormément avec un **serif éditorial à fort contraste pour les titres H1/H2** (registre « expertise, conseil, sérieux ») associé à une **grotesque raffinée pour le corps**. Pistes gratuites et solides : *Fraunces* ou *Newsreader* (serif de titre) + *Geist*, *Satoshi* ou *Inter Tight* (corps). Ce seul changement repositionne instantanément le site d'un cran au-dessus de la concurrence solaire.
- **Incohérence à corriger** : le design system déclare `--sg-font-main: "Inter", "Montserrat"` mais Inter n'est jamais chargé. Le corps retombe donc sur Montserrat. La déclaration ment sur l'intention.
- **Chiffres non tabulaires.** Prix, kWc, %, montants d'aides : aucun `font-variant-numeric: tabular-nums`. Sur un site très chiffré, les chiffres « dansent » verticalement. À activer sur tous les blocs prix/stats (`bloc4-price`, `bloc4-stats`, `bloc3`).
- **Hiérarchie un peu plate.** Les H2 de section sont nombreux et tous au même calibre. Augmenter le contraste d'échelle sur les titres clés (display plus grand, tracking négatif plus marqué autour de −0,02em) donnerait davantage de présence sans alourdir.

### 2. Le noir n'est pas teinté — surfaces (actuel ~7/10)

- Le site empile du **noir quasi pur non teinté** : `body bg-black` (#000), puis sections en #050505, #070707, #0A0A0A, #0B0B0B. Un dark premium ne reste jamais sur du noir neutre : il **teinte le fond vers la teinte de marque** (ici, un noir très légèrement chaud, vers le brun/or, chroma minuscule). Résultat actuel : la profondeur paraît « numérique » et un peu froide au lieu de feutrée.
- **Trop de niveaux de noir proches** (#050505 / #070707 / #0A0A0A / #0B0B0B) qui se distinguent à peine : la hiérarchie des surfaces n'est pas lisible. Mieux vaut 3 paliers clairs et teintés (fond / surface / surface élevée) qu'une demi-douzaine de noirs presque identiques.

### 3. L'or est surexposé (actuel ~6/10)

L'or fait tout en même temps : kickers, titres de section (`text-gold`), bordures de cartes, icônes, badges, prix, filets, puces de liste. À force d'être partout, **l'accent perd son pouvoir d'accent**. Le réflexe premium est inverse : réserver l'or aux 2-3 moments les plus importants par page, et passer **les titres en blanc cassé** plutôt qu'en or. Le contraste « titre blanc / accent or ponctuel » est bien plus chic et plus lisible que « tout en or ». C'est un changement de discipline d'usage, pas de palette.

### 4. Texture et profondeur absentes (actuel ~6/10)

- **`grain.png` est présent dans les assets mais n'est jamais utilisé.** Les grandes sections noires sont parfaitement plates, ce qui donne un fini « vectoriel » un peu stérile. Un overlay de grain/bruit fixe, très subtil (`pointer-events:none`, opacité ~3-5 %), casse la platitude numérique et apporte le grain « analogique » qu'on associe au premium.
- **Aucune arête lumineuse sur les cartes.** Toutes les cartes ont une bordure or basse opacité mais pas de **liseré clair en haut** (1px highlight interne) qui simule la réfraction de la lumière. C'est le détail qui distingue une vraie surface premium d'un simple rectangle bordé.
- **Ombres en noir pur** (`rgba(0,0,0,0.5)`) : sur un fond déjà noir, elles sont quasi invisibles et n'apportent aucune profondeur. La profondeur, en dark, vient des **glows teintés** (halo or très diffus) et des liserés clairs, pas des drop-shadows noires.

### 5. Layout répétitif — la « recette carte » unique (actuel ~7/10)

- Une seule recette de carte est dupliquée partout : fond translucide sombre + bordure or 0,18-0,30 + radius 12-20px + lift au survol. On la retrouve sur `sg-encadre-premium`, `bloc3-card`, `partner-card`, `produit-card`, les cartes « preuves ». L'œil finit par lire « encore la même carte ».
- **Grilles répétées** : 3 colonnes égales (section positionnement), 2×2 (preuves), 2 colonnes (bloc3, produits). C'est précisément le pattern le plus « IA générique ». Hors hero, le site manque d'asymétrie, de chevauchements, de variations de tailles (un bloc qui déborde, une image qui sort de la grille, un format éditorial alterné gauche/droite).
- **Rythme vertical uniforme** : padding de sections quasi constant (60-80px). Faire respirer davantage les sections clés et resserrer les transitions secondaires créerait une cadence plus cinématographique.

### 6. Effets et motion — un interdit et quelques approximations (actuel ~7/10)

- **Texte en dégradé sur le H1** (`bg-clip-text` or → jaune → or sur la 2ᵉ ligne du titre). C'est un effet à proscrire en premium : il fragilise la lisibilité, et c'est aussi le titre LCP (impact perf). Un or plein, avec le poids et la taille pour l'emphase, est plus fort et plus net. Idem pour le prix en blanc sur dégradé or (voir point 7).
- **Anneau pulsant `pulseGold`** sur le CTA : l'animation d'opacité en boucle infinie fait un peu « gadget » et attire l'œil en continu. Un glow statique au survol serait plus haut de gamme.
- **`transition: all`** utilisé largement (design system, éditorial, blog) : anime potentiellement des propriétés de layout, peu performant. À cibler sur `transform`/`opacity`/`border-color`.
- **FAQ en `max-height` animé** : on anime une propriété de layout (saccades possibles) et le motif accordéon est lui-même le plus convenu. Une transition sur grid-rows ou un affichage progressif inline serait plus propre.
- **Courbes d'easing** : le `ease` par défaut sur les cartes manque de la décélération exponentielle (ease-out-quart/expo) qui donne le poids premium. Le hero, lui, l'a déjà (bon modèle à généraliser). Ajouter aussi un retour `:active` (léger `scale(0.98)`) sur les boutons.

### 7. Détails de finition (actuel ~7/10)

- **Prix en blanc sur fond or** (`bloc4-price-value`) : blanc sur #C39847 ≈ contraste ~1,9:1, sous le seuil lisible et peu premium. Le réflexe correct est **texte sombre sur l'or** (l'or est une couleur claire). Plus lisible, plus luxe.
- Icônes produit/bloc3 en `<img>` PNG dans des carrés or : vérifier l'homogénéité de graisse de trait et la netteté en HiDPI ; des icônes raster d'épaisseurs différentes trahissent l'assemblage.

---

## Plan d'action priorisé (impact visuel par effort)

Ordre conseillé, du plus rentable au plus fin :

1. **Swap typographique** (serif éditorial titres + grotesque corps, charger réellement les fontes, activer `tabular-nums`). Plus gros saut de perception, risque faible. **+6 à +8 pts.**
2. **Discipline de l'or** : titres en blanc cassé, or réservé aux accents clés. Aucun nouvel asset. **+3 pts.**
3. **Teinter les noirs + réduire à 3 paliers de surface** cohérents et légèrement chauds. **+2 à +3 pts.**
4. **Texture + arêtes lumineuses** : activer un overlay grain subtil, ajouter le liseré clair en haut des cartes, remplacer les ombres noires par des glows teintés. **+3 pts.**
5. **Supprimer le texte dégradé du H1 et le prix blanc-sur-or**, corriger les contrastes. **+1 à +2 pts.**
6. **Casser la monotonie des cartes/grilles** : 1 ou 2 sections en format éditorial asymétrique, variation de tailles, un débord maîtrisé. **+2 à +3 pts.**
7. **Raffiner le motion** : easing exponentiel généralisé, `:active` sur boutons, retirer l'anneau pulsant, cibler les `transition`. **+1 à +2 pts.**

Cumulés, ces axes amènent largement au-dessus de 95/100, sans refonte ni changement de stack : le site reste en HTML + Tailwind + design system existant, on améliore l'existant.

---

## Synthèse chiffrée

| Axe | Actuel | Cible |
|---|---|---|
| Typographie | 6/10 | 9,5/10 |
| Couleur & surfaces | 7/10 | 9,5/10 |
| Usage de l'accent (or) | 6/10 | 9/10 |
| Texture & profondeur | 6/10 | 9,5/10 |
| Layout & rythme | 7/10 | 9/10 |
| Effets & motion | 7/10 | 9,5/10 |
| Finition / détails | 7/10 | 9,5/10 |
| **Global** | **80/100** | **95+/100** |
