/* Native links work without JavaScript; keep the current section when switching. */
(() => {
  const links = Array.from(document.querySelectorAll('[data-language-link]'));
  const updateLinks = () => links.forEach(link => {
    const destination = new URL(link.href, window.location.href);
    destination.hash = window.location.hash;
    link.href = destination.href;
  });
  updateLinks();
  window.addEventListener('hashchange', updateLinks);
})();
