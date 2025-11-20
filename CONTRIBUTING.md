# Contributing to Abbotsford Croquet Website

Thanks for helping improve this small static website. This document captures the repository-specific workflows and expectations.

Getting started
- Run a quick local server from the repo root to preview changes:
  - PowerShell: `python -m http.server 8000`
  - Node: `npx http-server -p 8000`
  Open `http://localhost:8000` in your browser.

Configuration and secrets
- Copy `js/config.sample.js` to `js/config.js` and populate any keys (e.g. `weatherApiKey`). Add `js/config.js` to `.gitignore`.

Code style and patterns
- This is a plain HTML/CSS/JS site (no bundler). Pages are independent HTML files that share a header/nav and CSS.
- Page-specific CSS: prefer adding small rules to the page CSS (e.g. `css/gallery.css`) rather than changing `css/styles.css` for narrow layout tweaks.
- Accessibility: preserve existing accessibility patterns (SVG `role`, `title`, `desc`, semantic headings and lists).
- JavaScript: `js/main.js` contains navigation behaviour and a special-case check for `contact` — review before changing navigation logic.

Assets
- Put images in `assets/images/` and favicons in `assets/images/favicons/`.
- To regenerate favicons, run `generate_favicons.sh` in a POSIX shell (WSL/Git-Bash/macOS). The script may not work in native PowerShell.

Adding pages
1. Create `newpage.html` in the repo root.
2. Add a page-specific CSS file under `css/` if needed.
3. Add a link in the nav inside `index.html` using the same relative URL style as existing links.

Manual QA checklist (before opening a PR)
- Start local server and verify the new/changed page loads at `http://localhost:8000/<page>`.
- Check relative asset paths (some pages assume root-prefixed paths like `/assets/...`).
- Test in at least one desktop and one mobile viewport.
- If you change metadata, update `site.webmanifest` and `robots.txt` if applicable.
- If SVGs are modified, preserve `role/title/desc` for accessibility.

Commit & PR guidance
- Keep commits small and focused (one logical change per PR).
- In the PR description, include the local preview steps and any manual checklist results.

If you'd like, I can also add a PR template or more issue templates.
