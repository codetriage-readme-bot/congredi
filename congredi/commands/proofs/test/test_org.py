#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..org import orgResponders

# pylint: disable=no-self-use


class test_org(unittest.TestCase):
    responderToTest = None

    def setUp(self):
        self.responderToTest = orgResponders()

    def test_org_a(self):
        print('IMPLEMENT tests/test_org')
