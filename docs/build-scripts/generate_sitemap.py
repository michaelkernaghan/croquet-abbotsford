#!/usr/bin/env python3
"""Regenerate sitemap.xml from the pages actually present in the repo.

Run from the repo root:  python docs/build-scripts/generate_sitemap.py

A page is included unless it either carries a `noindex` robots tag (the script
reads the file to decide - nothing to keep in sync) or appears in EXCLUDE below
with a stated reason.

`lastmod` comes from each file's last git commit date, so it is only as honest as
the commit history: a site-wide change such as a meta-tag pass will reset every
date to that day. That is accurate, if less informative.
"""
import datetime
import pathlib
import re
import subprocess

# single source of truth for the URL form, so the sitemap can never disagree
# with the canonical tags - see set_canonical_urls.py for why it matters
from set_canonical_urls import EXTENSIONLESS, url_for

SITE = 'https://abbotsfordcroquet.com'
ROOT = pathlib.Path(__file__).resolve().parents[2]

# Pages deliberately kept out of search results. Anything carrying a noindex tag
# is dropped automatically and does not need a line here.
EXCLUDE = {
    'brochure.html': 'advertises a past event (Open Fun Day, May 2025)',
    'croquet-open-day-poster.html': 'print poster, not a web page',
    'tournament-schedule-template.html': 'blank template, not content',
    'trimmer-drill.html': 'orphaned near-duplicate of trimmer-drills.html',
}


def lastmod(path: pathlib.Path) -> str:
    """Last git commit date, falling back to the file's mtime.

    The fallback matters: a page added but not yet committed has no git date,
    and dating it 1970 would tell search engines it is ancient.
    """
    out = subprocess.run(
        ['git', 'log', '-1', '--format=%ad', '--date=short', '--', path.name],
        capture_output=True, text=True, cwd=ROOT).stdout.strip()
    if out:
        return out
    return datetime.date.fromtimestamp(path.stat().st_mtime).isoformat()


def main() -> None:
    included, skipped = [], []
    for p in sorted(ROOT.glob('*.html')):
        txt = p.read_text(encoding='utf-8', errors='ignore')
        if re.search(r'<meta\s+name="robots"[^>]*noindex', txt, re.I):
            skipped.append((p.name, 'noindex'))
        elif p.name in EXCLUDE:
            skipped.append((p.name, EXCLUDE[p.name]))
        else:
            included.append(p)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for p in included:
        loc = url_for(p.name)
        lines += ['    <url>',
                  f'        <loc>{loc}</loc>',
                  f'        <lastmod>{lastmod(p)}</lastmod>',
                  '    </url>']
    lines.append('</urlset>')

    (ROOT / 'sitemap.xml').write_text('\n'.join(lines) + '\n',
                                      encoding='utf-8', newline='')

    print(f'sitemap.xml: {len(included)} urls')
    for name, why in skipped:
        print(f'  skipped {name}  ({why})')


if __name__ == '__main__':
    main()
