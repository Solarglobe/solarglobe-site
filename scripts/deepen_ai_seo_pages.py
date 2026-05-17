from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

EXTRA = {
    "le-solaire/3kwc-6kwc-9kwc/index.html": """
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Exemple de raisonnement sur une maison familiale</h2>
      <p>Une maison qui consomme 4 500 a 6 500 kWh par an n'a pas automatiquement besoin de 9 kWc. Si la consommation est surtout le matin et le soir, une grande partie de la production de midi peut partir en surplus. Dans ce cas, 6 kWc bien orientes et correctement pilotes peuvent donner un meilleur rapport cout / economie qu'une installation plus puissante.</p>
      <p class="mt-4">A l'inverse, une maison equipee d'une pompe a chaleur, d'un ballon d'eau chaude programmable, d'une piscine ou d'une recharge de vehicule electrique peut valoriser une puissance plus elevee. Le sujet n'est donc pas seulement la consommation annuelle : il faut regarder le moment ou l'electricite est consommee.</p>
      <h3 class="text-lg font-semibold text-gold mt-6">Les erreurs frequentes</h3>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Choisir 9 kWc parce que la toiture le permet, sans verifier le surplus.</li>
        <li>Comparer deux devis sans comparer la production estimee et l'autoconsommation.</li>
        <li>Oublier les futurs usages : pompe a chaleur, climatisation, borne de recharge.</li>
        <li>Ne pas verifier la compatibilite avec une batterie ou une extension future.</li>
      </ul>
    </div>
  </section>
""",
    "le-solaire/cout-installation-solaire-ile-de-france/index.html": """
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Pourquoi deux devis solaires peuvent etre incomparables</h2>
      <p>Deux installations de meme puissance peuvent avoir des prix tres differents. La difference peut venir des panneaux, de l'onduleur, du type de fixation, de la difficulte d'acces, des protections electriques, de la garantie, du suivi de production ou du niveau d'accompagnement administratif. Un prix au kWc ne suffit donc pas pour choisir.</p>
      <p class="mt-4">En Ile-de-France, les contraintes de toiture et d'urbanisme changent souvent le cout reel. Un pavillon simple avec toiture accessible n'a pas la meme logique qu'une maison mitoyenne, une copropriete, une zone patrimoniale ou une toiture avec nombreux masques. Le devis doit indiquer ce qui est inclus, ce qui reste a la charge du client et les hypotheses de production.</p>
      <h3 class="text-lg font-semibold text-gold mt-6">Ce qu'un prix serieux doit detailler</h3>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Puissance installee, nombre de panneaux et type de modules.</li>
        <li>Onduleur, micro-onduleurs ou architecture hybride si batterie envisagee.</li>
        <li>Production annuelle estimee et hypothese d'autoconsommation.</li>
        <li>Demarches administratives, raccordement, Consuel et suivi.</li>
        <li>Garanties produit, performance et conditions de maintenance.</li>
      </ul>
    </div>
  </section>
""",
    "le-solaire/batterie-ou-revente-surplus/index.html": """
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Le vrai arbitrage : stocker, vendre ou piloter</h2>
      <p>Une batterie physique peut augmenter l'autoconsommation, mais elle ajoute un investissement, une duree de vie propre et des limites de cycles. Elle doit donc etre comparee au gain net, pas seulement au confort d'independance. Dans beaucoup de maisons, le premier levier consiste a deplacer les consommations solaires : chauffe-eau, recharge, climatisation ou appareils programmables.</p>
      <p class="mt-4">La revente du surplus reste simple et robuste, mais la valeur du kWh revendu est plus faible que celle du kWh autoconsomme. Une installation bien dimensionnee cherche donc a limiter le surplus inutile, puis a valoriser le surplus restant. La batterie devient interessante lorsque le surplus est structurel et que les usages du soir sont importants.</p>
      <h3 class="text-lg font-semibold text-gold mt-6">Questions a poser avant d'acheter une batterie</h3>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Quelle part de la production part aujourd'hui en surplus ?</li>
        <li>Quels usages du soir peuvent reellement consommer l'energie stockee ?</li>
        <li>La batterie est-elle compatible avec l'onduleur et une extension future ?</li>
        <li>Quel est le ROI compare a un simple pilotage des usages ?</li>
      </ul>
    </div>
  </section>
""",
    "produits/micro-onduleur-ou-onduleur-central/index.html": """
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Choisir selon la toiture, pas selon une mode</h2>
      <p>Les micro-onduleurs sont souvent pertinents lorsque les panneaux ne recoivent pas tous le meme soleil : ombrage partiel, orientation est-ouest, cheminees, velux ou petites surfaces separees. Chaque module travaille alors de facon plus independante, ce qui limite l'impact d'un panneau moins productif sur l'ensemble du champ.</p>
      <p class="mt-4">Un onduleur central peut rester excellent sur une toiture simple, homogene et bien exposee. Il peut aussi etre interessant lorsqu'une batterie hybride est envisagee. La bonne decision depend donc du calpinage, des ombrages, de la maintenance attendue et du budget global.</p>
      <h3 class="text-lg font-semibold text-gold mt-6">Critere de decision rapide</h3>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Toiture simple plein sud : onduleur central possible.</li>
        <li>Toiture avec plusieurs orientations : micro-onduleurs a etudier.</li>
        <li>Ombres partielles regulieres : optimisation module par module utile.</li>
        <li>Projet batterie : verifier l'architecture hybride et les compatibilites.</li>
      </ul>
    </div>
  </section>
""",
    "le-solaire/panneaux-solaires-zone-abf-copropriete/index.html": """
  <section class="sg-section sg-section-dark">
    <div class="sg-container max-w-4xl">
      <h2 class="sg-section-title text-gold">Preparer un dossier acceptable</h2>
      <p>En zone patrimoniale ou en copropriete, la faisabilite ne depend pas seulement de la production. Le projet doit etre lisible pour les decideurs : integration visuelle, impact sur la toiture, responsabilites, maintenance, cout, gain attendu et calendrier. Un dossier clair evite que le projet soit bloque par manque d'informations.</p>
      <p class="mt-4">Pour une copropriete, le premier scenario a etudier concerne souvent les parties communes : ascenseur, eclairage, VMC, locaux techniques ou recharge commune. Pour une maison en zone ABF, l'enjeu porte plutot sur l'integration, la visibilite depuis l'espace public et le choix du calpinage.</p>
      <h3 class="text-lg font-semibold text-gold mt-6">Pieces utiles au cadrage</h3>
      <ul class="sg-list-premium sg-list-premium-dark mt-4">
        <li>Photos de toiture, plan ou vue satellite annotee.</li>
        <li>Factures ou profil de consommation.</li>
        <li>Contraintes connues : syndic, ABF, toiture terrasse, acces, etancheite.</li>
        <li>Objectif du projet : economie, autoconsommation collective, valeur patrimoniale.</li>
      </ul>
    </div>
  </section>
""",
}


def main() -> None:
    for rel, extra in EXTRA.items():
        path = ROOT / rel
        text = path.read_text(encoding="utf-8")
        if "Exemple de raisonnement" in text or "Pourquoi deux devis solaires" in text or "Le vrai arbitrage" in text or "Choisir selon la toiture" in text or "Preparer un dossier acceptable" in text:
            continue
        marker = '<section class="sg-section sg-section-dark">\n    <div class="sg-container max-w-4xl">\n      <h2 class="sg-section-title text-gold">Questions frequentes</h2>'
        idx = text.find(marker)
        if idx == -1:
            continue
        text = text[:idx] + extra + "\n" + text[idx:]
        path.write_text(text, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
