#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
protocol tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ..tests.timing import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from ..protocol import CongrediPeerProtocol
from ..factory import CongrediPeerFactory

# https://twistedmatrix.com/documents/current/core/howto/trial.html
# https://twistedmatrix.com/trac/attachment/ticket/3708/test_amp.py
# https://bazaar.launchpad.net/~game-hackers/game/trunk/view/head:/game/test/test_network.py

# class mock_transport(object):
#     def write(self, obj):
#         print(obj)
#     def getPeer(self):
#         return 'ab'


class test_protocol(TimedTestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.port = 8080
        self.proto.host = '0.0.0.0'
        self.proto.makeConnection(self.tr)
        self.proto.transport = self.tr
        super(test_protocol, self).setUp()

    def test_protocol(self):
        """Make sure everything is in order..."""
        self.threshold = .1
        # self.assertEqual(int(self.tr.value()), expected)
        self.proto.gotit(b'hello', b'8080')
        self.proto.hello(b'hello', b'8080')
        # self.proto.lineReceived('one')
        self.proto.dataReceived(b'two')
        self.proto.connectionLost(b'reason')
        # self.proto.connectionMade()
        # mock_one = mock_transport
        self.proto.makeConnection(self.tr)
        # self.proto.incomingConnectionBegin('data')
