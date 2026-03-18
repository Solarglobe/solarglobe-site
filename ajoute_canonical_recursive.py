import os

DOMAINE = "https://www.solarglobe.fr"

def url_absolue(chemin_fichier):
    chemin = chemin_fichier.replace("\\", "/")  # Compatible Windows
    if chemin.endswith("/index.html"):
        return f"{DOMAINE}/"
    else:
        chemin_url = chemin.replace("./", "").replace("pages/", "")
        return f"{DOMAINE}/{chemin_url}"

for dossier_racine, sous_dossiers, fichiers in os.walk("."):
    for fichier in fichiers:
        if fichier.endswith('.html'):
            chemin_complet = os.path.join(dossier_racine, fichier)
            with open(chemin_complet, 'r', encoding='utf-8') as f:
                contenu = f.read()
            url_canonique = url_absolue(os.path.relpath(chemin_complet, "."))
            balise = f'<link rel="canonical" href="{url_canonique}" />\n'
            if balise in contenu:
                continue
            contenu_mod = contenu.replace('<head>', f'<head>\n  {balise}', 1)
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(contenu_mod)
            print(f"✅ Canonical ajouté à : {chemin_complet}")

print("\nTous les fichiers traités.")
