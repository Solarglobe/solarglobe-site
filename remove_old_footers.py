#!/usr/bin/env python3
"""
Supprime tous les anciens blocs footer du site.
Ne garde que le placeholder + script footer.js.
"""
import re
from pathlib import Path

FOOTER_PLACEHOLDER = '''<div id="footer-placeholder"></div>
<script src="/assets/js/footer.js"></script>'''

EXCLUDE = {
    'components/footer.html',
    'components/header.html',
    '_header-global.html',
    'index.nginx-debian.html',
    'google8216ab55dcee3d13.html',
    'replace_footer.py',
    'remove_old_footers.py',
    'generate_seo_pages.py',
    'script-gen-page-dynamique.py',
    'SQUELETTE-REFERENCE.md',
}


def should_process(filepath: str) -> bool:
    path = Path(filepath)
    rel_str = str(path).replace('\\', '/')
    if not rel_str.endswith('.html'):
        return False
    for excl in EXCLUDE:
        if excl in rel_str or path.name == excl:
            return False
    return True


def remove_old_footer_blocks(content: str) -> str:
    """Supprime tous les blocs footer anciens."""
    # Cas 1: Placeholder DANS le footer (structure cassée) - remplacer tout le bloc par le placeholder
    pattern1 = r'\s*<!--\s*FOOTER\s*-->\s*\n\s*<footer class="bg-black[^"]*"[^>]*>.*?<div id="footer-placeholder"></div>\s*<script src="/assets/js/footer\.js"></script>\s*'
    content = re.sub(pattern1, '\n\n' + FOOTER_PLACEHOLDER + '\n\n', content, flags=re.DOTALL)

    pattern1b = r'<footer class="bg-black[^"]*"[^>]*>.*?<div id="footer-placeholder"></div>\s*<script src="/assets/js/footer\.js"></script>\s*'
    content = re.sub(pattern1b, FOOTER_PLACEHOLDER + '\n\n', content, flags=re.DOTALL)

    # Cas 2: Footer complet classique (avec </footer>)
    pattern2 = r'\s*<!--\s*FOOTER\s*-->\s*\n\s*<footer class="bg-black[^"]*"[^>]*>.*?</footer>'
    content = re.sub(pattern2, '', content, flags=re.DOTALL)

    pattern2b = r'\s*<footer class="bg-black text-white text-sm px-6 pt-16 pb-10 mt-12 border-t border-neutral-800">.*?</footer>'
    content = re.sub(pattern2b, '', content, flags=re.DOTALL)

    # Variante sans mt-12 border-t (ex: merci.html)
    pattern2c = r'\s*<!--\s*FOOTER[^>]*-->\s*\n\s*<footer class="bg-black[^"]*"[^>]*>.*?</footer>'
    content = re.sub(pattern2c, '', content, flags=re.DOTALL)

    pattern2d = r'\s*<footer class="bg-black text-white text-sm px-6 pt-16 pb-10">.*?</footer>'
    content = re.sub(pattern2d, '', content, flags=re.DOTALL)

    return content


def ensure_footer_placeholder(content: str) -> str:
    """S'assure que le placeholder est présent une seule fois avant </body>"""
    if 'footer-placeholder' in content:
        return content  # Déjà présent
    # Ajouter avant </body>
    content = content.replace('</body>', '\n' + FOOTER_PLACEHOLDER + '\n</body>')
    return content


def remove_duplicate_placeholders(content: str) -> str:
    """Supprime les placeholders en double, garde un seul avant </body>."""
    placeholder_block = r'<div id="footer-placeholder"></div>\s*<script src="/assets/js/footer\.js"></script>'
    matches = list(re.finditer(placeholder_block, content))
    if len(matches) <= 1:
        return content
    # Remplacer toutes les occurrences par vide, puis ajouter une seule avant </body>
    new_content = re.sub(placeholder_block + r'\s*', '', content)
    insert_pos = new_content.rfind('</body>')
    if insert_pos >= 0:
        new_content = new_content[:insert_pos] + '\n' + FOOTER_PLACEHOLDER + '\n\n' + new_content[insert_pos:]
    return new_content


def process_file(filepath: str) -> bool:
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    original = content

    # 1. Supprimer les anciens footers
    content = remove_old_footer_blocks(content)

    # 2. S'assurer qu'on a le placeholder (si la page avait un footer supprimé)
    if 'footer-placeholder' not in content and '</body>' in content:
        content = ensure_footer_placeholder(content)

    # 3. Supprimer les doublons de placeholder
    content = remove_duplicate_placeholders(content)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    root = Path(__file__).parent
    modified = []

    for html_file in root.rglob('*.html'):
        rel = html_file.relative_to(root)
        rel_str = str(rel).replace('\\', '/')

        if not should_process(rel_str):
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
