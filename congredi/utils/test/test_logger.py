#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test logger
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..logger import formatLevel


class test_logger(TimedTestCase):

    def test_logger_level(self):
        """Changing FormatLevel"""
        # need to check if this is logging correctly
        self.threshold = .4
        formatLevel('INFO')
