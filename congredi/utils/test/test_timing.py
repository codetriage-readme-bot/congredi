#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Timing tests, not using assert (need to test color?)
"""
from ..timing import TimedTestCase
import time


class test_timing(TimedTestCase):

    def test_example_no_warning(self):
        self.threshold = 3
        time.sleep(2)

    def test_example_warning(self):
        self.threshold = 1
        time.sleep(2)
