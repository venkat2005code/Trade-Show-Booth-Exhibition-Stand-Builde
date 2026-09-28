/* ==========================================================================
   forms.js: accessible client-side validation for every form marked [data-validate]
   - Inline errors linked with aria-describedby, aria-invalid, focus moves to the first error
   - Loading, success and error states
   - Demo mode: forms with [data-demo] (or a placeholder endpoint) simulate a successful send.
     To go live, remove data-demo and set data-endpoint to your Formspree / Netlify / API URL.
   - Newsletter forms (.newsletter) are Mailchimp / ConvertKit ready: set data-endpoint to your Mailchimp form action
     (https://YOUR_DC.list-manage.com/subscribe/post?u=YOUR_U&id=YOUR_LIST_ID, field EMAIL) or ConvertKit form URL
     (https://app.convertkit.com/forms/YOUR_FORM_ID/subscriptions, field email_address).
   - Also: password show/hide, password strength, query-string prefill for the contact form.
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const $ = (s, c) => (c || d).querySelector(s);
  const $$ = (s, c) => Array.from((c || d).querySelectorAll(s));
  const toast = (m, t) => { if (window.Standform) window.Standform.toast(m, t); };

  const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  const fieldOf = (el) => el.closest('.field') || el.parentElement;

  function errorNode(el) {
    const id = (el.id || el.name) + '-error';
    let node = d.getElementById(id);
    if (!node) {
      node = d.createElement('p');
      node.className = 'field__error';
      node.id = id;
      const host = fieldOf(el);
      host.appendChild(node);
    }
    return node;
  }

  function setDescribedBy(el, id, on) {
    const ids = (el.getAttribute('aria-describedby') || '').split(/\s+/).filter(Boolean).filter((x) => x !== id);
    if (on) ids.push(id);
    if (ids.length) el.setAttribute('aria-describedby', ids.join(' '));
    else el.removeAttribute('aria-describedby');
  }

  function message(el) {
    if (el.disabled || el.type === 'hidden' || el.type === 'file' || el.type === 'submit') return '';
    const data = el.dataset;
    if (el.type === 'checkbox') {
      return el.required && !el.checked ? (data.msgRequired || 'Please tick this box to continue.') : '';
    }
    const value = (el.value || '').trim();
    if (el.required && !value) {
      return data.msgRequired || (el.tagName === 'SELECT' ? 'Please choose an option.' : 'Please complete this field.');
    }
    if (!value) return '';
    if (el.type === 'email' && !EMAIL.test(value)) return data.msgType || 'Enter a valid email address, for example name@company.com.';
    if (el.minLength > 0 && value.length < el.minLength) return data.msgMinlength || 'Please enter at least ' + el.minLength + ' characters.';
    if (el.getAttribute('pattern') && !new RegExp('^(?:' + el.getAttribute('pattern') + ')$').test(value)) return data.msgPattern || 'Please check the format of this field.';
    if (data.match) {
      const other = d.getElementById(data.match);
      if (other && other.value !== el.value) return data.msgMatch || 'The values do not match.';
    }
    if (el.type === 'date') {
      const today = new Date();
      today.setHours(0, 0, 0, 0);
      if (new Date(value + 'T00:00:00') < today) return 'Choose today or a future date.';
    }
    return '';
  }

  function check(el) {
    const msg = message(el);
    const node = errorNode(el);
    node.textContent = msg;
    if (msg) {
      el.setAttribute('aria-invalid', 'true');
      setDescribedBy(el, node.id, true);
    } else {
      el.removeAttribute('aria-invalid');
      setDescribedBy(el, node.id, false);
    }
    return msg;
  }

  const controls = (form) => $$('input, select, textarea', form).filter((el) => !['hidden', 'submit', 'button', 'file', 'radio'].includes(el.type));

  function setStatus(form, text, kind) {
    const s = $('[data-status]', form);
    if (!s) return;
    s.textContent = text;
    s.className = 'form-status' + (kind ? ' is-' + kind : '');
  }

  function setAlert(form, text) {
    const a = $('[data-error]', form);
    if (!a) return;
    a.hidden = !text;
    a.textContent = text || '';
  }

  function setLoading(form, on) {
    const btn = $('[type="submit"]', form);
    form.setAttribute('aria-busy', String(on));
    if (btn) {
      btn.classList.toggle('is-loading', on);
      btn.disabled = on;
    }
  }

  function send(form) {
    const action = form.getAttribute('data-endpoint');
    const demo = form.hasAttribute('data-demo') || !action || /your-form-id/.test(action);
    if (demo) return new Promise((resolve) => setTimeout(resolve, 1100));
    return fetch(action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' } })
      .then((r) => { if (!r.ok) throw new Error('Request failed'); });
  }

  function reset(form) {
    form.reset();
    $$('[aria-invalid]', form).forEach((el) => el.removeAttribute('aria-invalid'));
    $$('.field__error', form).forEach((n) => { n.textContent = ''; });
    $$('[data-strength-meter]', form).forEach((m) => m.removeAttribute('data-level'));
    $$('[data-strength-label]', form).forEach((l) => { l.textContent = ''; });
    form.dispatchEvent(new CustomEvent('sf:reset'));
  }

  function init(form) {
    form.setAttribute('novalidate', '');
    form.addEventListener('focusout', (e) => {
      const el = e.target;
      if (el.matches && el.matches('input, select, textarea') && (el.value || el.hasAttribute('aria-invalid'))) check(el);
    });
    form.addEventListener('input', (e) => {
      const el = e.target;
      if (el.hasAttribute && el.hasAttribute('aria-invalid')) check(el);
    });
    form.addEventListener('change', (e) => {
      const el = e.target;
      if (el.type === 'checkbox' && el.hasAttribute('aria-invalid')) check(el);
    });
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      setStatus(form, '');
      const bad = controls(form).filter((el) => check(el));
      if (bad.length) {
        setAlert(form, bad.length === 1 ? 'Please fix 1 field below.' : 'Please fix ' + bad.length + ' fields below.');
        setStatus(form, '');
        bad[0].focus();
        return;
      }
      setAlert(form, '');
      setLoading(form, true);
      send(form).then(() => {
        setLoading(form, false);
        const redirect = form.getAttribute('data-redirect');
        const isDemo = form.hasAttribute('data-demo');
        if (redirect) {
          setStatus(form, 'Signed in (demo). Redirecting to the admin dashboard demo...', 'success');
          setTimeout(() => { window.location.href = redirect; }, 900);
          return;
        }
        setStatus(form, isDemo ? 'Thank you. Demo mode: your details were validated but not sent anywhere.' : 'Thank you. Your message has been sent.', 'success');
        toast(isDemo ? 'Form validated (demo mode, nothing was sent).' : 'Message sent. We will reply within one working day.', 'success');
        reset(form);
        if (form.hasAttribute('data-close-on-success')) {
          const dlg = form.closest('dialog');
          if (dlg) setTimeout(() => dlg.close(), 1400);
        }
      }).catch(() => {
        setLoading(form, false);
        setStatus(form, 'Sorry, something went wrong sending your message. Please try again, or email hello@standform.example.', 'error');
        toast('Sending failed. Please try again.', 'error');
      });
    });
  }

  $$('form[data-validate]').forEach(init);

  /* password show / hide */
  d.addEventListener('click', (e) => {
    const b = e.target.closest('[data-toggle-password]');
    if (!b) return;
    const input = d.getElementById(b.getAttribute('data-toggle-password'));
    const show = input.type === 'password';
    input.type = show ? 'text' : 'password';
    b.setAttribute('aria-pressed', String(show));
    b.setAttribute('aria-label', show ? 'Hide password' : 'Show password');
    const use = $('use', b);
    if (use) use.setAttribute('href', show ? '#i-eye-off' : '#i-eye');
  });

  /* password strength */
  $$('[data-strength]').forEach((input) => {
    const meter = $('[data-strength-meter]', fieldOf(input));
    const label = $('[data-strength-label]', fieldOf(input));
    input.addEventListener('input', () => {
      const v = input.value;
      let score = 0;
      if (v.length >= 8) score++;
      if (/[a-z]/.test(v) && /[A-Z]/.test(v)) score++;
      if (/\d/.test(v)) score++;
      if (/[^A-Za-z0-9]/.test(v) || v.length >= 14) score++;
      if (!v) score = 0;
      if (meter) meter.setAttribute('data-level', score);
      if (label) label.textContent = v ? ['Very weak', 'Weak', 'Fair', 'Good', 'Strong'][score] : '';
    });
  });

  /* contact form prefill: contact.html?type=island&size=20x20&mode=custom&msg=... */
  const params = new URLSearchParams(window.location.search);
  const contact = $('#enquiry form');
  if (contact && Array.from(params.keys()).length) {
    const set = (id, v) => { const el = d.getElementById(id); if (el && v) el.value = v; };
    const type = params.get('type');
    if (type) set('type', type);
    const size = params.get('size');
    if (size) set('size', size.replace('x', ' x ') + ' ft');
    const mode = params.get('mode');
    if (mode) set('service', mode === 'rental' ? 'rental' : 'custom-design');
    const service = params.get('service');
    if (service) set('service', service);
    set('event', params.get('event'));
    set('budget', params.get('budget'));
    const msg = params.get('msg');
    if (msg) set('message', msg);
  }
})();
