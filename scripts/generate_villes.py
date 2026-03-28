# -*- coding: utf-8 -*-
"""Génère les 36 pages panneaux-solaires-[ville] pour SolarGlobe."""

import os

BASE = r"c:\Users\Benoit\Desktop\Benoit\Site refait"

# Zone géographique et fourchette production (kWh/kWc/an) par département
REGION_TO_ZONE = {
    "Marne": ("Grand Est", "900 à 1 050"),
    "Oise": ("Hauts-de-France", "900 à 1 050"),
    "Somme": ("Hauts-de-France", "900 à 1 050"),
    "Aisne": ("Hauts-de-France", "900 à 1 050"),
    "Eure-et-Loir": ("Centre-Val de Loire", "950 à 1 100"),
    "Loiret": ("Centre-Val de Loire", "950 à 1 100"),
}
# Par défaut : Île-de-France (Seine-et-Marne, Essonne, Yvelines, Val-d'Oise, etc.)
DEFAULT_ZONE = ("Île-de-France", "950 à 1 100")

# slug, nom, région, région_dans, variation_intro (phrase unique par ville)
VILLES = [
    ("reims", "Reims", "Marne", "la Marne", "Dans la région Grand Est, la ville de Reims et ses environs comptent de nombreux pavillons adaptés au photovoltaïque."),
    ("beauvais", "Beauvais", "Oise", "l'Oise", "En périphérie de Beauvais, dans l'Oise, les pavillons et maisons individuelles offrent un bon potentiel pour le solaire."),
    ("argenteuil", "Argenteuil", "Val-d'Oise", "le Val-d'Oise", "À Argenteuil et dans le Val-d'Oise, le secteur périurbain mêle maisons individuelles et pavillons, idéaux pour l'autoconsommation."),
    ("meaux", "Meaux", "Seine-et-Marne", "la Seine-et-Marne", "À Meaux, dans le département de Seine-et-Marne, de nombreux quartiers pavillonnaires se prêtent bien à l'installation photovoltaïque."),
    ("chelles", "Chelles", "Seine-et-Marne", "la Seine-et-Marne", "À Chelles, dans l'est de la Seine-et-Marne, les maisons individuelles sont nombreuses et le solaire y progresse rapidement."),
    ("noisy-le-grand", "Noisy-le-Grand", "Seine-Saint-Denis", "la Seine-Saint-Denis", "À Noisy-le-Grand, en Seine-Saint-Denis, la mixité habitat collectif et pavillons permet des projets solaires variés."),
    ("melun", "Melun", "Seine-et-Marne", "la Seine-et-Marne", "À Melun, préfecture de Seine-et-Marne, les maisons individuelles en périphérie offrent de bonnes conditions d'installation."),
    ("fontainebleau", "Fontainebleau", "Seine-et-Marne", "la Seine-et-Marne", "À Fontainebleau et dans la forêt environnante, les pavillons et maisons de caractère sont de plus en plus équipés en solaire."),
    ("versailles", "Versailles", "Yvelines", "les Yvelines", "À Versailles et dans les Yvelines, les pavillons et maisons individuelles représentent une part importante du parc immobilier."),
    ("saint-denis", "Saint-Denis", "Seine-Saint-Denis", "la Seine-Saint-Denis", "À Saint-Denis, en Seine-Saint-Denis, les copropriétés et pavillons du secteur périurbain explorent le photovoltaïque."),
    ("aulnay-sous-bois", "Aulnay-sous-Bois", "Seine-Saint-Denis", "la Seine-Saint-Denis", "À Aulnay-sous-Bois, en Seine-Saint-Denis, les maisons individuelles des quartiers résidentiels sont de plus en plus équipées."),
    ("drancy", "Drancy", "Seine-Saint-Denis", "la Seine-Saint-Denis", "À Drancy, en Seine-Saint-Denis, le mix habitat collectif et pavillons permet des projets solaires adaptés à chaque type de toiture."),
    ("sarcelles", "Sarcelles", "Val-d'Oise", "le Val-d'Oise", "À Sarcelles et dans le Val-d'Oise, les pavillons et maisons individuelles offrent un bon potentiel pour l'autoconsommation."),
    ("cergy", "Cergy", "Val-d'Oise", "le Val-d'Oise", "À Cergy, ville nouvelle du Val-d'Oise, les pavillons et maisons individuelles sont nombreux et adaptés au photovoltaïque."),
    ("pontoise", "Pontoise", "Val-d'Oise", "le Val-d'Oise", "À Pontoise, préfecture du Val-d'Oise, les quartiers pavillonnaires et périurbains se prêtent bien au solaire."),
    ("nanterre", "Nanterre", "Hauts-de-Seine", "les Hauts-de-Seine", "À Nanterre, dans les Hauts-de-Seine, les pavillons et maisons individuelles des secteurs résidentiels sont de plus en plus équipés."),
    ("colombes", "Colombes", "Hauts-de-Seine", "les Hauts-de-Seine", "À Colombes, dans les Hauts-de-Seine, les maisons individuelles et pavillons représentent un parc important pour le photovoltaïque."),
    ("boulogne-billancourt", "Boulogne-Billancourt", "Hauts-de-Seine", "les Hauts-de-Seine", "À Boulogne-Billancourt, dans les Hauts-de-Seine, les pavillons et maisons individuelles des quartiers résidentiels sont de bons candidats au solaire."),
    ("issy-les-moulineaux", "Issy-les-Moulineaux", "Hauts-de-Seine", "les Hauts-de-Seine", "À Issy-les-Moulineaux, dans les Hauts-de-Seine, les pavillons et maisons individuelles des secteurs résidentiels sont de plus en plus équipés."),
    ("ivry-sur-seine", "Ivry-sur-Seine", "Val-de-Marne", "le Val-de-Marne", "À Ivry-sur-Seine, dans le Val-de-Marne, les pavillons et maisons individuelles des quartiers résidentiels offrent un bon potentiel solaire."),
    ("vitry-sur-seine", "Vitry-sur-Seine", "Val-de-Marne", "le Val-de-Marne", "À Vitry-sur-Seine, dans le Val-de-Marne, les maisons individuelles et pavillons sont de plus en plus nombreux à passer au solaire."),
    ("creteil", "Créteil", "Val-de-Marne", "le Val-de-Marne", "À Créteil, ville préfecture du Val-de-Marne, les pavillons et maisons individuelles des quartiers résidentiels se prêtent bien au photovoltaïque."),
    ("saint-maur-des-fosses", "Saint-Maur-des-Fossés", "Val-de-Marne", "le Val-de-Marne", "À Saint-Maur-des-Fossés, dans le Val-de-Marne, les pavillons et maisons individuelles sont nombreux et adaptés à l'autoconsommation."),
    ("choisy-le-roi", "Choisy-le-Roi", "Val-de-Marne", "le Val-de-Marne", "À Choisy-le-Roi, dans le Val-de-Marne, les maisons individuelles et pavillons offrent de bonnes conditions pour le photovoltaïque."),
    ("evry", "Évry", "Essonne", "l'Essonne", "À Évry, ville nouvelle de l'Essonne, les pavillons et maisons individuelles sont nombreux et le solaire y progresse rapidement."),
    ("corbeil-essonnes", "Corbeil-Essonnes", "Essonne", "l'Essonne", "À Corbeil-Essonnes, dans l'Essonne, les quartiers pavillonnaires et périurbains se prêtent bien à l'installation photovoltaïque."),
    ("palaiseau", "Palaiseau", "Essonne", "l'Essonne", "À Palaiseau, sur le plateau de Saclay, les maisons individuelles et pavillons sont de plus en plus équipés en panneaux solaires."),
    ("antony", "Antony", "Hauts-de-Seine", "les Hauts-de-Seine", "À Antony, dans les Hauts-de-Seine, les pavillons et maisons individuelles des secteurs résidentiels sont de bons candidats au photovoltaïque."),
    ("massy", "Massy", "Essonne", "l'Essonne", "À Massy, dans l'Essonne, les quartiers pavillonnaires et les maisons individuelles offrent un bon potentiel pour l'autoconsommation."),
    ("rambouillet", "Rambouillet", "Yvelines", "les Yvelines", "À Rambouillet, dans les Yvelines, les pavillons et maisons individuelles en périphérie de la forêt sont de plus en plus équipés en solaire."),
    ("chartres", "Chartres", "Eure-et-Loir", "l'Eure-et-Loir", "À Chartres, dans l'Eure-et-Loir, les maisons individuelles et pavillons représentent l'essentiel du parc immobilier adapté au photovoltaïque."),
    ("orleans", "Orléans", "Loiret", "le Loiret", "À Orléans, préfecture du Loiret, les quartiers pavillonnaires et périurbains offrent de bonnes conditions pour l'installation solaire."),
    ("amiens", "Amiens", "Somme", "la Somme", "À Amiens, dans la Somme, les maisons individuelles et pavillons représentent une part importante du parc immobilier."),
    ("compiegne", "Compiègne", "Oise", "l'Oise", "À Compiègne, dans l'Oise, les pavillons et maisons individuelles en périphérie de la forêt sont de plus en plus équipés en photovoltaïque."),
    ("soissons", "Soissons", "Aisne", "l'Aisne", "À Soissons, dans l'Aisne, les maisons individuelles et pavillons offrent un bon potentiel pour l'autoconsommation solaire."),
    ("laon", "Laon", "Aisne", "l'Aisne", "À Laon, préfecture de l'Aisne, les quartiers pavillonnaires et périurbains se prêtent bien à l'installation de panneaux solaires."),
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="fr">
<head>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-N2ZQKS6F');</script>
  <!-- End Google Tag Manager -->
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Panneaux solaires à {nom} | Étude solaire et installation photovoltaïque</title>
  <meta name="description" content="Étude solaire et installation de panneaux photovoltaïques à {nom}. Analyse de rentabilité, dimensionnement et accompagnement complet." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.solarglobe.fr/panneaux-solaires-{slug}/" />
  <link rel="icon" type="image/png" href="/assets/images/favicon.png" />
  <link rel="stylesheet" href="/assets/css/montserrat-local.css" />
  <link rel="stylesheet" href="/assets/css/solarglobe-design-system.css" />
  <link rel="stylesheet" href="/assets/css/header-common.css" />
  <link rel="stylesheet" href="/assets/css/footer-common.css" />
  <link rel="stylesheet" href="/assets/css/tailwind.css" />
  <style>.text-gold{color:#C39847!important}.bg-gold{background-color:#C39847!important}.border-gold{border-color:#C39847!important}body.menu-open{overflow:hidden}</style>
</head>
<body class="bg-black text-white">

<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-N2ZQKS6F" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>

<div id="header-placeholder"></div>
<script src="/assets/js/header.js"></script>

<!-- BREADCRUMB -->
<div class="sg-container">
  <nav class="sg-breadcrumb sg-breadcrumb-dark sg-breadcrumb--compact" aria-label="Fil d'Ariane">
    <ol class="sg-breadcrumb-list">
      <li><a href="/">Accueil</a></li>
      <li><a href="/qui-sommes-nous/#zones">Zones d'intervention</a></li>
      <li aria-current="page">Installer des panneaux solaires à {nom}</li>
    </ol>
  </nav>
</div>

<!-- SECTION HERO VILLE -->
<section class="sg-hero-premium">
  <div class="sg-hero-bg" aria-hidden="true"></div>
  <div class="sg-hero-content">
    <h1 class="sg-hero-title">Installer des panneaux solaires à <span class="sg-text-gold">{nom}</span></h1>
    <p class="sg-hero-subtitle">Étude solaire, dimensionnement et installation photovoltaïque à {nom} et dans sa région.</p>
    <div class="sg-hero-cta">
      <a href="/etude-gratuite/" class="sg-btn sg-btn-primary">Demander mon étude gratuite</a>
    </div>
  </div>
</section>

<!-- SECTION INTRODUCTION LOCALE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <p>{intro_variation} Comme partout dans {region_dans}, la hausse du prix de l'électricité pousse de plus en plus de propriétaires à produire leur propre énergie en <a href="/le-solaire/autoconsommation-solaire/" class="text-gold hover:text-gold underline">autoconsommation</a>.</p>
    <p class="mt-4">Solarglobe vous accompagne pour une <a href="/notre-methode/etude-solaire/" class="text-gold hover:text-gold underline">étude solaire</a> personnalisée et une installation adaptée à votre toiture. Nos installateurs locaux sont certifiés RGE QualiPV, indispensable pour bénéficier des aides de l'État.</p>
  </div>
</section>

<!-- SECTION POURQUOI INSTALLER -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <h2 class="sg-section-title text-gold">Pourquoi installer des panneaux solaires à {nom} ?</h2>
    <p>À {nom}, dans {region_dans}, de nombreux quartiers pavillonnaires et maisons individuelles disposent de toitures inclinées adaptées au photovoltaïque. Comme partout en {zone_nom}, la hausse du prix de l'électricité incite de plus en plus de propriétaires à produire leur propre énergie.</p>
  </div>
</section>

<!-- SECTION PROJET SOLAIRE TYPE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <h2 class="sg-section-title text-gold">Projet solaire à {nom}</h2>
    <p class="mb-4">Dans la région {zone_nom}, une installation bien orientée peut produire environ {prod_range} kWh par kWc installé chaque année. Les projets les plus courants à {nom} : <strong>maison individuelle</strong> en <a href="/le-solaire/autoconsommation-solaire/" class="text-gold hover:text-gold underline">autoconsommation</a>, <strong>vente du surplus</strong> à 0,04 €/kWh, et <strong>batterie</strong> en option pour consommer le soir l'électricité produite le jour. Découvrez les <a href="/le-solaire/" class="text-gold hover:text-gold underline">bases du solaire</a> et la <a href="/le-solaire/rentabilite-panneaux-solaires/" class="text-gold hover:text-gold underline">rentabilité</a> des panneaux.</p>
    <h3 class="text-lg font-semibold text-gold mt-6 mb-2">Toitures adaptées au solaire à {nom}</h3>
    <p class="mb-6">Les maisons individuelles avec toiture inclinée représentent la configuration la plus adaptée pour une installation photovoltaïque. Les orientations sud, sud-est et sud-ouest offrent généralement les meilleures performances à {nom} et dans les environs.</p>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div class="sg-card sg-card-dark p-6">
        <h3 class="text-lg font-bold text-gold mb-2">Maison individuelle</h3>
        <p class="text-sm opacity-90">Toiture inclinée ou plate : installation sur mesure pour maximiser la production et l'autoconsommation.</p>
      </div>
      <div class="sg-card sg-card-dark p-6">
        <h3 class="text-lg font-bold text-gold mb-2">Autoconsommation</h3>
        <p class="text-sm opacity-90">Consommez l'électricité produite par vos panneaux. Revente du surplus possible (0,04 €/kWh) pour optimiser la rentabilité.</p>
      </div>
      <div class="sg-card sg-card-dark p-6">
        <h3 class="text-lg font-bold text-gold mb-2">Batterie en option</h3>
        <p class="text-sm opacity-90">Stockage d'énergie pour augmenter l'autonomie et consommer le soir l'électricité produite le jour.</p>
      </div>
    </div>
  </div>
</section>

<!-- SECTION ÉTUDE SOLAIRE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <h2 class="sg-section-title text-gold">Pourquoi une étude solaire à {nom} ?</h2>
    <p class="mb-6">Une <a href="/notre-methode/etude-solaire/" class="text-gold hover:text-gold underline">étude solaire</a> est indispensable pour dimensionner correctement votre installation. Elle analyse votre toiture, simule la production et évalue la rentabilité. Demandez votre <a href="/etude-gratuite/" class="text-gold hover:text-gold underline">étude gratuite</a> pour un projet sur mesure.</p>
    <ul class="sg-list-premium sg-list-premium-dark space-y-2">
      <li><strong>Analyse de toiture</strong> : orientation, inclinaison, ombrages pour estimer le potentiel solaire à {nom}.</li>
      <li><strong>Dimensionnement</strong> : puissance adaptée (kWc) selon votre consommation électrique.</li>
      <li><strong>Simulation de production</strong> : estimation des kWh produits par an dans votre région.</li>
      <li><strong>Rentabilité</strong> : projection des économies et du temps de retour sur investissement.</li>
      <li><strong>Aides</strong> : prime à l'autoconsommation, TVA réduite, revente du surplus.</li>
    </ul>
  </div>
</section>

<!-- SECTION RÉGLEMENTATION LOCALE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <h2 class="sg-section-title text-gold">Faut-il une autorisation pour installer des panneaux solaires à {nom} ?</h2>
    <p>Pour une installation en toiture en autoconsommation avec revente du surplus, une <strong>déclaration préalable en mairie</strong> suffit généralement. L'installation sur toiture est le plus souvent autorisée sans permis de construire. Solarglobe vous accompagne dans ces démarches et vérifie les règles spécifiques à votre secteur (sites protégés, ABF). Demandez votre <a href="/etude-gratuite/" class="text-gold hover:text-gold underline">étude gratuite</a> pour un conseil personnalisé.</p>
  </div>
</section>

<!-- SECTION FAQ LOCALE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <h2 class="sg-section-title text-gold">Questions fréquentes</h2>
    <div class="sg-faq">
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Est-il rentable d'installer des panneaux solaires à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">Oui. L'ensoleillement de {nom} et de {region_dans} permet une production photovoltaïque intéressante. Avec la prime à l'autoconsommation et la TVA réduite (5,5 %), la rentabilité est généralement bonne. Une <a href="/etude-gratuite/" class="text-gold underline">étude gratuite</a> vous donnera une estimation précise.</div>
      </div>
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Quelle puissance solaire pour une maison à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">La puissance dépend de votre consommation (kWh/an) et de la surface de toiture disponible. En moyenne, une maison consomme 3 000 à 5 000 kWh/an. Une installation de 3 à 6 kWc est souvent adaptée. Notre étude gratuite définit la puissance idéale.</div>
      </div>
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Combien coûte une installation solaire à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">Le coût varie selon la puissance (kWc) et les équipements (batterie, micro-onduleurs). Comptez environ 1 500 à 2 500 €/kWc hors aides. La prime à l'autoconsommation et la TVA à 5,5 % réduisent significativement la facture. Demandez une <a href="/etude-gratuite/" class="text-gold underline">étude gratuite</a> pour un devis personnalisé.</div>
      </div>
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Qui installe les panneaux solaires à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">Solarglobe travaille avec des installateurs certifiés RGE QualiPV dans la région. L'éligibilité aux aides (prime, TVA réduite) impose une pose par un professionnel RGE.</div>
      </div>
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Faut-il un permis de construire pour des panneaux à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">En général, non. Pour une installation en toiture en autoconsommation avec revente du surplus, une déclaration préalable suffit si les panneaux sont intégrés au bâti ou en surimposition. Les règles peuvent varier selon les secteurs protégés. Notre étude inclut le conseil sur les démarches.</div>
      </div>
      <div class="sg-faq-item">
        <button class="sg-faq-question w-full text-left" type="button" aria-expanded="false">
          <span>Faut-il une autorisation en mairie à {nom} ?</span>
          <svg class="sg-faq-icon w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"/></svg>
        </button>
        <div class="sg-faq-answer hidden">Une déclaration préalable suffit le plus souvent pour une installation en toiture à {nom}. L'installation sur toiture est généralement autorisée sans permis de construire. Solarglobe vous accompagne pour vérifier les règles spécifiques à votre secteur.</div>
      </div>
    </div>
  </div>
</section>

<!-- PHRASE FINALE LOCALE -->
<section class="sg-section sg-section-dark">
  <div class="sg-container">
    <p>Si vous êtes propriétaire d'une maison à {nom} ou dans les environs, une <a href="/etude-gratuite/" class="text-gold hover:text-gold underline">étude solaire</a> permet d'évaluer précisément le potentiel de votre toiture et la rentabilité de votre projet.</p>
  </div>
</section>

<!-- SECTION CTA -->
<section class="sg-cta sg-cta-dark">
  <div class="sg-container">
    <h2>Faites étudier votre projet solaire à {nom}</h2>
    <p>Obtenez une étude personnalisée et gratuite : analyse de toiture, dimensionnement, simulation de production et rentabilité.</p>
    <a href="/etude-gratuite/" class="sg-btn sg-btn-primary">Demander mon étude gratuite</a>
  </div>
</section>

<div id="footer-placeholder"></div>
<script src="/assets/js/footer.js"></script>

<script>
document.querySelectorAll('.sg-faq-item').forEach(item => {
  const btn = item.querySelector('.sg-faq-question');
  const answer = item.querySelector('.sg-faq-answer');
  if (!btn || !answer) return;
  btn.addEventListener('click', () => {
    const isOpen = !answer.classList.toggle('hidden');
    btn.setAttribute('aria-expanded', isOpen);
    const icon = btn.querySelector('.sg-faq-icon');
    if (icon) icon.style.transform = isOpen ? 'rotate(45deg)' : 'none';
  });
});
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.solarglobe.fr/"},
    {"@type": "ListItem", "position": 2, "name": "Zones d'intervention", "item": "https://www.solarglobe.fr/qui-sommes-nous/#zones"},
    {"@type": "ListItem", "position": 3, "name": "Installer des panneaux solaires à {nom}"}
  ]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://www.solarglobe.fr/#solarglobe",
  "name": "Solarglobe",
  "url": "https://www.solarglobe.fr/",
  "telephone": "+33 1 72 99 47 53",
  "email": "contact@solarglobe.fr",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "19 avenue Pierre Curie",
    "addressLocality": "Chelles",
    "postalCode": "77500",
    "addressRegion": "Île-de-France",
    "addressCountry": "FR"
  },
  "areaServed": ["{nom}"]
}
</script>
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {"@type": "Question", "name": "Est-il rentable d'installer des panneaux solaires à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "Oui. L'ensoleillement de {nom} et de {region_dans} permet une production photovoltaïque intéressante. Avec la prime à l'autoconsommation et la TVA réduite (5,5 %), la rentabilité est généralement bonne. Une étude gratuite vous donnera une estimation précise."}},
    {"@type": "Question", "name": "Quelle puissance solaire pour une maison à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "La puissance dépend de votre consommation (kWh/an) et de la surface de toiture disponible. En moyenne, une maison consomme 3 000 à 5 000 kWh/an. Une installation de 3 à 6 kWc est souvent adaptée. Notre étude gratuite définit la puissance idéale."}},
    {"@type": "Question", "name": "Combien coûte une installation solaire à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "Le coût varie selon la puissance (kWc) et les équipements (batterie, micro-onduleurs). Comptez environ 1 500 à 2 500 €/kWc hors aides. La prime à l'autoconsommation et la TVA à 5,5 % réduisent significativement la facture. Demandez une étude gratuite pour un devis personnalisé."}},
    {"@type": "Question", "name": "Qui installe les panneaux solaires à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "Solarglobe travaille avec des installateurs certifiés RGE QualiPV dans la région. L'éligibilité aux aides (prime, TVA réduite) impose une pose par un professionnel RGE."}},
    {"@type": "Question", "name": "Faut-il un permis de construire pour des panneaux à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "En général, non. Pour une installation en toiture en autoconsommation avec revente du surplus, une déclaration préalable suffit si les panneaux sont intégrés au bâti ou en surimposition. Les règles peuvent varier selon les secteurs protégés."}},
    {"@type": "Question", "name": "Faut-il une autorisation en mairie à {nom} ?", "acceptedAnswer": {"@type": "Answer", "text": "Une déclaration préalable suffit le plus souvent pour une installation en toiture. L'installation sur toiture est généralement autorisée sans permis de construire. Solarglobe vous accompagne pour vérifier les règles spécifiques à votre secteur."}}
  ]
}
</script>

</body>
</html>
'''

def main():
    for slug, nom, region, region_dans, intro_variation in VILLES:
        zone_nom, prod_range = REGION_TO_ZONE.get(region, DEFAULT_ZONE)
        folder = os.path.join(BASE, f"panneaux-solaires-{slug}")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, "index.html")
        content = (TEMPLATE
            .replace("{slug}", slug)
            .replace("{nom}", nom)
            .replace("{region}", region)
            .replace("{region_dans}", region_dans)
            .replace("{intro_variation}", intro_variation)
            .replace("{zone_nom}", zone_nom)
            .replace("{prod_range}", prod_range))
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Créé : panneaux-solaires-{slug}/index.html")
    print(f"\n{len(VILLES)} pages créées.")

if __name__ == "__main__":
    main()
