/* ==========================================================================
   blog.js
   1. blog.html: category filter, search, "load more" (deep links: ?category=budget&q=cost)
   2. blog-details.html?post=<slug>: hydrates the article from window.SF_POSTS, builds the table of
      contents, scroll-spy and reading-progress bar.
   Requires plugins/posts-data.js (loaded first).
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const POSTS = window.SF_POSTS || [];
  const IMG = '../assets/images/';
  const params = new URLSearchParams(window.location.search);
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const esc = (s) => String(s).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

  /* ------------------------------------------------------------ blog list */
  const list = $('[data-blog]');
  if (list) {
    const size = Number(list.dataset.pageSize) || 6;
    const chips = $$('[data-filter]', list);
    const search = $('[data-search]', list);
    const cards = $$('[data-post]', list);
    const empty = $('[data-empty]', list);
    const count = $('[data-result-count]', list);
    const more = $('[data-load-more]', list);
    const featured = $('[data-featured]', list);
    const validCats = chips.map((c) => c.dataset.filter);
    const state = { cat: validCats.indexOf(params.get('category')) > -1 ? params.get('category') : 'all', q: (params.get('q') || '').toLowerCase().trim(), shown: size };
    if (search) search.value = params.get('q') || '';
    let ready = false;

    // In the unfiltered view the featured article already leads the page, so its grid card is skipped.
    const matching = () => cards.filter((c) => (state.cat === 'all' || c.dataset.cat === state.cat) && (!state.q || c.dataset.search.indexOf(state.q) > -1)
      && !(featured && state.cat === 'all' && !state.q && c.hasAttribute('data-is-featured')));

    function apply(focusNew) {
      const hits = matching();
      let firstNew = null;
      cards.forEach((c) => {
        const i = hits.indexOf(c);
        const show = i > -1 && i < state.shown;
        const was = !c.hidden;
        c.hidden = !show;
        if (show) {
          c.classList.add('is-visible');
          if (!was && ready) { c.classList.add('is-entering'); c.addEventListener('animationend', () => c.classList.remove('is-entering'), { once: true }); if (!firstNew) firstNew = c; }
        }
      });
      chips.forEach((c) => c.setAttribute('aria-pressed', String(c.dataset.filter === state.cat)));
      const shown = Math.min(hits.length, state.shown);
      if (count) count.textContent = hits.length === 0 ? 'No articles found' : 'Showing ' + shown + ' of ' + hits.length + ' article' + (hits.length === 1 ? '' : 's');
      if (empty) empty.hidden = hits.length > 0;
      if (more) more.parentElement.hidden = hits.length <= state.shown;
      if (featured) featured.hidden = state.cat !== 'all' || !!state.q;
      if (focusNew && firstNew) { const a = $('a', firstNew); if (a) a.focus({ preventScroll: false }); }
      if (ready) {
        const q = new URLSearchParams();
        if (state.cat !== 'all') q.set('category', state.cat);
        if (state.q) q.set('q', state.q);
        try { history.replaceState(null, '', window.location.pathname + (q.toString() ? '?' + q.toString() : '')); } catch (e) { /* file:// */ }
      }
    }
    chips.forEach((c) => c.addEventListener('click', () => { state.cat = c.dataset.filter; state.shown = size; apply(); }));
    if (search) {
      let t;
      search.addEventListener('input', () => { clearTimeout(t); t = setTimeout(() => { state.q = search.value.toLowerCase().trim(); state.shown = size; apply(); }, 120); });
    }
    $$('[data-reset]', list).forEach((b) => b.addEventListener('click', () => {
      state.cat = 'all'; state.q = ''; state.shown = size;
      if (search) search.value = '';
      apply();
    }));
    // "Load more" shows skeleton cards while the next batch loads (swap this delay for your real fetch).
    if (more) more.addEventListener('click', () => {
      const grid = $('[data-grid]', list);
      const pending = Math.min(size, Math.max(0, matching().length - state.shown));
      const skels = [];
      if (grid) {
        for (let i = 0; i < pending; i++) {
          const sk = d.createElement('div');
          sk.className = 'bcard bcard--skeleton';
          sk.setAttribute('aria-hidden', 'true');
          sk.innerHTML = '<div class="skeleton skeleton--media"></div><div class="bcard__body"><div class="skeleton skeleton--line skeleton--short"></div><div class="skeleton skeleton--title"></div><div class="skeleton skeleton--line"></div></div>';
          grid.appendChild(sk); skels.push(sk);
        }
      }
      more.disabled = true; more.setAttribute('aria-busy', 'true');
      setTimeout(() => {
        skels.forEach((sk) => sk.remove());
        more.disabled = false; more.removeAttribute('aria-busy');
        state.shown += size; apply(true);
      }, reduceMotion ? 0 : 450);
    });
    apply();
    ready = true;
  }

  /* ------------------------------------------------------------ article page */
  const article = $('[data-article]');
  if (article) {
    const slug = params.get('post');
    const p = POSTS.find((x) => x.slug === slug);
    const body = $('[data-post-body]');

    if (p && slug !== 'how-much-does-an-exhibition-stand-cost') {
      const set = (k, v) => $$('[data-post="' + k + '"]').forEach((el) => { el.textContent = v; });
      set('title', p.title); set('excerpt', p.excerpt); set('cat', p.catLabel); set('date', p.dateLabel); set('read', p.read + ' min read');
      set('author', p.author); set('author2', p.author);
      const initials = p.author.split(' ').map((w) => w[0]).join('').slice(0, 2);
      set('initials', initials); set('initials2', initials);
      $$('time[data-post="date"]').forEach((t) => t.setAttribute('datetime', p.date));
      const cover = $('[data-post-img]');
      if (cover) { cover.src = IMG + p.img; cover.alt = p.imgAlt || p.title; }
      const html = ['<p class="lead">' + esc(p.excerpt) + '</p>'];
      p.sections.forEach((s, i) => {
        html.push('<h2 id="s' + (i + 1) + '">' + esc(s[0]) + '</h2><p>' + esc(s[1]) + '</p>');
      });
      html.push('<h2 id="next-step">Your next step</h2><p>Every show is different. If you would like a designer to look at your footprint, goals and schedule, send us the details and we will reply within one working day. You can also run a quick range in our <a href="pricing.html#estimator">project estimator</a>.</p>');
      body.innerHTML = html.join('');
      d.title = p.title + ' | Standform';
      const setMeta = (sel, v) => { const m = $(sel); if (m) m.setAttribute('content', v); };
      const desc = p.excerpt.length > 158 ? p.excerpt.slice(0, 155) + '...' : p.excerpt;
      setMeta('meta[name="description"]', desc); setMeta('meta[property="og:title"]', d.title); setMeta('meta[name="twitter:title"]', d.title);
      setMeta('meta[property="og:description"]', desc); setMeta('meta[name="twitter:description"]', desc);
      $$('script[type="application/ld+json"]').forEach((s) => {
        try {
          const j = JSON.parse(s.textContent);
          if (j['@type'] === 'Article') {
            j.headline = p.title; j.description = p.excerpt; j.datePublished = p.date; j.dateModified = p.date; j.author.name = p.author;
            j.image = [j.image[0].replace(/images\/.*$/, 'images/' + p.img)];
            j.mainEntityOfPage = j.mainEntityOfPage.replace(/post=.*$/, 'post=' + p.slug);
            s.textContent = JSON.stringify(j);
          }
        } catch (err) { /* keep existing structured data */ }
      });
      const rel = $('[data-related-posts]');
      if (rel) {
        const others = POSTS.filter((x) => x.slug !== p.slug).sort((a, b) => (b.cat === p.cat) - (a.cat === p.cat));
        rel.innerHTML = others.slice(0, 3).map((x) => '<article class="bcard is-visible"><a class="bcard__media" href="blog-details.html?post=' + x.slug + '" tabindex="-1" aria-hidden="true"><img src="' + IMG + x.img + '" alt="' + esc(x.title) + '" width="800" height="500" loading="lazy"></a>'
          + '<div class="bcard__body"><p class="bcard__meta"><span class="badge">' + esc(x.catLabel) + '</span><time datetime="' + x.date + '">' + esc(x.dateLabel) + '</time><span>' + x.read + ' min read</span></p><h3 class="bcard__title"><a href="blog-details.html?post=' + x.slug + '">' + esc(x.title) + '</a></h3><p>' + esc(x.excerpt) + '</p></div></article>').join('');
      }
    }

    /* table of contents from the h2 headings */
    const heads = $$('h2[id]', body);
    const tocHtml = heads.map((h) => '<li><a href="#' + h.id + '">' + esc(h.textContent) + '</a></li>').join('');
    $$('[data-toc], [data-toc-inline]').forEach((ol) => { ol.innerHTML = tocHtml; });
    const links = $$('[data-toc] a');

    if ('IntersectionObserver' in window) {
      const spy = new IntersectionObserver((entries) => {
        entries.forEach((en) => {
          if (en.isIntersecting) {
            links.forEach((a) => { const on = a.getAttribute('href') === '#' + en.target.id; a.classList.toggle('is-active', on); if (on) a.setAttribute('aria-current', 'location'); else a.removeAttribute('aria-current'); });
          }
        });
      }, { rootMargin: '-15% 0px -70% 0px' });
      heads.forEach((h) => spy.observe(h));
    }

    const bar = $('[data-read-progress]');
    if (bar) {
      const upd = () => {
        const r = article.getBoundingClientRect();
        const total = r.height - window.innerHeight * 0.6;
        const done = Math.min(1, Math.max(0, (-r.top + window.innerHeight * 0.2) / Math.max(1, total)));
        bar.style.width = (done * 100).toFixed(1) + '%';
      };
      window.addEventListener('scroll', upd, { passive: true });
      upd();
    }
    if (window.Standform && !reduceMotion) window.Standform.reveal(article);
  }
})();
