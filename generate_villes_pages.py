import os

# Dossier de destination
output_dir = "seo/villes"
os.makedirs(output_dir, exist_ok=True)

# Liste officielle des villes
villes = [
    ("lagny-sur-marne", "Lagny-sur-Marne"), ("meaux", "Meaux"), ("fontainebleau", "Fontainebleau"), ("provins", "Provins"),
    ("evry-courcouronnes", "Évry-Courcouronnes"), ("etampes", "Étampes"), ("dourdan", "Dourdan"), ("massy", "Massy"),
    ("argenteuil", "Argenteuil"), ("l-isle-adam", "L’Isle-Adam"), ("magny-en-vexin", "Magny-en-Vexin"), ("montmorency", "Montmorency"),
    ("compiegne", "Compiègne"), ("beauvais", "Beauvais"), ("senlis", "Senlis"), ("nogent-sur-oise", "Nogent-sur-Oise"),
    ("soissons", "Soissons"), ("saint-quentin", "Saint-Quentin"), ("chateau-thierry", "Château-Thierry"), ("laon", "Laon"),
    ("reims", "Reims"), ("epernay", "Épernay"), ("chalons-en-champagne", "Châlons-en-Champagne"), ("vitry-le-francois", "Vitry-le-François"),
    ("troyes", "Troyes"), ("romilly-sur-seine", "Romilly-sur-Seine"), ("sainte-savine", "Sainte-Savine"), ("bar-sur-seine", "Bar-sur-Seine"),
    ("sens", "Sens"), ("auxerre", "Auxerre"), ("joigny", "Joigny"), ("migennes", "Migennes"),
    ("orleans", "Orléans"), ("montargis", "Montargis"), ("gien", "Gien"), ("olivet", "Olivet")
]

# Pages du silo + mots-clés
pages_silo = [
    ("panneaux-solaires.html", "panneaux solaires"),
    ("autoconsommation-solaire.html", "autoconsommation solaire"),
    ("batteries-solaires.html", "batteries solaires"),
    ("onduleurs-solaires.html", "onduleurs solaires"),
    ("installation-solaire.html", "installation solaire"),
    ("aides-panneaux-solaires.html", "aides panneaux solaires"),
    ("rentabilite-panneaux-solaires.html", "rentabilité panneaux solaires"),
    ("energie-solaire-maison.html", "énergie solaire maison"),
    ("production-solaire.html", "production solaire"),
    ("etude-solaire-gratuite.html", "étude solaire gratuite"),
    ("solution-solaire-sur-mesure.html", "solution solaire sur-mesure"),
    ("panneaux-photovoltaiques.html", "panneaux photovoltaïques")
]

# Génération des pages
for slug, nom_ville in villes:
    if slug == "lagny-sur-marne":
        continue  # On saute le modèle déjà existant

    index = villes.index((slug, nom_ville))
    liens = pages_silo[index % len(pages_silo):] + pages_silo[:index % len(pages_silo)]
    liens_choisis = liens[:6]

    liens_html = "\n        ".join([
        f'<a href="../{lien[0]}" class="underline hover:text-gold transition">{lien[1]}</a>'
        for lien in liens_choisis
    ])

    mots_cles_text = ", ".join([mc[1] for mc in pages_silo])

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Installation photovoltaïque à {nom_ville} | Solarglobe</title>
  <meta name="description" content="Solarglobe propose l'installation de panneaux solaires à {nom_ville}. Étude gratuite et solutions haut de gamme pour votre maison." />
  <link rel="icon" href="../../assets/images/favicon.ico" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            gold: '#C39847',
            noir: '#131314'
          }}
        }}
      }}
    }}
  </script>
</head>
<body class="bg-noir text-white font-sans leading-relaxed">
  <section class="px-6 py-24 text-center">
    <h1 class="text-4xl md:text-5xl font-bold mb-6 text-gold">Installation photovoltaïque à {nom_ville}</h1>
    <p class="text-xl max-w-3xl mx-auto">Solarglobe vous accompagne à {nom_ville} pour votre projet solaire : conseils, équipements premium, installateurs certifiés RGE, et étude personnalisée offerte.</p>
  </section>

  <section class="bg-[#1C1C1E] px-6 py-20">
    <div class="max-w-6xl mx-auto space-y-6 text-lg">
      <p>À {nom_ville}, de plus en plus de foyers passent à l’énergie solaire. En combinant {mots_cles_text}, vous maximisez votre autonomie énergétique et vos économies.</p>
      <p>Nos installateurs locaux sont certifiés <strong>RGE QualiPV</strong> pour garantir une pose conforme, durable et éligible aux aides de l’État.</p>
    </div>
  </section>

  <section class="px-6 py-20">
    <div class="max-w-6xl mx-auto text-center">
      <h2 class="text-2xl font-semibold text-gold mb-8">Découvrez nos solutions pour {nom_ville}</h2>
      <div class="flex flex-wrap justify-center gap-4 text-lg">
        {liens_html}
      </div>
    </div>
  </section>

  <section class="bg-gold text-black px-6 py-20">
    <div class="max-w-4xl mx-auto text-center space-y-6">
      <h2 class="text-3xl font-bold">Demandez votre étude solaire à {nom_ville}</h2>
      <p class="text-lg">Recevez gratuitement une analyse personnalisée de votre toiture et découvrez combien vous pouvez économiser grâce au solaire à {nom_ville}.</p>
      <a href="../etude-solaire-gratuite.html" class="inline-block bg-black text-white px-6 py-3 rounded-full hover:bg-neutral-800 transition">Je demande mon étude gratuite</a>
    </div>
  </section>
</body>
</html>"""

    with open(f"{output_dir}/{slug}.html", "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ {slug}.html généré.")

print("✅ Toutes les pages villes ont été générées avec succès.")
