# Changelog


## 2.2.0 — 2026-09-28

Home menu, requirements review and integration points.

- Home 2: the discovery-call offer moved into the enquiry section (with a calendar integration point) and the duplicate closing band was removed.
- Loading state: “Load more articles” shows skeleton cards while the next batch loads.
- Blog: the featured article is skipped in the grid's “All” view; Blog, Process and Services page heroes now use photos that are not repeated further down the page.
- Inner-page CTAs no longer open with “Ready to…?” (Services and FAQ now lead with the benefit).
- Mailchimp / ConvertKit notes in `forms.js`, a Stripe / PayPal payment note on the pricing page, and an *Integration points* table in the customization guide.
- Meta descriptions on five pages rewritten to 150–160 characters.

## 2.1.0 — 2026-09-28

Navigation, direction toggle, imagery and CTA update.

- Direction control is now a single **LTR** toggle button (header, mobile drawer, dashboard and Coming Soon): it shows the current direction, switches to RTL on click (label changes to “RTL”), and the choice persists across pages. The two-button LTR | RTL switch was removed. Generator (`tools/generator`) updated and pages rebuilt.

## 2.0.0 — 2026-09-27

Design, imagery and UX revision.

- Replaced the flat service, process and blog scenes with 27 photographs (WebP): a real show-floor stand as the Home 1 hero, workshop, installation, graphics, lighting, logistics and team photos for the eight services and ten process stages, and eight blog covers. Portfolio renders and floor plans stay as isometric SVG — they are design renders of fictional client work, not photos of real brands.
- New logomark, favicon and lockups: an isometric open-sided stand (floor, back wall, side wall, accent header fascia), replacing the generic square mark.
- Visible LTR | RTL switch in the desktop header, the drawer, Coming Soon and the dashboard (the old drawer/footer toggles still work).
- Contact: the stylised SVG map is now an interactive Google Maps embed with a documented Maps Embed API option (`YOUR_GOOGLE_MAPS_API_KEY`).
- SEO: raster social image (`og-cover.jpg`) on every page, hero preload points at the WebP photo, over-length titles shortened, Organization JSON-LD on 404/login/register, sitemap lastmod refreshed.
- Header CTA no longer wraps and the header no longer overflows at 1180–1300 px; phone/email links isolated as LTR in RTL.
- Generator: `layout.PHOTO` maps image names to photos (used by `img()`, the JS data files and the preload), so `python3 build.py` reproduces the shipped site. `build_assets.py` draws the new logo.

## 1.0.0: 2026-09-21

Initial release.

- 18 pages: two homepages, about, services, service details, booth types, portfolio, portfolio details, process, pricing, blog, blog details, contact, login, register, admin dashboard demo, 404, coming soon.
- 56 original SVG illustrations and brand marks.
- Light and dark themes with system detection and persistence.
- RTL support (`rtl.css`) with an in-page test switch.
- Portfolio filtering, search and deep links; project, service and article detail hydration from query strings.
- Project cost estimator with editable formula.
- Accessible form validation with loading, success and error states; drag-and-drop upload UI.
- Blog search, category filter, load more, table of contents with scroll-spy.
- Dashboard demo with dependency-free SVG charts and a table view for each chart.
- SEO: metadata on every page, JSON-LD, `robots.txt`, `sitemap.xml`.
- Documentation and README.
