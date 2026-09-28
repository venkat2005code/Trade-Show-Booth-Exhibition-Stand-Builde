# Standform: Trade Show Booth & Exhibition Stand Builder HTML Template

A bold, portfolio-driven website template for exhibition stand designers, fabricators and installers.
Built with plain HTML5, CSS3 and vanilla JavaScript (ES6+). No build step, no framework, no jQuery.

**Open `pages/index.html` in a browser and it runs.**

> Everything in this template (company, clients, projects, quotes, prices, addresses) is fictional demo content.
> The domain `standform.example` is reserved for documentation and cannot be registered.

---

## Features

- **18 pages**, two structurally different homepages, a full portfolio system and a demo admin dashboard.
- **Portfolio-first visual language**: 12 original isometric booth renders and 8 floor-plan diagrams (SVG), plus 27 royalty-free photographs (WebP) for the hero, services, process stages and blog covers — licences in `documentation/credits.md`, an AI prompt per photo slot in `documentation/image-prompts.md`.
- **Real functionality, not dead buttons**
  - Portfolio filtering, industry filter, search and deep links (`?category=island-booth`, `?category=rental`, `?industry=technology`, `?q=nova`)
  - Portfolio details, service details and blog articles hydrate from a `?project=`, `?service=` or `?post=` slug
  - Project cost estimator with a transparent, editable formula and a "quote with these details" hand-off to the enquiry form
  - Accessible form validation with loading, success and error states (demo mode by default)
  - Drag-and-drop file upload UI with type, size and count validation and per-file progress
  - Blog search, category filter and "load more"
  - Light and dark themes with system detection, manual toggle and persistence
  - RTL (Arabic / Hebrew) support with a visible LTR toggle (flips to RTL and relabels itself) in the header and drawer (persisted as `sf-dir`)
  - Dialogs (native `<dialog>`), lightbox gallery, tabs, accordions, toasts, share buttons, back-to-top, countdown
  - Admin dashboard demo with dependency-free SVG charts, table view for every chart and searchable tables
- **Accessibility target: WCAG 2.1 AA**: skip link, landmarks, one `h1` per page, labelled controls, visible focus, 44 px touch targets, reduced-motion support, keyboard-operable menus, dialogs, tabs and accordions.
- **SEO**: unique title and description per page, canonical, Open Graph, Twitter cards, JSON-LD (Organization, WebSite, LocalBusiness, BreadcrumbList, Service, FAQPage, Article, ImageObject, CollectionPage), `robots.txt`, `sitemap.xml`.
- **Performance-minded**: about 110 KB of hand-written CSS in three files (unminified), about 80 KB of unminified JavaScript in total (each page loads only its own scripts), no CSS framework, no JS libraries, SVG imagery, lazy loading, explicit image dimensions, `fetchpriority` on the hero image. Minify for production if you like; nothing requires it.

## Pages

| Page | File |
|---|---|
| Home 1: studio layout | `pages/index.html` |
| Home 2: architectural case-study layout | `pages/home-2.html` |
| About | `pages/about.html` |
| Services | `pages/services.html` |
| Service details | `pages/service-details.html` |
| Booth types | `pages/booth-types.html` |
| Portfolio gallery | `pages/portfolio.html` |
| Portfolio project details | `pages/portfolio-details.html` |
| Process | `pages/process.html` |
| Pricing and estimator | `pages/pricing.html` |
| Blog | `pages/blog.html` |
| Blog article | `pages/blog-details.html` |
| Contact / project enquiry | `pages/contact.html` |
| Login | `pages/login.html` |
| Register | `pages/register.html` |
| Admin dashboard (demo, not in public navigation) | `pages/admin-dashboard.html` |
| 404 | `pages/404.html` |
| Coming soon | `pages/coming-soon.html` |

## Technologies

HTML5 · CSS3 (custom properties, grid, logical properties, `clamp()`) · Vanilla JavaScript ES6+ · SVG · native `<dialog>`

The brief asked for Tailwind (preferred) or Bootstrap 5. This template uses **neither**: it ships a small hand-written stylesheet driven by design tokens. That keeps the project runnable offline with no CDN build step, avoids shipping an unused utility framework and keeps the page weight low. See `documentation/customization.md` for the token system.

## Installation

1. Unzip the package.
2. Open `pages/index.html` in any modern browser. That is all.
3. For local testing of query-string features under a real origin, any static server works, for example `python3 -m http.server` from the project root, then open `http://localhost:8000/pages/index.html`.

Details in `documentation/installation.md`.

## Browser support

Current and previous two versions of Chrome, Edge, Firefox and Safari (desktop and mobile). Requires support for CSS custom properties, CSS grid, logical properties, `<dialog>` and ES2017. Internet Explorer is not supported.

## Customization

- Colours, spacing and typography: `:root` tokens at the top of `assets/css/style.css`; dark theme tokens in `assets/css/dark-mode.css`.
- Content: edit the HTML in `pages/`. Demo project, blog and service data for the dynamic detail pages live in `assets/js/plugins/*-data.js`.
- Estimator formula: the `RATES` tables at the top of `assets/js/pricing.js`.
- Form endpoint: `data-endpoint` on the form (see `documentation/customization.md`).

## Credits

Fonts: Archivo and Inter (SIL Open Font License) via Google Fonts. All icons and illustrations are original to this template. No third-party JavaScript. See `documentation/credits.md`.

## Optional generator

`tools/generator/` holds the Python scripts the pages and SVG artwork were generated from. You never need them to run or edit the site; see `tools/generator/README.md`.

## License

See `LICENSE`.
