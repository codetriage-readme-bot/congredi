#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ..timedTests import TimedTestCase
from ..oracle import phony, hexify, random, pick_range


class test_censor_harness(TimedTestCase):

    def test_random(self):
        """No actual test, just if functions run..."""
        self.threshold = .1
        sentance = phony(hexify(random()))
        type(sentance)

    def test_range(self):
        """no assert"""
        self.threshold = .1
        ranges = pick_range(10)
        type(ranges[1])
