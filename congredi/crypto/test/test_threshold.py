#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ThresholdPGP tests...
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..threshold import ThresholdPGP


class test_threshold(TimedTestCase):
    sigGen = None

    def setUp(self):
        self.sigGen = ThresholdPGP()
        super(test_threshold, self).setUp()

    def test_threshold_generate(self):
        """Call init, sign"""
        self.sigGen.generate()
        print('IMPLEMENT crypto/test/test_threshold')

    def test_threshold_sign(self):
        """Call init, sign"""
        self.sigGen.sign(None)
        print('IMPLEMENT crypto/test/test_threshold')
