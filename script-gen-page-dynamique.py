import os

# Données personnalisées pour batteries-solaires
page = {
    "slug": "batteries-solaires",
    "h1": "Batteries solaires – Stockez votre énergie",
    "intro": "Les batteries solaires permettent de stocker l’électricité produite en journée pour l’utiliser le soir ou en cas de coupure. Elles offrent plus d’autonomie et une gestion plus intelligente de votre consommation énergétique.",
    "avantages": [
        "Autonomie énergétique accrue",
        "Optimisation de l’autoconsommation",
        "Sécurité en cas de coupure du réseau",
        "Technologie lithium longue durée",
        "Compatible avec les onduleurs hybrides",
        "Suivi de charge en temps réel"
    ],
    "pourquoi_solarglobe": "Solarglobe propose des batteries lithium haut de gamme de la marque ATMOCE, reconnues pour leur fiabilité, leur durabilité et leur sécurité. Nous concevons chaque projet pour maximiser l’indépendance énergétique de nos clients."
}

# Structure HTML
html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page['h1']}</title>
  <meta name="description" content="Solarglobe installe des batteries solaires haut de gamme. Stockage, autonomie, fiabilité. Étude gratuite, installateurs certifiés RGE.">
  <link rel="icon" href="/assets/images/favicon.ico" />
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {{
      theme: {{
        extend: {{
          colors: {{
            gold: '#C39847',
          }},
        }}
      }}
    }}
  </script>
</head>
<body class="bg-black text-white font-sans leading-relaxed">
  <header class="p-6 bg-black text-gold text-center text-3xl font-bold">
    {page['h1']}
  </header>

  <section class="max-w-4xl mx-auto p-6">
    <h1 class="text-2xl font-bold text-gold mb-4">{page['h1']}</h1>
    <p class="mb-4">{page['intro']}</p>
    <p class="mb-4">{page['pourquoi_solarglobe']}</p>
    <a href="/etude-solaire-gratuite.html" class="inline-block bg-gold text-black font-semibold px-6 py-3 rounded-xl hover:scale-105 transition mt-4">Demander mon étude gratuite</a>
  </section>

  <section class="bg-gray-900 p-6 mt-8">
    <div class="max-w-4xl mx-auto">
      <h2 class="text-xl text-gold font-semibold mb-4">Les avantages des batteries solaires Solarglobe</h2>
      <ul class="list-disc list-inside space-y-2">
        {''.join([f"<li>{av}</li>" for av in page['avantages']])}
      </ul>
    </div>
  </section>

  <footer class="text-center text-sm text-gray-500 mt-10 mb-4">
    © 2025 Solarglobe. Tous droits réservés.
  </footer>
</body>
</html>
"""

# Écriture du fichier
dossier_seo = os.path.join(os.path.dirname(__file__), "seo")
os.makedirs(dossier_seo, exist_ok=True)
with open(os.path.join(dossier_seo, f"{page['slug']}.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ Page générée : {page['slug']}.html dans /seo")
