from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def patch(path: str, replacements: dict[str, str]) -> None:
    p = ROOT / path
    s = p.read_text(encoding="utf-8")
    for old, new in replacements.items():
        if old not in s:
            print(f"MISS {path}: {old[:90]!r}")
        s = s.replace(old, new)
    p.write_text(s, encoding="utf-8", newline="\n")


def insert_after_first_section(path: str, block: str, marker: str) -> None:
    p = ROOT / path
    s = p.read_text(encoding="utf-8")
    if marker in s:
        return
    m = re.search(r"</section>\s*", s)
    if not m:
        print(f"NO SECTION {path}")
        return
    s = s[:m.end()] + "\n" + block + s[m.end():]
    p.write_text(s, encoding="utf-8", newline="\n")


def main() -> None:
    patch("index.html", {
        "Mat&eacute;riel haut de gamme, installation certifi&eacute;e RGE, garanties longues dur&eacute;es et accompagnement complet.":
            "Matériel sélectionné, prix expliqué, pose par professionnels qualifiés et projet encadré par SolarGlobe.",
        "<span class=\"font-bold text-gold\">Prix tout compris</span> : mat&eacute;riel premium, installation RGE, mise en service, garanties compl&egrave;tes et dossier d&rsquo;aides inclus. &Eacute;ligible &agrave; la Prime &agrave; l&rsquo;autoconsommation et aux aides locales. Transparence totale, aucun co&ucirc;t cach&eacute;.":
            "<span class=\"font-bold text-gold\">Prix lisible</span> : matériel, pose, mise en service, garanties et dossier d’aides sont expliqués avant engagement. L’étude vérifie ce qui est inclus, ce qui dépend de votre toiture et ce qui ne doit pas être vendu inutilement.",
        "<span class=\"produit-badge\">Premium</span>": "<span class=\"produit-badge\">Sélectionné</span>",
        "Panneaux premium all back contact": "Panneaux sélectionnés haut rendement",
        "alt=\"Solaire premium\"": "alt=\"Projet solaire vérifié par SolarGlobe\"",
        "Pourquoi choisir Solarglobe ? — Ultra Premium": "Pourquoi choisir SolarGlobe ?",
        "BLOC 4 : Nos packs solaires — Pro Max": "BLOC 4 : Repères prix",
        "BLOC 5 : NOS &Eacute;QUIPEMENTS — V2 Ultra Premium": "BLOC 5 : Matériel sélectionné",
        "BLOC 6 : PARTENAIRES V2 ULTRA PREMIUM": "BLOC 6 : Partenaires techniques",
    })

    patch("contact/index.html", {
        "Un conseiller Solarglobe vous accompagne de A à Z.<br>\n        Étude gratuite, réponses claires, projet maîtrisé.":
            "SolarGlobe vérifie votre projet avant engagement.<br>\n        Prix, puissance, matériel et installateur : vous avancez avec un cadre clair.",
        "Étude gratuite</span><span class=\"sg-badge-sep\">•</span><span>Réponse rapide</span><span class=\"sg-badge-sep\">•</span><span>Sans engagement</span><span class=\"sg-badge-sep\">•</span><span>Accompagnement complet":
            "Bureau d’étude</span><span class=\"sg-badge-sep\">•</span><span>Prix clair</span><span class=\"sg-badge-sep\">•</span><span>Matériel sélectionné</span><span class=\"sg-badge-sep\">•</span><span>Sans engagement",
        "Étude personnalisée": "Vérification du projet",
        "Analyse complète de votre toiture et de votre projet": "Toiture, puissance, prix et cohérence passés au crible",
        "Accompagnement complet": "Prix et options expliqués",
        "Installateurs certifiés": "Installateurs qualifiés",
        '"description": "Solarglobe installe des systèmes photovoltaïques haut de gamme en Île-de-France et départements limitrophes, avec accompagnement complet et garanties longues."':
            '"description": "SolarGlobe est un bureau d’étude solaire qui vérifie les projets photovoltaïques : étude, prix clair, matériel sélectionné et installateurs qualifiés."',
    })

    patch("produits/index.html", {
        "<title>Nos produits solaires haut de gamme | Solarglobe</title>":
            "<title>Matériel solaire sélectionné | SolarGlobe</title>",
        'content="Nos produits solaires haut de gamme avec Solarglobe : conseils, etude personnalisee, choix techniques et accompagnement pour votre projet solaire."':
            'content="SolarGlobe sélectionne le matériel solaire adapté à votre projet : panneaux, onduleurs, micro-onduleurs et batteries utiles, sans survente."',
        "Nos produits solaires <span class=\"sg-text-gold\">haut de gamme</span>":
            "Le matériel solaire <span class=\"sg-text-gold\">sélectionné pour votre projet</span>",
        "Panneaux solaires, onduleurs, micro-onduleurs et batteries : découvrez les technologies sélectionnées par Solarglobe pour construire une installation photovoltaïque fiable, performante et durable.":
            "Panneaux, onduleurs, micro-onduleurs ou batteries : SolarGlobe ne choisit pas le matériel au hasard. Chaque composant doit être utile pour votre toiture, votre consommation et votre rentabilité.",
        "Haute performance pour une production durable.": "Sélectionnés selon rendement, garantie et cohérence du projet.",
        "Stockage pour autonomie et confort énergétique.": "Étudiée seulement si votre profil la rend vraiment utile.",
        "Choisir les bons équipements pour son installation solaire": "Choisir le bon matériel sans se faire survendre",
        "Une installation photovoltaïque performante repose sur une combinaison adaptée de matériel. Toutes les maisons ne nécessitent pas la même configuration : selon votre consommation, votre toiture et vos objectifs, le dimensionnement varie.":
            "Une installation photovoltaïque fiable repose sur des choix cohérents, pas sur une liste d’équipements impressionnante. Toutes les maisons n’ont pas besoin de la même puissance, de la même architecture onduleur ou d’une batterie.",
        "Solarglobe structure son offre en quatre familles d'équipements : <strong>panneaux solaires</strong>, <strong>onduleurs</strong>, <strong>micro-onduleurs</strong> et <strong>batteries</strong>. Chaque famille joue un rôle précis dans la production, la conversion et le stockage de l'énergie. Découvrez ci-dessous nos catégories et accédez directement aux pages détaillées.":
            "SolarGlobe analyse d’abord le besoin, puis sélectionne les équipements : <strong>panneaux solaires</strong>, <strong>onduleurs</strong>, <strong>micro-onduleurs</strong> et <strong>batteries</strong>. Le matériel sert le projet, jamais l’inverse.",
        "Panneaux premium haut rendement : LONGi, Aiko et marques sélectionnées pour une production optimale.":
            "Panneaux sélectionnés pour leur rendement, leur fiabilité et leur cohérence économique.",
        "Solarglobe installe une combinaison performante : panneaux LONGi Hi-MO X10 Explorer ou Aiko Neostar 2S+ et micro-onduleurs ATMOCE. Suivez les étapes ci-dessous pour affiner votre choix selon votre profil.":
            "SolarGlobe compare les configurations possibles avant de recommander une combinaison : panneaux, micro-onduleurs, onduleur central, batterie ou pilotage. Le bon système dépend de votre profil, pas d’un catalogue standard.",
        "Pourquoi Solarglobe sélectionne des équipements premium": "Pourquoi SolarGlobe sélectionne le matériel pour vous",
        "Nous installons notamment LONGi Hi-MO X10 Explorer et Aiko Neostar 2S+, des panneaux premium avec garanties jusqu'à 25 ans.":
            "Nous recommandons notamment LONGi Hi-MO X10 Explorer ou Aiko Neostar 2S+ lorsque leur rendement, leurs garanties et leur cohérence économique correspondent au projet.",
        "Nos produits – Équipements photovoltaïques premium": "Matériel solaire sélectionné par SolarGlobe",
        "Sélection d'équipements photovoltaïques premium : panneaux solaires, onduleurs, micro-onduleurs et batteries.":
            "Sélection d'équipements photovoltaïques selon toiture, consommation, rentabilité et fiabilité.",
        "Équipements photovoltaïques premium : panneaux solaires, onduleurs, micro-onduleurs et batteries.":
            "Équipements photovoltaïques sélectionnés : panneaux solaires, onduleurs, micro-onduleurs et batteries utiles.",
        '"description": "Solarglobe installe des systèmes photovoltaïques haut de gamme en Île-de-France et départements limitrophes, avec accompagnement complet et garanties longues."':
            '"description": "SolarGlobe sélectionne le matériel solaire adapté et sécurise les choix techniques avant installation."',
    })

    insert_after_first_section("produits/index.html", """
<section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="selection-materiel-solarglobe">
  <div class="sg-container">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="selection-materiel-solarglobe">Notre rôle n’est pas de vendre le plus de matériel</span>
      <p>Notre rôle est de choisir ce qui protège votre projet. Un panneau plus cher, une batterie ou une architecture micro-onduleur ne sont utiles que s’ils améliorent réellement la production, la sécurité, la maintenance ou la rentabilité.</p>
      <p class="mt-4">SolarGlobe vérifie donc le besoin avant la recommandation&nbsp;: toiture, ombrages, consommation en journée, budget, évolution future et contraintes de pose. Vous ne comparez pas seul des fiches techniques incompréhensibles&nbsp;: nous faisons le tri pour vous.</p>
    </div>
  </div>
</section>
""", "selection-materiel-solarglobe")

    patch("notre-methode/index.html", {
        "<title>Passez au solaire. Nous gérons le reste. | Solarglobe</title>":
            "<title>Méthode SolarGlobe | Projet solaire sécurisé</title>",
        'content="Passez au solaire. Nous gérons le reste. avec Solarglobe : conseils, etude personnalisee, choix techniques et accompagnement pour votre projet solaire."':
            'content="La méthode SolarGlobe sécurise votre projet solaire : étude, dimensionnement, prix clair, matériel sélectionné, installateurs qualifiés et suivi."',
        "Passez au solaire. Nous gérons le reste.":
            "Passez au solaire sans choisir à l’aveugle.",
        "Installation de panneaux solaires photovoltaïques : étude solaire, dimensionnement, démarches administratives et installation par des experts.":
            "SolarGlobe sécurise chaque décision : étude solaire, dimensionnement, prix clair, matériel sélectionné, démarches et pose par partenaires qualifiés.",
        "Solarglobe accompagne votre projet photovoltaïque de A à Z : analyse du potentiel solaire, simulation de production, implantation des panneaux, étude financière et installation par des partenaires qualifiés.":
            "Nous sommes le cadre de confiance entre vous et le marché photovoltaïque : nous analysons, comparons, expliquons et sélectionnons avant que vous ne vous engagiez.",
        "✔ Installation par partenaires certifiés": "✔ Installateurs qualifiés sélectionnés",
        "Une méthode claire pour réussir votre projet solaire": "Une méthode claire pour réduire le risque",
        "Chez Solarglobe, chaque installation suit une méthode précise et éprouvée :\n        analyse de votre toiture, dimensionnement technique, gestion complète des démarches\n        administratives et installation par des partenaires qualifiés.":
            "Chez SolarGlobe, chaque projet suit une méthode précise : analyse de votre toiture, dimensionnement technique, vérification du prix, sélection du matériel, gestion des démarches et pose par partenaires qualifiés.",
        "Les 7 étapes d'un projet solaire maîtrisé": "Les 7 étapes d’un projet solaire sécurisé",
        "Installation des panneaux": "Pose par installateurs qualifiés",
        "Nos partenaires installateurs qualifiés réalisent la pose de votre\n        installation photovoltaïque dans le respect des normes techniques\n        et de sécurité. Chaque chantier est préparé pour garantir une\n        installation fiable et durable.":
            "La pose est confiée à des partenaires installateurs qualifiés, sélectionnés selon la zone, la toiture et les contraintes du projet. Chaque chantier est préparé à partir de l’étude pour garantir une exécution cohérente.",
        "Pourquoi choisir la m&eacute;thode Solarglobe&nbsp;?": "Pourquoi la méthode SolarGlobe rassure&nbsp;?",
        "Dimensionnement et implantation des panneaux pour maximiser la production solaire.":
            "Dimensionnement, matériel et prix vérifiés pour éviter survente et mauvais choix.",
        "Gestion des d&eacute;marches administratives, installation et suivi de votre production.":
            "Démarches, pose par partenaires qualifiés et suivi de production dans un cadre clair.",
        "Faites étudier votre projet solaire": "Faites vérifier votre projet solaire",
        "Obtenez une étude personnalisée et gratuite par nos experts.": "Obtenez une vérification claire avant de signer un devis photovoltaïque.",
        '"description": "Processus d\'accompagnement de A à Z : étude solaire, dimensionnement, calpinage, étude financière et installation."':
            '"description": "Processus SolarGlobe : étude, dimensionnement, choix du matériel, prix clair, installateurs qualifiés et suivi."',
    })

    insert_after_first_section("notre-methode/index.html", """
<section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="methode-confiance-solarglobe">
  <div class="sg-container">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="methode-confiance-solarglobe">La méthode SolarGlobe sert à éviter le mauvais choix</span>
      <p>Le photovoltaïque devient compliqué quand vous devez comparer seul des devis qui ne parlent pas le même langage. Une puissance plus forte, une batterie ou un matériel plus cher peuvent être pertinents, mais seulement si l’étude le prouve.</p>
      <p class="mt-4">Notre méthode remet de l’ordre&nbsp;: nous vérifions les hypothèses, expliquons le prix, sélectionnons le matériel utile et orientons la pose vers des installateurs qualifiés. Vous prenez une décision claire, pas une décision sous pression.</p>
    </div>
  </div>
</section>
""", "methode-confiance-solarglobe")

    patch("le-solaire/index.html", {
        'content="Produisez votre propre électricité grâce au solaire avec Solarglobe : conseils, etude personnalisee, choix techniques et accompagnement pour votre projet solaire."':
            'content="Comprendre le solaire avec SolarGlobe : prix, rentabilité, matériel, batterie, dimensionnement et pièges à éviter avant de choisir un devis."',
        "Produisez votre propre électricité grâce au solaire": "Comprendre le solaire avant de signer un devis",
        "Une installation photovoltaïque bien dimensionnée permet de réduire fortement votre facture d'électricité et de sécuriser votre énergie pendant des décennies.":
            "Le solaire peut être rentable, mais seulement si la puissance, le prix, le matériel et l’installateur sont cohérents. SolarGlobe vous aide à comprendre avant de choisir.",
        "Découvrez combien une installation photovoltaïque peut vous faire économiser sur votre facture d'électricité.":
            "Comprenez les vraies hypothèses derrière les économies annoncées.",
        "Passez à l'énergie solaire": "Faites vérifier votre projet avant de choisir",
        "Nos experts réalisent gratuitement l'étude de votre toiture et estiment vos économies.":
            "SolarGlobe vérifie gratuitement la toiture, la puissance, le prix, le matériel et la cohérence du projet.",
    })

    insert_after_first_section("le-solaire/index.html", """
<section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="solaire-choisir-confiance">
  <div class="sg-container">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="solaire-choisir-confiance">Le vrai sujet : savoir à qui faire confiance</span>
      <p>Comprendre le photovoltaïque ne veut pas dire devenir expert en panneaux, onduleurs et batteries. Le vrai enjeu est de savoir si le devis proposé est cohérent&nbsp;: bonne puissance, bon prix, matériel adapté, installateur qualifié et rentabilité réaliste.</p>
      <p class="mt-4">SolarGlobe agit comme bureau d’étude solaire indépendant&nbsp;: nous traduisons les choix techniques en décisions simples, vérifiables et compréhensibles.</p>
    </div>
  </div>
</section>
""", "solaire-choisir-confiance")

    # Target JSON-LD/meta phrasing without touching CSS class names such as sg-card-premium.
    for p in ROOT.rglob("*.html"):
        s = p.read_text(encoding="utf-8", errors="ignore")
        original = s
        s = s.replace(
            "Solarglobe installe des systèmes photovoltaïques haut de gamme en Île-de-France et départements limitrophes, avec accompagnement complet et garanties longues.",
            "SolarGlobe sécurise les projets photovoltaïques avec étude, prix clair, matériel sélectionné et installateurs qualifiés.",
        )
        if s != original:
            p.write_text(s, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
