/* service-details.js: fills service-details.html from window.SF_SERVICES using ?service=<slug>.
   Requires plugins/services-data.js (loaded first). The HTML ships with the first service so the page
   still reads correctly without JavaScript. */
(function () {
  'use strict';

  const d = document;
  const $ = (s) => d.querySelector(s);
  const $$ = (s) => Array.from(d.querySelectorAll(s));
  const DATA = window.SF_SERVICES || [];
  const IMG = '../assets/images/';
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const icon = (n) => '<svg class="icon" aria-hidden="true" focusable="false"><use href="#i-' + n + '"/></svg>';

  const slug = new URLSearchParams(window.location.search).get('service');
  const s = DATA.find((x) => x.slug === slug);
  if (!s || s.n === 1) return;

  const text = { title: s.title, tagline: s.tagline, overview: s.overview, priceLabel: s.priceLabel, priceNote: s.priceNote, num: String(s.n).padStart(2, '0') };
  $$('[data-svc]').forEach((el) => { const v = text[el.dataset.svc]; if (v !== undefined) el.textContent = v; });

  const fill = (name, item) => { const ul = $('[data-svc-list="' + name + '"]'); if (ul) ul.innerHTML = s[name].map(item).join(''); };
  fill('includes', (t) => '<li>' + icon('check') + '<span>' + esc(t) + '</span></li>');
  fill('benefits', (t) => '<li>' + icon('star') + '<h3>' + esc(t) + '</h3></li>');
  fill('deliverables', (t) => '<li>' + icon('file') + '<span>' + esc(t) + '</span></li>');
  const rows = $('[data-svc-rows]');
  if (rows) rows.innerHTML = s.priceRows.map((r) => '<tr><th scope="row">' + esc(r[0]) + '</th><td>' + esc(r[1]) + '</td></tr>').join('');

  const hero = $('.svc-hero-img');
  if (hero) { hero.src = IMG + s.img; hero.alt = s.imgAlt || s.title; }

  const related = $('[data-related]');
  if (related) {
    const pick = DATA.filter((x) => x.slug !== s.slug).sort((a, b) => Math.abs(a.n - s.n) - Math.abs(b.n - s.n)).slice(0, 3);
    related.innerHTML = pick.map((x) => '<article class="svc is-visible"><a class="svc__media" href="service-details.html?service=' + x.slug + '" tabindex="-1" aria-hidden="true"><img src="' + IMG + x.img + '" alt="' + esc(x.imgAlt || x.title) + '" width="640" height="480" loading="lazy"></a>'
      + '<div class="svc__body"><p class="svc__num">' + String(x.n).padStart(2, '0') + '</p><h3 class="svc__title">' + esc(x.title) + '</h3><p>' + esc(x.overview.split('. ')[0]) + '.</p><a class="link-arrow" href="service-details.html?service=' + x.slug + '"><span>View details</span>' + icon('arrow').replace('class="icon"', 'class="icon icon--flip"') + '<span class="sr-only"> for ' + esc(x.title) + '</span></a></div></article>').join('');
  }

  d.title = s.title + ' Service | Exhibition Stands | Standform';
  const meta = (sel, v) => { const m = $(sel); if (m) m.setAttribute('content', v); };
  const desc = s.overview.length > 158 ? s.overview.slice(0, 155) + '...' : s.overview;
  meta('meta[name="description"]', desc); meta('meta[property="og:title"]', d.title); meta('meta[name="twitter:title"]', d.title);
  meta('meta[property="og:description"]', desc); meta('meta[name="twitter:description"]', desc);
  $$('script[type="application/ld+json"]').forEach((el) => {
    try {
      const j = JSON.parse(el.textContent);
      if (j['@type'] === 'Service') { j.name = s.title; j.description = s.overview; delete j.offers; j.serviceType = 'Exhibition stand ' + s.title.toLowerCase(); el.textContent = JSON.stringify(j); }
    } catch (e) { /* keep existing structured data */ }
  });
})();
