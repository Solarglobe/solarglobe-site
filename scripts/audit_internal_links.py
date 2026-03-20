# -*- coding: utf-8 -*-
"""Internal link audit: HTML <a href> vs repo filesystem. Run: python scripts/audit_internal_links.py"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules"}

STATIC_EXT = {
    ".pdf", ".png", ".jpg", ".jpeg", ".webp", ".avif", ".svg", ".gif", ".ico",
    ".css", ".js", ".json", ".xml", ".txt", ".woff", ".woff2", ".ttf", ".eot",
    ".mp4", ".webm",
}

HREF_RE = re.compile(
    r"""<a\s[^>]*\bhref\s*=\s*(['"])(.*?)\1""",
    re.I | re.DOTALL,
)


def iter_html_files() -> list[Path]:
    out: list[Path] = []
    for p in ROOT.rglob("*.html"):
        rel = p.relative_to(ROOT)
        if rel.parts[0] in SKIP_DIRS:
            continue
        out.append(p)
    return sorted(out)


def normalize_href(raw: str) -> str | None:
    s = raw.strip()
    if not s or s.startswith("#"):
        return None
    low = s.lower()
    if low.startswith(("mailto:", "tel:", "javascript:")):
        return None
    if low.startswith("http://") or low.startswith("https://"):
        u = urlparse(s)
        host = (u.netloc or "").lower().replace("www.", "")
        if host and "solarglobe.fr" not in host:
            return None
        path = u.path or "/"
        return path
    return s.split("#")[0].split("?")[0] or None


def abs_path_candidates(href: str) -> list[Path]:
    """href is path-only, starts with /"""
    p = href.rstrip("/")
    if p == "" or p == "/":
        return [ROOT / "index.html"]
    rel = p.lstrip("/")
    lp = Path(rel)
    suf = lp.suffix.lower()

    if suf in STATIC_EXT:
        return [ROOT / rel]

    # HTML pages: directory index or legacy .html at root
    c: list[Path] = [ROOT / rel / "index.html"]
    if not href.endswith("/") and suf != ".html":
        c.append(ROOT / f"{rel}.html")
    if suf == ".html":
        c.insert(0, ROOT / rel)
    return c


def rel_path_candidates(source: Path, href: str) -> list[Path]:
    base = source.parent
    target = (base / href).resolve()
    try:
        target.relative_to(ROOT)
    except ValueError:
        return []
    c: list[Path] = []
    if href.endswith("/"):
        c.append(target / "index.html")
    else:
        if target.suffix.lower() in STATIC_EXT:
            c.append(target)
        else:
            c.append(target)
            c.append(target / "index.html")
            if target.suffix != ".html":
                c.append(target.with_name(target.name + ".html"))
    # dedupe
    seen = set()
    out: list[Path] = []
    for x in c:
        k = str(x)
        if k not in seen:
            seen.add(k)
            out.append(x)
    return out


def resolve(norm: str, source: Path) -> list[Path]:
    if norm.startswith("/"):
        return abs_path_candidates(norm)
    return rel_path_candidates(source, norm)


def exists_any(paths: list[Path]) -> tuple[bool, Path | None]:
    for p in paths:
        if p.is_file():
            return True, p
    return False, None


def main() -> int:
    html_files = iter_html_files()
    records: list[dict] = []

    for src in html_files:
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for m in HREF_RE.finditer(text):
            raw = m.group(2)
            norm = normalize_href(raw)
            if norm is None:
                continue
            cands = resolve(norm, src)
            ok, hit = exists_any(cands)
            rel_hit = hit.relative_to(ROOT).as_posix() if hit else None
            tail = text[m.end() : m.end() + 250]
            tm = re.search(r">([^<]{0,100})<", tail)
            label = (tm.group(1).strip() if tm else "")[:100]

            conv_issue = None
            if ok and norm.startswith("/") and hit and rel_hit:
                if rel_hit.endswith("index.html") and norm != "/" and not norm.endswith("/"):
                    if not Path(norm).suffix:
                        conv_issue = "trailing_slash"

            records.append(
                {
                    "source": src.relative_to(ROOT).as_posix(),
                    "href_raw": raw[:300],
                    "href_norm": norm[:300],
                    "label": label,
                    "ok": ok,
                    "resolved": rel_hit,
                    "candidates": [c.relative_to(ROOT).as_posix() for c in cands[:8]],
                    "conv_issue": conv_issue,
                }
            )

    total = len(records)
    ok_n = sum(1 for r in records if r["ok"])
    bad = [r for r in records if not r["ok"]]
    conv = [r for r in records if r["conv_issue"]]

    lines = []
    lines.append("=== INTERNAL LINK AUDIT (factuel, repo filesystem) ===")
    lines.append(f"Racine projet: {ROOT}")
    lines.append(f"Fichiers HTML parcourus: {len(html_files)}")
    lines.append(f"Balises <a href> internes (hors mailto/tel/#/http externes): {total}")
    lines.append(f"Résolus vers un fichier existant: {ok_n}")
    lines.append(f"Non résolus (cassés): {len(bad)}")
    lines.append(f"OK mais chemin absolu sans slash final alors que cible = .../index.html: {len(conv)}")
    lines.append("")

    if bad:
        lines.append("--- LIENS CASSÉS (détail) ---")
        for r in bad:
            lines.append(f"source={r['source']}")
            lines.append(f"  href={r['href_raw']!r}")
            lines.append(f"  candidats testés: {r['candidates']}")
            lines.append("")

    out_path = ROOT / "scripts" / "_audit_links_output.txt"
    out_path.write_text("\n".join(lines), encoding="utf-8")

    # Focus index.html
    home = [r for r in records if r["source"] == "index.html"]
    lines.append("")
    lines.append(f"--- FOCUS index.html ({len(home)} liens) ---")
    for r in home:
        st = "OK" if r["ok"] else "BROKEN"
        extra = f" [{r['conv_issue']}]" if r["conv_issue"] else ""
        lines.append(f"{st}{extra} | {r['href_raw']!r} -> {r['resolved'] or r['candidates']}")
        if r["label"]:
            lines.append(f"     libellé: {r['label'][:60]}")

    # Footer component
    foot = [r for r in records if r["source"] == "components/footer.html"]
    lines.append("")
    lines.append(f"--- components/footer.html ({len(foot)} liens) ---")
    for r in foot:
        st = "OK" if r["ok"] else "BROKEN"
        lines.append(f"{st} | {r['href_raw']!r} -> {r['resolved']}")

    out_path.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines[:40]))
    print(f"\n[...] Rapport complet: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
