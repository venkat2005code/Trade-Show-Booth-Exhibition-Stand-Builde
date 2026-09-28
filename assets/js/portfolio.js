/* ==========================================================================
   portfolio.js
   1. Filtering, search and deep links for any [data-portfolio] block
      (portfolio.html, and the featured grid on the home page).
      Deep links:  portfolio.html?category=island-booth  ?category=rental  ?industry=technology  ?q=nova
   2. Quick-view dialog for [data-quick-view] buttons.
   3. portfolio-details.html?project=<slug> hydration from window.SF_PROJECTS.
   Requires plugins/projects-data.js (loaded first).
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const PROJECTS = window.SF_PROJECTS || [];
  const PLANS = window.SF_PLANS || {};
  const IMG = '../assets/images/';
  const params = new URLSearchParams(window.location.search);
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /* ------------------------------------------------------------ category aliases */
  const norm = (v) => String(v || '').toLowerCase().replace(/[^a-z]/g, '');
  const ALIAS = {
    all: 'all', custom: 'custom-booth', customboth: 'custom-booth', custombooth: 'custom-booth', custombooths: 'custom-booth',
    rental: 'rental', rentals: 'rental', rentalstand: 'rental', rentalstands: 'rental',
    island: 'island-booth', islandbooth: 'island-booth', islandbooths: 'island-booth',
    inline: 'inline-booth', inlinebooth: 'inline-booth', inlinebooths: 'inline-booth',
    peninsula: 'peninsula-booth', peninsulabooth: 'peninsula-booth', peninsulabooths: 'peninsula-booth',
    doubledecker: 'double-decker', doubledeckers: 'double-decker',
    pavilion: 'pavilion', pavilions: 'pavilion',
  };
  const TYPE_OF = { 'island-booth': 'island', 'inline-booth': 'inline', 'peninsula-booth': 'peninsula', 'double-decker': 'double-decker', pavilion: 'pavilion' };

  function matches(card, state) {
    const ds = card.dataset;
    let okCat = true;
    if (state.cat === 'custom-booth') okCat = ds.mode === 'custom';
    else if (state.cat === 'rental') okCat = ds.mode === 'rental';
    else if (state.cat !== 'all') okCat = ds.type === TYPE_OF[state.cat];
    const okInd = state.industry === 'all' || ds.industry === state.industry;
    const okQ = !state.q || ds.search.indexOf(state.q) > -1;
    return okCat && okInd && okQ;
  }

  function initFilter(root) {
    const page = root.hasAttribute('data-portfolio-page');
    const chips = $$('[data-filter]', root);
    const select = $('[data-industry]', root);
    const search = $('[data-search]', root);
    const resets = $$('[data-reset]', root);
    const cards = $$('[data-project]', root);
    const empty = $('[data-empty]', root);
    const count = $('[data-result-count]', root);
    const state = { cat: 'all', industry: 'all', q: '' };
    let ready = false;

    if (page) {
      state.cat = ALIAS[norm(params.get('category'))] || 'all';
      const ind = norm(params.get('industry'));
      if (ind && select) {
        const opt = Array.from(select.options).find((o) => norm(o.value) === ind || norm(o.textContent) === ind);
        if (opt) state.industry = opt.value;
      }
      state.q = (params.get('q') || '').toLowerCase().trim();
      if (search) search.value = params.get('q') || '';
      if (select) select.value = state.industry;
    }

    function apply() {
      let shown = 0;
      cards.forEach((card) => {
        const show = matches(card, state);
        const was = !card.hidden;
        card.hidden = !show;
        if (show) {
          shown++;
          card.classList.add('is-visible');
          if (ready && !was) {
            card.classList.add('is-entering');
            card.addEventListener('animationend', () => card.classList.remove('is-entering'), { once: true });
          }
        }
      });
      chips.forEach((c) => c.setAttribute('aria-pressed', String(c.dataset.filter === state.cat)));
      if (empty) empty.hidden = shown > 0;
      if (count) count.textContent = shown === cards.length ? 'Showing all ' + shown + ' projects' : 'Showing ' + shown + ' of ' + cards.length + ' projects';
      if (page && ready) {
        const q = new URLSearchParams();
        if (state.cat !== 'all') q.set('category', state.cat);
        if (state.industry !== 'all') q.set('industry', state.industry);
        if (state.q) q.set('q', state.q);
        try { history.replaceState(null, '', window.location.pathname + (q.toString() ? '?' + q.toString() : '')); } catch (e) { /* file:// URLs may refuse replaceState */ }
      }
    }

    chips.forEach((c) => c.addEventListener('click', () => { state.cat = c.dataset.filter; apply(); }));
    if (select) select.addEventListener('change', () => { state.industry = select.value; apply(); });
    if (search) {
      let t;
      search.addEventListener('input', () => { clearTimeout(t); t = setTimeout(() => { state.q = search.value.toLowerCase().trim(); apply(); }, 120); });
    }
    resets.forEach((b) => b.addEventListener('click', () => {
      state.cat = 'all'; state.industry = 'all'; state.q = '';
      if (select) select.value = 'all';
      if (search) search.value = '';
      apply();
      const first = chips[0];
      if (first) first.focus();
    }));
    apply();
    ready = true;
  }
  $$('[data-portfolio]').forEach(initFilter);

  /* ------------------------------------------------------------ quick view */
  d.addEventListener('click', (e) => {
    const b = e.target.closest('[data-quick-view]');
    if (!b || !window.Standform) return;
    const p = PROJECTS.find((x) => x.slug === b.dataset.quickView);
    if (!p) return;
    const media = '<div class="modal__media"><img src="' + IMG + p.img + '.svg" alt="' + esc(p.title) + ' booth render" width="800" height="600"></div>';
    const html = '<p><span class="badge badge--accent">' + esc(p.typeLabel) + '</span> <span class="badge">' + esc(p.industryLabel) + '</span></p>'
      + '<dl class="modal__meta"><div><strong>Size:</strong> ' + esc(p.size) + '</div><div><strong>Event:</strong> ' + esc(p.event) + ', ' + esc(p.location) + '</div></dl>'
      + '<p>' + esc(p.desc) + '</p>'
      + '<div class="btn-row"><a class="btn btn--accent btn--sm" href="portfolio-details.html?project=' + p.slug + '"><span>Read the case study</span></a>'
      + '<a class="btn btn--outline btn--sm" href="contact.html?type=' + p.type + '&mode=' + p.mode + '&msg=' + encodeURIComponent('I would like a stand similar to ' + p.title + '.') + '#enquiry"><span>Request a similar stand</span></a></div>';
    window.Standform.modal({ title: p.title, html, media });
  });

  /* ------------------------------------------------------------ details page hydration */
  const hydrateRoot = $('[data-p="title"]');
  if (hydrateRoot && PROJECTS.length) {
    const slug = params.get('project');
    const p = PROJECTS.find((x) => x.slug === slug) || PROJECTS[0];

    $$('[data-p]').forEach((el) => { const v = p[el.dataset.p]; if (v !== undefined) el.textContent = v; });
    const mats = $('[data-p-list="materials"]');
    if (mats) mats.innerHTML = p.materials.map((m) => '<li><svg class="icon" aria-hidden="true" focusable="false"><use href="#i-check"/></svg><span>' + esc(m) + '</span></li>').join('');
    const res = $('[data-p-results]');
    if (res) res.innerHTML = p.results.map((r) => '<li class="result is-visible"><strong>' + esc(r[0]) + '</strong><span>' + esc(r[1]) + '</span></li>').join('');
    const hero = $('[data-p-img]');
    if (hero) { hero.src = IMG + p.img + '.svg'; hero.alt = p.title + ' booth render'; }
    const GALT = { 0: 'perspective render', 2: 'detail crop, left side', 3: 'detail crop, right side' };
    $$('[data-p-gallery]').forEach((im) => { im.src = IMG + p.img + '.svg'; im.alt = p.title + ' ' + (GALT[im.dataset.pGallery] || 'view'); });
    const plan = $('[data-p-plan]');
    if (plan) { plan.src = IMG + (PLANS[p.type] || 'plan-island') + '.svg'; plan.alt = p.typeLabel + ' floor plan'; }

    d.title = p.title + ' Case Study | Portfolio | Standform';
    const setMeta = (sel, val) => { const m = $(sel); if (m) m.setAttribute('content', val); };
    const desc = p.desc.length > 155 ? p.desc.slice(0, 152) + '...' : p.desc;
    setMeta('meta[name="description"]', desc);
    setMeta('meta[property="og:title"]', d.title);
    setMeta('meta[name="twitter:title"]', d.title);
    setMeta('meta[property="og:description"]', desc);
    setMeta('meta[name="twitter:description"]', desc);
    $$('script[type="application/ld+json"]').forEach((s) => {
      try {
        const j = JSON.parse(s.textContent);
        if (j['@type'] === 'ImageObject') {
          j.name = p.title; j.description = p.desc; j.caption = p.event + ', ' + p.location;
          j.contentUrl = j.contentUrl.replace(/project-\d+\.svg/, p.img + '.svg');
          s.textContent = JSON.stringify(j);
        }
      } catch (err) { /* leave structured data untouched */ }
    });

    const rel = $('[data-related-projects]');
    if (rel) {
      const others = PROJECTS.filter((x) => x.slug !== p.slug);
      others.sort((a, b) => (b.industry === p.industry) - (a.industry === p.industry) || (b.type === p.type) - (a.type === p.type));
      rel.innerHTML = others.slice(0, 3).map((x) => '<article class="pcard is-visible"><a class="pcard__media" href="portfolio-details.html?project=' + x.slug + '" tabindex="-1" aria-hidden="true"><img src="' + IMG + x.img + '.svg" alt="' + esc(x.title) + ' booth render" width="800" height="600" loading="lazy"><span class="pcard__badges"><span class="badge badge--dark">' + esc(x.typeLabel) + '</span></span></a>'
        + '<div class="pcard__body"><p class="pcard__kicker">' + esc(x.industryLabel) + '</p><h3 class="pcard__title"><a href="portfolio-details.html?project=' + x.slug + '">' + esc(x.title) + '</a></h3><p class="pcard__desc">' + esc(x.desc) + '</p>'
        + '<div class="pcard__foot"><a class="link-arrow" href="portfolio-details.html?project=' + x.slug + '"><span>View Project</span><svg class="icon icon--flip" aria-hidden="true" focusable="false"><use href="#i-arrow"/></svg><span class="sr-only"> ' + esc(x.title) + '</span></a></div></div></article>').join('');
    }
  }
})();
