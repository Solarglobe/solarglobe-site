from __future__ import annotations

import html
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.solarglobe.fr"


PAGES = [
    {
        "path": "le-solaire/cout-installation-solaire-ile-de-france/index.html",
        "title": "Prix panneaux solaires Ile-de-France | Solarglobe",
        "description": "Combien coute une installation solaire en Ile-de-France ? Prix 3, 6 et 9 kWc, aides, TVA, rentabilite et points de vigilance.",
        "h1": "Combien coute une installation solaire en Ile-de-France ?",
        "kicker": "Prix solaire",
        "short": "En Ile-de-France, le prix d'une installation solaire depend surtout de la puissance, de la complexite de la toiture, du materiel choisi et des demarches. Une comparaison fiable doit toujours regarder le prix net, les aides, la production attendue et le retour sur investissement, pas seulement le prix par panneau.",
        "summary": [
            ["3 kWc", "Petits foyers", "Budget plus contenu, ROI sensible a l'autoconsommation"],
            ["6 kWc", "Maison familiale", "Souvent le meilleur equilibre cout / production"],
            ["9 kWc", "Gros usages electriques", "Pertinent si consommation, toiture et surplus sont coherents"],
        ],
        "sections": [
            ("Ce qui fait varier le prix", "Le cout ne se resume pas au nombre de panneaux. La hauteur du toit, l'acces chantier, le type de couverture, les ombrages, le raccordement, les protections electriques et le choix onduleur ou micro-onduleur changent fortement le budget final."),
            ("Aides et TVA", "Les aides doivent etre verifiees a la date du devis. La prime a l'autoconsommation, l'obligation d'achat du surplus et les taux de TVA applicables peuvent evoluer. Le bon calcul compare donc le cout brut, le cout net et la rentabilite sur 20 a 25 ans."),
            ("Pourquoi Solarglobe chiffre avant de recommander", "Un prix bas peut etre mauvais si la puissance est mal dimensionnee. A l'inverse, une installation premium peut etre rentable si elle produit mieux, dure plus longtemps et correspond a vos usages. L'etude Solarglobe chiffre plusieurs scenarios avant de figer la puissance."),
        ],
        "faq": [
            ("Quel est le prix exact d'une installation solaire ?", "Il depend de la puissance, du toit, du materiel et des demarches. Une fourchette sans etude reste indicative."),
            ("Faut-il choisir le devis le moins cher ?", "Pas toujours. Il faut comparer le materiel, les garanties, le dimensionnement et le gain net sur la duree."),
            ("Les aides changent-elles le ROI ?", "Oui, mais la rentabilite vient surtout de l'autoconsommation. Les aides ameliorent le cout net, elles ne compensent pas un mauvais dimensionnement."),
        ],
    },
    {
        "path": "le-solaire/3kwc-6kwc-9kwc/index.html",
        "title": "3 kWc, 6 kWc ou 9 kWc | Quelle puissance choisir",
        "description": "Comparez 3 kWc, 6 kWc et 9 kWc pour une maison : consommation, toiture, autoconsommation, batterie, surplus et rentabilite.",
        "h1": "3 kWc, 6 kWc ou 9 kWc : quelle puissance solaire choisir ?",
        "kicker": "Dimensionnement",
        "short": "La bonne puissance solaire est celle qui maximise l'autoconsommation et le retour sur investissement. 3 kWc convient aux profils sobres, 6 kWc aux maisons familiales, 9 kWc aux gros consommateurs ou aux usages electriques importants, a condition que la toiture et le surplus restent coherents.",
        "summary": [
            ["3 kWc", "Sobriete, petite toiture", "Moins cher, production limitee"],
            ["6 kWc", "Maison familiale", "Bon compromis dans beaucoup de cas"],
            ["9 kWc", "PAC, VE, piscine, gros foyer", "A verifier pour eviter trop de surplus"],
        ],
        "sections": [
            ("Le piege du surdimensionnement", "Installer plus de kWc n'est pas toujours plus rentable. Si la production part trop en surplus a faible valeur, le retour sur investissement peut se degrader."),
            ("La consommation en journee compte beaucoup", "Un foyer qui consomme en journee valorise mieux sa production. Teletravail, pompe a chaleur, ballon d'eau chaude pilote ou vehicule electrique peuvent changer la puissance optimale."),
            ("Comment Solarglobe tranche", "Nous comparons plusieurs puissances avec production estimee, autoconsommation, surplus, cout net et ROI. La recommandation finale doit etre economique, pas seulement technique."),
        ],
        "faq": [
            ("6 kWc est-il le meilleur choix ?", "Souvent, mais pas toujours. Il faut verifier la consommation, la toiture et les usages en journee."),
            ("9 kWc est-il trop grand ?", "Il peut etre pertinent pour de gros usages electriques, mais risqué si la maison consomme peu en journee."),
            ("Peut-on ajouter des panneaux plus tard ?", "Oui dans certains cas, mais il vaut mieux anticiper l'onduleur, les protections et la surface disponible."),
        ],
    },
    {
        "path": "le-solaire/batterie-ou-revente-surplus/index.html",
        "title": "Batterie solaire ou revente du surplus | Comparatif",
        "description": "Batterie solaire ou revente du surplus : comparez cout, autoconsommation, ROI, usages du soir et limites avant de choisir.",
        "h1": "Batterie solaire ou revente du surplus : que choisir ?",
        "kicker": "Stockage",
        "short": "La batterie augmente l'autoconsommation, mais elle n'est rentable que si les usages du soir justifient le stockage. La revente du surplus est plus simple, souvent suffisante, mais valorise moins chaque kWh. Le bon choix depend du profil de consommation et du cout de la batterie.",
        "summary": [
            ["Revente du surplus", "Projet simple", "Moins de cout, ROI souvent robuste"],
            ["Batterie physique", "Consommation le soir", "Plus d'autonomie, investissement plus eleve"],
            ["Pilotage des usages", "Ballon, VE, PAC", "Souvent a tester avant batterie"],
        ],
        "sections": [
            ("Quand la batterie a du sens", "Elle devient interessante si une part importante de la production part au reseau alors que la maison consomme beaucoup le soir ou la nuit."),
            ("Quand la revente suffit", "Sur une installation bien dimensionnee, le surplus peut rester limite. Dans ce cas, ajouter une batterie peut allonger le retour sur investissement."),
            ("Le role du pilotage", "Avant de stocker, on peut deplacer des consommations : chauffe-eau, recharge voiture, climatisation ou appareils programmables. C'est parfois plus rentable qu'une batterie."),
        ],
        "faq": [
            ("Une batterie rend-elle autonome ?", "Elle augmente l'autonomie, mais ne rend pas toujours independant du reseau, surtout en hiver."),
            ("La batterie virtuelle est-elle equivalente ?", "Non. C'est une offre contractuelle, pas un stockage physique dans la maison. Les conditions doivent etre lues de pres."),
            ("Peut-on ajouter une batterie plus tard ?", "Oui si l'installation est prevue pour, notamment avec un onduleur compatible ou une architecture adaptee."),
        ],
    },
    {
        "path": "produits/micro-onduleur-ou-onduleur-central/index.html",
        "title": "Micro-onduleur ou onduleur central | Comparatif solaire",
        "description": "Micro-onduleur ou onduleur central : comparez rendement, ombrage, suivi, maintenance, cout et choix selon votre toiture.",
        "h1": "Micro-onduleur ou onduleur central : lequel choisir ?",
        "kicker": "Onduleurs",
        "short": "Les micro-onduleurs optimisent chaque panneau et conviennent bien aux toitures avec ombrages, orientations multiples ou suivi module par module. L'onduleur central reste pertinent sur une toiture simple, homogene et bien exposee. Le choix doit etre lie au toit, pas a une preference commerciale.",
        "summary": [
            ["Micro-onduleur", "Toiture complexe", "Optimisation panneau par panneau"],
            ["Onduleur central", "Toiture simple", "Architecture plus centralisee"],
            ["Onduleur hybride", "Projet batterie", "Prepare le stockage selon compatibilite"],
        ],
        "sections": [
            ("Ombrage et orientations", "Si les panneaux ne produisent pas tous dans les memes conditions, l'optimisation module par module limite les pertes."),
            ("Maintenance et suivi", "Les micro-onduleurs facilitent le suivi par panneau. L'onduleur central simplifie certains diagnostics, mais concentre la conversion sur un seul appareil."),
            ("Comment choisir", "La decision vient du calpinage, des masques, de la puissance et de l'eventuel besoin batterie. Solarglobe compare l'impact economique avant recommandation."),
        ],
        "faq": [
            ("Les micro-onduleurs sont-ils toujours meilleurs ?", "Non. Ils sont tres utiles sur toitures complexes, mais une toiture simple peut rester adaptee a un onduleur central."),
            ("Quel systeme coute le moins cher ?", "Cela depend de la puissance et de la configuration. Le moins cher n'est pas toujours le plus rentable sur 25 ans."),
            ("Faut-il un onduleur hybride pour une batterie ?", "Souvent oui pour une integration simple, mais certaines batteries ont leur propre architecture."),
        ],
    },
    {
        "path": "le-solaire/panneaux-solaires-zone-abf-copropriete/index.html",
        "title": "Panneaux solaires ABF et copropriete | Guide",
        "description": "Panneaux solaires en zone ABF ou copropriete : faisabilite, autorisations, esthetique, AG, toiture et methode d'etude.",
        "h1": "Panneaux solaires en zone ABF ou copropriete : que faut-il savoir ?",
        "kicker": "Contraintes",
        "short": "En zone ABF ou en copropriete, un projet solaire doit etre prepare plus finement : integration visuelle, autorisations, vote, acces toiture, structure et raccordement. La faisabilite n'est pas impossible, mais elle doit etre documentee avant de promettre une installation.",
        "summary": [
            ["Zone ABF", "Integration et autorisations", "Dossier plus sensible"],
            ["Copropriete", "Vote et gouvernance", "Projet a rendre lisible en AG"],
            ["Toiture complexe", "Structure, acces, etancheite", "Etude technique indispensable"],
        ],
        "sections": [
            ("Zone ABF", "La contrainte patrimoniale porte surtout sur l'impact visuel et l'integration. Le dossier doit etre coherent, sobre et techniquement justifie."),
            ("Copropriete", "La decision ne depend pas seulement de la technique. Il faut expliquer le cout, les benefices, les responsabilites, la maintenance et la repartition des gains."),
            ("La bonne methode", "Avant devis definitif, Solarglobe clarifie la surface utile, les masques, le schema electrique, les demarches et les points de blocage possibles."),
        ],
        "faq": [
            ("Une zone ABF interdit-elle les panneaux ?", "Pas automatiquement. Elle impose une analyse d'integration et une instruction plus attentive."),
            ("Une copropriete peut-elle autoconsommer ?", "Oui, selon le projet et le schema retenu. Les parties communes sont souvent le premier cas a etudier."),
            ("Faut-il voter avant l'etude ?", "Il est souvent utile d'avoir une pre-etude pour presenter un dossier credible en assemblee generale."),
        ],
    },
]


def layout(page: dict) -> str:
    url = f"{SITE}/{page['path'].removesuffix('index.html')}"
    rows = "\n".join(
        f"<tr><td>{html.escape(a)}</td><td>{html.escape(b)}</td><td>{html.escape(c)}</td></tr>"
        for a, b, c in page["summary"]
    )
    sections = "\n".join(
        f"""
    <section class="sg-section sg-section-dark">
      <div class="sg-container max-w-4xl">
        <h2 class="sg-section-title text-gold">{html.escape(title)}</h2>
        <p>{html.escape(body)}</p>
      </div>
    </section>"""
        for title, body in page["sections"]
    )
    faq_html = "\n".join(
        f"""
      <article class="sg-encadre-premium">
        <h3 class="text-lg font-semibold text-gold">{html.escape(q)}</h3>
        <p class="mt-2">{html.escape(a)}</p>
      </article>"""
        for q, a in page["faq"]
    )
    schema = [
        {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "name": page["h1"],
            "url": url,
            "description": page["description"],
            "publisher": {"@type": "Organization", "name": "Solarglobe", "url": SITE + "/"},
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {
                    "@type": "Question",
                    "name": q,
                    "acceptedAnswer": {"@type": "Answer", "text": a},
                }
                for q, a in page["faq"]
            ],
        },
    ]
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(page['title'])}</title>
  <meta name="description" content="{html.escape(page['description'], quote=True)}" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="{url}" />
  <meta property="og:title" content="{html.escape(page['title'], quote=True)}" />
  <meta property="og:description" content="{html.escape(page['description'], quote=True)}" />
  <meta property="og:url" content="{url}" />
  <meta property="og:image" content="{SITE}/assets/images/og-image.jpg" />
  <meta property="og:type" content="article" />
  <link rel="icon" type="image/png" href="/assets/images/favicon.png" />
  <link rel="stylesheet" href="/assets/css/montserrat-local.css" />
  <link rel="stylesheet" href="/assets/css/solarglobe-design-system.css" />
  <link rel="stylesheet" href="/assets/css/header-common.css" />
  <link rel="stylesheet" href="/assets/css/footer-common.css" />
  <link rel="stylesheet" href="/assets/css/tailwind.css" />
  <style>
    .text-gold{{color:#C39847!important}} body.menu-open{{overflow:hidden}}
    .sg-compare-table{{width:100%;border-collapse:collapse;margin-top:1.5rem;border:1px solid rgba(195,152,71,.25)}}
    .sg-compare-table th,.sg-compare-table td{{padding:1rem;border-bottom:1px solid rgba(255,255,255,.1);text-align:left;vertical-align:top}}
    .sg-compare-table th{{color:#C39847;background:rgba(195,152,71,.08)}}
  </style>
</head>
<body class="bg-black text-white">
<div id="header-placeholder"></div>
<script src="/assets/js/header.js"></script>

<main>
  <section class="sg-hero-premium">
    <div class="sg-hero-bg" aria-hidden="true"></div>
    <div class="sg-hero-content">
      <p class="sg-hero-breadcrumb"><a href="/">Accueil</a> <span aria-hidden="true">/</span> Guide solaire</p>
      <span class="sg-hero-kicker">{html.escape(page['kicker'])}</span>
      <h1 class="sg-hero-title">{html.escape(page['h1'])}</h1>
      <p class="sg-hero-subtitle">{html.escape(page['short'])}</p>
      <div class="sg-hero-cta">
        <a href="/etude-gratuite/" class="sg-btn sg-btn-primary">Obtenir mon etude solaire gratuite</a>
      </div>
    </div>
  </section>

  <section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="reponse-courte">
    <div class="sg-container max-w-4xl">
      <div class="sg-encadre-premium">
        <span class="sg-encadre-titre" id="reponse-courte">Reponse courte</span>
        <p>{html.escape(page['short'])}</p>
      </div>
      <table class="sg-compare-table">
        <thead><tr><th>Option</th><th>Pour qui ?</th><th>Point de vigilance</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
  </section>
{sections}
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Questions frequentes</h2>
      <div class="grid gap-4">{faq_html}
      </div>
      <p class="mt-8 text-sm text-gray-300">Sources utiles : <a href="https://www.economie.gouv.fr/particuliers/aides-installation-photovoltaiques" class="text-gold hover:underline" rel="noopener">economie.gouv.fr</a>, <a href="https://www.service-public.fr/particuliers/actualites/A18205" class="text-gold hover:underline" rel="noopener">Service-Public.fr</a> et <a href="https://www.edf-oa.fr/node/1107" class="text-gold hover:underline" rel="noopener">EDF OA</a>.</p>
    </div>
  </section>
</main>

<div id="footer-placeholder"></div>
<script src="/assets/js/footer.js"></script>
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False, separators=(',', ':'))}</script>
</body>
</html>
"""


def main() -> None:
    for page in PAGES:
        target = ROOT / page["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(layout(page), encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
