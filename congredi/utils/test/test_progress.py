#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
progress test (count to 1000)
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..progress import together


class test_progress(TimedTestCase):

    def test_prog(self):
        self.threshold = 0.1
        together(1000)
