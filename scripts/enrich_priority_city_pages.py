from __future__ import annotations

import html
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

CITY_DATA = {
    "panneaux-solaires-paris/index.html": ("Paris", "coproprietes, toitures plates, ombrages urbains et zones patrimoniales", "900 a 1 050 kWh/kWc/an selon masques"),
    "panneaux-solaires-chelles/index.html": ("Chelles", "maisons individuelles, pavillons et proximite directe du bureau Solarglobe", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-meaux/index.html": ("Meaux", "pavillons de Seine-et-Marne, grands pans de toiture et autoconsommation familiale", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-fontainebleau/index.html": ("Fontainebleau", "contraintes patrimoniales possibles, maisons anciennes et zones arborees", "900 a 1 050 kWh/kWc/an selon ombrage"),
    "panneaux-solaires-melun/index.html": ("Melun", "toitures pavillonnaires, periurbain et arbitrage entre 3, 6 et 9 kWc", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-versailles/index.html": ("Versailles", "secteurs patrimoniaux, integration visuelle et dossiers administratifs sensibles", "900 a 1 050 kWh/kWc/an selon exposition"),
    "panneaux-solaires-nanterre/index.html": ("Nanterre", "maisons urbaines, extensions, toitures complexes et autoconsommation en journee", "900 a 1 080 kWh/kWc/an"),
    "panneaux-solaires-creteil/index.html": ("Creteil", "maisons du Val-de-Marne, toits varies et usages electriques familiaux", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-massy/index.html": ("Massy", "pavillons, maisons recentes, pompe a chaleur et recharge de vehicule electrique", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-evry/index.html": ("Evry-Courcouronnes", "maisons familiales, grands pans de toiture et optimisation du surplus", "950 a 1 100 kWh/kWc/an"),
    "panneaux-solaires-argenteuil/index.html": ("Argenteuil", "forte densite urbaine, mitoyennete, ombrages et toiture a verifier", "900 a 1 080 kWh/kWc/an"),
}


def block(city: str, context: str, production: str) -> str:
    return f"""
<section class="sg-section sg-section-dark sg-ai-answer sg-local-proof" aria-labelledby="reponse-locale">
  <div class="sg-container max-w-4xl">
    <div class="sg-encadre-premium">
      <span class="sg-encadre-titre" id="reponse-locale">Reponse locale : panneaux solaires a {html.escape(city)}</span>
      <p>A {html.escape(city)}, l'etude solaire doit d'abord verifier {html.escape(context)}. La rentabilite depend moins d'une puissance standard que du bon calage entre toiture, consommation en journee, materiel et demarches.</p>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li><strong>Production prudente :</strong> {html.escape(production)}.</li>
        <li><strong>Point cle :</strong> comparer 3 kWc, 6 kWc et 9 kWc avant de signer.</li>
        <li><strong>Preuve attendue :</strong> un calpinage clair, une estimation de production et un calcul ROI lisible.</li>
      </ul>
      <p class="mt-4">Pour cadrer le projet, consultez aussi <a href="/le-solaire/3kwc-6kwc-9kwc/" class="text-gold hover:underline">le comparatif 3/6/9 kWc</a>, <a href="/rentabilite-solaire/" class="text-gold hover:underline">le calcul de rentabilite</a> et <a href="/le-solaire/cout-installation-solaire-ile-de-france/" class="text-gold hover:underline">les prix en Ile-de-France</a>.</p>
    </div>
  </div>
</section>
"""


def main() -> None:
    for rel, data in CITY_DATA.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if "sg-local-proof" in text:
            continue
        marker = "</section>"
        index = text.find(marker)
        if index == -1:
            continue
        insert_at = index + len(marker)
        text = text[:insert_at] + "\n" + block(*data) + text[insert_at:]
        path.write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
