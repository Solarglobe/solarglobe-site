# -*- coding: utf-8 -*-
"""Met à jour le fil d'Ariane (HTML ol/li + JSON-LD) des pages panneaux-solaires-*.

Logique unique : Accueil → Zones d'intervention (/qui-sommes-nous/#zones) → page courante.
Aligné sur la section « Zones d'intervention » de Qui sommes-nous (couverture IDF + France).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ZONES_HREF = "/qui-sommes-nous/#zones"
ZONES_LABEL = "Zones d'intervention"
ZONES_ITEM = "https://www.solarglobe.fr/qui-sommes-nous/#zones"

NAV_BLOCK_RE = re.compile(
    r'<div class="sg-container">\s*'
    r'<nav class="sg-breadcrumb sg-breadcrumb-dark[^"]*" aria-label="Fil d\'Ariane">\s*.*?</nav>\s*</div>',
    re.DOTALL,
)


def extract_current_label(nav_inner: str) -> str:
    m = re.search(r'<li\s+aria-current="page">([^<]+)</li>', nav_inner, re.DOTALL)
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()
    spans = re.findall(r"<span>([^<]+)</span>", nav_inner)
    if spans:
        return spans[-1].strip()
    return "Panneaux solaires"


def build_nav_html(label: str) -> str:
    return "\n".join(
        [
            '<div class="sg-container">',
            '  <nav class="sg-breadcrumb sg-breadcrumb-dark sg-breadcrumb--compact" aria-label="Fil d\'Ariane">',
            '    <ol class="sg-breadcrumb-list">',
            '      <li><a href="/">Accueil</a></li>',
            f'      <li><a href="{ZONES_HREF}">{ZONES_LABEL}</a></li>',
            f'      <li aria-current="page">{label}</li>',
            "    </ol>",
            "  </nav>",
            "</div>",
        ]
    )


def build_breadcrumb_json(label: str) -> dict:
    base = "https://www.solarglobe.fr"
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": f"{base}/"},
            {"@type": "ListItem", "position": 2, "name": ZONES_LABEL, "item": ZONES_ITEM},
            {"@type": "ListItem", "position": 3, "name": label},
        ],
    }


def replace_ld_json_breadcrumb(html: str, data: dict) -> str:
    # JSON pretty-printé ou minifié (@type":"BreadcrumbList")
    pos = html.find('"BreadcrumbList"')
    if pos == -1:
        return html
    script_start = html.rfind('<script type="application/ld+json">', 0, pos)
    script_end = html.find("</script>", pos)
    if script_start == -1 or script_end == -1:
        return html
    new_script = '<script type="application/ld+json">\n' + json.dumps(data, ensure_ascii=False, indent=2) + "\n</script>"
    return html[:script_start] + new_script + html[script_end + len("</script>") :]


def process_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    m = NAV_BLOCK_RE.search(text)
    if not m:
        print(f"[skip] Pas de bloc nav attendu: {path}")
        return False
    inner = m.group(0)
    nav_only = re.search(
        r'<nav class="sg-breadcrumb sg-breadcrumb-dark[^"]*" aria-label="Fil d\'Ariane">\s*(.*?)\s*</nav>',
        inner,
        re.DOTALL,
    )
    label = extract_current_label(nav_only.group(1)) if nav_only else "Panneaux solaires"
    new_nav = build_nav_html(label)
    text = NAV_BLOCK_RE.sub(new_nav, text, count=1)
    text = replace_ld_json_breadcrumb(text, build_breadcrumb_json(label))
    path.write_text(text, encoding="utf-8")
    return True


def main() -> None:
    n = 0
    for p in sorted(ROOT.glob("panneaux-solaires-*/index.html")):
        if process_file(p):
            n += 1
    print(f"OK — {n} pages villes mises à jour.")


if __name__ == "__main__":
    main()
