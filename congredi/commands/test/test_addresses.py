#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..addresses import addressesResponders
from ...storage.MockRedis import RedisMock


class test_addresses(TimedTestCase):

    responderToTest = None

    def setUp(self):
        mock = RedisMock()
        self.responderToTest = addressesResponders(mock)
        super(test_addresses, self).setUp()

    def test_addresses_a(self):
        self.responderToTest.AddressTell()
        print('IMPLEMENT tests/test_setting')
