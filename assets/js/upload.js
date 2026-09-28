/* ==========================================================================
   upload.js: drag-and-drop file upload UI (demo: nothing is sent to a server)
   Validates type, size and file count, shows per-file progress and lets users remove files.
   Configure with data-accept="pdf,jpg,..." data-max-files="5" data-max-mb="20" on [data-upload].
   ========================================================================== */
(function () {
  'use strict';

  const d = document;
  const icon = (n) => '<svg class="icon" aria-hidden="true" focusable="false"><use href="#i-' + n + '"/></svg>';
  const fmt = (b) => (b >= 1048576 ? (b / 1048576).toFixed(1) + ' MB' : Math.max(1, Math.round(b / 1024)) + ' KB');

  function init(zone) {
    const input = zone.querySelector('input[type="file"]');
    const list = zone.querySelector('[data-file-list]');
    const err = zone.querySelector('[data-upload-error]');
    const max = Number(zone.dataset.maxFiles) || 5;
    const maxMb = Number(zone.dataset.maxMb) || 20;
    const allowed = (zone.dataset.accept || '').split(',').map((s) => s.trim().toLowerCase()).filter(Boolean);
    let files = [];

    function sync() {
      try {
        const dt = new DataTransfer();
        files.forEach((f) => dt.items.add(f));
        input.files = dt.files;
      } catch (e) { /* DataTransfer constructor unsupported: the visual list still works */ }
    }

    function addItem(file) {
      const li = d.createElement('li');
      li.innerHTML = icon('file') + '<div><p class="file-list__name"></p><p class="file-list__meta"></p><div class="file-list__bar"><i></i></div></div>'
        + '<button type="button" class="icon-btn" aria-label="">' + icon('close') + '</button>';
      li.querySelector('.file-list__name').textContent = file.name;
      const meta = li.querySelector('.file-list__meta');
      const bar = li.querySelector('.file-list__bar');
      const fill = bar.querySelector('i');
      const btn = li.querySelector('button');
      btn.setAttribute('aria-label', 'Remove ' + file.name);
      meta.textContent = fmt(file.size) + ' - uploading (demo)...';
      let pct = 0;
      const timer = setInterval(() => {
        pct = Math.min(100, pct + 8 + Math.random() * 14);
        fill.style.width = pct + '%';
        if (pct >= 100) {
          clearInterval(timer);
          bar.classList.add('is-done');
          meta.textContent = fmt(file.size) + ' - ready (demo, not uploaded)';
        }
      }, 120);
      btn.addEventListener('click', () => {
        clearInterval(timer);
        files = files.filter((f) => f !== file);
        li.remove();
        err.textContent = '';
        sync();
        if (window.Standform) window.Standform.toast(file.name + ' removed.');
        input.focus();
      });
      list.appendChild(li);
    }

    function add(incoming) {
      const problems = [];
      incoming.forEach((f) => {
        const ext = f.name.split('.').pop().toLowerCase();
        if (allowed.length && allowed.indexOf(ext) < 0) problems.push(f.name + ': ".' + ext + '" files are not supported.');
        else if (f.size > maxMb * 1048576) problems.push(f.name + ' is larger than ' + maxMb + ' MB.');
        else if (files.length >= max) problems.push('Only ' + max + ' files are allowed. "' + f.name + '" was not added.');
        else if (files.some((x) => x.name === f.name && x.size === f.size)) problems.push(f.name + ' has already been added.');
        else { files.push(f); addItem(f); }
      });
      err.textContent = problems.join(' ');
      sync();
    }

    input.addEventListener('change', () => { add(Array.from(input.files)); });
    ['dragenter', 'dragover'].forEach((t) => zone.addEventListener(t, (e) => { e.preventDefault(); zone.classList.add('is-drag'); }));
    ['dragleave', 'dragend'].forEach((t) => zone.addEventListener(t, () => zone.classList.remove('is-drag')));
    zone.addEventListener('drop', (e) => {
      e.preventDefault();
      zone.classList.remove('is-drag');
      if (e.dataTransfer && e.dataTransfer.files) add(Array.from(e.dataTransfer.files));
    });

    const form = zone.closest('form');
    if (form) {
      form.addEventListener('sf:reset', () => {
        files = [];
        list.innerHTML = '';
        err.textContent = '';
        sync();
      });
    }
  }

  document.querySelectorAll('[data-upload]').forEach(init);
})();
