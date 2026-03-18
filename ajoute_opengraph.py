import os
import re

DOMAINE = "https://solarglobe.fr"
IMAGE_URL = "https://solarglobe.fr/assets/images/ton-visuel.jpg"  # Mets le chemin de ton image/logo ici

TITLE_DEFAULT = "Solarglobe – Panneaux photovoltaïques premium en Île-de-France"
DESC_DEFAULT = "Solarglobe, le spécialiste de l’installation solaire premium, études gratuites, installateurs certifiés RGE."

def get_title_and_desc(chemin_fichier):
    nom = os.path.basename(chemin_fichier)
    # Accueil
    if nom == "index.html":
        return TITLE_DEFAULT, DESC_DEFAULT, f"{DOMAINE}/"
    # Ville
    elif "/villes/" in chemin_fichier.replace("\\", "/"):
        ville = nom.replace(".html", "").replace("-", " ").title()
        title = f"Installation solaire à {ville} | Solarglobe"
        desc = f"Installation de panneaux solaires à {ville} : étude gratuite, équipements haut de gamme, installateurs RGE."
        url = f"{DOMAINE}/seo/villes/{nom}"
        return title, desc, url
    # Page SEO
    elif "/seo/" in chemin_fichier.replace("\\", "/"):
        titre_simple = nom.replace(".html", "").replace("-", " ").capitalize()
        title = f"{titre_simple} – Solarglobe"
        desc = f"Tout savoir sur {titre_simple} avec Solarglobe, le spécialiste du solaire premium."
        url = f"{DOMAINE}/seo/{nom}"
        return title, desc, url
    else:
        titre_simple = nom.replace(".html", "").replace("-", " ").capitalize()
        title = f"{titre_simple} – Solarglobe"
        desc = DESC_DEFAULT
        url = f"{DOMAINE}/{nom}"
        return title, desc, url

def inject_open_graph(contenu, title, desc, url, image):
    block = f"""<!-- Balises OpenGraph & Twitter -->
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:image" content="{image}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{image}" />\n"""
    # Injecte après <title>
    return re.sub(r'(<title>.*?</title>)', r'\1\n' + block, contenu, flags=re.DOTALL)

for dossier_racine, sous_dossiers, fichiers in os.walk("."):
    for fichier in fichiers:
        if fichier.endswith('.html'):
            chemin_complet = os.path.join(dossier_racine, fichier)
            with open(chemin_complet, 'r', encoding='utf-8') as f:
                contenu = f.read()
            title, desc, url = get_title_and_desc(chemin_complet)
            if f'<meta property="og:title" content="{title}"' in contenu:
                continue  # déjà présent
            contenu_mod = inject_open_graph(contenu, title, desc, url, IMAGE_URL)
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(contenu_mod)
            print(f"✅ OpenGraph ajouté à : {chemin_complet}")

print("\nTous les fichiers traités.")
