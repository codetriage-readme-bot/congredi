#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test logger
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
from ..logger import formatLevel


# pylint: disable=no-self-use
class test_logger(unittest.TestCase):

    def test_logger_level(self):
        """Changing FormatLevel"""
        # need to check if this is logging correctly
        formatLevel('INFO')
