#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
client tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..client import ClientProtocol, CongrediClient


class test_client(TimedTestCase):
    host = "0.0.0.0"
    port = "8800"
    key = "abab"

    def test_client(self):
        """Will need to have the client being tested (duplicate from test_run?)"""
        self.threshold = .1
        factory = CongrediClient(self.host, self.port, self.key)
        protocol = ClientProtocol(self.host, self.port, self.key)
        print('Well, this one will be interesting')
        assert protocol != factory
