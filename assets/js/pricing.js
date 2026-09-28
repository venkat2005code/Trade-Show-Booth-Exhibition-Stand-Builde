/* ==========================================================================
   pricing.js: demo project estimator for pricing.html
   Formula (all demo values, US dollars):
     area (sq ft) x [structure rate low..high by booth type and build approach]
     + area x [graphics + lighting + furniture add-on rates]
     + area x [installation and dismantle rate]  (custom 12-18, rental 8-12)
     x location factor  (local 1.00, domestic 1.05-1.12, international 1.18-1.35)
     x rental duration factor (+5% per day beyond 4 days)
   Results are rounded and always shown as a range. Edit the tables below to match your prices.
   ========================================================================== */
(function () {
  'use strict';

  const root = document.querySelector('[data-calc]');
  if (!root) return;

  const RATES = {
    custom: { inline: [95, 150], corner: [110, 165], peninsula: [125, 190], island: [145, 230], modular: [70, 115], double: [170, 260], pavilion: [170, 260] },
    rental: { inline: [42, 72], corner: [48, 76], peninsula: [50, 76], island: [55, 85], modular: [42, 72], double: [110, 170], pavilion: [60, 92] },
  };
  const NAMES = { inline: 'inline', corner: 'corner', peninsula: 'peninsula', island: 'island', modular: 'modular', double: 'double-decker', pavilion: 'pavilion' };
  const CONTACT_TYPE = { inline: 'inline', corner: 'corner', peninsula: 'peninsula', island: 'island', modular: 'modular', double: 'double-decker', pavilion: 'pavilion' };
  const GFX = [[0, 0], [4, 7], [9, 15]];
  const LIT = [[0, 0], [3, 6], [10, 18]];
  const FUR = [[0, 0], [3, 6], [9, 16]];
  const INST = { custom: [12, 18], rental: [8, 12] };
  const LOC = { local: [1, 1], domestic: [1.05, 1.12], intl: [1.18, 1.35] };

  const $ = (s) => root.querySelector(s);
  const out = { range: $('[data-calc-range]'), sub: $('[data-calc-sub]'), brk: $('[data-calc-break]'), cta: $('[data-calc-cta]') };
  const inputs = Array.from(root.querySelectorAll('[data-calc-input]'));
  const rentalOnly = root.querySelector('[data-rental-only]');

  const money = (n) => '$' + Math.round(n).toLocaleString('en-US');
  const round = (n) => (n < 10000 ? Math.round(n / 100) * 100 : Math.round(n / 500) * 500);
  const val = (name) => {
    const el = root.querySelector('[name="' + name + '"]');
    if (!el) return '';
    if (el.type === 'radio') { const c = root.querySelector('[name="' + name + '"]:checked'); return c ? c.value : ''; }
    if (el.type === 'checkbox') return el.checked;
    return el.value;
  };
  const clamp = (n, lo, hi) => Math.min(hi, Math.max(lo, n));

  function calc() {
    const w = clamp(parseFloat(val('w')) || 0, 5, 200);
    const dp = clamp(parseFloat(val('d')) || 0, 5, 200);
    const type = val('type');
    const mode = val('mode');
    const area = w * dp;
    const rental = mode === 'rental';
    if (rentalOnly) rentalOnly.hidden = !rental;
    const days = clamp(parseInt(val('days'), 10) || 4, 3, 14);
    const dayF = rental ? 1 + Math.max(0, days - 4) * 0.05 : 1;
    const loc = LOC[val('loc')] || LOC.local;
    const rate = RATES[mode][type];
    const g = GFX[+val('gfx')], l = LIT[+val('lit')], f = FUR[+val('fur')];
    const inst = val('inst') ? INST[mode] : [0, 0];

    const part = (r) => [area * r[0] * dayF, area * r[1] * dayF];
    const rows = [
      [rental ? 'Rental structure and design' : 'Structure and design', part(rate)],
      ['Graphics', part(g)],
      ['Lighting', part(l)],
      ['Furniture', part(f)],
      ['Installation and dismantle', part(inst)],
    ];
    const subLo = rows.reduce((a, r) => a + r[1][0], 0);
    const subHi = rows.reduce((a, r) => a + r[1][1], 0);
    const lo = round(subLo * loc[0]);
    const hi = round(subHi * loc[1]);
    const upLo = subLo * (loc[0] - 1), upHi = subHi * (loc[1] - 1);

    out.range.textContent = money(lo) + ' - ' + money(hi);
    out.sub.textContent = Math.round(area).toLocaleString('en-US') + ' sq ft ' + (rental ? 'rental' : 'custom') + ' ' + NAMES[type] + ' stand, about ' + money(lo / area) + ' - ' + money(hi / area) + ' per sq ft.';
    out.brk.innerHTML = rows.filter((r) => r[1][1] > 0).map((r) => '<div><dt>' + r[0] + '</dt><dd>' + money(round(r[1][0])) + ' - ' + money(round(r[1][1])) + '</dd></div>').join('')
      + (upHi > 0 ? '<div><dt>Location factor</dt><dd>+' + money(round(upLo)) + ' - ' + money(round(upHi)) + '</dd></div>' : '');

    const size = Math.round(w) + 'x' + Math.round(dp);
    const msg = 'Estimate from the website: ' + Math.round(area) + ' sq ft ' + (rental ? 'rental' : 'custom') + ' ' + NAMES[type] + ', range ' + money(lo) + ' - ' + money(hi) + '.';
    out.cta.setAttribute('href', 'contact.html?type=' + CONTACT_TYPE[type] + '&size=' + size + '&mode=' + (rental ? 'rental' : 'custom') + '&msg=' + encodeURIComponent(msg) + '#enquiry');
  }

  inputs.forEach((el) => { el.addEventListener('input', calc); el.addEventListener('change', calc); });
  root.querySelector('form').addEventListener('submit', (e) => e.preventDefault());
  calc();
})();
