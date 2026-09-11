/* Apply the saved choice before styles load; Auto follows the operating system. */
(() => {
  const key = 'yichen-color-theme';
  const valid = value => ['light', 'dark', 'system'].includes(value);
  let choice = 'system';
  try {
    const saved = localStorage.getItem(key);
    if (valid(saved)) choice = saved;
  } catch (_) { /* Theme selection still works when storage is unavailable. */ }
  const apply = () => {
    if (choice === 'system') document.documentElement.removeAttribute('data-theme');
    else document.documentElement.setAttribute('data-theme', choice);
    document.querySelectorAll('[data-theme-choice]').forEach(button => {
      button.setAttribute('aria-pressed', String(button.dataset.themeChoice === choice));
    });
  };
  apply();
  document.addEventListener('DOMContentLoaded', () => {
    const controls = document.querySelector('.theme-switch');
    if (!controls) return;
    controls.hidden = false;
    apply();
    controls.addEventListener('click', event => {
      const button = event.target.closest('[data-theme-choice]');
      if (!button || !controls.contains(button)) return;
      choice = button.dataset.themeChoice;
      apply();
      try { localStorage.setItem(key, choice); } catch (_) { /* Optional persistence. */ }
    });
  });
  window.addEventListener('storage', event => {
    if (event.key !== key && event.key !== null) return;
    choice = valid(event.newValue) ? event.newValue : 'system';
    apply();
  });
})();
