import os

# Liste officielle des pages SEO
pages = [
    {
        "slug": "panneaux-solaires",
        "h1": "Panneaux solaires – Produisez votre énergie",
        "mot_cle": "panneaux solaires",
        "intro": "Découvrez comment les panneaux solaires peuvent transformer votre toiture en source d’énergie propre. Produisez votre électricité et réduisez vos factures."
    },
    {
        "slug": "autoconsommation-solaire",
        "h1": "Autoconsommation solaire – Utilisez votre propre énergie",
        "mot_cle": "autoconsommation solaire",
        "intro": "Avec l’autoconsommation solaire, consommez directement l’électricité que vous produisez. Gagnez en autonomie énergétique tout en économisant."
    },
    {
        "slug": "batteries-solaires",
        "h1": "Batteries solaires – Stockez votre énergie",
        "mot_cle": "batteries solaires",
        "intro": "Les batteries solaires vous permettent de conserver l’énergie produite pour l’utiliser à tout moment. Ne perdez plus un seul kilowatt."
    },
    {
        "slug": "onduleurs-solaires",
        "h1": "Onduleurs solaires – Le cœur de votre installation",
        "mot_cle": "onduleurs solaires",
        "intro": "Les onduleurs solaires transforment le courant continu en courant alternatif. Un équipement central pour une installation performante."
    },
    {
        "slug": "installation-solaire",
        "h1": "Installation solaire – Votre projet clé en main",
        "mot_cle": "installation solaire",
        "intro": "Confiez votre installation solaire à des experts. Étude gratuite, matériel premium et pose par des installateurs certifiés RGE QualiPV."
    },
    {
        "slug": "aides-panneaux-solaires",
        "h1": "Aides panneaux solaires – Profitez des dispositifs disponibles",
        "mot_cle": "aides panneaux solaires",
        "intro": "De nombreuses aides existent pour financer vos panneaux solaires. Prime à l’autoconsommation, TVA réduite et plus encore."
    },
    {
        "slug": "rentabilite-panneaux-solaires",
        "h1": "Rentabilité panneaux solaires – Un investissement durable",
        "mot_cle": "rentabilité panneaux solaires",
        "intro": "La rentabilité des panneaux solaires est plus rapide que jamais. Réduisez vos factures et réalisez un retour sur investissement durable."
    },
    {
        "slug": "energie-solaire-maison",
        "h1": "Énergie solaire maison – Gagnez en autonomie",
        "mot_cle": "énergie solaire maison",
        "intro": "Alimentez votre maison grâce à l’énergie solaire. Une solution écologique, économique et évolutive pour votre habitation."
    },
    {
        "slug": "production-solaire",
        "h1": "Production solaire – Maximisez votre rendement énergétique",
        "mot_cle": "production solaire",
        "intro": "Maximisez votre production solaire grâce à un bon dimensionnement, une orientation optimale et des équipements performants."
    },
    {
        "slug": "etude-solaire-gratuite",
        "h1": "Étude solaire gratuite – Faites évaluer votre potentiel",
        "mot_cle": "étude solaire gratuite",
        "intro": "Demandez votre étude solaire gratuite et découvrez combien vous pouvez économiser grâce à une installation adaptée à votre toiture."
    },
    {
        "slug": "solution-solaire-sur-mesure",
        "h1": "Solution solaire sur-mesure – Un projet adapté à vos besoins",
        "mot_cle": "solution solaire sur-mesure",
        "intro": "Chaque maison est différente. Solarglobe conçoit une solution solaire sur-mesure, en fonction de votre consommation et de vos objectifs."
    },
    {
        "slug": "panneaux-photovoltaiques",
        "h1": "Panneaux photovoltaïques – Technologie et performance",
        "mot_cle": "panneaux photovoltaïques",
        "intro": "Les panneaux photovoltaïques convertissent la lumière du soleil en électricité. Découvrez des modèles performants et durables."
    }
]

# Création du dossier /seo
seo_dir = os.path.join(os.path.dirname(__file__), "seo")
os.makedirs(seo_dir, exist_ok=True)

# Génération de chaque page
for page in pages:
    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['h1']} | Solarglobe</title>
  <meta name="description" content="{page['intro']}" />
  <link rel="icon" type="image/png" href="/assets/images/favicon.png" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{ gold: '#C39847' }}
        }}
      }}
    }}
  </script>
</head>
<body class="bg-black text-white font-sans leading-relaxed">
  <header class="p-6 bg-black text-gold text-center text-3xl font-bold">
    {page['h1']}
  </header>

  <main class="max-w-4xl mx-auto p-6">
    <h1 class="text-2xl font-bold text-gold mb-4">{page['h1']}</h1>
    <p class="mb-4">{page['intro']}</p>
    <p class="mb-4">Mot-clé ciblé : <strong>{page['mot_cle']}</strong></p>
    <a href="/etude-solaire-gratuite.html" class="inline-block bg-gold text-black font-semibold px-6 py-3 rounded-xl hover:scale-105 transition mt-4">
      Demander mon étude gratuite
    </a>
  </main>

  <footer class="text-center text-sm text-gray-500 mt-10 mb-4">
    © 2025 Solarglobe. Tous droits réservés.
  </footer>
</body>
</html>"""
    with open(os.path.join(seo_dir, f"{page['slug']}.html"), "w", encoding="utf-8") as f:
        f.write(html)

print("✅ Tous les fichiers SEO ont été générés avec les bons mots-clés.")
