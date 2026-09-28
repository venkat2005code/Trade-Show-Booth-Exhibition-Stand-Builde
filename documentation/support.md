# Support

## What support covers

- Questions about how the template is structured and how to use its features
- Reporting bugs in the template as delivered (unmodified files)
- Guidance on the customisation points described in `customization.md`

## What it does not cover

- Custom design or development work, or fixing changes you made to the code
- Third-party services you connect (form providers, analytics, hosting)
- Server configuration, domain setup or content writing

## Before you write

1. Read `installation.md`, `customization.md` and `page-structure.md`.
2. Test in a current browser and check the developer console for messages.
3. Try the unmodified template to see whether the issue is in your changes.

## Include in your message

- Browser and version, operating system, device
- The page URL or file name and, if relevant, the query string
- What you expected, what happened, and a screenshot or the console error text

## Common questions

**Forms do not send anything.** Forms ship in demo mode. Remove `data-demo` and set `data-endpoint` (see `customization.md`).

**Fonts look different offline.** Fonts load from Google Fonts; without a connection the system fallbacks are used. Self-host the fonts to avoid this.

**Filters do not update the address bar on `file://`.** Browsers restrict `history.replaceState` for local files. It works on any web server.

**Where do I change the estimator prices?** `assets/js/pricing.js`, the tables at the top of the file.

**How do I add a project?** Add an entry to `assets/js/plugins/projects-data.js`, copy a `.pcard` in `pages/portfolio.html` and add an image.

**Can I use my own photos?** Yes. Replace the `<img>` sources, keep the aspect ratio and the `width` / `height` attributes.
