#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factory tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .timing import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from ..factory import CongrediPeerFactory
from ..protocol import CongrediPeerProtocol


class test_factory(TimedTestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)
        super(test_factory, self).setUp()

    def test_factory(self):
        """Make sure everything is in order..."""
        self.threshold = .1
        a = CongrediPeerFactory()

        a.startedConnecting('well then')
        print('IMPLEMENT tests/test_factory with StringTransport')
