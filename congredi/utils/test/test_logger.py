#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test logger
"""
import unittest
from ..logger import setLog


class test_logger(unittest.TestCase):

    def test_logger(self):
        # need to check if this is logging correctly
        setLog('INFO')
