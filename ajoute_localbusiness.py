import os

bloc_jsonld = '''
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "Solarglobe",
  "image": "https://solarglobe.fr/assets/images/logo-solarglobe.png",
  "url": "https://solarglobe.fr/",
  "telephone": "01 72 99 47 53",
  "email": "contact@solarglobe.fr",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "19 avenue Pierre Curie",
    "addressLocality": "Chelles",
    "postalCode": "77500",
    "addressCountry": "FR"
  },
  "description": "Solarglobe est le spécialiste des installations photovoltaïques haut de gamme en Île-de-France et départements limitrophes.",
  "openingHours": "Mo-Fr 08:30-16:30"
}
</script>
'''

for dossier_racine, sous_dossiers, fichiers in os.walk("."):
    for fichier in fichiers:
        if fichier.endswith('.html'):
            chemin_complet = os.path.join(dossier_racine, fichier)
            with open(chemin_complet, 'r', encoding='utf-8') as f:
                contenu = f.read()
            # Ajoute le bloc juste avant </body> (si pas déjà présent)
            if bloc_jsonld.strip() in contenu:
                continue
            if '</body>' in contenu:
                contenu_mod = contenu.replace('</body>', f'{bloc_jsonld}\n</body>', 1)
                with open(chemin_complet, 'w', encoding='utf-8') as f:
                    f.write(contenu_mod)
                print(f"✅ LocalBusiness ajouté à : {chemin_complet}")

print("\nTous les fichiers traités.")
