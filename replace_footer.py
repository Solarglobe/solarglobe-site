#!/usr/bin/env python3
"""
Remplace le bloc footer par le placeholder et le script footer.js
dans tous les fichiers HTML éligibles.
Ajoute aussi le lien footer-common.css dans le head.
"""
import re
from pathlib import Path

FOOTER_PLACEHOLDER = '''<div id="footer-placeholder"></div>
<script src="/assets/js/footer.js"></script>
'''

FOOTER_CSS = '<link rel="stylesheet" href="/assets/css/footer-common.css" />'

EXCLUDE = {
    'components/header.html',
    'components/footer.html',
    '_header-global.html',
    'index.nginx-debian.html',
    'google8216ab55dcee3d13.html',
}


def should_exclude(filepath: str) -> bool:
    path = Path(filepath)
    rel_str = str(path).replace('\\', '/')
    return rel_str in EXCLUDE


def add_footer_css(content: str) -> str:
    """Ajoute footer-common.css après header-common.css si absent."""
    if 'footer-common.css' in content:
        return content
    if 'header-common.css' in content:
        content = re.sub(
            r'(<link rel="stylesheet" href="/assets/css/header-common\.css"[^>]*/>)',
            r'\1\n  ' + FOOTER_CSS,
            content,
            count=1
        )
    elif '</head>' in content:
        content = content.replace('</head>', '  ' + FOOTER_CSS + '\n</head>')
    return content


def find_footer_block(content: str) -> tuple[int, int] | None:
    """Trouve les indices début et fin du bloc footer à remplacer."""
    # Cas 1: index.html - pas de <footer> ouvrante, bloc social + copyright + </footer>
    icones_match = re.search(r'\n\s*<!-- Icônes réseaux sociaux -->.*?</footer>', content, re.DOTALL)
    if icones_match:
        return (icones_match.start(), icones_match.end())

    # Cas 2: <!-- FOOTER --> ou <!-- Footer --> suivi de <footer ...>
    start_pos = -1
    for pattern in [r'<!--\s*FOOTER\s*-->', r'<!--\s*Footer\s*-->']:
        m = re.search(pattern, content, re.IGNORECASE)
        if m:
            start_pos = m.start()
            break

    if start_pos < 0:
        m = re.search(r'<footer\s', content)
        if m:
            start_pos = m.start()
        else:
            return None

    end_match = re.search(r'</footer>', content[start_pos:])
    if not end_match:
        return None
    end_pos = start_pos + end_match.end()
    return (start_pos, end_pos)


def process_file(filepath: str) -> bool:
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    modified = False

    # 1. Remplacer le footer
    result = find_footer_block(content)
    if result:
        start, end = result
        content = content[:start] + FOOTER_PLACEHOLDER + content[end:]
        modified = True
    elif 'footer-placeholder' not in content and '</body>' in content:
        # Pas de footer trouvé: ajouter le placeholder avant </body>
        content = content.replace(
            '</body>',
            '\n' + FOOTER_PLACEHOLDER + '\n</body>'
        )
        modified = True

    # 2. Ajouter footer CSS si on a le placeholder
    if modified and 'footer-placeholder' in content:
        new_content = add_footer_css(content)
        if new_content != content:
            content = new_content

    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return modified


def main():
    root = Path(__file__).parent
    modified = []

    for html_file in root.rglob('*.html'):
        rel = html_file.relative_to(root)
        rel_str = str(rel).replace('\\', '/')

        if should_exclude(rel_str):
            continue

        try:
            if process_file(str(html_file)):
                modified.append(rel_str)
                print(f"  [OK] {rel_str}")
        except Exception as e:
            print(f"  [ERREUR] {rel_str}: {e}")

    print(f"\n{len(modified)} fichier(s) modifié(s).")


if __name__ == '__main__':
    main()
