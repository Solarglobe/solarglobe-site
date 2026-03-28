# -*- coding: utf-8 -*-
"""Remplace le bundle CDN Tailwind + config inline par le lien CSS compilé (usage ponctuel)."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(
    r'<script\s+src="https://cdn\.tailwindcss\.com"></script>\s*<script>[\s\S]*?</script>',
    re.MULTILINE,
)
LINK = '<link rel="stylesheet" href="/assets/css/tailwind.css" />'

def main():
    unmatched = []
    replaced = 0
    for path in list(ROOT.rglob('*.html')) + list(ROOT.rglob('*.py')):
        if 'node_modules' in path.parts:
            continue
        text = path.read_text(encoding='utf-8')
        if ('cdn.' + 'tailwindcss' + '.com') not in text:
            continue
        new, n = PATTERN.subn(LINK, text, count=1)
        if n:
            path.write_text(new, encoding='utf-8')
            replaced += 1
        else:
            unmatched.append(path)
    print(f'OK: {replaced} fichiers remplacés.')
    if unmatched:
        print('NON MATCHÉS (à traiter à la main):')
        for p in unmatched:
            print(' ', p.relative_to(ROOT))

if __name__ == '__main__':
    main()
