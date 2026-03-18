#!/usr/bin/env python3
"""
Remplace le bloc header (nav#main-nav + mobile-overlay + mobile-menu + 2 scripts)
par le placeholder et le script header.js dans tous les fichiers HTML éligibles.
"""
import re
import os
from pathlib import Path

REPLACEMENT = '''<div id="header-placeholder"></div>
<script src="/assets/js/header.js"></script>
'''

# Fichiers à exclure
EXCLUDE = {
    '_header-global.html',
    'etude-gratuite.html',  # redirect à la racine
    'components/header.html',  # source du header chargé par header.js
}
# Dossiers/pages avec nav simplifiée (pas de main-nav dans ce projet)
EXCLUDE_PATHS = ['mentions-legales', 'cookies', 'cgv', 'politique-de-confidentialite']

def should_exclude(filepath: str) -> bool:
    """Vérifie si le fichier doit être exclu."""
    path = Path(filepath)
    name = path.name
    if name in EXCLUDE:
        return True
    # Exclure les fichiers dans les dossiers mentions-legales, cookies, etc.
    for part in path.parts:
        if part in EXCLUDE_PATHS:
            return True
    return False

def find_header_block(content: str) -> tuple[int, int] | None:
    """
    Trouve les indices de début et fin du bloc header à remplacer.
    Retourne (start, end) ou None si non trouvé.
    """
    # Marqueurs de début possibles
    start_patterns = [
        r'<!--\s*NAV\s*-->',
        r'<!--\s*======\s*MENU PREMIUM\s*======\s*-->',
        r'<!--\s*HEADER GLOBAL[^>]*-->',
        r'<!--\s*Header global[^>]*-->',
        r'<nav\s[^>]*id="main-nav"',
    ]
    
    # Trouver le début du bloc
    start_match = None
    start_pos = -1
    for pattern in start_patterns:
        m = re.search(pattern, content, re.IGNORECASE)
        if m:
            pos = m.start()
            if start_pos < 0 or pos < start_pos:
                start_pos = pos
                start_match = m
    
    if start_pos < 0:
        return None
    
    # Si on a matché un commentaire, inclure les espaces/newlines avant le <nav>
    # Sinon on a déjà le <nav>
    # Chercher le <nav id="main-nav"> si on a commencé par un commentaire
    nav_start = content.find('<nav', start_pos)
    if nav_start >= 0 and nav_start < start_pos + 200:
        start_pos = min(start_pos, nav_start)
    
    # Trouver la fin : après le 2ème <script>...</script> (celui avec querySelectorAll / initActiveLink)
    mobile_menu_pos = content.find('id="mobile-menu"', start_pos)
    search_from = content.find('</div>', mobile_menu_pos) if mobile_menu_pos >= 0 else start_pos
    if search_from < 0:
        search_from = start_pos
    
    script_pattern = re.compile(r'<script(?:\s[^>]*)?>([\s\S]*?)</script>', re.IGNORECASE)
    end_pos = -1
    for m in script_pattern.finditer(content, search_from):
        script_content = m.group(1)
        if 'querySelectorAll' in script_content or ('#main-nav' in script_content and 'mobile-menu' in script_content):
            end_pos = m.end()
            break
    
    if end_pos < 0:
        return None
    
    return (start_pos, end_pos)

def process_file(filepath: str) -> bool:
    """Traite un fichier. Retourne True si modifié."""
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    if 'id="main-nav"' not in content:
        return False
    
    result = find_header_block(content)
    if not result:
        return False
    
    start, end = result
    new_content = content[:start] + REPLACEMENT + content[end:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    root = Path(__file__).parent
    modified = []
    
    for html_file in root.rglob('*.html'):
        rel = html_file.relative_to(root)
        rel_str = str(rel).replace('\\', '/')
        
        if should_exclude(rel_str):
            print(f"  [EXCLU] {rel_str}")
            continue
        
        if 'id="main-nav"' not in html_file.read_text(encoding='utf-8', errors='replace'):
            continue
        
        try:
            if process_file(str(html_file)):
                modified.append(rel_str)
                print(f"  [OK] {rel_str}")
            else:
                print(f"  [SKIP - pattern non trouvé] {rel_str}")
        except Exception as e:
            print(f"  [ERREUR] {rel_str}: {e}")
    
    print(f"\n{len(modified)} fichier(s) modifié(s).")

if __name__ == '__main__':
    main()
