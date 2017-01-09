#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ThresholdPGP tests...
"""
import unittest
from ..threshold import ThresholdPGP


# pylint: disable=no-self-use
class test_threshold(unittest.TestCase):

    def test_threshold(self):
        thresh = ThresholdPGP()
        thresh.sign(None)
        print('IMPLEMENT crypto/test/test_threshold')
