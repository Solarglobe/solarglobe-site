# -*- coding: utf-8 -*-
"""Ajoute fil d'Ariane + JSON-LD BreadcrumbList aux pages /seo/*/."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Libellé courant (cohérent avec les H1) + URL canonique
SEO_PAGES: list[tuple[str, str, str]] = [
    ("etude-solaire-gratuite", "Étude solaire gratuite", "https://www.solarglobe.fr/seo/etude-solaire-gratuite/"),
]

NAV_SNIP = """<div class="sg-container">
  <nav class="sg-breadcrumb sg-breadcrumb-dark sg-breadcrumb--compact" aria-label="Fil d'Ariane">
    <ol class="sg-breadcrumb-list">
      <li><a href="/">Accueil</a></li>
      <li><a href="/le-solaire/">Le solaire</a></li>
      <li aria-current="page">{label}</li>
    </ol>
  </nav>
</div>
"""


def ld_json(label: str, url: str) -> str:
    data = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://www.solarglobe.fr/"},
            {"@type": "ListItem", "position": 2, "name": "Le solaire", "item": "https://www.solarglobe.fr/le-solaire/"},
            {"@type": "ListItem", "position": 3, "name": label, "item": url},
        ],
    }
    return "<script type=\"application/ld+json\">\n" + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>\n"


def main() -> None:
    marker = '<script src="/assets/js/header.js"></script>'
    for slug, label, url in SEO_PAGES:
        path = ROOT / "seo" / slug / "index.html"
        text = path.read_text(encoding="utf-8")
        if "sg-breadcrumb-list" in text:
            print(f"[skip nav] {path}")
        else:
            if marker not in text:
                raise SystemExit(f"Marker manquant: {path}")
            text = text.replace(marker, marker + "\n\n" + NAV_SNIP.format(label=label), 1)
        foot = '<div id="footer-placeholder"></div>'
        if '"@type": "BreadcrumbList"' not in text:
            if foot not in text:
                raise SystemExit(f"Footer manquant: {path}")
            text = text.replace(foot, ld_json(label, url) + foot, 1)
        path.write_text(text, encoding="utf-8")
        print(f"OK {slug}")


if __name__ == "__main__":
    main()
