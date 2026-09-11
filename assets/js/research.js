/* Progressive enhancement: original figures remain links; videos retain native controls. */
document.querySelectorAll('[data-figure-tabs]').forEach(group => {
  const tabs = Array.from(group.querySelectorAll('[role="tab"]'));
  const activate = tab => {
    tabs.forEach(item => {
      const selected = item === tab;
      item.setAttribute('aria-selected', String(selected));
      item.tabIndex = selected ? 0 : -1;
      document.getElementById(item.getAttribute('aria-controls')).hidden = !selected;
    });
  };
  tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => activate(tab));
    tab.addEventListener('keydown', event => {
      let next;
      if (event.key === 'ArrowRight') next = (index + 1) % tabs.length;
      if (event.key === 'ArrowLeft') next = (index - 1 + tabs.length) % tabs.length;
      if (event.key === 'Home') next = 0;
      if (event.key === 'End') next = tabs.length - 1;
      if (next === undefined) return;
      event.preventDefault();
      activate(tabs[next]);
      tabs[next].focus();
    });
  });
});

const figureDialog = document.querySelector('.figure-dialog');
if (figureDialog && typeof figureDialog.showModal === 'function') {
  const image = figureDialog.querySelector('img');
  const title = figureDialog.querySelector('#figure-dialog-title');
  document.querySelectorAll('[data-zoom]').forEach(link => {
    link.addEventListener('click', event => {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      image.src = link.href;
      image.alt = link.querySelector('img').alt;
      title.textContent = link.getAttribute('aria-label') || image.alt;
      figureDialog.showModal();
      const scroll = figureDialog.querySelector('.dialog-scroll');
      scroll.scrollTop = 0;
      scroll.scrollLeft = 0;
    });
  });
  figureDialog.querySelector('[data-close-dialog]').addEventListener('click', () => figureDialog.close());
  figureDialog.addEventListener('click', event => {
    const rect = figureDialog.getBoundingClientRect();
    if (event.target === figureDialog && (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom)) figureDialog.close();
  });
}

document.querySelectorAll('[data-demo]').forEach(demo => {
  const videos = Array.from(demo.querySelectorAll('[data-demo-video]'));
  const scene = demo.querySelector('[data-demo-scene]');
  const playButton = demo.querySelector('[data-play-all]');
  const status = demo.querySelector('[role="status"]');
  const labels = {gt:'Simulator ground truth', collapse:'Model output with visual collapse', mismatch:'Model output with action mismatch'};
  let revision = 0;
  scene.addEventListener('change', () => {
    revision += 1;
    videos.forEach(video => {
      video.pause();
      const base = demo.dataset.assetBase + scene.value + '-' + video.dataset.demoVideo;
      video.poster = base + '.png';
      video.querySelector('source').src = base + '.mp4';
      video.setAttribute('aria-label', labels[video.dataset.demoVideo] + ' for ' + scene.selectedOptions[0].textContent);
      video.load();
    });
    status.textContent = 'Scene ready. Press play to compare.';
    playButton.innerHTML = '<span aria-hidden="true">▶</span> Play comparison';
    playButton.disabled = false;
  });
  playButton.addEventListener('click', async () => {
    const startedRevision = revision;
    playButton.disabled = true;
    status.textContent = 'Loading clips…';
    const results = await Promise.allSettled(videos.map(video => {
      video.currentTime = 0;
      return video.play();
    }));
    if (startedRevision !== revision) return;
    status.textContent = results.some(result => result.status === 'rejected') ? 'Use the individual video controls to play a clip.' : 'Playing recorded comparison.';
    playButton.innerHTML = '<span aria-hidden="true">↻</span> Replay comparison';
    playButton.disabled = false;
  });
  videos.forEach(video => video.addEventListener('ended', () => {
    if (videos.every(item => item.ended)) status.textContent = 'Comparison finished. Replay to inspect the motion.';
  }));
  document.addEventListener('visibilitychange', () => {
    if (document.hidden) videos.forEach(video => video.pause());
  });
});
