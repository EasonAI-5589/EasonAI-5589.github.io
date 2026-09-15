/* Both collections remain readable through native anchor links without JavaScript. */
(() => {
  document.querySelectorAll('[data-work-switcher]').forEach(switcher => {
    const tabs = Array.from(switcher.querySelectorAll('[data-work-tab]'));
    const panels = Array.from(switcher.querySelectorAll('[data-work-panel]'));
    const tablist = switcher.querySelector('[data-work-tablist]');
    const aliases = {
      'selected-work': 'selected', 'selected-work-panel': 'selected',
      publications: 'selected', completed: 'selected',
      projects: 'ongoing', ongoing: 'ongoing', 'ongoing-projects': 'ongoing'
    };
    tablist.setAttribute('role', 'tablist');
    tabs.forEach(tab => tab.setAttribute('role', 'tab'));
    panels.forEach(panel => {
      panel.setAttribute('role', 'tabpanel');
      panel.tabIndex = 0;
    });

    const activate = group => {
      tabs.forEach(tab => {
        const selected = tab.dataset.workTab === group;
        tab.setAttribute('aria-selected', String(selected));
        tab.tabIndex = selected ? 0 : -1;
      });
      panels.forEach(panel => { panel.hidden = panel.dataset.workPanel !== group; });
    };

    const followHash = (initial = false) => {
      let id;
      try { id = decodeURIComponent(window.location.hash.slice(1)); }
      catch { return; }
      const target = document.getElementById(id);
      const panel = target && target.closest('[data-work-panel]');
      const group = panel && switcher.contains(panel) ? panel.dataset.workPanel : aliases[id];
      if (!group) {
        if (initial) activate('selected');
        return;
      }
      const revealTarget = panel && target !== panel && (initial || panel.hidden);
      activate(group);
      // A browser cannot scroll to an anchor inside a hidden panel until it is revealed.
      if (revealTarget) requestAnimationFrame(() => target.scrollIntoView({block: 'start'}));
    };

    const choose = tab => {
      activate(tab.dataset.workTab);
      const hash = tab.getAttribute('href');
      if (window.location.hash !== hash) {
        // Keep the controls in place; native hash navigation would scroll past them.
        window.history.pushState(null, '', hash);
        // Language links also follow the current collection.
        window.dispatchEvent(new Event('hashchange'));
      }
    };

    tabs.forEach((tab, index) => {
      tab.addEventListener('click', event => {
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        choose(tab);
      });
      tab.addEventListener('keydown', event => {
        let next;
        if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
        if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = tabs.length - 1;
        if (event.key === ' ') next = index;
        if (next === undefined) return;
        event.preventDefault();
        choose(tabs[next]);
        tabs[next].focus();
      });
    });
    followHash(true);
    window.addEventListener('hashchange', () => followHash());
  });
})();
