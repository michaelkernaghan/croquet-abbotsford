<!-- Guidance for AI coding agents editing the Abbotsford Croquet website -->
# Copilot instructions — croquet-abbotsford

Purpose: give an AI agent immediate, actionable knowledge to be productive editing this static website.

- **Big picture**: this is a small, static website (no build system) composed of plain HTML pages in the repo root, scoped CSS under `css/`, and a few small JS utilities in `js/`. Images and favicons live under `assets/`.

- **Key files & why they matter**:
  - `index.html` — canonical home page; contains site-wide schema/metadata and the header/nav used across pages.
  - `css/styles.css` and `css/*.css` — site styling; individual pages sometimes add page-specific css (e.g. `gallery.css`).
  - `js/main.js` — site interaction helpers. Note: it contains a special-case link check (`if (this.getAttribute('href') === 'contact')`) — watch this when changing navigation behavior.
  - `js/config.sample.js` — sample runtime configuration. For secrets/config, copy to `js/config.js` (or `config.js`) and add to `.gitignore`. The sample exposes `window.siteConfig`.
  - `assets/images/favicons/*` and `generate_favicons.sh` — favicon assets and a helper shell script (POSIX). On Windows use WSL/Git-Bash to run the script.
  - `site.webmanifest` and `robots.txt` — PWA and crawling metadata; keep them in sync with `index.html` metadata.

- **Architecture & patterns**:
  - No frontend framework — pages are independent HTML files that share a common header/nav and CSS files.
  - Navigation links are relative and hand-authored. New pages should follow existing URL conventions (e.g. `membership.html`, `contact.html`).
  - Global configuration is provided by a global `window.siteConfig` object when `js/config.js` is present.

- **Developer workflows (how to test & debug locally)**:
  - Quick local server (PowerShell): `python -m http.server 8000` run from the repo root, then open `http://localhost:8000`.
  - Alternative (Node): `npx http-server -p 8000`.
  - Edit files and refresh browser. There is no build step or bundler.
  - Run `generate_favicons.sh` only in a POSIX shell (WSL/Git-Bash/macOS). On Windows native PowerShell the script may not work.

- **Conventions & code patterns**:
  - Keep markup semantic and accessible — existing SVG logo uses `role`, `title` and `desc`; preserve these patterns when editing.
  - CSS is page-scoped by filename; prefer adding small rules to the page CSS (e.g. `gallery.css`) rather than editing `styles.css` for page-specific tweaks.
  - JS is minimal and unobtrusive. `js/main.js` attaches event listeners to `nav a` and assumes certain href formats (see above).

- **Integration points & external dependencies**:
  - Optional weather integration via `js/config.sample.js` (`weatherApiKey`) — not required for basic site operation.
  - No server-side code in this repo. Deploys are static file uploads to the host (GitHub Pages, S3, etc.).

- **Common edits & examples**:
  - Add a new page: create `newpage.html`, link it from the nav in `index.html` and add a page-specific CSS file under `css/` if needed.
  - Add runtime config: copy `js/config.sample.js` -> `js/config.js`, populate keys, and ensure `js/config.js` is gitignored.
  - Fix nav smooth scrolling: `js/main.js` prevents default only for hash links — if changing nav structure, inspect `main.js` for logic that special-cases `contact`.

- **Gotchas to watch for**:
  - Relative paths: many pages assume they are served from the site root (e.g. `/assets/...`). When testing locally with a subpath, verify asset URLs.
  - `generate_favicons.sh` is a shell script; Windows contributors will need WSL or Git-Bash to run it.
  - There are no unit tests or CI configuration in the repo; changes should be validated manually in a browser.

If anything here is unclear or you want more examples (e.g., a checklist for PR reviewers or a short QA script), tell me which parts to expand and I will iterate.
