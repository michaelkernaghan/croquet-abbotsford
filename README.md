# Abbotsford Croquet Club Website

Official website for the Abbotsford Croquet Club, located in Mill Lake Park, Abbotsford, BC, Canada.

**Live Site:** [abbotsfordcroquet.ca](https://abbotsfordcroquet.ca)

## About This Repository

This is a pure static website built with HTML, CSS, and vanilla JavaScript. No build process or frameworks are required - all files are served directly to visitors.

### Technology Stack
- **HTML5** - Semantic markup with accessibility features
- **CSS3** - Responsive design with flexbox layouts
- **Vanilla JavaScript** - Minimal JS for smooth navigation
- **Hosting** - Netlify (auto-deploys from main branch)

## Repository Structure

```
croquet-abbotsford/
├── *.html              # Website pages (19 pages)
├── assets/             # Images, graphics, and media files
│   ├── images/         # Photos and graphics (~33MB)
│   └── svg/            # Vector logos
├── css/                # Stylesheets
│   ├── styles.css      # Main global styles
│   └── *.css           # Page-specific styles
├── js/                 # JavaScript utilities
│   ├── main.js         # Navigation and smooth scrolling
│   └── config.js       # Runtime configuration (not in git)
├── site.webmanifest    # Progressive Web App manifest
├── robots.txt          # Search engine crawling rules
├── sitemap.xml         # SEO sitemap
└── docs/               # Development documentation and assets
```

## Website Pages

- **index.html** - Homepage
- **calendar.html** - Event calendar
- **contact.html** - Contact information
- **membership.html** - Membership details
- **gallery.html** - Photo gallery
- **lessons.html** - Croquet lessons
- **resources.html** - Learning resources
- **mallets.html** - Equipment information
- **variations.html** - Game variations
- **court-status.html** - Court availability
- **session-registration.html** - Session booking
- Tournament and event pages

## Development

### Local Development
Simply open any `.html` file in a browser. For full functionality (navigation, etc.), use a local server:

```bash
# Python 3
python -m http.server 8000

# Node.js (if you have http-server installed)
npx http-server

# PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`

### Making Changes
1. Edit HTML, CSS, or JS files directly
2. Test locally in a browser
3. Commit changes to git
4. Push to GitHub main branch
5. Netlify auto-deploys within minutes

### Configuration
If using features that require API keys (e.g., weather):
1. Copy `js/config.sample.js` to `js/config.js`
2. Add your API keys to `js/config.js`
3. Never commit `js/config.js` (it's in .gitignore)

## Deployment

**Netlify Configuration:**
- **Build Command:** None (static site)
- **Publish Directory:** `.` (repository root)
- **Production Branch:** main

Any push to the `main` branch automatically deploys to production.

## Documentation

See the [/docs](./docs) folder for:
- Build scripts and utilities
- Design assets
- Promotional materials
- Additional documentation

## Contributing

This repository is maintained by the Abbotsford Croquet Club. For questions or suggestions, please use the contact form on the website or reach out to the club directly.

## License

© 2024-2025 Abbotsford Croquet Club. All rights reserved.