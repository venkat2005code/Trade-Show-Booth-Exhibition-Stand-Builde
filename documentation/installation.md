# Installation

## Requirements

- A modern browser (Chrome, Edge, Firefox, Safari: current and the two previous versions)
- A text editor
- An internet connection **only** to load the two Google Fonts (Archivo, Inter). Without it the site falls back to system fonts and remains fully usable.

There is no build step, no package manager and no server-side code.

## Run it

1. Unzip the package.
2. Open `pages/index.html` (double-click or drag it into a browser window).

All links between pages are relative, so the site works from `file://`.

### Recommended: use a local server for testing

A few browser features behave differently on `file://` (for example `history.replaceState` when a filter changes
the URL, clipboard access for "Copy link", and the Web Share API). Any static server works:

```bash
python3 -m http.server 8000
```

then open `http://localhost:8000/pages/index.html`.

## Folder structure

```
trade-show-booth-builder/
├── assets/
│   ├── css/
│   │   ├── style.css        design tokens, base, components, page blocks
│   │   ├── dark-mode.css    dark theme tokens and overrides
│   │   └── rtl.css          right-to-left overrides
│   ├── js/
│   │   ├── main.js          theme, RTL, header, drawer, modals, toasts, reveal, share...
│   │   ├── forms.js         form validation, password tools, contact prefill
│   │   ├── portfolio.js     portfolio filtering, quick view, project detail hydration
│   │   ├── pricing.js       cost estimator
│   │   ├── blog.js          blog filtering, load more, article hydration, table of contents
│   │   ├── upload.js        drag-and-drop upload UI
│   │   ├── dashboard.js     admin dashboard views and SVG charts
│   │   └── plugins/
│   │       ├── projects-data.js   demo project data (12 projects)
│   │       ├── posts-data.js      demo blog data (8 posts)
│   │       ├── services-data.js   demo service data (8 services)
│   │       ├── service-details.js fills service-details.html from ?service=
│   │       ├── lightbox.js        gallery lightbox
│   │       └── countdown.js       launch countdown
│   ├── images/              56 original SVG illustrations and brand marks
│   └── fonts/               (empty: see fonts/README.md to self-host)
├── pages/                   the 18 HTML pages
├── documentation/
├── tools/generator/         optional Python scripts the pages and artwork were generated from
├── robots.txt
├── sitemap.xml
├── README.md
└── LICENSE
```

## Script loading

Every page loads `main.js` and `forms.js` (the footer newsletter uses the form engine). Page-specific scripts are
listed at the end of each page and are loaded with `defer`, so order matters: data files first, then the script that uses them.

| Page | Extra scripts |
|---|---|
| index | `plugins/projects-data.js`, `portfolio.js` |
| portfolio | `plugins/projects-data.js`, `portfolio.js` |
| portfolio-details | `plugins/projects-data.js`, `plugins/lightbox.js`, `portfolio.js` |
| service-details | `plugins/services-data.js`, `plugins/service-details.js` |
| pricing | `pricing.js` |
| blog | `plugins/posts-data.js`, `blog.js` |
| blog-details | `plugins/posts-data.js`, `blog.js` |
| contact | `upload.js` |
| admin-dashboard | `dashboard.js` |
| coming-soon | `plugins/countdown.js` |

## Going live checklist

1. Replace `https://www.standform.example` with your domain in every `<link rel="canonical">`, Open Graph tag, JSON-LD block, `sitemap.xml` and `robots.txt`.
2. Replace `assets/images/og-cover.svg` with a 1200 × 630 JPG or PNG (most social networks do not render SVG previews) and update the `og:image` / `twitter:image` tags.
3. Connect the forms (see `customization.md` → Forms) and remove `data-demo`.
4. Replace demo text, clients, prices, phone, email and address.
5. Replace the demo login / register pages with a real authentication flow or remove them, and remove `pages/admin-dashboard.html` if you do not need it.
6. Optional: self-host the fonts (see `assets/fonts/README.md`) for full privacy and offline use.
7. Replace the placeholder social links in the footer (they point to each network's home page).
8. Update `robots.txt` if you keep the demo pages.
