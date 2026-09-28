# Optional generator

The shipped site is plain static HTML: **you do not need anything in this folder to run or edit it.**

These Python 3 scripts (standard library only) are the source the pages and illustrations were generated from. They are useful if you want to change
something that repeats on all 18 pages (header, footer, navigation, icon sprite) or regenerate the SVG artwork.

| File | Purpose |
|---|---|
| `data.py` | Demo content: projects, services, booth types, blog posts, testimonials, FAQ |
| `layout.py` | Page shell: head/SEO, header, mobile drawer, footer, icon sprite, reusable components |
| `pages_a.py`, `pages_b.py`, `pages_c.py` | Page bodies |
| `build.py` | Writes `pages/*.html`, `assets/js/plugins/*-data.js`, `sitemap.xml`, `robots.txt` |
| `kit.py`, `scenes.py`, `build_assets.py` | Isometric SVG engine and the illustration set (`assets/images/*.svg`) |
| `audit.py` | Checks links, anchors, ids, headings, labels and CSS class coverage |

```bash
cd tools/generator
python3 build_assets.py   # regenerate SVG artwork
python3 build.py          # regenerate pages, data files, sitemap, robots
python3 audit.py          # sanity checks
```

**Warning:** `build.py` overwrites `pages/*.html` and `assets/js/plugins/*-data.js`. If you have edited those files by hand, do not run it.
CSS and the other JavaScript files are hand-written and are never touched by the generator.

## Photos

`layout.PHOTO` maps an image name (e.g. `service-03`, `process-07`, `blog-02`, `hero-booth`) to a WebP file in `assets/images/photos/` plus its alt text. `img()` and the JS data files use it automatically, so re-running `build.py` keeps the photography. Remove an entry to fall back to the generated SVG.
