/* Keep all news readable when JavaScript is unavailable. */
(() => {
  const list = document.querySelector('[data-news-list]');
  const button = document.querySelector('[data-news-toggle]');
  if (!list || !button) return;
  const now = new Date();
  // Month-precision announcements: current month plus the previous five.
  const cutoff = now.getFullYear() * 12 + now.getMonth() - 5;
  const older = Array.from(list.querySelectorAll('[data-news-date]')).filter(item => {
    const match = /^(\d{4})-(0[1-9]|1[0-2])$/.exec(item.dataset.newsDate);
    return match && Number(match[1]) * 12 + Number(match[2]) - 1 < cutoff;
  });
  if (!older.length) return;
  let expanded = false;
  const render = () => {
    older.forEach(item => { item.hidden = !expanded; });
    button.setAttribute('aria-expanded', String(expanded));
    button.textContent = expanded ? button.dataset.collapseLabel : button.dataset.expandLabel;
  };
  button.addEventListener('click', () => { expanded = !expanded; render(); });
  list.classList.add('news-list--collapsible');
  render();
  button.hidden = false;
})();
