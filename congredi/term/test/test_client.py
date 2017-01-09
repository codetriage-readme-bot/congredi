#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
client tests
"""
import unittest
from ..client import ClientProtocol, CongrediClient


# pylint: disable=no-self-use, unused-variable
class test_client(unittest.TestCase):

    def test_client(self):
        factory = CongrediClient()
        protocol = ClientProtocol()
        print('Well, this one will be interesting')
