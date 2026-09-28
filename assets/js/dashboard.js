/* ==========================================================================
   dashboard.js: demo admin dashboard (admin-dashboard.html)
   - Section switching, mobile menu, table search / status filter, reply dialog
   - Dependency-free SVG charts: line, bar, horizontal bar, donut.
     Chart data lives on each <figure data-chart="line|bar|hbar|donut" data-labels="a,b" data-series="[1,2]">.
     Marks follow the data-viz spec: 2px lines, bars <= 24px with a 4px rounded data end, 2px surface
     gaps between donut segments, hairline grid, legend for 2+ series, hover tooltip and a table view.
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const NS = 'http://www.w3.org/2000/svg';
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const fmt = (n) => Number(n).toLocaleString('en-US');

  /* ------------------------------------------------------------ views */
  const panels = $$('[data-view-panel]');
  const navBtns = $$('[data-view]');
  const title = $('[data-dash-title]');
  const side = $('#dash-side');
  const menuBtn = $('[data-dash-menu]');

  function setMenu(open) {
    if (!side || !menuBtn) return;
    side.classList.toggle('is-open', open);
    menuBtn.setAttribute('aria-expanded', String(open));
    menuBtn.setAttribute('aria-label', open ? 'Close dashboard menu' : 'Open dashboard menu');
    if (open) { const f = $('.dash__nav', side); if (f) f.focus(); }
  }
  if (menuBtn) menuBtn.addEventListener('click', () => setMenu(!side.classList.contains('is-open')));
  d.addEventListener('keydown', (e) => { if (e.key === 'Escape' && side && side.classList.contains('is-open')) { setMenu(false); menuBtn.focus(); } });
  d.addEventListener('click', (e) => {
    if (side && side.classList.contains('is-open') && !e.target.closest('#dash-side') && !e.target.closest('[data-dash-menu]')) setMenu(false);
  });

  function show(view, focus) {
    panels.forEach((p) => { p.hidden = p.dataset.viewPanel !== view; p.classList.toggle('is-active', p.dataset.viewPanel === view); });
    navBtns.forEach((b) => {
      const on = b.dataset.view === view;
      b.classList.toggle('is-active', on);
      if (on) { b.setAttribute('aria-current', 'page'); if (title) title.textContent = $('span', b).textContent; } else b.removeAttribute('aria-current');
    });
    setMenu(false);
    renderVisible();
    const q = $('[data-dash-search]');
    if (q && q.value) filterRows();
    if (focus) { const m = $('#main'); if (m) m.focus({ preventScroll: true }); window.scrollTo({ top: 0 }); }
    try { history.replaceState(null, '', '#' + view); } catch (e) { /* file:// */ }
  }
  navBtns.forEach((b) => b.addEventListener('click', () => show(b.dataset.view, true)));

  /* ------------------------------------------------------------ search + status filter */
  const search = $('[data-dash-search]');
  const status = $('[data-filter-status]');
  function filterRows() {
    const panel = panels.find((p) => !p.hidden);
    if (!panel) return;
    const q = search ? search.value.toLowerCase().trim() : '';
    const st = status ? status.value.toLowerCase() : '';
    $$('tbody tr, .msg, .switch-list li', panel).forEach((row) => {
      const text = row.textContent.toLowerCase();
      const okStatus = !st || !row.closest('[data-view-panel="enquiries"]') || text.indexOf(st) > -1;
      row.hidden = !(okStatus && (!q || text.indexOf(q) > -1));
    });
  }
  if (search) search.addEventListener('input', filterRows);
  if (status) status.addEventListener('change', filterRows);

  /* ------------------------------------------------------------ reply dialog */
  d.addEventListener('click', (e) => {
    const b = e.target.closest('[data-reply]');
    if (!b) return;
    const dlg = $('#reply-modal');
    $('[data-reply-name]', dlg).textContent = b.dataset.reply;
    dlg._opener = b;
    dlg.showModal();
  });

  /* ------------------------------------------------------------ chart helpers */
  const tip = d.createElement('div');
  tip.className = 'chart__tip';
  tip.setAttribute('aria-hidden', 'true');
  d.body.appendChild(tip);
  function showTip(html, x, y) {
    tip.innerHTML = html;
    tip.classList.add('is-on');
    const w = tip.offsetWidth;
    const h = tip.offsetHeight;
    tip.style.left = Math.max(8, Math.min(window.innerWidth - w - 8, x - w / 2)) + 'px';
    tip.style.top = Math.max(8, y - h - 12) + 'px';
  }
  const hideTip = () => tip.classList.remove('is-on');

  function svg(w, h, label) {
    const s = d.createElementNS(NS, 'svg');
    s.setAttribute('viewBox', '0 0 ' + w + ' ' + h);
    s.setAttribute('width', w);
    s.setAttribute('height', h);
    s.setAttribute('role', 'img');
    s.setAttribute('aria-label', label);
    return s;
  }
  function el(tag, attrs, parent) {
    const n = d.createElementNS(NS, tag);
    Object.keys(attrs || {}).forEach((k) => { if (k === 'text') n.textContent = attrs[k]; else n.setAttribute(k, attrs[k]); });
    if (parent) parent.appendChild(n);
    return n;
  }
  // Round-number axis: step of 1 / 2 / 5 x 10^n, about five gridlines
  function niceScale(v) {
    const raw = Math.max(v, 1) / 5;
    const p = Math.pow(10, Math.floor(Math.log10(raw)));
    const n = raw / p;
    const step = (n <= 1 ? 1 : n <= 2 ? 2 : n <= 5 ? 5 : 10) * p;
    const max = Math.ceil(v / step) * step;
    const list = [];
    for (let t = 0; t <= max + step / 1000; t += step) list.push(t);
    return { max, ticks: list };
  }

  function yAxis(s, m, iw, ih, sc) {
    const max = sc.max;
    sc.ticks.forEach((t) => {
      const y = m.t + ih * (1 - t / max);
      el('line', { x1: m.l, x2: m.l + iw, y1: y, y2: y, class: t === 0 ? 'chart__axis' : 'chart__grid' }, s);
      el('text', { x: m.l - 8, y: y + 4, 'text-anchor': 'end', text: fmt(t) }, s);
    });
  }

  /* ------------------------------------------------------------ chart types */
  function line(canvas, cfg) {
    const w = canvas.clientWidth;
    const h = Math.round(Math.min(280, Math.max(190, w * 0.4)));
    const m = { t: 18, r: 40, b: 26, l: 44 };
    const iw = w - m.l - m.r;
    const ih = h - m.t - m.b;
    const n = cfg.data.length;
    const sc = niceScale(Math.max.apply(null, cfg.data));
    const max = sc.max;
    const x = (i) => m.l + iw * (i / (n - 1));
    const y = (v) => m.t + ih * (1 - v / max);
    const s = svg(w, h, cfg.label);
    yAxis(s, m, iw, ih, sc);
    const step = Math.ceil((34 * n) / iw);
    cfg.labels.forEach((l, i) => { if (i % step === 0 || i === n - 1) el('text', { x: x(i), y: h - 6, 'text-anchor': 'middle', text: l }, s); });
    const pts = cfg.data.map((v, i) => x(i).toFixed(1) + ',' + y(v).toFixed(1));
    el('path', { d: 'M' + pts.join(' L') + ' L' + x(n - 1).toFixed(1) + ',' + y(0) + ' L' + x(0).toFixed(1) + ',' + y(0) + ' Z', class: 'chart__area' }, s);
    el('path', { d: 'M' + pts.join(' L'), class: 'chart__line' }, s);
    const cross = el('line', { y1: m.t, y2: m.t + ih, class: 'chart__cross', opacity: 0 }, s);
    const hover = el('circle', { r: 5, class: 'chart__dot', opacity: 0 }, s);
    el('circle', { cx: x(n - 1), cy: y(cfg.data[n - 1]), r: 5, class: 'chart__dot' }, s);
    el('text', { x: x(n - 1) + 10, y: y(cfg.data[n - 1]) + 4, class: 'chart__val', text: fmt(cfg.data[n - 1]) }, s);
    const bw = iw / (n - 1);
    cfg.data.forEach((v, i) => {
      const hit = el('rect', { x: x(i) - bw / 2, y: m.t, width: bw, height: ih, class: 'chart__hit' }, s);
      const on = () => {
        cross.setAttribute('x1', x(i)); cross.setAttribute('x2', x(i)); cross.setAttribute('opacity', 1);
        hover.setAttribute('cx', x(i)); hover.setAttribute('cy', y(v)); hover.setAttribute('opacity', 1);
        const r = canvas.getBoundingClientRect();
        showTip('<strong>' + esc(cfg.labels[i]) + '</strong>: ' + fmt(v) + ' ' + esc(cfg.unit), r.left + x(i), r.top + y(v));
      };
      hit.addEventListener('pointerenter', on);
      hit.addEventListener('pointermove', on);
      hit.addEventListener('pointerleave', () => { cross.setAttribute('opacity', 0); hover.setAttribute('opacity', 0); hideTip(); });
    });
    canvas.replaceChildren(s);
  }

  function columnPath(x, y, w, base, r) {
    r = Math.min(r, w / 2, Math.max(0, base - y));
    return 'M' + x + ',' + base + ' L' + x + ',' + (y + r) + ' Q' + x + ',' + y + ' ' + (x + r) + ',' + y + ' L' + (x + w - r) + ',' + y + ' Q' + (x + w) + ',' + y + ' ' + (x + w) + ',' + (y + r) + ' L' + (x + w) + ',' + base + ' Z';
  }

  function bar(canvas, cfg) {
    const w = canvas.clientWidth;
    const h = Math.round(Math.min(280, Math.max(200, w * 0.42)));
    const m = { t: 24, r: 8, b: 40, l: 44 };
    const iw = w - m.l - m.r;
    const ih = h - m.t - m.b;
    const n = cfg.data.length;
    const sc = niceScale(Math.max.apply(null, cfg.data));
    const max = sc.max;
    const band = iw / n;
    const bw = Math.min(24, band * 0.6);
    const s = svg(w, h, cfg.label);
    yAxis(s, m, iw, ih, sc);
    const small = band < 62;
    cfg.data.forEach((v, i) => {
      const cx = m.l + band * i + band / 2;
      const top = m.t + ih * (1 - v / max);
      const path = el('path', { d: columnPath(cx - bw / 2, top, bw, m.t + ih, 4), class: 'chart__bar' }, s);
      el('text', { x: cx, y: top - 6, 'text-anchor': 'middle', class: 'chart__val', text: fmt(v) }, s);
      const words = cfg.labels[i].split('-');
      const lbl = small && cfg.labels[i].length > 6 ? cfg.labels[i].slice(0, 5) + '.' : cfg.labels[i];
      el('text', { x: cx, y: h - 18, 'text-anchor': 'middle', text: lbl }, s);
      void words;
      const hit = el('rect', { x: cx - band / 2, y: m.t, width: band, height: ih + 24, class: 'chart__hit' }, s);
      const on = () => { const r = canvas.getBoundingClientRect(); path.classList.add('is-hover'); showTip('<strong>' + esc(cfg.labels[i]) + '</strong>: ' + fmt(v) + ' ' + esc(cfg.unit), r.left + cx, r.top + top); };
      hit.addEventListener('pointerenter', on);
      hit.addEventListener('pointermove', on);
      hit.addEventListener('pointerleave', () => { path.classList.remove('is-hover'); hideTip(); });
    });
    canvas.replaceChildren(s);
  }

  function hbar(canvas, cfg) {
    const w = canvas.clientWidth;
    const rowH = 36;
    const h = cfg.data.length * rowH + 8;
    const labelW = Math.min(150, Math.max(84, Math.round(w * 0.34)));
    const valueW = 52;
    const iw = w - labelW - valueW;
    const max = Math.max.apply(null, cfg.data);
    const s = svg(w, h, cfg.label);
    el('line', { x1: labelW, x2: labelW, y1: 0, y2: h - 4, class: 'chart__axis' }, s);
    cfg.data.forEach((v, i) => {
      const cy = 4 + i * rowH + rowH / 2;
      const len = Math.max(4, (v / max) * iw);
      el('text', { x: labelW - 10, y: cy + 4, 'text-anchor': 'end', text: cfg.labels[i] }, s);
      const r = Math.min(4, len);
      const path = el('path', { d: 'M' + labelW + ',' + (cy - 10) + ' L' + (labelW + len - r) + ',' + (cy - 10) + ' Q' + (labelW + len) + ',' + (cy - 10) + ' ' + (labelW + len) + ',' + (cy - 10 + r) + ' L' + (labelW + len) + ',' + (cy + 10 - r) + ' Q' + (labelW + len) + ',' + (cy + 10) + ' ' + (labelW + len - r) + ',' + (cy + 10) + ' L' + labelW + ',' + (cy + 10) + ' Z', class: 'chart__bar' }, s);
      el('text', { x: labelW + len + 8, y: cy + 4, class: 'chart__val', text: fmt(v) }, s);
      const hit = el('rect', { x: 0, y: cy - rowH / 2, width: w, height: rowH, class: 'chart__hit' }, s);
      const on = () => { const rc = canvas.getBoundingClientRect(); path.classList.add('is-hover'); showTip('<strong>' + esc(cfg.labels[i]) + '</strong>: ' + fmt(v) + (cfg.unit ? ' ' + esc(cfg.unit) : ''), rc.left + labelW + len, rc.top + cy - 10); };
      hit.addEventListener('pointerenter', on);
      hit.addEventListener('pointermove', on);
      hit.addEventListener('pointerleave', () => { path.classList.remove('is-hover'); hideTip(); });
    });
    canvas.replaceChildren(s);
  }

  function donut(canvas, cfg) {
    const w = canvas.clientWidth;
    const size = Math.min(w, 220);
    const r = size / 2 - 16;
    const c = 2 * Math.PI * r;
    const total = cfg.data.reduce((a, b) => a + b, 0);
    const s = svg(size, size, cfg.label);
    s.classList.add('chart__donut');
    let offset = 0;
    cfg.data.forEach((v, i) => {
      const len = (v / total) * c;
      const seg = el('circle', { cx: size / 2, cy: size / 2, r, fill: 'none', 'stroke-width': 24, 'stroke-dasharray': Math.max(0, len - 2) + ' ' + (c - Math.max(0, len - 2)), 'stroke-dashoffset': -offset, transform: 'rotate(-90 ' + size / 2 + ' ' + size / 2 + ')', class: 'chart__seg s' + (i + 1) }, s);
      offset += len;
      const on = (e) => { seg.classList.add('is-hover'); showTip('<strong>' + esc(cfg.labels[i]) + '</strong>: ' + Math.round((v / total) * 100) + '%', e.clientX, e.clientY); };
      seg.addEventListener('pointerenter', on);
      seg.addEventListener('pointermove', on);
      seg.addEventListener('pointerleave', () => { seg.classList.remove('is-hover'); hideTip(); });
    });
    const top = cfg.data.indexOf(Math.max.apply(null, cfg.data));
    el('text', { x: size / 2, y: size / 2 + 4, 'text-anchor': 'middle', class: 'chart__val chart__center', text: Math.round((cfg.data[top] / total) * 100) + '%' }, s);
    el('text', { x: size / 2, y: size / 2 + 22, 'text-anchor': 'middle', text: cfg.labels[top] }, s);
    const wrap = d.createElement('div');
    wrap.className = 'chart__donutwrap';
    wrap.appendChild(s);
    const ul = d.createElement('ul');
    ul.className = 'chart__legend';
    ul.innerHTML = cfg.labels.map((l, i) => '<li><i class="s' + (i + 1) + '"></i>' + esc(l) + ' <strong>' + Math.round((cfg.data[i] / total) * 100) + '%</strong></li>').join('');
    wrap.appendChild(ul);
    canvas.replaceChildren(wrap);
  }

  const TYPES = { line, bar, hbar, donut };

  /* ------------------------------------------------------------ mount */
  const figs = $$('[data-chart]');
  const cfgOf = (fig) => ({
    labels: fig.dataset.labels.split(','),
    data: JSON.parse(fig.dataset.series),
    unit: fig.dataset.unit || '',
    label: ($('h2', fig).textContent + ': ' + fig.dataset.labels.split(',').map((l, i) => l + ' ' + JSON.parse(fig.dataset.series)[i]).join(', ')),
  });

  figs.forEach((fig) => {
    const cfg = cfgOf(fig);
    const canvas = $('.chart__canvas', fig);
    // table view (accessible alternative to the plot)
    const tbl = d.createElement('div');
    tbl.className = 'chart__tablewrap table-wrap';
    tbl.hidden = true;
    tbl.innerHTML = '<table class="table"><caption class="sr-only">' + esc($('h2', fig).textContent) + ' data</caption><thead><tr><th scope="col">Item</th><th scope="col">Value</th></tr></thead><tbody>'
      + cfg.labels.map((l, i) => '<tr><th scope="row">' + esc(l) + '</th><td>' + fmt(cfg.data[i]) + (cfg.unit === '%' ? '%' : '') + '</td></tr>').join('') + '</tbody></table>';
    fig.appendChild(tbl);
    const btn = d.createElement('button');
    btn.type = 'button';
    btn.className = 'btn btn--outline btn--sm chart__toggle';
    btn.setAttribute('aria-pressed', 'false');
    btn.innerHTML = '<span>Table view</span>';
    $('figcaption', fig).appendChild(btn);
    btn.addEventListener('click', () => {
      const on = btn.getAttribute('aria-pressed') !== 'true';
      btn.setAttribute('aria-pressed', String(on));
      $('span', btn).textContent = on ? 'Chart view' : 'Table view';
      canvas.hidden = on;
      tbl.hidden = !on;
      if (!on) render(fig);
    });
  });

  function render(fig) {
    const canvas = $('.chart__canvas', fig);
    if (canvas.hidden || !canvas.clientWidth) return;
    TYPES[fig.dataset.chart](canvas, cfgOf(fig));
  }
  function renderVisible() { figs.forEach((f) => { if (f.offsetParent !== null) render(f); }); }

  if ('ResizeObserver' in window) {
    const ro = new ResizeObserver((entries) => entries.forEach((en) => { const f = en.target.closest('[data-chart]'); if (f && en.contentRect.width) render(f); }));
    figs.forEach((f) => ro.observe($('.chart__canvas', f)));
  } else {
    window.addEventListener('resize', renderVisible);
  }

  const start = (location.hash || '').slice(1);
  show(navBtns.some((b) => b.dataset.view === start) ? start : 'overview', false);
})();
