import os

# Chemins
base_dir = os.path.dirname(__file__)
dossier_seo = os.path.join(base_dir, "seo")
modele = os.path.join(dossier_seo, "panneaux-photovoltaiques.html")

# Pages à générer
pages = [
    ("onduleurs-solaires", "Onduleurs solaires"),
    ("batteries-solaires", "Batteries solaires"),
    ("autoconsommation", "Autoconsommation solaire"),
    ("revente-electricite", "Revente de l’électricité solaire"),
    ("aides-photovoltaiques", "Aides et subventions photovoltaïques"),
    ("rentabilite-solaire", "Rentabilité d’une installation solaire"),
    ("entretien-panneaux", "Entretien des panneaux solaires"),
    ("installation-toiture", "Installation sur toiture"),
    ("installation-carport", "Installation sur carport ou au sol"),
    ("fonctionnement-installation", "Fonctionnement d’une installation solaire"),
    ("installation-rge", "Pourquoi choisir un installateur RGE")
]

# Lire le modèle
with open(modele, "r", encoding="utf-8") as f:
    template = f.read()

# Génération dans /seo
for slug, titre in pages:
    contenu = template
    contenu = contenu.replace("panneaux-photovoltaiques", slug)
    contenu = contenu.replace("Panneaux photovoltaïques", titre)
    contenu = contenu.replace("panneaux photovoltaïques", titre.lower())

    nom_fichier = f"{slug}.html"
    chemin_final = os.path.join(dossier_seo, nom_fichier)

    with open(chemin_final, "w", encoding="utf-8") as f:
        f.write(contenu)

    print(f"✅ Fichier généré dans /seo : {nom_fichier}")
