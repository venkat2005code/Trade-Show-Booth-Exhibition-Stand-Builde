/* lightbox.js: accessible image lightbox for [data-gallery] blocks.
   Buttons with [data-lightbox] open a native <dialog>. Arrow keys move between images, Esc closes. */
(function () {
  'use strict';

  const d = document;
  const galleries = Array.from(d.querySelectorAll('[data-gallery]'));
  if (!galleries.length) return;
  const icon = (n) => '<svg class="icon icon--flip" aria-hidden="true" focusable="false"><use href="#i-' + n + '"/></svg>';

  galleries.forEach((gal) => {
    gal.addEventListener('click', (e) => {
      const trigger = e.target.closest('[data-lightbox]');
      if (!trigger) return;
      const buttons = Array.from(gal.querySelectorAll('[data-lightbox]'));
      let index = buttons.indexOf(trigger);

      const dlg = d.createElement('dialog');
      dlg.className = 'lightbox';
      dlg.setAttribute('aria-label', 'Image gallery');
      dlg.innerHTML = '<div class="lightbox__stage"><img alt="" width="800" height="600"></div>'
        + '<button class="icon-btn lightbox__close" type="button" aria-label="Close gallery"><svg class="icon" aria-hidden="true" focusable="false"><use href="#i-close"/></svg></button>'
        + '<div class="lightbox__bar"><button class="icon-btn" type="button" data-prev aria-label="Previous image">' + icon('arrow').replace('icon icon--flip', 'icon icon--prev') + '</button>'
        + '<p aria-live="polite"></p><button class="icon-btn" type="button" data-next aria-label="Next image">' + icon('arrow') + '</button></div>';
      const img = dlg.querySelector('img');
      const cap = dlg.querySelector('p');
      const prev = dlg.querySelector('[data-prev]');

      const show = (i) => {
        index = (i + buttons.length) % buttons.length;
        const src = buttons[index].querySelector('img');
        img.src = src.currentSrc || src.src;
        img.alt = src.alt;
        img.className = Array.from(src.classList).filter((c) => c.indexOf('crop') === 0).join(' ');
        cap.textContent = (index + 1) + ' / ' + buttons.length + ' - ' + src.alt;
      };
      prev.addEventListener('click', () => show(index - 1));
      dlg.querySelector('[data-next]').addEventListener('click', () => show(index + 1));
      dlg.querySelector('.lightbox__close').addEventListener('click', () => dlg.close());
      dlg.addEventListener('keydown', (ev) => {
        const rtl = d.documentElement.getAttribute('dir') === 'rtl';
        if (ev.key === 'ArrowRight') show(index + (rtl ? -1 : 1));
        if (ev.key === 'ArrowLeft') show(index + (rtl ? 1 : -1));
      });
      dlg.addEventListener('click', (ev) => {
        if (ev.target === dlg || ev.target.classList.contains('lightbox__stage')) dlg.close();
      });
      dlg.addEventListener('close', () => { dlg.remove(); trigger.focus(); });
      d.body.appendChild(dlg);
      show(index);
      dlg.showModal();
    });
  });
})();
