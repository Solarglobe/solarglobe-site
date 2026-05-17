# Audit SEO et referencement IA - Solarglobe

Date de l'audit : 17 mai 2026  
Perimetre analyse : fichiers locaux du site statique `Site Solarglobe`  
Limite : audit technique et contenu realise depuis le code source local, sans donnees Google Search Console, GA4, logs serveur ni crawl live de production.

## 1. Synthese executive

Le site Solarglobe dispose deja d'une base SEO solide : nombreuses pages locales, sitemap, robots.txt, canonicals, balisage Schema.org, maillage interne fonctionnel et contenus thematiques pertinents autour du solaire residentiel.

Les principaux freins actuels ne sont pas des 404, mais des problemes de qualite SEO :

- trop de titres trop longs, donc tronques dans les resultats Google ;
- plusieurs descriptions absentes ou mal calibrees ;
- duplication structurelle entre anciennes pages, pages `seo/`, pages `pages-expertise/` et pages canoniques ;
- pages de redirection encore presentes dans le depot, parfois sans H1 ni description ;
- donnees structurees riches mais repetees, avec risque de sur-optimisation ou d'incoherence ;
- couverture sitemap incomplete par rapport aux fichiers existants ;
- manque de formats specifiquement optimises pour les moteurs IA : reponses courtes, sources, preuves, entites, comparatifs et pages "questions".

Priorite globale : nettoyer les signaux techniques avant d'ajouter de nouvelles pages. Le site a deja beaucoup de contenu ; il faut maintenant renforcer la confiance, clarifier les canoniques et transformer les contenus en reponses facilement citables par Google AI Overviews, ChatGPT, Perplexity, Copilot et autres moteurs generatifs.

## 2. Donnees mesurees

### Structure et indexation

- 119 fichiers HTML detectes dans le depot.
- 85 URLs declarees dans `sitemap.xml`.
- 29 pages HTML hors sitemap, dont plusieurs pages de redirection, pages privees ou anciennes pages `seo/`.
- 0 lien interne casse detecte dans le precedent audit interne : 1869 liens internes resolus vers un fichier existant.
- `robots.txt` autorise tout le site et pointe vers `https://www.solarglobe.fr/sitemap.xml`.

### Balises SEO

- 5 fichiers sans balise `<title>` pertinente, surtout fichiers techniques ou verification.
- 32 pages sans meta description.
- 11 pages sans canonical.
- 31 fichiers avec un nombre de H1 different de 1, dont plusieurs redirections, pages privees ou pages anciennes.
- 71 titres depassent 65 caracteres.
- 18 descriptions sont trop courtes sous 120 caracteres.
- 29 descriptions depassent 170 caracteres.

### Images

- 168 balises image analysees.
- 1 image sans attribut `alt`.
- 17 images avec `alt=""`, ce qui est acceptable pour les images decoratives, mais a verifier pour les images commerciales ou explicatives.

### Donnees structurees

Le site utilise deja plusieurs schemas pertinents :

- `LocalBusiness` / `SolarEnergyContractor`
- `Organization`
- `BreadcrumbList`
- `FAQPage`
- `BlogPosting`
- `Product`
- `Service`
- `WebPage`
- `ItemList`
- `AggregateRating`

Point positif : c'est une base forte pour SEO local et IA.  
Point de vigilance : les schemas sont nombreux et repetes. Ils doivent rester strictement coherents avec le contenu visible de chaque page.

## 3. Audit SEO technique

### 3.1 Indexation et sitemap

Defaut constate : le sitemap contient 85 URLs alors que 119 fichiers HTML existent. Certaines pages absentes sont normales si elles sont privees, redirections ou pages techniques. En revanche, il faut documenter clairement lesquelles doivent etre indexees.

Exemples de pages hors sitemap :

- `etude-solaire-gratuite/index.html`
- `le-solaire/rentabilite-panneaux-solaires/index.html`
- `merci/index.html`
- `pages-expertise/*`
- `seo/*`
- plusieurs pages HTML racine anciennes : `aides-financieres.html`, `autonomie-solaire.html`, `rendement-panneaux.html`

Solution :

- classer toutes les pages en 4 statuts : indexable, redirection, noindex, privee ;
- mettre dans le sitemap uniquement les pages indexables finales ;
- ajouter `noindex` aux pages privees et pages merci ;
- supprimer du depot ou rediriger proprement les anciennes pages qui ne doivent plus ranker ;
- regenerer le sitemap apres nettoyage.

Priorite : haute.

### 3.2 Canonicals

Defaut constate : 22 pages ont un canonical qui ne correspond pas a leur URL physique attendue. C'est souvent volontaire pour les pages de redirection ou pages `seo/`, mais cela cree un signal complexe.

Probleme SEO : Google peut passer du temps a crawler des pages qui disent "je ne suis pas la version principale". A grande echelle, cela dilue le budget crawl et rend la structure moins lisible.

Solution :

- conserver une seule URL finale par intention de recherche ;
- remplacer les pages doublons par des redirections 301 quand elles n'ont plus de valeur propre ;
- eviter de garder des pages HTML completes avec canonical vers une autre page si une 301 suffit ;
- verifier que chaque page indexable a un canonical auto-referent.

Priorite : haute.

### 3.3 Pages de redirection conservees en HTML

Defaut constate : plusieurs pages sont des pages de redirection avec peu ou pas de contenu SEO :

- `seo/aides-financements/index.html`
- `seo/autoconsommation-solaire/index.html`
- `seo/batteries-solaires/index.html`
- `seo/installation-solaire/index.html`
- `pages-expertise/rentabilite-solaire/index.html`
- `etude-solaire-gratuite/index.html`
- fichiers racine comme `aides-financieres.html`, `rendement-panneaux.html`

Solution :

- si ces pages sont anciennes URLs : remplacer par redirection 301 serveur via `vercel.json`;
- si elles doivent rester accessibles : ajouter `noindex, follow`;
- eviter qu'elles apparaissent dans le maillage interne principal.

Priorite : haute.

### 3.4 Titres trop longs

Defaut constate : 71 titres depassent 65 caracteres. Exemples :

- `bureau-etude-photovoltaique/index.html` : 107 caracteres ;
- `qui-sommes-nous/index.html` : 92 caracteres ;
- `dimensionnement-photovoltaique/index.html` : 89 caracteres ;
- plusieurs pages villes entre 80 et 90 caracteres.

Impact : les titres sont tronques dans Google, perdent en lisibilite et diluent le mot-cle principal.

Solution :

- viser 45 a 60 caracteres ;
- placer le mot-cle principal au debut ;
- garder la marque uniquement si elle apporte de la confiance ;
- eviter les doubles promesses dans le titre.

Exemples de reecriture :

- Ancien : `Bureau d'etude photovoltaique : pourquoi l'etude est essentielle avant d'installer des panneaux solaires`
- Nouveau : `Bureau d'etude photovoltaique | Solarglobe`

- Ancien : `Panneaux solaires a Saint-Maur-des-Fosses : etude photovoltaique et rentabilite locale`
- Nouveau : `Panneaux solaires Saint-Maur-des-Fosses`

Priorite : moyenne a haute.

### 3.5 Meta descriptions absentes ou trop longues

Defaut constate : 32 pages sans meta description et 29 descriptions trop longues.

Impact : Google reecrit souvent les snippets, et les pages perdent en controle commercial.

Solution :

- ajouter une description unique sur chaque page indexable ;
- viser 140 a 160 caracteres ;
- inclure : service + zone + preuve + action.

Modele :

`Etude solaire a [ville] avec Solarglobe : dimensionnement, rentabilite, demarches et installation premium. Recevez une estimation claire.`

Priorite : moyenne.

### 3.6 H1 multiples ou absents

Defaut constate : 31 fichiers avec un nombre de H1 different de 1. Beaucoup sont des redirections ou pages privees, mais certaines pages utiles sont concernees.

Solution :

- chaque page indexable doit avoir exactement un H1 ;
- les pages de redirection doivent etre en 301 ou `noindex`;
- les pages privees peuvent rester hors SEO, mais doivent etre bloquees proprement.

Priorite : moyenne.

### 3.7 Maillage interne

Point positif : l'audit interne precedent indique 0 lien interne casse sur 1869 liens analyses.

Defaut qualitatif : certains liens de villes pointent vers des pages departementales ou pages generiques. Ce n'est pas une erreur technique, mais cela peut decevoir l'utilisateur et affaiblir la pertinence locale.

Exemples :

- villes sans page dediee qui pointent vers `/etude-gratuite/` ;
- villes eloignees rattachees a une grande ville voisine ;
- hubs departementaux utilises comme pages ville.

Solution :

- distinguer visuellement "pages villes" et "zones couvertes" ;
- creer des pages dediees seulement pour les villes prioritaires ;
- pour les villes secondaires, assumer le lien vers une page departementale avec un libelle clair ;
- ajouter des liens contextuels depuis les pages villes vers pages piliers : rentabilite, aides, dimensionnement, batterie, etude gratuite.

Priorite : moyenne.

### 3.8 Performance et ressources

Points positifs :

- image hero prechargee ;
- polices locales Montserrat prechargees ;
- nombreuses images en AVIF/WebP ;
- lazy loading present.

Risques :

- scripts externes GSAP via CDN sur la page d'accueil ;
- Google Tag Manager charge tot ;
- header et footer injectes via `fetch()`, ce qui peut retarder le rendu de liens importants pour certains crawlers secondaires ;
- videos presentes sur le parcours d'etude, a surveiller pour le poids.

Solutions :

- deferer les scripts non critiques ;
- servir GSAP localement si besoin ;
- s'assurer que le header et le footer critiques sont visibles dans le HTML final ou pre-rendus ;
- tester Core Web Vitals sur mobile avec PageSpeed Insights ou Lighthouse ;
- surveiller LCP, INP, CLS page par page.

Priorite : moyenne.

## 4. Audit SEO contenu

### 4.1 Architecture thematique

Forces :

- pages produits : panneaux, onduleurs, micro-onduleurs, batteries ;
- pages education : autoconsommation, rendement, aides, puissance, batterie ;
- pages methodes : etude, dimensionnement, calpinage, installation, suivi ;
- pages locales nombreuses ;
- blog actif avec sujets de longue traine.

Defauts :

- trop de repertoires paralleles pour des intentions proches ;
- anciennes pages `seo/` qui semblent remplacees mais restent presentes ;
- risque de cannibalisation sur rentabilite, etude solaire, dimensionnement et panneaux solaires ;
- plusieurs pages semblent viser les memes requetes avec des angles tres proches.

Solution :

- definir une page pilier par intention :
  - `panneaux solaires` : `/produits/panneaux-solaires/`
  - `rentabilite solaire` : `/rentabilite-solaire/`
  - `dimensionnement photovoltaique` : `/dimensionnement-photovoltaique/`
  - `bureau d'etude photovoltaique` : `/bureau-etude-photovoltaique/`
  - `etude solaire gratuite` : `/etude-gratuite/`
- rediriger les doublons vers la page pilier ;
- renforcer les liens internes vers ces pages piliers.

Priorite : haute.

### 4.2 SEO local

Forces :

- nombreuses pages villes et departements ;
- Schema `LocalBusiness` ;
- adresse, telephone, email, horaires ;
- zone servie explicite ;
- pages Ile-de-France et departements.

Defauts :

- les pages villes peuvent paraitre generiques si elles ne contiennent pas assez de specificites locales ;
- certaines villes hors coeur de zone renvoient vers des pages trop generales ;
- les preuves locales visibles pourraient etre plus fortes : chantiers, photos, avis, contraintes administratives locales.

Solutions :

- ajouter sur les pages villes prioritaires :
  - contexte local : type de toiture, urbanisme, zone ABF si pertinent ;
  - exemple de production locale ;
  - cas client ou exemple de configuration ;
  - lien vers Google Business Profile ;
  - FAQ locale courte ;
  - preuve d'intervention dans le departement.
- prioriser les villes commerciales fortes : Chelles, Meaux, Fontainebleau, Melun, Paris, Versailles, Nanterre, Creteil, Massy, Evry, Argenteuil.

Priorite : haute pour les pages locales business.

### 4.3 E-E-A-T et confiance

Forces :

- page qui-sommes-nous ;
- mentions de garanties ;
- partenaires et marques ;
- methode detaillee ;
- donnees structurees avec organisation et entreprise locale.

Defauts :

- les contenus experts devraient mieux montrer qui parle, sur quelle experience, et avec quelles sources ;
- les chiffres de rentabilite, aides et tarifs doivent etre dates et sources ;
- les avis clients doivent etre prouvables et coherents avec Google Business Profile.

Solutions :

- ajouter un bloc "Verifie par Solarglobe" ou "Mise a jour le..." sur les contenus aides, rentabilite, batterie ;
- citer les sources officielles quand il s'agit d'aides, tarifs de rachat, TVA, Enedis, obligations administratives ;
- ajouter des auteurs ou validateurs internes ;
- publier 3 a 5 cas concrets anonymises avec chiffres : puissance, departement, production estimee, economie, ROI.

Priorite : haute pour les pages argent, aides et rentabilite.

## 5. Audit donnees structurees

### Points positifs

Le site exploite deja les schemas qui comptent pour ce secteur :

- `LocalBusiness` pour le local ;
- `SolarEnergyContractor` pour l'activite ;
- `FAQPage` pour les questions ;
- `BreadcrumbList` pour la navigation ;
- `Product` pour les equipements ;
- `BlogPosting` pour les articles.

### Defauts et risques

1. `AggregateRating` est repete sur de nombreuses pages avec `ratingValue: 5` et `reviewCount: 12`.

Risque : si ces avis ne sont pas visibles sur chaque page ou pas justifies par une source, Google peut ignorer ou considerer le balisage comme abusif.

Solution : afficher la preuve visible ou limiter l'aggregateRating aux pages ou l'avis est contextualise.

2. Les schemas `FAQPage` sont nombreux.

Risque : Google affiche moins de rich results FAQ qu'avant, mais les FAQ restent utiles pour l'IA. Le danger est surtout la repetition.

Solution : garder des FAQ uniques par page, avec reponses courtes, factuelles et non dupliquees.

3. Les donnees LocalBusiness sont repetees.

Solution : conserver un bloc canonique coherent, idéalement identique, et eviter les variantes de zone ou d'adresse non maitrisees.

4. Verifier l'encodage.

Plusieurs sorties terminal peuvent afficher des caracteres mal interpretes selon l'encodage de la console. Il faut distinguer cet affichage du contenu reel des fichiers, qui doit etre verifie en UTF-8 dans le navigateur et dans le HTML source live.

Priorite : moyenne a haute.

## 6. Audit referencement IA / GEO / LLMO

Le referencement IA consiste a rendre le site facile a comprendre, citer et recommander par les moteurs generatifs. Les criteres principaux ne sont pas seulement les mots-cles : ce sont la clarte des entites, la fiabilite des reponses, les preuves, les comparatifs et la structure.

### 6.1 Forces actuelles pour l'IA

- Domaine specialise et coherent : solaire residentiel premium.
- Bonne couverture thematique : aides, rentabilite, batterie, dimensionnement, autoconsommation.
- Presence de FAQ, schemas et blog.
- Identite locale claire : Solarglobe, Chelles, Ile-de-France et departements limitrophes.
- Donnees de contact structurees.
- Contenus explicatifs susceptibles d'etre repris en reponse IA.

### 6.2 Defauts IA prioritaires

Defaut 1 : les contenus sont parfois longs sans reponse directe en haut de page.

Solution :

- ajouter sous chaque H1 un bloc "Reponse courte" de 40 a 70 mots ;
- inclure la reponse a la question principale sans attendre le milieu de page ;
- exemple : "Une installation solaire est rentable lorsque la puissance est dimensionnee selon la consommation diurne, le taux d'autoconsommation et le cout pose. En Ile-de-France, le retour sur investissement se situe souvent autour de X a Y ans selon profil."

Defaut 2 : manque de sources explicites.

Solution :

- ajouter des liens vers sources officielles sur les pages aides et reglementation ;
- indiquer la date de mise a jour ;
- separer les donnees factuelles des recommandations Solarglobe.

Defaut 3 : entites pas assez consolidees.

Solution :

- creer une page ou section "Solarglobe en bref" avec :
  - nom legal ;
  - adresse ;
  - zone couverte ;
  - specialites ;
  - certifications ;
  - marques posees ;
  - garanties ;
  - contact ;
  - liens sociaux.
- reprendre ces informations de facon identique dans les schemas.

Defaut 4 : manque de comparatifs exploitables par l'IA.

Solution :

- creer des tableaux comparatifs courts :
  - micro-onduleur vs onduleur central ;
  - batterie physique vs batterie virtuelle ;
  - 3 kWc vs 6 kWc vs 9 kWc ;
  - autoconsommation vs revente du surplus ;
  - panneaux LONGi vs Aiko selon usage.

Defaut 5 : manque de "claim pages" ou pages preuves.

Solution :

- publier une page "Nos garanties" ;
- publier une page "Nos marques et pourquoi nous les avons choisies" ;
- publier une page "Exemples de projets solaires en Ile-de-France" ;
- publier 3 fiches cas client anonymisees.

### 6.3 Pages a creer pour l'IA

Priorite 1 :

- `Combien coute une installation solaire en Ile-de-France ?`
- `Quelle rentabilite pour des panneaux solaires en Ile-de-France ?`
- `Quelle puissance solaire choisir pour une maison ?`
- `Batterie solaire ou revente du surplus : que choisir ?`
- `Micro-onduleur ou onduleur central : comparaison`

Priorite 2 :

- `Panneaux solaires et zone ABF : que faut-il savoir ?`
- `Installation solaire en copropriete : faisabilite et demarches`
- `Comment Solarglobe calcule la rentabilite d'un projet solaire ?`
- `Les erreurs a eviter avant de signer un devis solaire`

Chaque page doit contenir :

- une reponse courte ;
- un tableau de synthese ;
- une FAQ unique ;
- des sources ;
- un schema `FAQPage` ou `Article` ;
- un CTA vers l'etude gratuite.

### 6.4 Format de contenu recommande pour IA

Pour chaque page informative :

1. H1 clair sous forme de question ou intention.
2. Reponse courte des les 100 premiers mots.
3. Tableau de decision.
4. Explication detaillee.
5. Exemple chiffre.
6. Limites et cas ou la reponse change.
7. FAQ.
8. Sources et date de mise a jour.
9. CTA.

Cette structure aide Google, Perplexity et ChatGPT a extraire des passages fiables.

## 7. Priorites d'action

### Priorite 1 - Nettoyage technique

- Mettre a plat toutes les URLs indexables.
- Remplacer les pages doublons par 301.
- Mettre `noindex` sur pages privees, merci, presentation, redirections conservees.
- Corriger les canonicals pour toutes les pages indexables.
- Regenerer le sitemap.

### Priorite 2 - Titres et descriptions

- Raccourcir les 71 titres trop longs.
- Ajouter les 32 meta descriptions manquantes.
- Harmoniser les pages villes avec un modele SEO propre.
- Corriger les pages avec 0 ou plusieurs H1 si elles sont indexables.

### Priorite 3 - SEO local et preuves

- Renforcer les pages villes prioritaires.
- Ajouter cas clients ou exemples de projets.
- Afficher les preuves d'avis et certifications.
- Clarifier les zones couvertes au lieu de faire croire a une page ville quand c'est un hub.

### Priorite 4 - Donnees structurees

- Verifier `AggregateRating`.
- Dedoublonner les schemas LocalBusiness.
- Garder des FAQ uniques et visibles.
- Ajouter `Article`/`BlogPosting` propre avec auteur, date, date de modification et sources.

### Priorite 5 - Referencement IA

- Ajouter des blocs "Reponse courte".
- Creer les pages comparatives et questions prioritaires.
- Ajouter sources officielles et dates de mise a jour.
- Structurer les contenus pour extraction IA : tableaux, listes courtes, exemples chiffres, limites.

## 8. Quick wins en 7 jours

1. Generer une liste definitive des URLs indexables.
2. Rediriger ou noindex toutes les anciennes pages `seo/` et `pages-expertise/`.
3. Corriger sitemap et canonicals.
4. Raccourcir les titres des 20 pages les plus importantes.
5. Ajouter meta descriptions sur les pages indexables sans description.
6. Ajouter un bloc "Reponse courte" sur rentabilite, aides, dimensionnement, batterie, panneaux solaires.
7. Verifier `AggregateRating` et supprimer le balisage la ou la preuve n'est pas visible.

## 9. Plan 30 jours

Semaine 1 : hygiene technique, sitemap, canonicals, noindex, redirections.  
Semaine 2 : optimisation titles/descriptions/H1 et maillage vers pages piliers.  
Semaine 3 : renforcement SEO local sur les pages villes prioritaires.  
Semaine 4 : referencement IA avec blocs reponses, tableaux comparatifs, sources et pages questions.

## 10. Conclusion

Solarglobe n'a pas un probleme de volume de contenu. Le site a deja beaucoup de matiere et une bonne base locale. Le vrai levier est la consolidation : moins de doublons, des URLs plus nettes, des signaux techniques plus propres, des titres plus lisibles, des preuves plus visibles et des reponses plus directes pour les moteurs IA.

Une fois ce nettoyage fait, les nouvelles pages auront beaucoup plus de chance de performer, car Google et les moteurs generatifs comprendront mieux quelle page fait autorite pour chaque sujet.
