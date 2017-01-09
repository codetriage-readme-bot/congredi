#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test logger
"""
import unittest
from ..logger import formatLevel


# pylint: disable=no-self-use
class test_logger(unittest.TestCase):

    def test_logger_level(self):
        # need to check if this is logging correctly
        formatLevel('INFO')
