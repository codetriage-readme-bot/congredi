#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
protocol tests
"""
import unittest
from ..protocol import CongrediPeerProtocol


class test_protocol(unittest.TestCase):

    def test_protocol(self):
        a = CongrediPeerProtocol(object, object)
        print('IMPLEMENT tests/test_protocol')
