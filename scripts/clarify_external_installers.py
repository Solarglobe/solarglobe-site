from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REPLACEMENTS = {
    "installateurs qualifiés": "installateurs externes sélectionnés pour leur professionnalisme",
    "Installateurs qualifiés": "Installateurs externes sélectionnés",
    "installateur qualifié": "installateur externe sélectionné",
    "Installateur qualifié": "Installateur externe sélectionné",
    "partenaires qualifiés": "partenaires externes sélectionnés",
    "partenaires installateurs qualifiés": "partenaires installateurs externes sélectionnés",
    "professionnels qualifiés": "professionnels externes sélectionnés",
    "professionnels adaptés au dossier": "professionnels externes adaptés au dossier",
    "Pose par des professionnels qualifiés": "Pose par installateurs externes sélectionnés",
    "pose par professionnels qualifiés": "pose par installateurs externes sélectionnés",
    "pose par partenaires qualifiés": "pose par partenaires externes sélectionnés",
    "Installation par nos partenaires certifiés RGE": "Pose par des partenaires externes sélectionnés et certifiés RGE",
    "Installation RGE incluse": "Pose RGE par partenaire externe sélectionné",
    "Installation par partenaires certifiés": "Pose par partenaires externes sélectionnés",
    "nos partenaires installateurs": "des partenaires installateurs externes",
    "Nos partenaires installateurs": "Des partenaires installateurs externes",
    "notre installation": "la pose sélectionnée",
    "La nôtre non": "Celle que nous sélectionnons non",
    "La n&ocirc;tre non": "Celle que nous sélectionnons non",
}

TARGETED = {
    "index.html": {
        "SolarGlobe est le bureau d&rsquo;&eacute;tude qui sécurise votre projet&nbsp;: vraie analyse, prix clair, matériel sélectionné et installateurs externes sélectionnés pour leur professionnalisme.":
            "SolarGlobe est le bureau d&rsquo;&eacute;tude qui sécurise votre projet&nbsp;: vraie analyse, prix clair, matériel sélectionné et pose confiée à des installateurs externes sélectionnés pour leur professionnalisme.",
        "Nous analysons votre maison, dimensionnons la bonne puissance, sélectionnons le matériel adapté, puis orientons la pose vers des installateurs externes sélectionnés pour leur professionnalisme.":
            "Nous analysons votre maison, dimensionnons la bonne puissance, sélectionnons le matériel adapté, puis confions la pose à des installateurs externes sélectionnés pour leur professionnalisme. SolarGlobe ne pose pas directement&nbsp;: nous cadrons, sélectionnons et pilotons.",
        "Installateurs externes sélectionnés</h3>":
            "Installateurs externes sélectionnés</h3>",
        "La pose est confiée à des professionnels externes sélectionnés, sélectionnés selon la zone, la toiture et le niveau d’exigence du dossier.":
            "La pose est confiée à des installateurs externes sélectionnés selon leur professionnalisme, la zone, la toiture et le niveau d’exigence du dossier.",
        "SolarGlobe cadre l’étude et sélectionne des installateurs externes sélectionnés pour leur professionnalisme RGE / QualiPV lorsque la pose est lancée.":
            "SolarGlobe cadre l’étude et sélectionne des installateurs externes RGE / QualiPV pour leur professionnalisme lorsque la pose est lancée.",
        "Intervention par des professionnels qualifi&eacute;s":
            "Intervention par un partenaire externe sélectionné",
        "Installation conforme aux normes":
            "Pose conforme aux normes",
        '"serviceType": "Installation photovoltaïque résidentielle"':
            '"serviceType": "Bureau d’étude solaire et sélection d’installateurs externes"',
    },
    "components/footer.html": {
        "installateurs externes sélectionnés pour leur professionnalisme.": "installateurs externes sélectionnés pour leur professionnalisme.",
    },
    "etude-gratuite/index.html": {
        "matériel, batterie éventuelle et installateur externe sélectionné avec SolarGlobe":
            "matériel, batterie éventuelle et pose par installateur externe sélectionné avec SolarGlobe",
        "<span>Installateur externe sélectionné</span>":
            "<span>Installateur externe sélectionné</span>",
        "le matériel, l’installateur et les points de vigilance":
            "le matériel, le choix de l’installateur externe et les points de vigilance",
        "matériel adapté et installateur externe sélectionné selon votre projet":
            "matériel adapté et installateur externe sélectionné selon son professionnalisme et les contraintes de votre projet",
    },
    "qui-sommes-nous/index.html": {
        "Installateurs externes sélectionnés</span>":
            "Installateurs externes sélectionnés</span>",
        "Nous réalisons une étude sérieuse, dimensionnons juste, sélectionnons le matériel et orientons la pose vers des installateurs externes sélectionnés pour leur professionnalisme.":
            "Nous réalisons une étude sérieuse, dimensionnons juste, sélectionnons le matériel et sélectionnons des installateurs externes pour la pose. SolarGlobe ne pose pas directement&nbsp;: nous faisons le tri, cadrons le projet et pilotons la cohérence.",
        "Sélection rigoureuse du matériel utile, puis pose confiée à des installateurs externes sélectionnés pour leur professionnalisme et suivie selon le niveau d’exigence du dossier.":
            "Sélection rigoureuse du matériel utile, puis pose confiée à des installateurs externes sélectionnés pour leur professionnalisme et suivie selon le niveau d’exigence du dossier.",
        "Basés en Île-de-France, nous accompagnons des clients partout en France grâce à un réseau de partenaires installateurs certifiés.":
            "Basés en Île-de-France, nous accompagnons les clients grâce à des partenaires installateurs externes, sélectionnés pour leur sérieux, leur certification et leur qualité d’exécution.",
    },
    "notre-methode/index.html": {
        "pose par partenaires externes sélectionnés.":
            "pose par partenaires externes sélectionnés pour leur professionnalisme.",
        "La pose est confiée à des partenaires installateurs externes sélectionnés, sélectionnés selon la zone":
            "La pose est confiée à des partenaires installateurs externes, sélectionnés selon leur professionnalisme, la zone",
        "Démarches, pose par partenaires externes sélectionnés et suivi":
            "Démarches, pose par partenaires externes sélectionnés pour leur professionnalisme et suivi",
    },
    "faq/index.html": {
        "d’orienter vers des installateurs externes sélectionnés pour leur professionnalisme":
            "d’orienter vers des installateurs externes sélectionnés pour leur professionnalisme. SolarGlobe ne pose pas directement",
        "sécurise le choix de l’installateur.":
            "sécurise le choix de l’installateur externe.",
    },
    "contact/index.html": {
        "Prix, puissance, matériel et installateur : vous avancez avec un cadre clair.":
            "Prix, puissance, matériel et installateur externe sélectionné : vous avancez avec un cadre clair.",
        "ou le choix d’un installateur ?":
            "ou le choix d’un installateur externe ?",
    },
    "rentabilite-solaire/index.html": {
        "le choix de l’installateur externe sélectionné":
            "le choix de l’installateur externe sélectionné pour son professionnalisme",
        "pose par un installateur RGE":
            "pose par un installateur externe RGE",
    },
    "produits/index.html": {
        "Quelles marques de panneaux installez-vous ?":
            "Quelles marques de panneaux recommandez-vous ?",
    },
}


def main() -> None:
    for p in ROOT.rglob("*.html"):
        s = p.read_text(encoding="utf-8", errors="ignore")
        old_s = s
        for old, new in REPLACEMENTS.items():
            s = s.replace(old, new)
        rel = p.relative_to(ROOT).as_posix()
        for old, new in TARGETED.get(rel, {}).items():
            s = s.replace(old, new)
        if s != old_s:
            p.write_text(s, encoding="utf-8", newline="\n")
            print(rel)


if __name__ == "__main__":
    main()
