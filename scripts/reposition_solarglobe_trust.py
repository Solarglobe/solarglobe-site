from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def write(path: str, text: str) -> None:
    (ROOT / path).write_text(text, encoding="utf-8", newline="\n")


def replace(text: str, old: str, new: str) -> str:
    if old not in text:
        print(f"MISS: {old[:90]!r}")
        return text
    return text.replace(old, new)


def patch_home() -> None:
    path = "index.html"
    s = read(path)

    s = replace(s, "<title>Solarglobe | Panneaux solaires premium en Ile-de-France</title>",
                "<title>Solarglobe | Bureau d'&eacute;tude solaire de confiance</title>")
    s = replace(s,
                '<meta name="description" content="Installation de panneaux solaires premium en Ile-de-France : etude gratuite, prix clair, garanties longues et accompagnement complet Solarglobe." />',
                '<meta name="description" content="SolarGlobe sécurise votre projet solaire : vraie étude, prix clair, matériel sélectionné, installateurs qualifiés et accompagnement sans mauvaise surprise." />')
    s = replace(s,
                '<meta property="og:title" content="Solarglobe | Panneaux solaires premium en Ile-de-France" />',
                '<meta property="og:title" content="Solarglobe | Bureau d\'étude solaire de confiance" />')
    s = replace(s,
                '<meta property="og:description" content="Installation de panneaux solaires premium en Ile-de-France : etude gratuite, prix clair, garanties longues et accompagnement complet Solarglobe." />',
                '<meta property="og:description" content="SolarGlobe sécurise votre projet solaire : vraie étude, prix clair, matériel sélectionné, installateurs qualifiés et accompagnement sans mauvaise surprise." />')
    s = replace(s,
                '<meta name="twitter:title" content="Solarglobe | Panneaux solaires premium en Ile-de-France" />',
                '<meta name="twitter:title" content="Solarglobe | Bureau d\'étude solaire de confiance" />')
    s = replace(s,
                '<meta name="twitter:description" content="Installation de panneaux solaires premium en Ile-de-France : etude gratuite, prix clair, garanties longues et accompagnement complet Solarglobe." />',
                '<meta name="twitter:description" content="SolarGlobe sécurise votre projet solaire : vraie étude, prix clair, matériel sélectionné, installateurs qualifiés et accompagnement sans mauvaise surprise." />')

    s = replace(s,
                '<span class="text-white block">Nous ne vendons pas des panneaux.</span>\n        <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold via-yellow-200/95 to-gold block mt-1">Nous concevons des projets solaires.</span>',
                '<span class="text-white block">Vous voulez du solaire,</span>\n        <span class="text-transparent bg-clip-text bg-gradient-to-r from-gold via-yellow-200/95 to-gold block mt-1">mais vous ne savez pas à qui faire confiance&nbsp;?</span>')
    s = replace(s,
                'Chaque installation est dimensionn&eacute;e, optimis&eacute;e et valid&eacute;e pour maximiser votre rentabilit&eacute;.',
                'SolarGlobe est le bureau d&rsquo;&eacute;tude qui sécurise votre projet&nbsp;: vraie analyse, prix clair, matériel sélectionné et installateurs qualifiés.')
    s = replace(s,
                '<span>Bureau d&rsquo;&eacute;tudes solaire</span>',
                '<span>Bureau d&rsquo;&eacute;tudes indépendant</span>')
    s = replace(s,
                '<span>Rentabilit&eacute; optimis&eacute;e</span>',
                '<span>Projet sécurisé</span>')
    s = replace(s,
                '<span>Mat&eacute;riel s&eacute;lectionn&eacute;</span>',
                '<span>Matériel sélectionné</span>')
    s = replace(s,
                'Obtenir mon &eacute;tude solaire gratuite',
                'Faire vérifier mon projet solaire')

    s = replace(s,
                "Solarglobe est un specialiste du photovoltaique residentiel premium base a Chelles, en Ile-de-France. L&#x27;entreprise accompagne les particuliers depuis l&#x27;etude de faisabilite jusqu&#x27;au dimensionnement, aux demarches, a l&#x27;installation et au suivi de production.",
                "SolarGlobe est un bureau d&rsquo;étude solaire basé à Chelles. Notre rôle est simple&nbsp;: vous éviter de choisir seul entre des devis difficiles à comparer. Nous analysons votre maison, dimensionnons la bonne puissance, sélectionnons le matériel adapté, puis orientons la pose vers des installateurs qualifiés.")
    s = replace(s, '<li>Zone principale : Ile-de-France et departements limitrophes.</li>',
                '<li>Zone principale&nbsp;: Île-de-France et départements limitrophes.</li>')
    s = replace(s, '<li>Expertise : panneaux solaires, onduleurs, micro-onduleurs, batteries et autoconsommation.</li>',
                '<li>Expertise&nbsp;: étude, dimensionnement, rentabilité, matériel, installateurs et démarches.</li>')
    s = replace(s, '<li>Promesse : une etude chiffree avant recommandation materielle.</li>',
                '<li>Promesse&nbsp;: un projet clair, cohérent et sécurisé avant toute décision.</li>')

    s = replace(s,
                'Le bon projet n&rsquo;est pas celui qui a le plus de panneaux, mais celui qui vous rapporte vraiment.',
                'Le bon projet n&rsquo;est pas celui qui vous vend le plus de panneaux, mais celui qui vous évite le mauvais choix.')
    s = replace(s, '<div class="bloc2-cell bloc2-cell-solar">Solarglobe</div>',
                '<div class="bloc2-cell bloc2-cell-solar">SolarGlobe, bureau d&rsquo;étude</div>')
    s = replace(s, '<div class="bloc2-cell bloc2-cell-install">Installateur classique</div>',
                '<div class="bloc2-cell bloc2-cell-install">Devis solaire classique</div>')
    s = replace(s, 'Dimensionnement bas&eacute; sur votre consommation r&eacute;elle',
                'Dimensionnement basé sur votre maison et vos usages réels')
    s = replace(s, 'Objectif&nbsp;: vendre une installation',
                'Objectif&nbsp;: faire signer un devis')
    s = replace(s, 'Choix techniques arbitr&eacute;s selon le co&ucirc;t sur 20&ndash;25 ans',
                'Matériel sélectionné selon performance, fiabilité et intérêt économique')
    s = replace(s, 'Choix dict&eacute;s par le mat&eacute;riel en stock ou la marge',
                'Matériel parfois dicté par le stock, l’habitude ou la marge')
    s = replace(s, 'D&eacute;cision bas&eacute;e sur la rentabilit&eacute; r&eacute;elle du client',
                'Installateur qualifié sélectionné et projet piloté jusqu’à la mise en service')
    s = replace(s, 'D&eacute;cision bas&eacute;e sur le devis &agrave; signer',
                'Vous devez souvent comparer seul des offres incomparables')
    s = replace(s,
                "Un projet solaire rentable repose sur une &eacute;tude pr&eacute;cise de votre consommation, de votre toiture et de votre potentiel de production. Chez Solarglobe, chaque installation est dimensionn&eacute;e pour optimiser l&rsquo;autoconsommation, la rentabilit&eacute; et la coh&eacute;rence &eacute;conomique sur le long terme.",
                "Un projet solaire fiable ne repose pas sur une promesse commerciale, mais sur une étude vérifiable. SolarGlobe fait le tri pour vous&nbsp;: puissance, matériel, prix, installateur et rentabilité sont contrôlés avant engagement.")

    s = replace(s,
                'Pourquoi choisir <span class="sg-highlight">Solarglobe</span> pour votre installation solaire&nbsp;?',
                'Pourquoi passer par <span class="sg-highlight">SolarGlobe</span> avant de choisir&nbsp;?')
    s = replace(s,
                "Chez Solarglobe, nous concevons des installations photovolta&iuml;ques r&eacute;ellement rentables, dimensionn&eacute;es selon votre consommation r&eacute;elle. Moins de promesses, plus de r&eacute;sultats mesurables sur 20 &agrave; 25 ans.",
                "Parce que le plus grand risque dans le photovoltaïque n&rsquo;est pas le soleil&nbsp;: c&rsquo;est de choisir le mauvais devis. Nous sécurisons chaque décision avant la pose.")

    card_replacements = {
        "Rentabilit&eacute; mesurable": "Vraie étude avant devis",
        "Jusqu&rsquo;&agrave; 90&nbsp;% de r&eacute;duction sur la facture d&rsquo;&eacute;lectricit&eacute; selon les profils. Un retour sur investissement g&eacute;n&eacute;ralement constat&eacute; entre 8 et 14 ans, bas&eacute; sur votre consommation r&eacute;elle et v&eacute;rifi&eacute; apr&egrave;s installation.<br><br>Pas de kW inutiles&nbsp;: chaque projet est dimensionn&eacute; pour produire juste ce qu&rsquo;il faut.": "Nous partons de votre toiture, de votre consommation et de vos objectifs. La puissance recommandée doit être justifiée, lisible et rentable.<br><br>Pas de kW inutiles&nbsp;: le bon projet est celui qui tient dans la durée.",
        "Technologie utile": "Matériel sélectionné",
        "Panneaux Longi Hi-MO X10 Explorer et micro-onduleurs ATMOCE, s&eacute;lectionn&eacute;s pour leur rendement, leur fiabilit&eacute; et leur coh&eacute;rence &eacute;conomique.<br><br>Le mat&eacute;riel est un moyen, pas une finalit&eacute;&nbsp;: il est choisi uniquement s&rsquo;il am&eacute;liore la rentabilit&eacute; globale du projet.": "Panneaux, onduleurs, micro-onduleurs ou batterie&nbsp;: chaque composant est choisi pour son intérêt réel dans votre projet.<br><br>Nous ne vendons pas une marque au hasard&nbsp;: nous sélectionnons ce qui protège votre performance.",
        "Vision long terme": "Installateurs qualifiés",
        "25 ans de garantie sur les modules et la production, 10 ans sur l&rsquo;installation, avec des partenaires certifi&eacute;s RGE / QualiPV.<br><br>Des garanties utiles, pens&eacute;es pour s&eacute;curiser la performance dans le temps, pas pour rassurer sur le papier.": "La pose est confiée à des professionnels qualifiés, sélectionnés selon la zone, la toiture et le niveau d’exigence du dossier.<br><br>Vous ne cherchez pas seul à qui faire confiance&nbsp;: nous faisons ce tri pour vous.",
        "Accompagnement r&eacute;el": "Prix clair et défendu",
        "Un interlocuteur d&eacute;di&eacute; dans votre d&eacute;partement, pr&eacute;sent avant, pendant et apr&egrave;s la pose.<br><br>Parce qu&rsquo;un projet rentable se pilote aussi dans le temps.": "Le prix doit être compréhensible&nbsp;: puissance, matériel, options, aides et limites sont expliqués avant décision.<br><br>Un prix juste n’est pas le plus bas&nbsp;: c’est celui qui correspond au bon projet.",
        "Prix coh&eacute;rent": "Pas de survente",
        "Prix TTC annonc&eacute;s d&egrave;s le d&eacute;part, puissance et options justifi&eacute;es.<br><br>Vous payez un projet &eacute;quilibr&eacute;, pas des kilowatts superflus.": "Batterie, puissance élevée, options techniques&nbsp;: nous les recommandons seulement si elles ont du sens pour vous.<br><br>Notre intérêt est un projet cohérent, pas une facture gonflée.",
        "R&eacute;seau ma&icirc;tris&eacute;": "Un seul cadre de confiance",
        "Installations r&eacute;alis&eacute;es par des &eacute;quipes locales certifi&eacute;es RGE / QualiPV, s&eacute;lectionn&eacute;es et suivies.<br><br>La pose est ex&eacute;cut&eacute;e par des professionnels, le projet est pilot&eacute; par Solarglobe.": "Étude, matériel, installateur, démarches et suivi sont pensés ensemble.<br><br>Vous gardez un interlocuteur qui comprend le projet complet, pas une succession de promesses séparées."
    }
    for old, new in card_replacements.items():
        s = replace(s, old, new)

    s = replace(s, 'Nos packs solaires tout compris', 'Des repères de prix, pas des devis imposés')
    s = replace(s, 'Qualit&eacute; premium, prix clair, &eacute;conomies durables.',
                'Prix visibles, projet ajusté, décisions expliquées.')
    s = replace(s,
                "Ces packs servent de <strong>rep&egrave;res tarifaires</strong>. Chaque projet est <strong>ajust&eacute; selon votre consommation r&eacute;elle, votre toiture et votre objectif de rentabilit&eacute;</strong>.",
                "Ces packs servent de <strong>repères tarifaires</strong>. L’étude SolarGlobe vérifie ensuite la bonne puissance, les options utiles et l’installateur adapté, pour éviter le devis trop cher ou mal dimensionné.")
    s = replace(s, 'Nos &eacute;quipements solaires d&rsquo;exception', 'Le matériel que nous sélectionnons pour vous')
    s = replace(s,
                'Panneaux solaires LONGi, micro-onduleurs performants, &eacute;quipements certifi&eacute;s RGE&nbsp;: nous travaillons avec les meilleures technologies du march&eacute; pour garantir performance et durabilit&eacute;.',
                'Nous sélectionnons les panneaux, micro-onduleurs, batteries et équipements selon votre toiture, votre consommation et votre rentabilité. Le matériel doit servir le projet, pas l’inverse.')
    s = replace(s, 'Nos partenaires technologiques', 'Nos choix techniques sont assumés')
    s = replace(s, 'Entreprise certifi&eacute;e RGE', 'Pose par des professionnels qualifiés')
    s = replace(s,
                "Solarglobe est certifi&eacute;e RGE (Reconnu Garant de l&rsquo;Environnement), une qualification indispensable pour garantir la qualit&eacute; des installations photovolta&iuml;ques et permettre l&rsquo;acc&egrave;s aux aides de l&rsquo;&Eacute;tat.",
                "SolarGlobe cadre l’étude et sélectionne des installateurs qualifiés RGE / QualiPV lorsque la pose est lancée. Le client bénéficie d’un projet étudié en amont, d’un matériel choisi et d’une exécution confiée à des professionnels adaptés au dossier.")
    s = replace(s, 'Certification v&eacute;rifiable aupr&egrave;s des organismes officiels.',
                'Les qualifications et conditions d’éligibilité sont vérifiées dossier par dossier avant engagement.')
    s = replace(s, 'Accompagnement et suivi sur le long terme', 'Un projet suivi, pas seulement vendu')
    s = replace(s,
                'Chaque client b&eacute;n&eacute;ficie d&rsquo;un interlocuteur d&eacute;di&eacute; et d&rsquo;un suivi de production en temps r&eacute;el.<br>\n          <span style="color: rgba(195,152,71,0.9); font-weight: 500;">Garanties 25 ans, performance v&eacute;rifi&eacute;e.</span>',
                'Vous gardez un interlocuteur qui connaît l’étude, les choix techniques et les étapes de pose.<br>\n          <span style="color: rgba(195,152,71,0.9); font-weight: 500;">Le projet reste lisible du premier échange à la mise en service.</span>')
    s = replace(s, 'Passez &agrave; l&rsquo;&eacute;nergie solaire haut de gamme d&egrave;s aujourd&rsquo;hui',
                'Ne choisissez pas votre projet solaire à l’aveugle')
    s = replace(s, 'Demandez votre &eacute;tude gratuite, faites le choix de la qualit&eacute;.',
                'Faites vérifier votre toiture, votre puissance, votre matériel et votre prix avant de vous engager.')
    s = replace(s, 'Solarglobe, entreprise locale ind&eacute;pendante, fond&eacute;e par deux passionn&eacute;s du solaire.<br>',
                'SolarGlobe, bureau d’étude solaire indépendant, fondé pour redonner confiance dans le photovoltaïque.<br>')

    # JSON-LD descriptions
    s = s.replace("Solarglobe installe des panneaux solaires premium en Île-de-France et départements voisins, avec garanties longues et accompagnement complet.",
                  "SolarGlobe sécurise les projets photovoltaïques résidentiels : étude, dimensionnement, sélection du matériel, installateurs qualifiés et prix clair.")
    s = s.replace("Produisez votre propre électricité avec Solarglobe. Étude gratuite, installation certifiée RGE, garanties jusqu’à 25 ans et suivi après la pose.",
                  "Passez au solaire sans choisir à l'aveugle : étude gratuite, projet vérifié, matériel sélectionné, prix clair et installateurs qualifiés.")
    s = s.replace("Solarglobe installe des systèmes photovoltaïques haut de gamme en Île-de-France et départements limitrophes, avec accompagnement complet et garanties longues.",
                  "SolarGlobe est un bureau d'étude solaire qui sécurise les projets photovoltaïques en Île-de-France et alentours.")

    write(path, s)


def patch_header_footer() -> None:
    s = read("components/header.html")
    s = s.replace("Solarglobe â€” Panneaux solaires premium", "Solarglobe — Bureau d'étude solaire")
    s = s.replace(">Le solaire<", ">Comprendre<")
    s = s.replace(">Notre m&eacute;thode<", ">Méthode<")
    s = s.replace(">Produits<", ">Matériel<")
    s = s.replace("Notre gamme de produits photovolta&iuml;ques", "Matériel sélectionné selon votre projet")
    s = s.replace("&Eacute;tude gratuite", "Projet vérifié")
    s = s.replace("Les 7 &eacute;tapes d'un projet solaire avec Solarglobe", "Comment SolarGlobe sécurise votre projet")
    write("components/header.html", s)

    s = read("components/footer.html")
    s = s.replace("Bureau d&rsquo;&eacute;tude photovolta&iuml;que nouvelle g&eacute;n&eacute;ration.",
                  "Bureau d&rsquo;étude solaire indépendant&nbsp;: étude, prix clair, matériel sélectionné et installateurs qualifiés.")
    s = s.replace("<li>Simulation solaire</li>", "<li>Prix clair</li>")
    s = s.replace("<li>Dimensionnement</li>", "<li>Matériel sélectionné</li>")
    s = s.replace("<li>Gestion administrative</li>", "<li>Installateurs qualifiés</li>")
    s = s.replace("Obtenir mon &eacute;tude solaire gratuite", "Faire vérifier mon projet solaire")
    s = s.replace("Produits", "Matériel")
    s = s.replace("Prix panneaux solaires", "Prix clair")
    s = s.replace("Installation photovolta&iuml;que", "Pose encadrée")
    write("components/footer.html", s)


def patch_page(path: str, replacements: dict[str, str]) -> None:
    s = read(path)
    for old, new in replacements.items():
        s = replace(s, old, new)
    write(path, s)


def patch_strategic_pages() -> None:
    patch_page("etude-gratuite/index.html", {
        "<title>Etude solaire gratuite | Solarglobe</title>": "<title>Faire vérifier son projet solaire | SolarGlobe</title>",
        'content="Demandez une etude solaire gratuite : faisabilite, dimensionnement, production, rentabilite et conseils pour votre maison."': 'content="Faites vérifier votre projet solaire : toiture, puissance, prix, matériel, batterie éventuelle et installateur qualifié avec SolarGlobe."',
        "Étude <span class=\"text-gold\">solaire</span> gratuite": "Faites vérifier votre <span class=\"text-gold\">projet solaire</span>",
        "Obtenez une estimation fiable de votre installation photovoltaïque, adaptée à votre maison, votre toiture et votre consommation réelle.": "Vous hésitez entre plusieurs devis ou vous ne savez pas à qui faire confiance ? SolarGlobe vérifie la puissance, le prix, le matériel et la cohérence du projet avant engagement.",
        "Étude personnalisée</span><span class=\"sg-badge-sep\">•</span><span>Production estimée</span><span class=\"sg-badge-sep\">•</span><span>Rentabilité</span><span class=\"sg-badge-sep\">•</span><span>Autoconsommation</span><span class=\"sg-badge-sep\">•</span><span>Batteries</span><span class=\"sg-badge-sep\">•</span><span>Installation": "Prix clair</span><span class=\"sg-badge-sep\">•</span><span>Matériel sélectionné</span><span class=\"sg-badge-sep\">•</span><span>Installateur qualifié</span><span class=\"sg-badge-sep\">•</span><span>Pas de survente</span>",
        "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
        "Lancez votre étude en quelques étapes": "Lancez une vérification claire de votre projet",
        "Nous préparons une étude solaire personnalisée fiable et réaliste.": "Nous vérifions si votre projet est cohérent avant qu'un devis ne vous engage.",
        "Ce que contient votre etude solaire gratuite": "Ce que SolarGlobe vérifie pour vous",
        "Une etude solaire gratuite Solarglobe sert a verifier si votre toiture, votre consommation et votre budget peuvent former un projet photovoltaique coherent. Elle ne se limite pas a une estimation de prix : elle cadre la puissance, la production, l'autoconsommation, les aides et les points de vigilance avant devis.": "Une étude SolarGlobe sert à vous éviter le mauvais choix photovoltaïque. Nous vérifions votre toiture, votre consommation et votre budget, puis nous cadrons la puissance, le prix, le matériel, l’installateur et les points de vigilance avant décision.",
        "<li><strong>Choix techniques :</strong> panneaux, onduleur ou micro-onduleurs, batterie si elle a du sens.</li>": "<li><strong>Choix techniques :</strong> panneaux, onduleur ou micro-onduleurs, batterie seulement si elle a du sens.</li>\n        <li><strong>Sélection :</strong> matériel adapté et installateur qualifié selon votre projet.</li>",
        "3. Recommandation claire": "3. Recommandation sécurisée",
        "Vous obtenez une orientation chiffrable : puissance conseillee, logique materielle, rentabilite attendue et prochaines etapes.": "Vous obtenez une orientation compréhensible : puissance conseillée, prix cohérent, matériel adapté, rentabilité attendue et prochaines étapes.",
        "Non. Vous pouvez partir de zero ou comparer une proposition existante. L'etude aide justement a comprendre si la puissance et le materiel proposes sont adaptes.": "Non. Vous pouvez partir de zéro ou comparer une proposition existante. L’étude sert justement à savoir si le devis, la puissance, le matériel et les options sont cohérents.",
    })

    patch_page("qui-sommes-nous/index.html", {
        'content="Decouvrez Solarglobe, specialiste des installations solaires premium en Ile-de-France : methode, engagements, garanties et expertise."': 'content="Découvrez SolarGlobe, bureau d’étude solaire indépendant : étude fiable, prix clair, matériel sélectionné et installateurs qualifiés."',
        "Plus qu'un installateur. Un <span class=\"gold\">partenaire solaire</span>.": "Le bureau d’étude qui <span class=\"gold\">sécurise votre projet solaire</span>.",
        "Nous concevons des projets photovoltaïques premium avec exigence, transparence et logique de rentabilité réelle.": "Nous aidons les particuliers à passer au solaire sans choisir seuls entre des devis opaques, du matériel incompréhensible et des promesses difficiles à vérifier.",
        "Matériel haut de gamme</span><span class=\"sg-badge-sep\">•</span><span>Économies réelles</span><span class=\"sg-badge-sep\">•</span><span>Conseil sans pression": "Prix clair</span><span class=\"sg-badge-sep\">•</span><span>Matériel sélectionné</span><span class=\"sg-badge-sep\">•</span><span>Installateurs qualifiés",
        "Lancer mon étude gratuite": "Faire vérifier mon projet",
        "Qui est Solarglobe": "Pourquoi SolarGlobe existe",
        "Solarglobe est un bureau d'études photovoltaïque indépendant, spécialisé dans la conception d'installations solaires performantes, durables et esthétiques. Fondée par Benoît et Nicolas, notre mission est simple : vous aider à produire votre énergie dans les meilleures conditions.": "SolarGlobe est un bureau d’étude solaire indépendant, fondé pour répondre à une peur très simple : vouloir passer au photovoltaïque, mais ne pas savoir à qui faire confiance. Notre mission est de faire le tri pour vous avant toute décision.",
        "Une étude sérieuse, un dimensionnement sur mesure et une sélection d'équipements haut de gamme (panneaux, onduleurs, batteries), pour des résultats réellement atteignables. Nous croyons que le solaire doit être rentable, fiable et sans promesses exagérées.": "Nous réalisons une étude sérieuse, dimensionnons juste, sélectionnons le matériel et orientons la pose vers des installateurs qualifiés. Le client garde un cadre clair : prix compréhensible, options justifiées, pas de batterie inutile, pas de surdimensionnement.",
        "Matériel haut de gamme, prix maîtrisé": "Matériel sélectionné, prix défendu",
        "Nous sélectionnons des équipements premium (performance, fiabilité, esthétique) et nous optimisons le projet pour éviter les surcoûts inutiles.": "Nous sélectionnons les équipements selon votre toiture, votre consommation et votre rentabilité, puis nous expliquons ce qui justifie le prix.",
        "On ne vend pas simplement des panneaux. On construit des projets cohérents, durables et rentables.": "On ne vous demande pas de faire confiance au hasard. On construit un projet solaire clair, cohérent et vérifiable.",
    })

    patch_page("contact/index.html", {
        'content="Contactez Solarglobe pour une etude solaire, une question technique, un devis ou un accompagnement photovoltaique en Ile-de-France."': 'content="Contactez SolarGlobe pour faire vérifier un projet solaire, comparer un devis, clarifier un prix ou sécuriser votre installation photovoltaïque."',
        "Chaque installation est unique. Nous analysons votre toiture, votre consommation et votre objectif pour vous proposer une solution réellement adaptée. Découvrez notre <a href=\"/notre-methode/\" class=\"text-gold hover:underline\">méthode d'accompagnement</a>.": "Vous avez un doute sur un devis, un prix, une batterie ou le choix d’un installateur ? SolarGlobe vérifie le projet avant engagement : toiture, puissance, matériel, rentabilité et cohérence globale. Découvrez notre <a href=\"/notre-methode/\" class=\"text-gold hover:underline\">méthode d'accompagnement</a>.",
        "Pourquoi nous faire confiance ?": "Pourquoi nous contacter avant de signer ?",
        "Matériel premium": "Projet vérifié",
    })

    patch_page("faq/index.html", {
        "Vous vous posez des questions sur l'installation de panneaux solaires, la rentabilité, les aides ou le fonctionnement d'une installation photovoltaïque ?": "Vous vous demandez surtout à qui faire confiance pour votre projet solaire ? Voici les réponses sur l’étude, le prix, le matériel, les installateurs, la rentabilité et les pièges à éviter.",
        "C'est pour cette raison que Solarglobe fonctionne comme un bureau d'étude photovoltaïque. Notre rôle est d'analyser précisément chaque projet afin de dimensionner une installation réellement adaptée à votre maison.": "C'est pour cette raison que SolarGlobe fonctionne comme un bureau d'étude photovoltaïque. Notre rôle est d'analyser le projet avant la pose, de vérifier le prix, de sélectionner le matériel utile et d’orienter vers des installateurs qualifiés.",
        "Pourquoi passer par un bureau d'étude solaire ?": "Pourquoi passer par SolarGlobe avant de choisir ?",
        "Un bureau d'étude photovoltaïque analyse précisément votre projet avant toute installation. Cette approche garantit une solution adaptée à votre situation réelle.": "Un bureau d'étude photovoltaïque vous évite de choisir à l’aveugle. SolarGlobe compare les options, vérifie les hypothèses du devis, sélectionne le matériel adapté et sécurise le choix de l’installateur.",
        "Faites étudier votre projet solaire gratuitement": "Faites vérifier votre projet solaire gratuitement",
        "Chaque maison est différente. Notre bureau d'étude analyse précisément votre toiture afin de déterminer la solution solaire la plus performante.": "Chaque maison est différente. Notre bureau d'étude vérifie la toiture, la puissance, le prix, le matériel et la cohérence du projet avant engagement.",
        "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
    })

    simple_pages = {
        "notre-methode/index.html": {
            "Les 7 étapes d'un projet solaire avec Solarglobe": "La méthode SolarGlobe pour ne pas choisir à l’aveugle",
            "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
            "installation solaire": "projet solaire",
        },
        "produits/index.html": {
            "Notre gamme de produits photovoltaïques": "Le matériel que SolarGlobe sélectionne",
            "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
        },
        "rentabilite-solaire/index.html": {
            "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
            "Faites étudier votre projet solaire": "Faites vérifier votre projet solaire",
        },
        "le-solaire/index.html": {
            "Obtenir mon étude solaire gratuite": "Faire vérifier mon projet solaire",
            "bureau d'étude photovoltaïque": "bureau d'étude solaire indépendant",
        },
    }
    for path, repl in simple_pages.items():
        if (ROOT / path).exists():
            patch_page(path, repl)


def city_name_from_path(p: Path) -> str:
    slug = p.parent.name.replace("panneaux-solaires-", "")
    return " ".join(part.capitalize() for part in slug.split("-"))


def patch_city_pages() -> None:
    block_tpl = """
<section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="solarglobe-confiance-locale">
  <div class="sg-container">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="solarglobe-confiance-locale">Pourquoi passer par SolarGlobe à {city}&nbsp;?</span>
      <p>À {city}, le plus difficile n’est pas seulement de poser des panneaux solaires. C’est de savoir quel devis croire, quelle puissance choisir, quel matériel accepter et à quel installateur faire confiance.</p>
      <p class="mt-4">SolarGlobe agit comme bureau d’étude solaire&nbsp;: nous vérifions la toiture, la consommation, le prix, le matériel, les options et la rentabilité avant de vous orienter vers une solution cohérente. Vous ne choisissez pas seul entre des offres incomparables&nbsp;: nous sécurisons le projet avec vous.</p>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Puissance dimensionnée selon votre maison, pas selon une formule standard.</li>
        <li>Matériel sélectionné selon performance, fiabilité et intérêt économique.</li>
        <li>Installateur qualifié choisi selon la zone, la toiture et les contraintes du chantier.</li>
        <li>Prix expliqué clairement pour éviter surdimensionnement, batterie inutile ou options mal justifiées.</li>
      </ul>
    </div>
  </div>
</section>
"""
    for p in ROOT.glob("panneaux-solaires-*/index.html"):
        s = p.read_text(encoding="utf-8")
        if "solarglobe-confiance-locale" in s:
            continue
        city = city_name_from_path(p)
        block = block_tpl.format(city=city)
        m = re.search(r"</section>\s*", s)
        if m:
            s = s[:m.end()] + "\n" + block + s[m.end():]
            p.write_text(s, encoding="utf-8", newline="\n")
            print(f"city patched: {p}")


def main() -> None:
    patch_home()
    patch_header_footer()
    patch_strategic_pages()
    patch_city_pages()


if __name__ == "__main__":
    main()
