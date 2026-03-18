#!/usr/bin/env python3
"""
Uniformise les layouts des pages SolarGlobe.
Ajoute sg-container, sg-section, sg-hero, sg-cta, sg-transition-block.
"""
import re
from pathlib import Path

EXCLUDE = {
    'components/', '_header-global.html', 'google8216ab55dcee3d13.html',
    'index.nginx-debian.html', 'partenaires.html', 'proprietaires.html',
}

def should_process(p: Path) -> bool:
    s = str(p).replace('\\', '/')
    if not s.endswith('.html'):
        return False
    for ex in EXCLUDE:
        if ex in s:
            return False
    return True

def replace_container(html: str) -> str:
    """Remplace max-w-*xl mx-auto par sg-container (sauf dans <p> pour max-w-3xl)."""
    # Ne pas remplacer max-w-3xl mx-auto dans les paragraphes (centrage texte)
    html = re.sub(r'\bmax-w-4xl\s+mx-auto\b', 'sg-container', html)
    html = re.sub(r'\bmax-w-6xl\s+mx-auto\b', 'sg-container', html)
    html = re.sub(r'\bmax-w-7xl\s+mx-auto\s+px-[246]\b', 'sg-container', html)
    html = re.sub(r'\bmax-w-7xl\s+mx-auto\b', 'sg-container', html)
    # max-w-3xl mx-auto sur div/section -> sg-container. Sur p -> garder max-w-3xl mx-auto
    html = re.sub(r'(<(?:div|section)[^>]*class="[^"]*)\bmax-w-3xl\s+mx-auto\b', r'\1sg-container', html)
    return html

def add_section_classes(html: str) -> str:
    """Ajoute sg-section aux sections avec padding."""
    # Section avec py-24 ou py-20 au début de page = hero
    html = re.sub(
        r'<section class="([^"]*?)px-6 py-24 text-center([^"]*?)">',
        r'<section class="sg-hero sg-hero-dark \1\2">',
        html, count=1
    )
    return html

def main():
    root = Path(__file__).parent
    count = 0
    for f in root.rglob('*.html'):
        if not should_process(f):
            continue
        try:
            content = f.read_text(encoding='utf-8', errors='replace')
            orig = content
            content = replace_container(content)
            if content != orig:
                f.write_text(content, encoding='utf-8')
                count += 1
                print(f"  {f.relative_to(root)}")
        except Exception as e:
            print(f"  ERREUR {f}: {e}")
    print(f"\n{count} fichier(s) modifié(s).")

if __name__ == '__main__':
    main()
