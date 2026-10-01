#!/usr/bin/env python3
"""Check built language routes and navigation, without browser dependencies.

Catches accidental English fallback, language links to the wrong section,
missing translations, and filtering the full archive as selected work.
Run after Jekyll: python3 scripts/verify_bilingual.py [_site]
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
import sys
import struct
import unittest

ROOT = Path(sys.argv.pop(1) if len(sys.argv) > 1 else '_site')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.lang = None
        self.links = []
        self.ids = []
        self.papers = []
        self.paper_details = {}
        self.text = []
        self.images = []
        self.entries = []
        self.entry = None
        self.work_switchers = []
        self.work_tabs = []
        self.work_panels = []
        self._elements = []
        self.feed(path.read_text())
    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        context = dict(self._elements[-1]) if self._elements else {
            'switcher': None, 'panel': None, 'tab': None, 'paper': None, 'aria_hidden': False,
        }
        context['tag'] = tag
        context['aria_hidden'] = context['aria_hidden'] or data.get('aria-hidden') == 'true'
        if 'pub-item' in data.get('class', '').split():
            context['paper'] = {'text': [], 'images': []}
            self.paper_details[data.get('id')] = context['paper']
        if tag == 'img':
            self.images.append(data)
            if context['paper'] is not None:
                context['paper']['images'].append(data)
        if 'data-work-switcher' in data:
            context['switcher'] = {'tabs': [], 'panels': []}
            self.work_switchers.append(context['switcher'])
        if 'data-work-panel' in data:
            context['panel'] = {'attrs': data, 'entries': []}
            self.work_panels.append(context['panel'])
            if context['switcher'] is not None:
                context['switcher']['panels'].append(context['panel'])
        if 'data-work-tab' in data:
            context['tab'] = {'tag': tag, 'attrs': data, 'label': ''}
            self.work_tabs.append(context['tab'])
            if context['switcher'] is not None:
                context['switcher']['tabs'].append(context['tab'])
        if tag == 'article' and 'work-entry' in data.get('class', '').split():
            self.entry = {'id': data.get('id'), 'links': [], 'images': [], 'details': 0}
            self.entries.append(self.entry)
            if context['panel'] is not None:
                context['panel']['entries'].append(self.entry)
        if self.entry is not None:
            if tag == 'a': self.entry['links'].append(data)
            if tag == 'img' and 'resource-icon' not in data.get('class', '').split():
                self.entry['images'].append(data)
            if tag == 'details': self.entry['details'] += 1
        if tag == 'html': self.lang = data.get('lang')
        if tag == 'a': self.links.append(data)
        if data.get('id'): self.ids.append(data['id'])
        if 'pub-item' in data.get('class', '').split(): self.papers.append(data.get('id'))
        if tag not in {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
                       'link', 'meta', 'param', 'source', 'track', 'wbr'}:
            self._elements.append(context)

    def handle_data(self, data):
        if self._elements and not self._elements[-1]['aria_hidden']:
            self.text.append(data)
            if self._elements[-1]['paper'] is not None:
                self._elements[-1]['paper']['text'].append(data)
        if (self._elements and not self._elements[-1]['aria_hidden']
                and self._elements[-1]['tab'] is not None):
            self._elements[-1]['tab']['label'] += data

    def handle_endtag(self, tag):
        if tag == 'article': self.entry = None
        for index in range(len(self._elements) - 1, -1, -1):
            if self._elements[index]['tag'] == tag:
                del self._elements[index:]
                break

class BilingualRoutes(unittest.TestCase):
    def page(self, route):
        path = ROOT / route.strip('/') / 'index.html'
        self.assertTrue(path.is_file(), f'Missing rendered page: {route}')
        return Page(path)

    def test_each_homepage_image_and_title_open_the_project_page(self):
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                entries = self.page(route).entries
                self.assertEqual(len(entries), 6, 'All listed works need project entry cards')
                for entry in entries:
                    self.assertEqual(len(entry['images']), 1)
                    self.assertEqual(entry['details'], 0, 'Entry cards should navigate, not expand inline')
                    actions = [a for a in entry['links'] if 'data-project-entry' in a]
                    self.assertEqual(len(actions), 3, 'Available card actions should open the same project page')
                    targets = {a.get('href') for a in actions}
                    self.assertEqual(len(targets), 1)
                    url = urlsplit(next(iter(targets)))
                    self.assertNotEqual(url.hostname, 'arxiv.org', 'A paper link is not a project page')
                    self.assertNotIn(url.path.rsplit('.', 1)[-1], ['png', 'svg', 'jpg'])
                    self.assertTrue(url.path not in ['', '/'], 'Project entry must have a real destination')
                    if not url.hostname:
                        self.assertTrue((ROOT / url.path.strip('/') / 'index.html').is_file(), f'Broken project destination: {url.path}')

    def test_qwan_is_not_listed_on_public_project_surfaces(self):
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                page = self.page(route)
                self.assertNotIn('qwan', page.ids)
                self.assertFalse(any('qwan-physworldai-2026' in a.get('href', '') for a in page.links))

    def test_work_panels_keep_selected_and_ongoing_entries_separate(self):
        expected = {
            'selected': ['paper-starpro', 'paper-worldecho-worldsync', 'paper-mico',
                         'paper-safedojo', 'paper-regimevggt'],
            'ongoing': ['inferencenet'],
        }
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                p = self.page(route)
                self.assertEqual([panel['attrs'].get('data-work-panel')
                                  for panel in p.work_panels], list(expected))
                for panel in p.work_panels:
                    group = panel['attrs']['data-work-panel']
                    self.assertEqual([entry['id'] for entry in panel['entries']],
                                     expected[group], f'Incorrect {group} group or order')

    def test_work_tabs_link_to_their_panels_without_javascript(self):
        expected = {'selected': 'selected-work-panel', 'ongoing': 'ongoing-projects'}
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                p = self.page(route)
                self.assertEqual(len(p.work_switchers), 1)
                switcher = p.work_switchers[0]
                self.assertEqual(len(p.work_tabs), 2)
                self.assertEqual(len(p.work_panels), 2)
                self.assertEqual(switcher['tabs'], p.work_tabs)
                self.assertEqual(switcher['panels'], p.work_panels)
                self.assertEqual([tab['attrs'].get('data-work-tab')
                                  for tab in p.work_tabs], list(expected))
                panels = {panel['attrs'].get('data-work-panel'): panel['attrs']
                          for panel in p.work_panels}
                self.assertEqual(set(panels), set(expected))
                for tab in p.work_tabs:
                    group = tab['attrs']['data-work-tab']
                    panel_id = expected[group]
                    self.assertEqual(tab['tag'], 'a', 'Fallback tabs must be usable links')
                    self.assertEqual(tab['attrs'].get('href'), '#' + panel_id)
                    self.assertEqual(tab['attrs'].get('aria-controls'), panel_id)
                    self.assertEqual(panels[group].get('id'), panel_id)
                    self.assertNotIn('hidden', panels[group], 'Both groups must be readable without JavaScript')
                    self.assertNotEqual(panels[group].get('aria-hidden'), 'true')

    def test_work_tab_labels_are_translated(self):
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                expected = (['代表工作', '进行中项目'] if route.startswith('/zh/')
                            else ['Selected Work', 'Ongoing Projects'])
                labels = [' '.join(tab['label'].split()) for tab in self.page(route).work_tabs]
                self.assertEqual(labels, expected)

    def test_work_surfaces_have_unique_anchors(self):
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                ids = self.page(route).ids
                self.assertEqual(len(ids), len(set(ids)), 'Duplicate anchors break tab and project navigation')

    def test_language_switch_keeps_same_page(self):
        pairs = ['/', '/publications/', '/projects/', '/projects/mico/', '/projects/safedojo/', '/projects/regimevggt/']
        cases = [(route, '/zh' + route, 'en') for route in pairs]
        cases += [('/zh' + route, route, 'zh-CN') for route in pairs]
        for route, counterpart, lang in cases:
            with self.subTest(route=route):
                p = self.page(route)
                self.assertEqual(p.lang, lang)
                switch = [a for a in p.links if 'data-language-link' in a]
                self.assertTrue(any(urlsplit(a.get('href', '')).path == counterpart for a in switch), f'No counterpart language link from {route} to {counterpart}')

    def test_local_navigation_stays_in_chosen_language(self):
        for route, home, archive in [('/', '/', '/publications/'), ('/zh/', '/zh/', '/zh/publications/')]:
            with self.subTest(route=route):
                links = {a.get('href') for a in self.page(route).links}
                self.assertIn(home + '#selected-work', links)
                self.assertIn(home + '#experience', links)
                self.assertIn(archive, links)

    def test_translation_keeps_paper_identity_and_full_archive(self):
        en, zh = self.page('/'), self.page('/zh/')
        self.assertEqual(en.papers, zh.papers)
        full_en, full_zh = self.page('/publications/'), self.page('/zh/publications/')
        self.assertEqual(full_en.papers, full_zh.papers)
        self.assertLess(len(en.papers), len(full_en.papers))
        for p in [en, zh, full_en, full_zh]:
            self.assertEqual(len(p.ids), len(set(p.ids)), 'Duplicate anchors break navigation')
            self.assertGreater(len(p.papers), 0)

    def test_mico_paper_link_is_available_in_both_languages(self):
        for route in ['/', '/zh/', '/projects/', '/zh/projects/',
                      '/publications/', '/zh/publications/',
                      '/projects/mico/', '/zh/projects/mico/']:
            with self.subTest(route=route):
                page = self.page(route)
                self.assertTrue(any(a.get('href') == 'https://arxiv.org/abs/2609.34330'
                                    for a in page.links), f'Missing MICO paper link: {route}')
                if not route.endswith('/mico/'):
                    self.assertIn('paper-mico', page.papers)

    def test_mico_has_real_figures_ordered_authors_and_complete_project_pages(self):
        authors = ('Tinghao Wang, Yichen Guo, Qizhe Zhang, Yuan Zhang, '
                   'Weimin Ouyang, Rui Huang, Jiajun Cao, Sixiang Chen, '
                   'Hao Jiang, Jixian Wu, Zheng Lu, Bofan Zhu, Renyuan Li, '
                   'Shanghang Zhang')
        title = ('MiCo: Mutual Information Coverage Optimization through '
                 'Semantic Erasure Modeling for Efficient MLLM Inference')
        hero = '/assets/research/mico-method.png'
        experiment = '/assets/research/mico-efficiency.png'
        for route in ['/', '/zh/', '/projects/', '/zh/projects/',
                      '/publications/', '/zh/publications/',
                      '/projects/mico/', '/zh/projects/mico/']:
            with self.subTest(route=route):
                page = self.page(route)
                if route.endswith('/mico/'):
                    text = ' '.join(''.join(page.text).split())
                    images = page.images
                    for section in ['overview', 'method', 'evaluation', 'resources']:
                        self.assertIn(section, page.ids)
                    self.assertIn(experiment, [img.get('src') for img in images])
                    self.assertTrue(any(a.get('href') == 'https://arxiv.org/html/2609.34330v2'
                                        for a in page.links))
                    self.assertGreater(len(text), 900, 'Project page still contains only a placeholder')
                else:
                    paper = page.paper_details['paper-mico']
                    text = ' '.join(''.join(paper['text']).split())
                    images = paper['images']
                    self.assertIn(title, text)
                self.assertIn(authors, text, 'Missing or reordered MiCo authors')
                self.assertIn('共同第一作者' if route.startswith('/zh/')
                              else 'Co-first author', text)
                self.assertIn(hero, [img.get('src') for img in images])
                self.assertFalse(any('mico-cover.svg' in img.get('src', '') for img in images))
                for img in images:
                    if img.get('src') not in [hero, experiment]:
                        continue
                    asset = ROOT / img['src'].lstrip('/')
                    with asset.open('rb') as handle:
                        header = handle.read(24)
                    self.assertEqual(header[:8], b'\x89PNG\r\n\x1a\n')
                    self.assertEqual(struct.unpack('>II', header[16:24]),
                                     (int(img['width']), int(img['height'])))

if __name__ == '__main__': unittest.main()
