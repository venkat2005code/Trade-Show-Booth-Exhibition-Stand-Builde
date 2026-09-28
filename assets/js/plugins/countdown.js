/* countdown.js: launch countdown for coming-soon.html.
   Set the target with data-countdown="2026-12-15T09:00:00" (local time). */
(function () {
  'use strict';

  const box = document.querySelector('[data-countdown]');
  if (!box) return;
  const target = new Date(box.getAttribute('data-countdown')).getTime();
  const cells = {};
  box.querySelectorAll('[data-cd]').forEach((el) => { cells[el.getAttribute('data-cd')] = el; });
  const pad = (n) => String(n).padStart(2, '0');

  function tick() {
    let left = Math.max(0, target - Date.now());
    const days = Math.floor(left / 86400000); left -= days * 86400000;
    const hours = Math.floor(left / 3600000); left -= hours * 3600000;
    const minutes = Math.floor(left / 60000); left -= minutes * 60000;
    const seconds = Math.floor(left / 1000);
    if (cells.days) cells.days.textContent = pad(days);
    if (cells.hours) cells.hours.textContent = pad(hours);
    if (cells.minutes) cells.minutes.textContent = pad(minutes);
    if (cells.seconds) cells.seconds.textContent = pad(seconds);
    if (target - Date.now() <= 0) { clearInterval(timer); box.setAttribute('aria-label', 'Launch time reached'); }
  }
  const timer = setInterval(tick, 1000);
  tick();
})();
