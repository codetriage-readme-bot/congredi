#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factory tests
"""
# pylint: disable=duplicate-code
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from twisted.test.proto_helpers import StringTransport
from ..factory import CongrediPeerFactory
from ..protocol import CongrediPeerProtocol


# pylint: disable=no-self-use
class test_factory(unittest.TestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)

    def test_factory(self):
        a = CongrediPeerFactory()

        a.startedConnecting('well then')
        print('IMPLEMENT tests/test_factory')
