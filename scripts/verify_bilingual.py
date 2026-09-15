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
import unittest

ROOT = Path(sys.argv.pop(1) if len(sys.argv) > 1 else '_site')

class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.lang = None
        self.links = []
        self.ids = []
        self.papers = []
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
            'switcher': None, 'panel': None, 'tab': None, 'aria_hidden': False,
        }
        context['tag'] = tag
        context['aria_hidden'] = context['aria_hidden'] or data.get('aria-hidden') == 'true'
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
                self.assertEqual(len(entries), 6, 'All selected works need project entry cards')
                for entry in entries:
                    expected_images = 0 if entry['id'] == 'qwan' else 1
                    self.assertEqual(len(entry['images']), expected_images)
                    self.assertEqual(entry['details'], 0, 'Entry cards should navigate, not expand inline')
                    actions = [a for a in entry['links'] if 'data-project-entry' in a]
                    expected_actions = 2 if entry['id'] == 'qwan' else 3
                    self.assertEqual(len(actions), expected_actions, 'Available card actions should open the same project page')
                    targets = {a.get('href') for a in actions}
                    self.assertEqual(len(targets), 1)
                    url = urlsplit(next(iter(targets)))
                    self.assertNotEqual(url.hostname, 'arxiv.org', 'A paper link is not a project page')
                    self.assertNotIn(url.path.rsplit('.', 1)[-1], ['png', 'svg', 'jpg'])
                    self.assertTrue(url.path not in ['', '/'], 'Project entry must have a real destination')
                    if not url.hostname:
                        self.assertTrue((ROOT / url.path.strip('/') / 'index.html').is_file(), f'Broken project destination: {url.path}')

    def test_qwan_opens_the_confirmed_github_repository(self):
        expected = 'https://github.com/Haohaha-11/qwan-physworldai-2026'
        for route in ['/', '/zh/', '/projects/', '/zh/projects/']:
            with self.subTest(route=route):
                entries = [entry for entry in self.page(route).entries if entry['id'] == 'qwan']
                self.assertEqual(len(entries), 1, 'qwan must appear once on every project surface')
                actions = [a for a in entries[0]['links'] if 'data-project-entry' in a]
                self.assertEqual({a.get('href') for a in actions}, {expected})

    def test_work_panels_keep_selected_and_ongoing_entries_separate(self):
        expected = {
            'selected': ['paper-starpro', 'paper-worldecho-worldsync',
                         'paper-safedojo', 'paper-regimevggt'],
            'ongoing': ['inferencenet', 'qwan'],
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
        pairs = ['/', '/publications/', '/projects/', '/projects/safedojo/', '/projects/regimevggt/']
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

if __name__ == '__main__': unittest.main()
