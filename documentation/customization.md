# Customization

## Colours

All colours are CSS custom properties at the top of `assets/css/style.css` (`:root`).

| Token | Light | Purpose |
|---|---|---|
| `--color-primary` | `#0e1013` | Ink / charcoal |
| `--color-secondary` | `#2b59ff` | Blueprint blue (focus ring, info) |
| `--color-accent` | `#ff5a1f` | Signal orange: buttons, highlights |
| `--color-accent-text` | `#c2410c` | Accent used as **text** on light backgrounds (passes 4.5:1) |
| `--color-background` / `--color-surface` / `--color-surface-2` | white / white / `#f4f3ef` | Page and card backgrounds |
| `--color-text` / `--color-muted` | `#0e1013` / `#575d68` | Text |
| `--color-border` | `#dcdad3` | Hairlines |
| `--color-dark-bg` / `--color-dark-2` / `--color-dark-3` | `#0e1013` / `#171a20` / `#1f232b` | Sections that are dark in both themes (`.on-dark`) |

To rebrand, change `--color-accent`, then re-check text contrast: `--color-accent-text` must reach 4.5:1 on white and on `--color-surface-2`,
and `--color-on-accent` must reach 4.5:1 on the accent (buttons).

**Dark theme:** `assets/css/dark-mode.css` redefines the tokens under `:root[data-theme="dark"]`, and again under
`@media (prefers-color-scheme: dark)` for visitors without JavaScript. Keep both blocks in sync.

**`.on-dark`** is a helper class that switches the local tokens to a dark palette regardless of theme. It is used for the hero, footer and
CTA-style sections. Add it to any section you want dark in both modes.

## Typography

Two families, loaded from Google Fonts in each page `<head>`:

- Headings: **Archivo** (500 to 900)
- Body: **Inter** (400 to 700)

Change them by editing `--font-display` and `--font-body` in `:root` and the `<link>` in the page heads (search and replace across `pages/`).
To self-host the fonts see `assets/fonts/README.md`.

Fluid sizes use `clamp()` (`--fs-h1`, `--fs-h2`, `--fs-display`). Adjust the min / preferred / max values there.

## Spacing

A 4 px scale: `--sp-1` (4 px), `--sp-2` (8), `--sp-3` (12), `--sp-4` (16), `--sp-5` (20), `--sp-6` (24), `--sp-8` (32), `--sp-10` (40), `--sp-12` (48),
`--sp-16` (64), `--sp-20` (80), `--sp-24` (96), `--sp-30` (120). Use these tokens in new CSS instead of arbitrary values.

## Breakpoints

Mobile first. Media queries use `min-width`: **640px** (tablet), **1024px** (desktop), **1280px** (large desktop).
The desktop navigation appears at **1180px** so seven links plus the CTA never crowd the header; below that the drawer is used.

## Images

Every image is an SVG in `assets/images/`:

| Files | Used for | Size |
|---|---|---|
| `project-01.svg` to `project-12.svg` | Portfolio renders | 800 × 600 |
| `plan-*.svg` | Booth-type floor plans | 600 × 450 |
| `service-01.svg` to `service-08.svg` | Service visuals | 640 × 480 |
| `process-01.svg` to `process-10.svg` | Process stages | 400 × 300 |
| `blog-01.svg` to `blog-08.svg` | Blog covers | 800 × 500 |
| `hero-booth.svg`, `case-study-hero.svg` | Home 1 / Home 2 heroes | 1200 × 900, 1600 × 900 |
| `logo.svg`, `logo-light.svg`, `logo-mark.svg`, `favicon.svg` | Brand | |
| `og-cover.svg`, `map.svg`, `pattern-*.svg` | Sharing, contact map, decoration | |

Replace an image by dropping in a file with the same name, or update the `src`. Photography works too: keep the same aspect ratio,
export WebP or AVIF, add `srcset` / `sizes` for responsive delivery, and keep the `width` and `height` attributes to avoid layout shift.

## Logo

The header and footer logo is the inline `<symbol id="i-mark">` in the SVG sprite at the top of each page plus the text `STANDFORM`.
Search and replace `STANDFORM` and the symbol in `pages/*.html` (and `assets/images/logo*.svg` for stand-alone use).

## Content

- **Page copy:** edit the HTML in `pages/`.
- **Portfolio detail pages** (`portfolio-details.html?project=...`): edit `assets/js/plugins/projects-data.js`. The cards on `portfolio.html` and the home page are static HTML: keep card and data in sync (`data-slug` must match `slug`).
- **Blog articles:** `assets/js/plugins/posts-data.js` for the shortened articles; the featured article is full static HTML in `pages/blog-details.html`.
- **Service pages:** `assets/js/plugins/services-data.js`.
- **Add a project:** add an object to `SF_PROJECTS`, copy a `.pcard` in `portfolio.html`, add an image `project-13.svg`.

## Navigation

The header nav is repeated in every page (`<nav class="nav" aria-label="Primary">`) and again in the drawer (`#mobile-drawer`). Search and replace to add an item.
Sub-menus use `<li class="nav__item has-sub">` with a `nav__sub-toggle` button. Keep the `aria-current="page"` attribute on the current page link.

## Forms

Every form with `data-validate` is handled by `assets/js/forms.js`.

```html
<form data-validate data-endpoint="https://formspree.io/f/your-form-id" data-demo novalidate> ... </form>
```

- **Demo mode** (default): `data-demo` is present, or the endpoint contains `your-form-id`. The form validates, shows the loading state and a success message, but **sends nothing**.
- **Go live:** remove `data-demo` and set `data-endpoint` to your Formspree, Netlify Forms or custom API URL. The form is posted as `FormData`; a non-2xx response shows the error state.
- **Validation:** `required`, `type="email"`, `minlength`, `pattern`, `data-match="other-field-id"`, date fields must be today or later. Custom messages: `data-msg-required`, `data-msg-type`, `data-msg-minlength`, `data-msg-pattern`, `data-msg-match`.
- **Redirect after success:** `data-redirect="page.html"` (used by the demo login).
- **Close a dialog after success:** `data-close-on-success`.
- **Contact prefill:** `contact.html?type=island&size=20x20&mode=rental&msg=Hello` fills the form. The estimator uses this.

### File upload

```html
<div class="dropzone" data-upload data-max-files="5" data-max-mb="20" data-accept="pdf,jpg,jpeg,png,svg,ai,eps,psd"> ... </div>
```

The upload UI is a front-end demo: files stay in the browser. Files are attached to the form's `<input type="file">`, so they are included in the
`FormData` posted to your endpoint if it accepts uploads.

## Estimator

`assets/js/pricing.js` has the formula documented at the top and editable tables: `RATES` (dollars per sq ft by booth type and build approach), `GFX`, `LIT`,
`FUR`, `INST`, `LOC`. The range shown is low to high; results are rounded. Keep the price tables in `pricing.html` and the blog article consistent with your rates.

## Dark mode

- Detection order: saved choice (`localStorage` key `sf-theme`), then the system preference.
- Toggle: buttons with `data-theme-toggle` (header, drawer, coming-soon, dashboard).
- A tiny inline script in each `<head>` applies the theme before first paint to avoid a flash.

## RTL

- Layout uses CSS logical properties (`margin-inline`, `padding-inline`, `inset-inline`, `text-align: start`).
- `assets/css/rtl.css` handles arrows, animations, translate transforms, background positions and fonts.
- **Test it:** click "Test RTL" in the footer or "RTL" in the mobile menu, or add `?dir=rtl` to any URL. The choice is saved in `localStorage` (`sf-dir`).
- **Ship it:** set `<html lang="ar" dir="rtl">` on translated pages. Directional icons carry the `icon--flip` class; images are intentionally not mirrored.

## Adding a page

1. Duplicate an existing page with a similar layout.
2. Change `<title>`, description, canonical, Open Graph / Twitter tags and JSON-LD.
3. Keep one `<h1>`, the skip link, `<main id="main" tabindex="-1">` and the script tags at the end.
4. Add the page to `sitemap.xml` and to the navigation or footer.

## Reduced motion

`@media (prefers-reduced-motion: reduce)` disables transitions and animations, shows revealed content immediately and stops the ticker.
JavaScript also checks `matchMedia` before animating counters and smooth-scrolling.

## Integration points

Every third-party integration is placeholder-ready. Search the code for `TODO:` to find each hook.

| Integration | Where | What to change |
|---|---|---|
| Forms | `assets/js/forms.js` (`data-endpoint`, `data-demo`) | Remove `data-demo` and set `data-endpoint` to your Formspree, Netlify or API URL. |
| Newsletter | Footer `form.newsletter` | Set `data-endpoint` to your Mailchimp or ConvertKit URL — see the header of `forms.js`. |
| Google Maps | `pages/contact.html` | Keyless embed by default; replace `YOUR_GOOGLE_MAPS_API_KEY` for the Maps Embed API. |
| Calendar / booking | Home 2 enquiry → `a[data-booking-link]` (generator: `tools/generator/pages_a.py`) | Set `data-booking-url` and `href` to your Calendly, Cal.com or Google appointment page, then rebuild. |
| Payments | `pages/pricing.html` → `.payment-note` (generator: `pages_b.py`) | Add a Stripe Payment Link or PayPal button, then rebuild. |
