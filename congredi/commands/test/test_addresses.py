#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..addresses import addressesResponders


class test_addresses(TimedTestCase):

    responderToTest = None

    def setUp(self):
        self.responderToTest = addressesResponders()
        super(test_addresses, self).setUp()

    def test_addresses_a(self):
        self.responderToTest.AddressTell()
        print('IMPLEMENT tests/test_setting')
