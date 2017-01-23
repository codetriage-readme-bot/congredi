#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..user import userResponders

# pylint: disable=no-self-use


class test_addresses(unittest.TestCase):
    responderToTest = None

    def SetUp(self):
        self.responderToTest = userResponders()

    def test_addresses_a(self):
        print('IMPLEMENT tests/test_user')
