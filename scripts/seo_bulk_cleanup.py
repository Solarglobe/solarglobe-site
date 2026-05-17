from __future__ import annotations

import html
import re
from pathlib import Path
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.solarglobe.fr"


EXCLUDE_DIRS = {
    "components",
    "node_modules",
    "seo",
    "pages-expertise",
}

NOINDEX_PATHS = {
    "404.html",
    "google8216ab55dcee3d13.html",
    "_header-global.html",
    "aides-financieres.html",
    "autonomie-solaire.html",
    "C.G.V.html",
    "choisir-puissance-solaire.html",
    "contrat-apporteur-solarglobe.html",
    "partenaires.html",
    "rendement-panneaux.html",
    "merci/index.html",
    "page-de-presentation/index.html",
    "proprietaires/index.html",
    "etude-solaire-gratuite/index.html",
}

CANONICAL_OVERRIDES = {
    "aides-financieres.html": "/blog/aides-financieres/",
    "autonomie-solaire.html": "/blog/autonomie-solaire/",
    "C.G.V.html": "/cgv/",
    "choisir-puissance-solaire.html": "/blog/choisir-puissance-solaire/",
    "rendement-panneaux.html": "/blog/rendement-panneaux/",
    "etude-solaire-gratuite/index.html": "/etude-gratuite/",
    "le-solaire/rentabilite-panneaux-solaires/index.html": "/rentabilite-solaire/",
    "pages-expertise/bureau-etude-photovoltaique/index.html": "/bureau-etude-photovoltaique/",
    "pages-expertise/dimensionnement-photovoltaique/index.html": "/dimensionnement-photovoltaique/",
    "pages-expertise/etude-solaire/index.html": "/etude-solaire/",
    "pages-expertise/rentabilite-solaire/index.html": "/rentabilite-solaire/",
    "seo/aides-financements/index.html": "/le-solaire/aides-panneaux-solaires/",
    "seo/autoconsommation-solaire/index.html": "/le-solaire/autoconsommation-solaire/",
    "seo/batteries-solaires/index.html": "/le-solaire/batterie-solaire/",
    "seo/energie-solaire-maison/index.html": "/le-solaire/",
    "seo/etude-solaire-gratuite/index.html": "/etude-gratuite/",
    "seo/installation-solaire/index.html": "/notre-methode/installation/",
    "seo/onduleurs-solaires/index.html": "/produits/onduleurs/",
    "seo/panneaux-photovoltaiques/index.html": "/produits/panneaux-solaires/",
    "seo/panneaux-solaires/index.html": "/produits/panneaux-solaires/",
    "seo/production-solaire/index.html": "/le-solaire/rendement-panneaux-solaires/",
    "seo/rentabilite-panneaux-solaires/index.html": "/rentabilite-solaire/",
    "seo/solution-solaire-sur-mesure/index.html": "/notre-methode/",
}

TITLE_OVERRIDES = {
    "index.html": "Solarglobe | Panneaux solaires premium en Ile-de-France",
    "rentabilite-solaire/index.html": "Rentabilite solaire | Calcul ROI panneaux solaires",
    "dimensionnement-photovoltaique/index.html": "Dimensionnement photovoltaique | Puissance solaire",
    "bureau-etude-photovoltaique/index.html": "Bureau d'etude photovoltaique | Solarglobe",
    "etude-solaire/index.html": "Etude solaire | Faisabilite et rentabilite",
    "etude-gratuite/index.html": "Etude solaire gratuite | Solarglobe",
    "qui-sommes-nous/index.html": "Qui sommes-nous | Solarglobe",
    "produits/panneaux-solaires/index.html": "Panneaux solaires LONGi et Aiko | Solarglobe",
    "produits/onduleurs/index.html": "Onduleurs solaires Huawei | Solarglobe",
    "produits/micro-onduleurs/index.html": "Micro-onduleurs solaires ATMOCE | Solarglobe",
    "produits/batteries-solaires/index.html": "Batteries solaires | Solarglobe",
    "le-solaire/aides-panneaux-solaires/index.html": "Aides panneaux solaires 2026 | Solarglobe",
    "le-solaire/batterie-solaire/index.html": "Batterie solaire | Physique ou virtuelle",
    "le-solaire/rendement-panneaux-solaires/index.html": "Rendement panneaux solaires | Production reelle",
    "blog/aides-financieres/index.html": "Aides photovoltaiques 2026 | Prime, TVA, surplus",
    "blog/batterie-virtuelle-solaire/index.html": "Batterie virtuelle solaire | Analyse et limites",
}

DESC_OVERRIDES = {
    "index.html": "Installation de panneaux solaires premium en Ile-de-France : etude gratuite, prix clair, garanties longues et accompagnement complet Solarglobe.",
    "rentabilite-solaire/index.html": "Calculez la rentabilite de panneaux solaires : economies, autoconsommation, surplus, aides et retour sur investissement avec Solarglobe.",
    "dimensionnement-photovoltaique/index.html": "Determinez la bonne puissance solaire pour votre maison : consommation, toiture, autoconsommation, batterie et rentabilite.",
    "bureau-etude-photovoltaique/index.html": "Bureau d'etude photovoltaique Solarglobe : faisabilite toiture, calpinage, production estimee, rentabilite et choix techniques.",
    "etude-solaire/index.html": "Etude solaire personnalisee : analyse de toiture, production estimee, dimensionnement, aides et rentabilite avant installation.",
    "etude-gratuite/index.html": "Demandez une etude solaire gratuite : faisabilite, dimensionnement, production, rentabilite et conseils pour votre maison.",
    "qui-sommes-nous/index.html": "Decouvrez Solarglobe, specialiste des installations solaires premium en Ile-de-France : methode, engagements, garanties et expertise.",
    "le-solaire/rendement-panneaux-solaires/index.html": "Comprenez le rendement des panneaux solaires : orientation, inclinaison, ombrage, temperature et production reelle en France.",
    "le-solaire/aides-panneaux-solaires/index.html": "Prime a l'autoconsommation, TVA reduite, surplus et aides locales : les points a verifier avant votre projet solaire.",
    "notre-methode/etude-solaire/index.html": "Analyse toiture, consommation, production et rentabilite : la methode Solarglobe pour cadrer une installation solaire fiable.",
    "contact/index.html": "Contactez Solarglobe pour une etude solaire, une question technique, un devis ou un accompagnement photovoltaique en Ile-de-France.",
    "faq/index.html": "Questions frequentes sur les panneaux solaires : cout, aides, rentabilite, installation, batteries et accompagnement Solarglobe.",
    "mentions-legales/index.html": "Mentions legales de Solarglobe : editeur du site, hebergement, propriete intellectuelle et informations administratives.",
    "politique-de-confidentialite/index.html": "Politique de confidentialite Solarglobe : donnees personnelles, finalites de traitement, conservation, droits et contact.",
    "cookies/index.html": "Politique cookies Solarglobe : mesure d'audience, consentement, traceurs utilises et gestion de vos preferences.",
    "cgv/index.html": "Conditions generales de vente Solarglobe : commande, paiement, installation, garanties, retractation et obligations contractuelles.",
}

AI_BLOCKS = {
    "index.html": {
        "title": "Solarglobe en bref",
        "body": "Solarglobe est un specialiste du photovoltaique residentiel premium base a Chelles, en Ile-de-France. L'entreprise accompagne les particuliers depuis l'etude de faisabilite jusqu'au dimensionnement, aux demarches, a l'installation et au suivi de production.",
        "items": [
            "Zone principale : Ile-de-France et departements limitrophes.",
            "Expertise : panneaux solaires, onduleurs, micro-onduleurs, batteries et autoconsommation.",
            "Promesse : une etude chiffree avant recommandation materielle.",
        ],
    },
    "rentabilite-solaire/index.html": {
        "title": "Reponse courte : la rentabilite solaire",
        "body": "Une installation solaire est rentable quand la puissance est ajustee a la consommation reelle et que l'autoconsommation reste elevee. Le calcul doit croiser cout pose, production estimee, aides, surplus revendu et evolution du prix de l'electricite. Solarglobe chiffre ces variables avant de recommander une puissance.",
        "items": [
            "Variable cle : taux d'autoconsommation.",
            "Risque principal : surdimensionner et revendre trop de surplus.",
            "Decision fiable : comparer 3 kWc, 6 kWc et 9 kWc sur 25 ans.",
        ],
    },
    "dimensionnement-photovoltaique/index.html": {
        "title": "Reponse courte : choisir la bonne puissance",
        "body": "Le bon dimensionnement photovoltaique ne depend pas seulement de la surface disponible. Il depend surtout de la consommation annuelle, des usages en journee, de l'orientation, des ombrages et de l'objectif : autoconsommation, surplus ou batterie. Une puissance plus grande n'est pas toujours plus rentable.",
        "items": [
            "3 kWc : profils sobres ou petite toiture.",
            "6 kWc : maison familiale avec usages electriques reguliers.",
            "9 kWc : gros consommateurs, pompe a chaleur, vehicule electrique ou toiture tres favorable.",
        ],
    },
    "bureau-etude-photovoltaique/index.html": {
        "title": "Reponse courte : role du bureau d'etude",
        "body": "Un bureau d'etude photovoltaique transforme une intention solaire en projet techniquement faisable : toiture, ombrages, calpinage, puissance, materiel, raccordement et rentabilite. Cette etape evite les devis approximatifs et les promesses de production trop optimistes.",
        "items": [
            "Avant le devis : valider la faisabilite.",
            "Avant la pose : securiser puissance, materiel et demarches.",
            "Apres l'etude : comparer les scenarios sur des chiffres.",
        ],
    },
    "le-solaire/aides-panneaux-solaires/index.html": {
        "title": "Reponse courte : aides et rentabilite",
        "body": "Les aides reduisent le cout d'un projet solaire, mais elles ne remplacent pas un bon dimensionnement. Prime, TVA, surplus et conditions d'eligibilite doivent etre verifies au moment du devis. La rentabilite vient surtout de l'electricite autoconsommee, pas uniquement des aides.",
        "items": [
            "Verifier les conditions officielles avant signature.",
            "Distinguer aide nationale, fiscalite et aide locale.",
            "Calculer le ROI avec et sans aide pour mesurer la robustesse du projet.",
        ],
    },
    "produits/panneaux-solaires/index.html": {
        "title": "Reponse courte : choisir ses panneaux solaires",
        "body": "Un bon panneau solaire ne se resume pas a sa puissance en watts. Il faut comparer rendement, garantie produit, garantie de performance, comportement en chaleur, compatibilite avec la toiture et qualite de pose. Solarglobe privilegie des modules premium adaptes au projet plutot qu'un choix uniquement au prix.",
        "items": [
            "Comparer rendement, garanties et degradation annuelle.",
            "Adapter le module a la surface et aux contraintes de toiture.",
            "Associer les panneaux au bon onduleur ou micro-onduleur.",
        ],
    },
    "le-solaire/batterie-solaire/index.html": {
        "title": "Reponse courte : batterie solaire ou non",
        "body": "Une batterie solaire est pertinente quand une partie importante de la production n'est pas consommee en journee et que les usages du soir justifient le stockage. Elle augmente l'autoconsommation, mais elle doit etre comparee a la revente du surplus et au pilotage des usages.",
        "items": [
            "Sans batterie : souvent le meilleur ROI pour une maison simple.",
            "Avec batterie : utile si consommation decalee le soir.",
            "Batterie virtuelle : a analyser contrat par contrat.",
        ],
    },
}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def page_url(relative: str) -> str:
    if relative == "index.html":
        return SITE + "/"
    if relative.endswith("/index.html"):
        return SITE + "/" + relative[:-11].rstrip("/") + "/"
    if relative.endswith(".html"):
        return SITE + "/" + relative[:-5]
    return SITE + "/" + relative


def canonical_for(relative: str) -> str:
    override = CANONICAL_OVERRIDES.get(relative)
    if override:
        return SITE + override
    return page_url(relative)


def is_noindex(relative: str) -> bool:
    parts = relative.split("/")
    if relative in NOINDEX_PATHS:
        return True
    if parts[0] in {"seo", "pages-expertise"}:
        return True
    if relative == "le-solaire/rentabilite-panneaux-solaires/index.html":
        return True
    return False


def extract_h1(text: str) -> str:
    match = re.search(r"<h1\b[^>]*>(.*?)</h1>", text, flags=re.I | re.S)
    if not match:
        return ""
    value = re.sub(r"<[^>]+>", "", match.group(1))
    return html.unescape(re.sub(r"\s+", " ", value)).strip()


def title_for(relative: str, text: str) -> str:
    if relative in TITLE_OVERRIDES:
        return TITLE_OVERRIDES[relative]
    if relative.startswith("panneaux-solaires-") and relative.endswith("/index.html"):
        slug = relative.removeprefix("panneaux-solaires-").removesuffix("/index.html")
        city = " ".join(part.capitalize() for part in slug.split("-"))
        fixes = {
            "Ile De France": "Ile-de-France",
            "Seine Et Marne": "Seine-et-Marne",
            "Seine Saint Denis": "Seine-Saint-Denis",
            "Val De Marne": "Val-de-Marne",
            "Val Doise": "Val-d'Oise",
            "Hauts De Seine": "Hauts-de-Seine",
            "Saint Maur Des Fosses": "Saint-Maur-des-Fosses",
            "Boulogne Billancourt": "Boulogne-Billancourt",
            "Noisy Le Grand": "Noisy-le-Grand",
            "Issy Les Moulineaux": "Issy-les-Moulineaux",
            "Ivry Sur Seine": "Ivry-sur-Seine",
            "Vitry Sur Seine": "Vitry-sur-Seine",
        }
        city = fixes.get(city, city)
        return f"Panneaux solaires {city} | Solarglobe"
    h1 = extract_h1(text)
    if h1:
        clean = re.sub(r"\s+", " ", h1).strip()
        clean = clean.replace(" : ", " | ")
        if len(clean) > 58:
            clean = clean[:55].rsplit(" ", 1)[0]
        return f"{clean} | Solarglobe" if "Solarglobe" not in clean and len(clean) < 50 else clean
    return "Solarglobe"


def description_for(relative: str, text: str) -> str:
    if relative in DESC_OVERRIDES:
        return DESC_OVERRIDES[relative]
    if relative.startswith("panneaux-solaires-") and relative.endswith("/index.html"):
        title = title_for(relative, text).replace(" | Solarglobe", "")
        place = title.replace("Panneaux solaires ", "")
        return f"Etude solaire a {place} : faisabilite toiture, dimensionnement, rentabilite, demarches et installation premium avec Solarglobe."
    title = title_for(relative, text).replace(" | Solarglobe", "")
    return f"{title} avec Solarglobe : conseils, etude personnalisee, choix techniques et accompagnement pour votre projet solaire."


def upsert_meta(text: str, name: str, content: str) -> str:
    tag = f'<meta name="{name}" content="{html.escape(content, quote=True)}" />'
    pattern = re.compile(rf'<meta\s+name=["\']{re.escape(name)}["\'][^>]*>', flags=re.I)
    if pattern.search(text):
        return pattern.sub(tag, text, count=1)
    return text.replace("</title>", f"</title>\n  {tag}", 1)


def upsert_canonical(text: str, href: str) -> str:
    tag = f'<link rel="canonical" href="{href}" />'
    pattern = re.compile(r'<link\s+rel=["\']canonical["\'][^>]*>', flags=re.I)
    if pattern.search(text):
        return pattern.sub(tag, text, count=1)
    insert_after = re.search(r'<meta\s+name=["\']robots["\'][^>]*>', text, flags=re.I)
    if insert_after:
        return text[: insert_after.end()] + "\n  " + tag + text[insert_after.end():]
    return text.replace("</title>", f"</title>\n  {tag}", 1)


def set_title(text: str, title: str) -> str:
    tag = f"<title>{html.escape(title, quote=False)}</title>"
    if re.search(r"<title\b[^>]*>.*?</title>", text, flags=re.I | re.S):
        return re.sub(r"<title\b[^>]*>.*?</title>", tag, text, count=1, flags=re.I | re.S)
    return text.replace("</head>", f"  {tag}\n</head>", 1)


def sync_social_meta(text: str, title: str, description: str, url: str) -> str:
    replacements = {
        "og:title": title,
        "og:description": description,
        "og:url": url,
        "twitter:title": title,
        "twitter:description": description,
    }
    for prop, value in replacements.items():
        escaped = html.escape(value, quote=True)
        if prop.startswith("og:"):
            pattern = re.compile(rf'<meta\s+property=["\']{re.escape(prop)}["\'][^>]*>', flags=re.I)
            tag = f'<meta property="{prop}" content="{escaped}" />'
        else:
            pattern = re.compile(rf'<meta\s+name=["\']{re.escape(prop)}["\'][^>]*>', flags=re.I)
            tag = f'<meta name="{prop}" content="{escaped}" />'
        if pattern.search(text):
            text = pattern.sub(tag, text, count=1)
    return text


def insert_ai_block(relative: str, text: str) -> str:
    if relative not in AI_BLOCKS or "sg-ai-answer" in text:
        return text
    data = AI_BLOCKS[relative]
    items = "\n".join(f"      <li>{html.escape(item)}</li>" for item in data["items"])
    block = f"""
<section class="sg-section sg-section-dark sg-ai-answer" aria-labelledby="reponse-courte">
  <div class="sg-container">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="reponse-courte">{html.escape(data["title"])}</span>
      <p>{html.escape(data["body"])}</p>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
{items}
      </ul>
    </div>
  </div>
</section>

"""
    hero_end = re.search(r"</section>\s*(?:<div class=\"sg-divider\" aria-hidden=\"true\"></div>\s*)?", text, flags=re.I)
    if not hero_end:
        return text
    return text[: hero_end.end()] + "\n" + block + text[hero_end.end():]


def should_optimize(relative: str) -> bool:
    if any(part in EXCLUDE_DIRS for part in relative.split("/")[:-1]):
        return False
    if is_noindex(relative):
        return False
    if relative.endswith(".html"):
        return True
    return False


def update_html_files() -> None:
    for path in ROOT.rglob("*.html"):
        relative = rel(path)
        if "node_modules/" in relative:
            continue
        text = path.read_text(encoding="utf-8")
        original = text
        noindex = is_noindex(relative)

        if noindex:
            text = upsert_meta(text, "robots", "noindex, follow")
            text = upsert_canonical(text, canonical_for(relative))
        elif should_optimize(relative):
            title = title_for(relative, text)
            description = description_for(relative, text)
            url = canonical_for(relative)
            text = set_title(text, title)
            text = upsert_meta(text, "description", description)
            text = upsert_meta(text, "robots", "index, follow")
            text = upsert_canonical(text, url)
            text = sync_social_meta(text, title, description, url)
            text = insert_ai_block(relative, text)

        if text != original:
            path.write_text(text, encoding="utf-8", newline="")


def sitemap_priority(relative: str) -> str:
    if relative == "index.html":
        return "1.0"
    if relative in {"etude-gratuite/index.html", "contact/index.html"}:
        return "0.9"
    if relative.startswith(("produits/", "le-solaire/", "notre-methode/")):
        return "0.8"
    if relative in {
        "bureau-etude-photovoltaique/index.html",
        "dimensionnement-photovoltaique/index.html",
        "etude-solaire/index.html",
        "rentabilite-solaire/index.html",
    }:
        return "0.8"
    if relative.startswith("panneaux-solaires-"):
        return "0.7"
    if relative.startswith("blog/"):
        return "0.6"
    return "0.5"


def sitemap_changefreq(relative: str) -> str:
    if relative.startswith(("mentions-legales", "politique-de-confidentialite", "cookies", "cgv", "faq")):
        return "monthly"
    return "weekly"


def write_sitemap() -> None:
    urls = []
    for path in ROOT.rglob("*.html"):
        relative = rel(path)
        if "node_modules/" in relative:
            continue
        if any(part in EXCLUDE_DIRS for part in relative.split("/")[:-1]):
            continue
        if is_noindex(relative):
            continue
        if relative.startswith("components/") or relative.startswith("assets/"):
            continue
        urls.append(relative)

    urls = sorted(set(urls), key=lambda item: (item != "index.html", item))
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for relative in urls:
        loc = page_url(relative)
        lines.extend(
            [
                "  <url>",
                f"    <loc>{escape(loc)}</loc>",
                "    <lastmod>2026-05-17</lastmod>",
                f"    <changefreq>{sitemap_changefreq(relative)}</changefreq>",
                f"    <priority>{sitemap_priority(relative)}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="")


if __name__ == "__main__":
    update_html_files()
    write_sitemap()
