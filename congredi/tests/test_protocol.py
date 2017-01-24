#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
protocol tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .timing import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from ..protocol import CongrediPeerProtocol
from ..factory import CongrediPeerFactory

# https://twistedmatrix.com/documents/current/core/howto/trial.html
# https://twistedmatrix.com/trac/attachment/ticket/3708/test_amp.py
# https://bazaar.launchpad.net/~game-hackers/game/trunk/view/head:/game/test/test_network.py


class test_protocol(TimedTestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)
        super(test_protocol, self).setUp()

    def test_protocol(self):
        """Make sure everything is in order..."""
        # a = CongrediPeerProtocol(object, object)
        self.threshold = .1
        print('IMPLEMENT tests/test_protocol with StringTransport')
        # self.proto.dataReceived('%s %d %d\r\n' % (operation, a, b))
        # self.assertEqual(int(self.tr.value()), expected)
