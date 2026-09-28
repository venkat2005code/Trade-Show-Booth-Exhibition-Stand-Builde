# Self-hosting the fonts (optional)

The pages load **Archivo** and **Inter** from Google Fonts. To self-host them for privacy, offline use or stricter performance budgets:

1. Download the font files (variable or static) from Google Fonts or the projects' GitHub repositories. Both are licensed under the SIL Open Font License 1.1.
2. Convert to `.woff2` and place the files in this folder, for example `archivo-var.woff2` and `inter-var.woff2`.
3. Add to the top of `assets/css/style.css`:

```css
@font-face {
  font-family: "Archivo";
  src: url("../fonts/archivo-var.woff2") format("woff2");
  font-weight: 500 900;
  font-display: swap;
}
@font-face {
  font-family: "Inter";
  src: url("../fonts/inter-var.woff2") format("woff2");
  font-weight: 400 700;
  font-display: swap;
}
```

4. Remove the two `preconnect` links and the Google Fonts stylesheet `<link>` from the `<head>` of every page.
5. Preload the two files in each page head for the best LCP:

```html
<link rel="preload" href="../assets/fonts/archivo-var.woff2" as="font" type="font/woff2" crossorigin>
```
