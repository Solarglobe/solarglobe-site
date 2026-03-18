#!/usr/bin/env python3
"""Ajoute le design system comme première feuille de style dans toutes les pages HTML."""
from pathlib import Path

DS_LINK = '<link rel="stylesheet" href="/assets/css/solarglobe-design-system.css" />'

EXCLUDE = {
    'components/header.html',
    'components/footer.html',
    '_header-global.html',
    'google8216ab55dcee3d13.html',
    'index.nginx-debian.html',
}


def should_process(filepath: str) -> bool:
    p = Path(filepath)
    rel = str(p).replace('\\', '/')
    if not rel.endswith('.html'):
        return False
    for excl in EXCLUDE:
        if excl in rel or p.name == excl:
            return False
    return True


def add_design_system(content: str) -> str:
    if 'solarglobe-design-system.css' in content:
        return content
    # Trouver la première balise link stylesheet et ajouter le DS avant
    target = 'rel="stylesheet"'
    idx = content.find(target)
    if idx == -1:
        return content
    # Remonter au début de la balise <link
    start = content.rfind('<link', 0, idx)
    if start == -1:
        return content
    # Insérer le design system avant cette balise
    insert = DS_LINK + '\n  '
    return content[:start] + insert + content[start:]


def main():
    root = Path(__file__).parent
    modified = []
    for f in root.rglob('*.html'):
        rel = str(f.relative_to(root)).replace('\\', '/')
        if not should_process(rel):
            continue
        try:
            text = f.read_text(encoding='utf-8', errors='replace')
            new_text = add_design_system(text)
            if new_text != text:
                f.write_text(new_text, encoding='utf-8')
                modified.append(rel)
                print(f"  [OK] {rel}")
        except Exception as e:
            print(f"  [ERREUR] {rel}: {e}")
    print(f"\n{len(modified)} fichier(s) modifié(s).")


if __name__ == '__main__':
    main()
