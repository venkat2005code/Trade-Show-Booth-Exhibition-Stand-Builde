/* ==========================================================================
   main.js: site-wide behaviour (vanilla ES6+, no dependencies)
   Theme, direction (RTL), header, drawer, dropdowns, reveal, counters, accordion, tabs,
   modals, legal dialogs, toasts, share, back-to-top, Home 2 rail and scroll story.
   Exposes window.Standform = { toast, modal, icon, reveal, store }
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const root = d.documentElement;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const store = (key, value) => {
    try {
      if (value === undefined) return localStorage.getItem(key);
      localStorage.setItem(key, value);
    } catch (e) { /* storage unavailable: fall back to session-only state */ }
    return null;
  };

  const icon = (name, cls) => '<svg class="icon' + (cls ? ' ' + cls : '') + '" aria-hidden="true" focusable="false"><use href="#i-' + name + '"/></svg>';

  /* ---------------------------------------------------------------- toasts */
  function toast(message, type, ms) {
    const box = $('[data-toasts]');
    if (!box) return;
    const t = d.createElement('div');
    t.className = 'toast' + (type ? ' toast--' + type : '');
    const text = d.createElement('span');
    text.textContent = message;
    const close = d.createElement('button');
    close.type = 'button';
    close.setAttribute('aria-label', 'Dismiss notification');
    close.innerHTML = '&times;';
    t.append(text, close);
    box.appendChild(t);
    const remove = () => {
      t.classList.add('is-leaving');
      setTimeout(() => t.remove(), 320);
    };
    close.addEventListener('click', remove);
    setTimeout(remove, ms || 4500);
  }

  /* ---------------------------------------------------------------- theme */
  const systemDark = window.matchMedia('(prefers-color-scheme: dark)');
  function applyTheme(theme, persist) {
    root.setAttribute('data-theme', theme);
    if (persist) store('sf-theme', theme);
    const dark = theme === 'dark';
    $$('[data-theme-toggle]').forEach((btn) => {
      btn.setAttribute('aria-pressed', String(dark));
      if (btn.hasAttribute('aria-label')) btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
      const label = $('[data-theme-label]', btn);
      if (label) label.textContent = dark ? 'Light mode' : 'Dark mode';
    });
    const meta = $('meta[name="theme-color"]');
    if (meta) meta.setAttribute('content', dark ? '#0a0b0d' : '#0e1013');
  }
  applyTheme(root.getAttribute('data-theme') || (systemDark.matches ? 'dark' : 'light'), false);
  d.addEventListener('click', (e) => {
    if (e.target.closest('[data-theme-toggle]')) {
      applyTheme(root.getAttribute('data-theme') === 'dark' ? 'light' : 'dark', true);
    }
  });
  const onSystemChange = (e) => { if (!store('sf-theme')) applyTheme(e.matches ? 'dark' : 'light', false); };
  systemDark.addEventListener ? systemDark.addEventListener('change', onSystemChange) : systemDark.addListener(onSystemChange);

  /* ---------------------------------------------------------------- direction (RTL testing) */
  function applyDir(dir, persist) {
    root.setAttribute('dir', dir);
    if (persist) store('sf-dir', dir);
    const rtl = dir === 'rtl';
    $$('[data-dir-toggle]').forEach((btn) => {
      btn.setAttribute('aria-pressed', String(rtl));
      if (btn.classList.contains('dir-toggle')) {
        // single header/drawer toggle: the label shows the current direction
        btn.textContent = rtl ? 'RTL' : 'LTR';
        btn.setAttribute('aria-label', rtl ? 'Switch to left-to-right layout' : 'Switch to right-to-left layout');
      }
      const label = $('[data-dir-label]', btn);
      if (label) {
        if (!label.dataset.idle) label.dataset.idle = label.textContent;
        label.textContent = rtl ? 'Back to LTR' : label.dataset.idle;
      }
    });
  }
  applyDir(root.getAttribute('dir') === 'rtl' ? 'rtl' : 'ltr', false);
  d.addEventListener('click', (e) => {
    if (e.target.closest('[data-dir-toggle]')) {
      applyDir(root.getAttribute('dir') === 'rtl' ? 'ltr' : 'rtl', true);
    }
  });

  /* ---------------------------------------------------------------- header */
  const header = $('[data-header]');
  const onScroll = () => {
    if (header) header.classList.toggle('is-scrolled', window.scrollY > 8);
    const top = $('[data-to-top]');
    if (top) top.classList.toggle('is-visible', window.scrollY > 700);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const toTop = $('[data-to-top]');
  if (toTop) {
    toTop.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: reduceMotion ? 'auto' : 'smooth' });
      const main = $('#main');
      if (main) main.focus({ preventScroll: true });
    });
  }

  /* ---------------------------------------------------------------- mobile drawer */
  const drawer = $('[data-drawer]');
  const navToggle = $('[data-nav-toggle]');
  function setDrawer(open) {
    if (!drawer || !navToggle) return;
    drawer.classList.toggle('is-open', open);
    if (header) header.classList.toggle('is-menu-open', open);
    navToggle.setAttribute('aria-expanded', String(open));
    navToggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    d.body.classList.toggle('is-locked', open);
    if (open) {
      const first = $('a', drawer);
      if (first) setTimeout(() => first.focus({ preventScroll: true }), 60);
    }
  }
  if (navToggle) {
    navToggle.addEventListener('click', () => setDrawer(!drawer.classList.contains('is-open')));
    drawer.addEventListener('click', (e) => { if (e.target.closest('a')) setDrawer(false); });
    window.addEventListener('resize', () => { if (window.innerWidth >= 1180) setDrawer(false); });
    d.addEventListener('keydown', (e) => {
      if (!drawer.classList.contains('is-open')) return;
      if (e.key === 'Escape') { setDrawer(false); navToggle.focus(); return; }
      if (e.key !== 'Tab') return;
      const items = $$('a[href], button:not([disabled])', drawer).concat($$('.site-header__actions button, .site-header__actions a'));
      const visible = items.filter((el) => el.offsetParent !== null);
      const first = visible[0];
      const last = visible[visible.length - 1];
      if (e.shiftKey && d.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && d.activeElement === last) { e.preventDefault(); first.focus(); }
    });
  }

  /* ---------------------------------------------------------------- desktop dropdowns */
  d.addEventListener('click', (e) => {
    const t = e.target.closest('[data-sub-toggle]');
    $$('.has-sub.is-open').forEach((li) => {
      if (!t || li !== t.closest('.has-sub')) {
        li.classList.remove('is-open');
        const b = $('[data-sub-toggle]', li);
        if (b) b.setAttribute('aria-expanded', 'false');
      }
    });
    if (t) {
      const li = t.closest('.has-sub');
      const open = !li.classList.contains('is-open');
      li.classList.toggle('is-open', open);
      t.setAttribute('aria-expanded', String(open));
    }
  });
  d.addEventListener('keydown', (e) => {
    if (e.key !== 'Escape') return;
    $$('.has-sub.is-open').forEach((li) => {
      li.classList.remove('is-open');
      const b = $('[data-sub-toggle]', li);
      if (b) { b.setAttribute('aria-expanded', 'false'); b.focus(); }
    });
  });

  /* ---------------------------------------------------------------- scroll reveal */
  let io = null;
  if ('IntersectionObserver' in window && !reduceMotion) {
    io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { rootMargin: '0px 0px -6% 0px', threshold: 0.05 });
  }
  function reveal(scope) {
    $$('.reveal:not(.is-visible)', scope || d).forEach((el) => (io ? io.observe(el) : el.classList.add('is-visible')));
  }
  reveal();

  /* ---------------------------------------------------------------- counters */
  const counters = $$('[data-count]');
  if (counters.length) {
    const run = (el) => {
      const end = parseFloat(el.dataset.count);
      const suffix = el.dataset.suffix || '';
      if (reduceMotion || isNaN(end)) { el.textContent = end + suffix; return; }
      const start = performance.now();
      const dur = 1400;
      const tick = (now) => {
        const p = Math.min(1, (now - start) / dur);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    if ('IntersectionObserver' in window) {
      const co = new IntersectionObserver((entries) => entries.forEach((en) => { if (en.isIntersecting) { run(en.target); co.unobserve(en.target); } }), { threshold: 0.4 });
      counters.forEach((c) => co.observe(c));
    }
  }

  /* ---------------------------------------------------------------- accordion */
  $$('[data-accordion]').forEach((acc) => {
    acc.addEventListener('click', (e) => {
      const btn = e.target.closest('.accordion__btn');
      if (!btn) return;
      const open = btn.getAttribute('aria-expanded') !== 'true';
      btn.setAttribute('aria-expanded', String(open));
      const panel = d.getElementById(btn.getAttribute('aria-controls'));
      if (panel) panel.hidden = !open;
    });
  });

  /* ---------------------------------------------------------------- tabs */
  $$('[data-tabs]').forEach((tabs) => {
    const list = $('[role="tablist"]', tabs);
    const btns = $$('[role="tab"]', tabs);
    const select = (btn, focus) => {
      btns.forEach((b) => {
        const on = b === btn;
        b.setAttribute('aria-selected', String(on));
        b.tabIndex = on ? 0 : -1;
        const p = d.getElementById(b.getAttribute('aria-controls'));
        if (p) p.hidden = !on;
      });
      if (focus) btn.focus();
    };
    btns.forEach((b) => b.addEventListener('click', () => select(b)));
    list.addEventListener('keydown', (e) => {
      const i = btns.indexOf(d.activeElement);
      if (i < 0) return;
      const rtl = root.getAttribute('dir') === 'rtl';
      const next = e.key === (rtl ? 'ArrowLeft' : 'ArrowRight') ? (i + 1) % btns.length
        : e.key === (rtl ? 'ArrowRight' : 'ArrowLeft') ? (i - 1 + btns.length) % btns.length
          : e.key === 'Home' ? 0 : e.key === 'End' ? btns.length - 1 : -1;
      if (next >= 0) { e.preventDefault(); select(btns[next], true); }
    });
  });

  /* ---------------------------------------------------------------- modals */
  const insideDialog = (dlg, e) => {
    const r = dlg.getBoundingClientRect();
    return e.clientX >= r.left && e.clientX <= r.right && e.clientY >= r.top && e.clientY <= r.bottom;
  };
  d.addEventListener('click', (e) => {
    const dlg = e.target;
    if (dlg.tagName === 'DIALOG' && dlg.open && !insideDialog(dlg, e)) dlg.close();
    const opener = e.target.closest('[data-modal-open]');
    if (opener) {
      const target = d.getElementById(opener.getAttribute('data-modal-open'));
      if (target && target.showModal) {
        target._opener = opener;
        target.showModal();
      }
    }
  });
  d.addEventListener('close', (e) => {
    if (e.target.tagName === 'DIALOG' && e.target._opener) e.target._opener.focus();
  }, true);

  function modal(opts) {
    const dlg = d.createElement('dialog');
    dlg.className = 'modal' + (opts.cls ? ' ' + opts.cls : '');
    dlg.setAttribute('aria-labelledby', 'sf-modal-title');
    dlg.innerHTML = '<form method="dialog" class="modal__close-form"><button class="icon-btn modal__close" aria-label="Close dialog">' + icon('close') + '</button></form>'
      + (opts.media || '') + '<h2 id="sf-modal-title"></h2><div class="modal__body">' + (opts.html || '') + '</div>';
    $('h2', dlg).textContent = opts.title || '';
    const opener = d.activeElement;
    d.body.appendChild(dlg);
    dlg.addEventListener('close', () => { dlg.remove(); if (opener && opener.focus) opener.focus(); });
    dlg.showModal();
    return dlg;
  }

  const LEGAL = {
    privacy: ['Privacy Policy', '<p>This is placeholder policy text for the Standform demo template. Replace it with your own privacy policy before launch.</p><h3>What this demo collects</h3><p>Nothing. Forms in this template run in demo mode and do not send data anywhere until you connect an endpoint such as Formspree, Netlify Forms or your own API.</p><h3>Local storage</h3><p>The theme (light or dark) and text direction (LTR or RTL) you pick are saved in your browser\'s local storage so the site remembers them. No personal data is stored.</p><h3>Contact</h3><p>Questions about privacy? Email hello@standform.example.</p>'],
    terms: ['Terms of Use', '<p>These are placeholder terms for the Standform demo template. Replace them with terms reviewed by your legal adviser.</p><h3>Estimates</h3><p>Any pricing or estimate shown on this site is a demonstration range only. Final pricing depends on show, footprint, materials and scope, and is confirmed in a written quotation.</p><h3>Content</h3><p>Project names, clients, quotes and figures are fictional demo content and must be replaced with your own.</p>'],
    accessibility: ['Accessibility Statement', '<p>Standform aims to meet WCAG 2.1 level AA. This template includes a skip link, semantic landmarks, visible focus states, keyboard-operable menus, dialogs, tabs and accordions, form labels with associated error messages, 44 px minimum touch targets and support for reduced motion.</p><h3>Feedback</h3><p>If you find a barrier on this site, email hello@standform.example and tell us the page and the problem. We aim to reply within two working days.</p>'],
  };
  d.addEventListener('click', (e) => {
    const b = e.target.closest('[data-legal]');
    if (!b) return;
    const doc = LEGAL[b.getAttribute('data-legal')];
    if (doc) modal({ title: doc[0], html: doc[1] });
  });

  /* ---------------------------------------------------------------- toast triggers */
  d.addEventListener('click', (e) => {
    const t = e.target.closest('[data-toast]');
    if (t) toast(t.getAttribute('data-toast'), 'success');
  });
  d.addEventListener('change', (e) => {
    const t = e.target.closest('[data-toast-change]');
    if (t) toast(t.getAttribute('data-toast-change') + (t.checked ? ' is now visible' : ' is now hidden') + ' (demo).');
  });

  /* ---------------------------------------------------------------- share */
  const nativeShare = $('[data-share="native"]');
  if (nativeShare && navigator.share) nativeShare.hidden = false;
  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(text);
    return new Promise((resolve, reject) => {
      const ta = d.createElement('textarea');
      ta.value = text;
      ta.setAttribute('readonly', '');
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      d.body.appendChild(ta);
      ta.select();
      try { d.execCommand('copy') ? resolve() : reject(); } catch (err) { reject(err); }
      ta.remove();
    });
  }
  d.addEventListener('click', (e) => {
    const b = e.target.closest('[data-share]');
    if (!b) return;
    const url = location.href.split('#')[0];
    const title = d.title;
    const q = encodeURIComponent;
    const kind = b.getAttribute('data-share');
    const pop = (u) => window.open(u, '_blank', 'noopener,noreferrer,width=620,height=520');
    if (kind === 'x') pop('https://twitter.com/intent/tweet?url=' + q(url) + '&text=' + q(title));
    else if (kind === 'linkedin') pop('https://www.linkedin.com/sharing/share-offsite/?url=' + q(url));
    else if (kind === 'facebook') pop('https://www.facebook.com/sharer/sharer.php?u=' + q(url));
    else if (kind === 'native') navigator.share({ title, url }).catch(() => {});
    else if (kind === 'copy') copyText(url).then(() => toast('Link copied to clipboard.', 'success'), () => toast('Could not copy the link. Copy it from the address bar.', 'error'));
  });

  /* ---------------------------------------------------------------- Home 2: rail + story */
  const rail = $('[data-rail]');
  if (rail && 'IntersectionObserver' in window) {
    const links = $$('a', rail);
    const map = new Map();
    links.forEach((a) => { const s = d.getElementById(a.getAttribute('href').slice(1)); if (s) map.set(s, a); });
    const ro = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) {
          links.forEach((a) => { a.classList.remove('is-active'); a.removeAttribute('aria-current'); });
          const a = map.get(en.target);
          a.classList.add('is-active');
          a.setAttribute('aria-current', 'true');
        }
      });
    }, { rootMargin: '-40% 0px -55% 0px' });
    map.forEach((_, s) => ro.observe(s));
    const bar = $('[data-rail-progress]', rail);
    if (bar) {
      const upd = () => {
        const h = d.documentElement.scrollHeight - window.innerHeight;
        bar.style.height = (h > 0 ? Math.min(100, (window.scrollY / h) * 100) : 0) + '%';
      };
      window.addEventListener('scroll', upd, { passive: true });
      upd();
    }
  }
  const stage = $('[data-story-stage]');
  if (stage && 'IntersectionObserver' in window) {
    const imgs = $$('.story__frame img', stage);
    const cap = $('[data-story-cap]', stage);
    const steps = $$('[data-story-step]');
    const so = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (!en.isIntersecting) return;
        steps.forEach((s) => s.classList.remove('is-active'));
        en.target.classList.add('is-active');
        const i = Number(en.target.dataset.img) || 0;
        imgs.forEach((im, k) => im.classList.toggle('is-on', k === i));
        if (cap) cap.textContent = en.target.dataset.cap || '';
      });
    }, { rootMargin: '-45% 0px -45% 0px' });
    steps.forEach((s) => so.observe(s));
    if (steps[0]) steps[0].classList.add('is-active');
  }

  window.Standform = { toast, modal, icon, reveal, store };
})();
