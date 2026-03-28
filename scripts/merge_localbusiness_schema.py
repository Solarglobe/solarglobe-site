# -*- coding: utf-8 -*-
"""Fusionne les blocs JSON-LD LocalBusiness avec la version canonique (réf. components/ld-localbusiness-canonical.json)."""
import json
import re
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parents[1]
CANON_PATH = ROOT / "components" / "ld-localbusiness-canonical.json"

SCRIPT_OPEN = '<script type="application/ld+json">'
SCRIPT_CLOSE = "</script>"


def is_local_business(obj: dict) -> bool:
    t = obj.get("@type")
    if t == "LocalBusiness":
        return True
    if isinstance(t, list) and "LocalBusiness" in t:
        return True
    return False


def preserve_area_served(old: dict) -> Optional[Any]:
    """Conserve areaServed local (ville / département) si pertinent."""
    asv = old.get("areaServed")
    if asv is None:
        return None
    if isinstance(asv, list) and len(asv) == 1:
        return asv
    if isinstance(asv, dict) and asv.get("@type") == "AdministrativeArea":
        return asv
    return None


def merge_block(old: dict) -> dict:
    with open(CANON_PATH, encoding="utf-8") as f:
        new = json.load(f)
    local_as = preserve_area_served(old)
    if local_as is not None:
        new["areaServed"] = local_as
    return new


def process_html(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    changed = False
    out = []
    pos = 0
    for m in re.finditer(
        re.escape(SCRIPT_OPEN) + r"\s*([\s\S]*?)\s*" + re.escape(SCRIPT_CLOSE),
        text,
    ):
        out.append(text[pos : m.start()])
        inner = m.group(1).strip()
        try:
            data = json.loads(inner)
        except json.JSONDecodeError:
            out.append(m.group(0))
            pos = m.end()
            continue
        if isinstance(data, dict) and is_local_business(data):
            merged = merge_block(data)
            pretty = json.dumps(merged, ensure_ascii=False, indent=2)
            out.append(SCRIPT_OPEN + "\n" + pretty + "\n" + SCRIPT_CLOSE)
            changed = True
        else:
            out.append(m.group(0))
        pos = m.end()
    out.append(text[pos:])
    if changed:
        path.write_text("".join(out), encoding="utf-8")
    return changed


def main():
    n = 0
    for path in ROOT.rglob("*.html"):
        if "node_modules" in path.parts:
            continue
        if process_html(path):
            n += 1
            print("OK", path.relative_to(ROOT))
    print("Fichiers mis à jour:", n)


if __name__ == "__main__":
    main()
