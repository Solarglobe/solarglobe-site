# -*- coding: utf-8 -*-
"""Audit SEO meta tags; run from repo root: python scripts/audit_seo_meta.py"""
import collections
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {"scripts", "node_modules", ".git", "components"}


def walk_html():
    for dp, dns, fns in os.walk(ROOT):
        base = os.path.basename(dp)
        if base in SKIP_DIRS or base.startswith("."):
            dns[:] = []
            continue
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith(".")]
        for fn in fns:
            if not fn.endswith(".html"):
                continue
            if "node_modules" in dp:
                continue
            yield os.path.join(dp, fn)


def extract(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        t = f.read()

    def m1(pat):
        r = re.search(pat, t, re.I | re.S)
        return r.group(1).strip() if r else None

    return {
        "path": path,
        "desc": m1(r'<meta\s+name=["\']description["\']\s+content="([^"]*)"'),
        "can": m1(r'<link\s+rel=["\']canonical["\']\s+href=["\']([^"\']*)["\']'),
        "ogu": m1(r'<meta\s+property=["\']og:url["\']\s+content="([^"]*)"'),
        "title": m1(r"<title>(.*?)</title>"),
    }


def main():
    rows = [extract(p) for p in walk_html()]

    byd = collections.defaultdict(list)
    for e in rows:
        if e["desc"]:
            byd[e["desc"]].append(e["path"])

    dups = {k: v for k, v in byd.items() if len(v) > 1}
    print("=== META DESCRIPTION DUPLICATES ===")
    for k, v in sorted(dups.items(), key=lambda x: -len(x[1])):
        print(len(v), repr(k[:100]))
        for p in v:
            rel = os.path.relpath(p, ROOT)
            print("   ", rel)
    print("dup groups:", len(dups))

    print("\n=== CANONICAL vs OG MISMATCH ===")
    bad = []
    for e in rows:
        if e["can"] and e["ogu"] and e["ogu"] != e["can"]:
            bad.append(e)
    for e in bad:
        print(os.path.relpath(e["path"], ROOT))
        print("  canonical:", e["can"])
        print("  og:url:   ", e["ogu"])
    print("mismatches:", len(bad))

    print("\n=== CANONICAL ISSUES ===")
    issues = []
    for e in rows:
        c = e["can"]
        rel = os.path.relpath(e["path"], ROOT)
        if not c:
            issues.append((rel, "missing"))
            continue
        if not c.startswith("https://www.solarglobe.fr/"):
            issues.append((rel, "host " + c))
        if not c.endswith("/"):
            issues.append((rel, "no slash " + c))
    for rel, msg in issues:
        print(rel, "|", msg)
    print("canonical issues:", len(issues))

    print("\n=== OG:url NO TRAILING SLASH ===")
    for e in rows:
        if e["ogu"] and not e["ogu"].endswith("/"):
            print(os.path.relpath(e["path"], ROOT), e["ogu"])


if __name__ == "__main__":
    main()
