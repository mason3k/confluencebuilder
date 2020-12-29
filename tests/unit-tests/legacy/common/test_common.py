# -*- coding: utf-8 -*-
"""
:copyright: Copyright 2016-2020 Sphinx Confluence Builder Contributors (AUTHORS)
:license: BSD-2-Clause (LICENSE)
"""

from sphinxcontrib.confluencebuilder.std.sphinx import DEFAULT_ALIGNMENT
from tests.lib import EXT_NAME
from tests.lib import assertExpectedWithOutput
from tests.lib import prepare_conf
from tests.lib import prepare_dirs
from tests.lib import prepare_sphinx
import os
import unittest

class TestConfluenceCommon(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.config = prepare_conf()
        test_dir = os.path.dirname(os.path.realpath(__file__))
        dataset = os.path.join(test_dir, 'dataset-common')
        self.expected = os.path.join(test_dir, 'expected')

        doc_dir = prepare_dirs('common')
        self.doc_dir = doc_dir

        with prepare_sphinx(dataset, config=self.config, out_dir=doc_dir) as app:
            app.build(force_all=True)

            # track registered extensions
            if hasattr(app, 'extensions'):
                self.extensions = list(app.extensions.keys())
            else:
                self.extensions = list(app._extensions.keys())

    def _assertExpectedWithOutput(self, name, expected=None):
        expected = expected if expected else self.expected
        assertExpectedWithOutput(self, name, expected, self.doc_dir)

    def test_legacy_attribution(self):
        self._assertExpectedWithOutput('attribution')

    def test_legacy_bibliographic(self):
        self._assertExpectedWithOutput('bibliographic')

    def test_legacy_block_quotes(self):
        self._assertExpectedWithOutput('block-quotes')

    def test_legacy_citations(self):
        self._assertExpectedWithOutput('citations')

    def test_legacy_definition_lists(self):
        self._assertExpectedWithOutput('definition-lists')

    def test_legacy_epigraph(self):
        self._assertExpectedWithOutput('epigraph')

    def test_legacy_figure(self):
        if DEFAULT_ALIGNMENT == 'center':
            expected = self.expected + '-center'
            self._assertExpectedWithOutput('figure', expected)
        else:
            self._assertExpectedWithOutput('figure')

    def test_legacy_footnotes(self):
        self._assertExpectedWithOutput('footnotes')

    def test_legacy_image(self):
        self._assertExpectedWithOutput('image')

    def test_legacy_lists(self):
        self._assertExpectedWithOutput('lists')

    def test_legacy_list_table(self):
        self._assertExpectedWithOutput('list-table')

    def test_legacy_markup(self):
        self._assertExpectedWithOutput('markup')

    def test_legacy_option_lists(self):
        self._assertExpectedWithOutput('option-lists')

    def test_legacy_parsed_literal(self):
        self._assertExpectedWithOutput('parsed-literal')

    def test_legacy_references(self):
        self._assertExpectedWithOutput('references')
        self._assertExpectedWithOutput('references-ref')

    def test_legacy_registry(self):
        # validate builder's registration into Sphinx
        self.assertTrue(EXT_NAME in self.extensions)

    def test_legacy_table(self):
        self._assertExpectedWithOutput('tables')
