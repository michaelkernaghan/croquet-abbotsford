#!/usr/bin/env python3
"""Put one rel="canonical" tag on every page, and keep them all consistent.

Run from the repo root:  python docs/build-scripts/set_canonical_urls.py

Why this exists: Netlify's Pretty URLs feature rewrites internal links, so the
site serves `/lessons` while the repo holds `lessons.html`. Both URLs return 200
with no redirect, so without a canonical tag every page is reachable at two
addresses and search engines have to guess which one to index.

EXTENSIONLESS = True matches what Netlify serves and links to, so the canonical
tag, the internal links and the sitemap all agree.

Set EXTENSIONLESS = False if the site ever moves off Netlify, or if Pretty URLs
is switched off - `.html` works on any static host, `/lessons` does not. Then
re-run this and generate_sitemap.py, which reads the same flag.

Idempotent: it strips any canonical tag it finds before writing a fresh one, so
running it twice changes nothing.
"""
import pathlib
import re

SITE = 'https://abbotsfordcroquet.com'
EXTENSIONLESS = True
ROOT = pathlib.Path(__file__).resolve().parents[2]

# Pages that should point at a different page rather than at themselves.
POINTS_AT = {
    'signup.html': 'court-status.html',   # meta-refresh redirect stub
}

CANONICAL = re.compile(r'[ \t]*<link\s+rel="canonical"[^>]*>\n', re.I)


def url_for(filename: str) -> str:
    if filename == 'index.html':
        return SITE + '/'
    slug = filename[:-5] if EXTENSIONLESS and filename.endswith('.html') else filename
    return f'{SITE}/{slug}'


def main() -> None:
    changed = 0
    for p in sorted(ROOT.glob('*.html')):
        txt = original = p.read_text(encoding='utf-8', errors='ignore')
        txt = CANONICAL.sub('', txt)

        target = POINTS_AT.get(p.name, p.name)
        tag = f'    <link rel="canonical" href="{url_for(target)}">\n'

        # sit it directly after the title, above the description and OG block
        new, n = re.subn(r'(</title>\n)', r'\1' + tag, txt, count=1)
        if not n:
            print(f'  SKIPPED {p.name}: no </title> to anchor to')
            continue
        if new != original:
            p.write_text(new, encoding='utf-8', newline='')
            changed += 1

    form = 'extensionless (/lessons)' if EXTENSIONLESS else 'explicit (.html)'
    print(f'canonical tags written in {form} form; {changed} files changed')


if __name__ == '__main__':
    main()
