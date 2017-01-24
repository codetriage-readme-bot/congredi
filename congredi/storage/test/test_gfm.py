#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
HTML tests
"""
from __future__ import absolute_import
from __future__ import print_function
from ...tests.timing import TimedTestCase
from ...storage.gfm import resolveHtml
from ...tests.sources import source


class test_html(TimedTestCase):
    result_html = None

    def test_html(self):
        """Why do I have HTML resolving when people should do this themselves?"""
        self.threshold = .38
        html = resolveHtml(source)
        print(html)
        self.result_html = html
