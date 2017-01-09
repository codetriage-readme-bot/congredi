#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
client tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..client import ClientProtocol, CongrediClient


# pylint: disable=no-self-use, unused-variable
class test_client(unittest.TestCase):
    host = "0.0.0.0"
    port = "8800"
    key = "abab"

    def test_client(self):
        factory = CongrediClient(self.host, self.port, self.key)
        protocol = ClientProtocol(self.host, self.port, self.key)
        print('Well, this one will be interesting')
