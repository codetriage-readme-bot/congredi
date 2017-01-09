#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
protocol tests
"""
# pylint: disable=duplicate-code
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from twisted.test.proto_helpers import StringTransport
from ..protocol import CongrediPeerProtocol
from ..factory import CongrediPeerFactory

# https://twistedmatrix.com/documents/current/core/howto/trial.html
# https://twistedmatrix.com/trac/attachment/ticket/3708/test_amp.py
# https://bazaar.launchpad.net/~game-hackers/game/trunk/view/head:/game/test/test_network.py
# pylint: disable=no-self-use


class test_protocol(unittest.TestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)

    def test_protocol(self):
        # a = CongrediPeerProtocol(object, object)
        print('IMPLEMENT tests/test_protocol')
        # self.proto.dataReceived('%s %d %d\r\n' % (operation, a, b))
        # self.assertEqual(int(self.tr.value()), expected)
