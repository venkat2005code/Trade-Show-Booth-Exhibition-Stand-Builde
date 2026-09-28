# Page structure

Every public page shares the same shell: skip link, SVG icon sprite, sticky header (`[data-header]`), mobile drawer, `<main id="main">`, footer, back-to-top
button and toast region. Sections use these classes: `.section` (default rhythm), `.section--alt` (grey band), `.on-dark` (dark band), `.cta-band` (orange call to action).

## Public pages

### `index.html`: Home 1 (studio layout)
UNDERSTAND → EXPLORE → TRUST → DECIDE → ACT.
1. **Hero** (dark, transparent header): headline, dual CTAs, stat row, isometric booth render with spec tags, booth-type ticker.
2. **Featured portfolio**: six projects, category chips (working filters, `[data-portfolio]`), first card spans two columns.
3. **Services overview**: eight service cards.
4. **Why choose us**: eight numbered business benefits (dark).
5. **Booth design styles**: six floor-plan cards.
6. **Process preview**: five steps (Discover, Design, Build, Install, Deliver) with a link to the full process.
7. **Testimonials**: one large and two small quotes.
8. **Final CTA**: "Planning Your Next Exhibition?"

### `home-2.html`: Home 2 (architectural case-study layout)
Different composition: full-bleed project hero, fixed section rail (≥ 1280 px), sticky scroll-driven story, index-style industry list.
1. **Hero**: "Your Brand. Your Space. Your Moment." with a floating project specification sheet.
2. **Featured project** (`#featured`): sticky image stage with four story steps that change the image (`[data-story-step]`).
3. **Industries** (`#industries`): seven index rows linking to `portfolio.html?industry=...`.
4. **Booth types** (`#booth-types`): horizontal scroll strip of eight plan cards (keyboard focusable region).
5. **Design capabilities** (`#capabilities`): six-cell specification grid.
6. **Selected work** (`#selected-work`): bento mosaic of six projects.
7. **Process** (`#process`): five oversized numbered rows.
8. **Project enquiry** (`#enquiry`): compact enquiry form (demo mode).

### `about.html`
Company introduction with animated counters, mission and vision, history timeline (2011 to 2025), expertise, design philosophy, team (six people), why clients work with us, testimonials, CTA.

### `services.html`
Hero, eight numbered service rows (alternating layout) with benefits and a View Details link, "not sure where to start" links, CTA.

### `service-details.html`
`?service=<slug>` (default `custom-booth-design`). Hero, overview, what is included, benefits, deliverables, design approach (tabs), how it works, pricing table with "starting from" model, FAQ (accordion, `FAQPage` JSON-LD), related services, sticky quote card and on-page navigation.
Slugs: `custom-booth-design`, `exhibition-stand-construction`, `rental-exhibition-stands`, `booth-installation`, `booth-dismantling`, `graphic-branding-production`, `lighting-and-electrical`, `project-management`.

### `booth-types.html`
Eight booth types (`#island`, `#peninsula`, `#inline`, `#corner`, `#modular`, `#double-decker`, `#pavilion`, `#rental`), each with a floor plan, ideal use, typical layout, benefits, customisation options and CTAs, plus a responsive comparison table.
Each "See projects" button deep-links to the portfolio filter.

### `portfolio.html`
Filter bar (sticky on desktop): eight category chips, industry select, search and reset. Twelve project cards with quick-view dialogs. Result count is announced with `aria-live`.
Query parameters: `category` (`custom-booth`, `rental`, `island-booth`, `inline-booth`, `peninsula-booth`, `double-decker`, `pavilion`; plural and short forms such as `island` also work), `industry` (`technology`, `healthcare`, `automotive`, `manufacturing`, `retail`, `finance`, `food-beverage`), `q` (search text).
The URL updates as filters change.

### `portfolio-details.html`
`?project=<slug>` (default `novatech-island-booth`). Case-study layout: hero, specification strip (event, location, size, industry, type, year), design challenge and solution, materials / lighting / branding / construction / installation, gallery with lightbox, project outcome (results), related projects, CTA. `ImageObject` JSON-LD is updated for the chosen project.

### `process.html`
Ten-stage vertical timeline (Project Discovery to Dismantling) with illustrations, a 16-week timeline chart (horizontally scrollable on small screens), discovery checklist, CTA "Discuss Your Exhibition Project".

### `pricing.html`
Four project-based pricing models (rental, custom, large island, custom exhibition projects), ten cost factors, the **estimator** (`#estimator`), indicative ranges table, CTA. No Basic / Standard / Premium tiers.

### `blog.html`
Featured article, category chips, search, eight article cards with "load more" (six per step). Query: `category` (`design`, `planning`, `budget`, `trends`, `tips`), `q`.

### `blog-details.html`
`?post=<slug>` (default `how-much-does-an-exhibition-stand-cost`, full article). Header with author and date, cover, collapsible inline table of contents (mobile), article, share buttons (X, LinkedIn, Facebook, copy link, native share where supported), author card, sticky sidebar with table of contents (scroll-spy and reading progress), estimator CTA and newsletter, related articles. `Article` JSON-LD.

### `contact.html`
Contact cards (phone, email, office, hours), stylised map with an "Open in Maps" link, and the enquiry form (`#enquiry`) with all requested fields, file upload and consent. Prefill via query string (see `customization.md`).

### `login.html` / `register.html`
Demo authentication pages (`noindex`). Login validates and then redirects to the dashboard demo. Register includes a password strength meter, show / hide password and confirm-password matching. "Forgot password" opens a reset dialog.

### `404.html`
"Looks Like This Page Missed the Exhibition Floor." with Back to Home, View Portfolio and Contact Us.

### `coming-soon.html`
Minimal chrome, headline "Something Great Is Being Built.", countdown (`data-countdown` ISO date), launch notification form, social links, contact CTA.

## Demo-only page

### `admin-dashboard.html`
Not linked from the public navigation (only from the login redirect). Nine views: Overview, Project Enquiries, Portfolio Projects, Services, Blog Posts, Messages, Users, Settings, Analytics. Overview shows five KPIs, four charts (enquiries over time, projects by booth type, leads by source, project status) and three tables.
Every chart has a **Table view** toggle, a hover tooltip and an accessible label. `noindex`, blocked in `robots.txt`.

## JavaScript hooks (data attributes)

| Attribute | Behaviour |
|---|---|
| `data-theme-toggle` | Toggle light / dark |
| `data-dir-toggle` | Toggle LTR / RTL |
| `data-nav-toggle`, `data-drawer` | Mobile menu |
| `data-sub-toggle` | Desktop sub-menu button |
| `data-accordion`, `data-tabs` | Accordion, tabs |
| `data-modal-open="id"` | Opens a `<dialog id="id">` |
| `data-legal="privacy|terms|accessibility"` | Legal dialogs |
| `data-share="x|linkedin|facebook|copy|native"` | Share buttons |
| `data-count="600" data-suffix="+"` | Animated counter |
| `data-portfolio`, `data-filter`, `data-industry`, `data-search`, `data-reset`, `data-project` | Portfolio and blog filtering |
| `data-quick-view="slug"` | Project quick-view dialog |
| `data-lightbox`, `data-gallery` | Lightbox |
| `data-validate`, `data-demo`, `data-endpoint`, `data-redirect` | Forms |
| `data-upload` | Upload widget |
| `data-calc`, `data-calc-input` | Estimator |
| `data-chart`, `data-labels`, `data-series`, `data-unit` | Dashboard charts |
| `data-countdown` | Countdown target |
| `data-toast="message"` | Shows a toast on click |
