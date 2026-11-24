#!/usr/bin/env python3
"""
Build a GitHub Pages sub-path preview from app/dist.

The production build targets the domain root (https://www.chuangyuancorp.com/),
so every asset and link is written as an absolute root path ("/images/...",
"/_astro/...", "/zh/..."). That is correct at the domain root but 404s when the
same files are served from https://jimmyta0899.github.io/chuangyuan/.

This script rewrites those absolute paths to include the "/chuangyuan" prefix and
adds a noindex meta tag so the staging copy never competes with the real domain.

The source dist is left untouched; the production build stays root-relative.
"""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

PREFIX = "/chuangyuan"          # GitHub Pages project sub-path
SRC = Path(__file__).resolve().parent.parent / "dist"
DST = Path(__file__).resolve().parent.parent / "dist-preview"

ATTR_RE = re.compile(r'\b(href|src)="(/[^"]*)"')
SRCSET_RE = re.compile(r'\b(srcset)="([^"]*)"')
CSS_URL_RE = re.compile(r'url\((/[^)]*)\)')
NOINDEX = '<meta name="robots" content="noindex, nofollow">'


def fix_css_url(match: re.Match[str]) -> str:
    value = match.group(1)
    if value.startswith(f"{PREFIX}/"):
        return match.group(0)
    return f"url({PREFIX}{value})"


def fix_srcset(match: re.Match[str]) -> str:
    attr, value = match.group(1), match.group(2)
    # Each candidate is "url [descriptor]", comma separated.
    value = re.sub(rf'(^|,\s*)/(?!{PREFIX.strip("/")}/|/)', rf'\1{PREFIX}/', value)
    return f'{attr}="{value}"'


def fix_attr(match: re.Match[str]) -> str:
    attr, value = match.group(1), match.group(2)
    if value.startswith("//") or value.startswith(f"{PREFIX}/"):
        return match.group(0)
    return f'{attr}="{PREFIX}{value}"'


def rewrite_html(text: str) -> str:
    text = SRCSET_RE.sub(fix_srcset, text)
    text = ATTR_RE.sub(fix_attr, text)
    # Inline <style> blocks keep absolute url(/images/...) references that the
    # attribute rewrite above does not touch.
    text = CSS_URL_RE.sub(fix_css_url, text)
    if NOINDEX not in text and "<head>" in text:
        text = text.replace("<head>", f"<head>\n    {NOINDEX}", 1)
    return text


def main() -> int:
    if not SRC.is_dir():
        print(f"missing source dir: {SRC}", file=sys.stderr)
        return 1
    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    # GitHub Pages would read a CNAME file as a custom-domain claim and 301 the
    # whole project site to www.chuangyuancorp.com. The preview must not carry it.
    cname = DST / "CNAME"
    if cname.exists():
        cname.unlink()

    # Jekyll silently drops every path that starts with "_", which kills /_astro.
    # A .nojekyll file switches the raw-file pipeline on.
    (DST / ".nojekyll").touch()

    changed = 0
    for html in DST.rglob("*.html"):
        original = html.read_text(encoding="utf-8")
        updated = rewrite_html(original)
        if updated != original:
            html.write_text(updated, encoding="utf-8")
            changed += 1

    css_changed = 0
    for css in DST.rglob("*.css"):
        original = css.read_text(encoding="utf-8")
        updated = CSS_URL_RE.sub(fix_css_url, original)
        if updated != original:
            css.write_text(updated, encoding="utf-8")
            css_changed += 1

    print(f"rewrote {changed} html files and {css_changed} css files with {PREFIX} prefix + noindex")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
