const fs = require("fs");
const path = require("path");

const root = process.cwd();

const files = [
  "index.html",
  "etude-gratuite/index.html",
  "qui-sommes-nous/index.html",
  "notre-methode/index.html",
  "faq/index.html",
  "rentabilite-solaire/index.html",
  "produits/index.html",
  "merci/index.html",
];

const replacements = [
  ["Solarglobe", "SolarGlobe"],

  ["Faisabilite toiture", "Faisabilité toiture"],
  ["contraintes d'acces", "contraintes d'accès"],
  ["puissance adaptee", "puissance adaptée"],
  ["Demarches", "Démarches"],
  ["points administratifs a anticiper", "points administratifs à anticiper"],
  ["Comment se deroule l'etude ?", "Comment se déroule l'étude ?"],
  ["usages electriques", "usages électriques"],
  ["economie, autonomie", "économie, autonomie"],
  ["preparation d'un futur vehicule electrique", "préparation d'un futur véhicule électrique"],
  ["le cout ou la production", "le coût ou la production"],
  ["demander l'etude", "demander l'étude"],
  ["valider la coherence", "valider la cohérence"],
  ["mal dimensionne", "mal dimensionné"],
  ["Faut-il deja avoir un devis ?", "Faut-il déjà avoir un devis ?"],
  ["Peut-on etudier une batterie ?", "Peut-on étudier une batterie ?"],
  ["Quels documents preparer ?", "Quels documents préparer ?"],
  ["facture d'electricite", "facture d'électricité"],
  ["suffisent pour demarrer", "suffisent pour démarrer"],

  ["Calculez la rentabilite de panneaux solaires : economies, autoconsommation, surplus, aides et retour sur investissement avec SolarGlobe.", "Calculez la rentabilité de panneaux solaires : économies, autoconsommation, surplus, aides et retour sur investissement avec SolarGlobe."],
  ["Une installation solaire est rentable quand la puissance est ajustee a la consommation reelle et que l&#x27;autoconsommation reste elevee. Le calcul doit croiser cout pose, production estimee, aides, surplus revendu et evolution du prix de l&#x27;electricite.", "Une installation solaire est rentable quand la puissance est ajustée à la consommation réelle et que l&#x27;autoconsommation reste élevée. Le calcul doit croiser coût de pose, production estimée, aides, surplus revendu et évolution du prix de l&#x27;électricité."],
  ["Sources utiles pour verifier les aides", "Sources utiles pour vérifier les aides"],
  ["economie.gouv.fr", "economie.gouv.fr"],
  ["Questions frequentes sur les panneaux solaires : cout, aides, rentabilite, installation, batteries et accompagnement SolarGlobe.", "Questions fréquentes sur les panneaux solaires : coût, aides, rentabilité, installation, batteries et accompagnement SolarGlobe."],

  ["alt=\"Ancienne mention RGE obsolète\"", "alt=\"Installateurs RGE indépendants QualiPV\""],
  ["alt=\"Certification RGE QualiPV\"", "alt=\"Installateurs RGE indépendants externes RGE QualiPV\""],
  ["alt=\"Certification RGE QualiPV pour installations photovolta&iuml;ques\"", "alt=\"Installateurs RGE indépendants QualiPV pour la pose photovolta&iuml;que\""],
  ["&#10003; Certification RGE", "&#10003; Partenaires RGE"],
  ["Projets r&eacute;alis&eacute;s avec des installateurs certifi&eacute;s RGE / QualiPV, audit&eacute;s pour garantir la conformit&eacute; et la performance.", "Pose confi&eacute;e &agrave; des installateurs RGE indépendants / QualiPV, v&eacute;rifi&eacute;s dossier par dossier pour la conformit&eacute; et la qualit&eacute; d'ex&eacute;cution."],
  ["Pose par des partenaires certifi&eacute;s RGE.", "Pose par des partenaires externes certifi&eacute;s RGE."],
  ["installation par des partenaires RGE QualiPV et suivi", "pose par des installateurs RGE indépendants / QualiPV sélectionnés et suivi"],

  ["Les modèles installés par SolarGlobe respectent les normes en vigueur.", "Les modèles sélectionnés par SolarGlobe respectent les normes en vigueur ; la pose est réalisée par un professionnel RGE sélectionné."],
  ["Le dimensionnement se fait au cas par cas lors de l'étude.", "Le dimensionnement se fait au cas par cas lors de l'étude SolarGlobe."],

  ["retours publics reformulés pour le web, sans en modifier le sens.", "avis publics consultables sur Google."],
  ["Extraits issus d&rsquo;avis Google publics, adapt&eacute;s pour la lisibilit&eacute; sur le site. Les avis sans texte sont inclus dans le total affich&eacute; (12), sans citation.", "Avis publics consultables sur Google. Les avis sans texte sont inclus dans le total affich&eacute; (12), sans citation."],
  ["Textes adaptés pour le web à partir d’avis publics ; le fond des retours est respecté.", "Avis publics consultables sur Google ; les avis sans texte sont inclus dans le total affiché."],
];

const removeReviewLinks = [
  /<a href="https:\/\/g\.page\/r\/CbEg9WD5YfYCEBM\/review" class="sg-google-reviews__btn-google sg-google-reviews__btn-google--leave"[^>]*>\s*Laisser un avis\s*<\/a>/g,
];

for (const rel of files) {
  const full = path.join(root, rel);
  let html = fs.readFileSync(full, "utf8");
  for (const [from, to] of replacements) html = html.split(from).join(to);
  html = html
    .split("https://www.SolarGlobe.fr").join("https://www.solarglobe.fr")
    .split("https://SolarGlobe.fr").join("https://solarglobe.fr")
    .split("www.SolarGlobe.fr").join("www.solarglobe.fr")
    .split("contact@SolarGlobe.fr").join("contact@solarglobe.fr")
    .split("instagram.com/SolarGlobe.fr").join("instagram.com/solarglobe.fr")
    .split("/assets/css/SolarGlobe-design-system.css").join("/assets/css/solarglobe-design-system.css")
    .split("methode-confiance-SolarGlobe").join("methode-confiance-solarglobe");
  for (const re of removeReviewLinks) html = html.replace(re, "");
  fs.writeFileSync(full, html, "utf8");
  console.log(`cleaned ${rel}`);
}
