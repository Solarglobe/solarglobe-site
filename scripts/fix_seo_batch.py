# -*- coding: utf-8 -*-
"""Batch SEO fixes: ville titles, seo og:url. Run: python scripts/fix_seo_batch.py"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEPT_SLUGS = {
    "ile-de-france",
    "essonne",
    "hauts-de-seine",
    "paris",
    "seine-et-marne",
    "seine-saint-denis",
    "val-de-marne",
    "val-doise",
    "yvelines",
}


def fix_ville_titles(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        s = f.read()
    orig = s
    # <title>Panneaux solaires X -> add à if not already "Panneaux solaires à"
    s = re.sub(
        r"<title>Panneaux solaires\s+(?!à\s)",
        "<title>Panneaux solaires à ",
        s,
        count=1,
    )
    s = re.sub(
        r'(<meta\s+property="og:title"\s+content=")Panneaux solaires\s+(?!à\s)',
        r"\1Panneaux solaires à ",
        s,
        count=1,
    )
    if s != orig:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
        return True
    return False


def fix_seo_og_url(path: str) -> bool:
    with open(path, encoding="utf-8") as f:
        s = f.read()
    m = re.search(
        r'<link\s+rel="canonical"\s+href="(https://www\.solarglobe\.fr[^"]+)"',
        s,
    )
    if not m:
        return False
    can = m.group(1)
    orig = s
    s = re.sub(
        r'<meta\s+property="og:url"\s+content="[^"]*"',
        f'<meta property="og:url" content="{can}"',
        s,
        count=1,
    )
    if s != orig:
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
        return True
    return False


def main():
    n1 = n2 = 0
    for entry in sorted(os.listdir(ROOT)):
        if not entry.startswith("panneaux-solaires-"):
            continue
        slug = entry.replace("panneaux-solaires-", "")
        if slug in DEPT_SLUGS:
            continue
        p = os.path.join(ROOT, entry, "index.html")
        if os.path.isfile(p):
            if fix_ville_titles(p):
                n1 += 1
                print("title:", p)

    seo_dir = os.path.join(ROOT, "seo")
    if os.path.isdir(seo_dir):
        for fn in os.listdir(seo_dir):
            p = os.path.join(seo_dir, fn, "index.html")
            if os.path.isfile(p):
                if fix_seo_og_url(p):
                    n2 += 1
                    print("og:url:", p)

    print("Ville titles fixed:", n1)
    print("SEO og:url fixed:", n2)


if __name__ == "__main__":
    main()
