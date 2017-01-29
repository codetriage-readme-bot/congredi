#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
client tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from ..client import ClientProtocol, CongrediClient
from ...crypto.RSA import default_rsa


class test_client(TimedTestCase):
    host = "0.0.0.0"
    port = "8800"
    key = default_rsa()

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediClient('a', 'b', 'c')
        self.protocol = ClientProtocol(self.factory, users)
        self.protocol.makeConnection(self.tr)
        super(test_client, self).setUp()

    def test_client(self):
        """Will need to have the client being tested (duplicate from test_run?)"""
        self.threshold = .1
        factory = CongrediClient(self.host, self.port, self.key)
        factory.clientConnectionFailed('ab', 'cd')
        factory.clientConnectionLost('ab', 'cd')
        factory.startedConnecting('ab')
        # key = self.key.publicKey()
        factory.buildProtocol('addr')
        #req = self.protocol.wrapRequest(b'hello', self.key)
        #unwrapped = self.protocol.unwrapRequest(req)
        self.protocol.lineReceived(b'ab')
        self.protocol.lineReceived(b'get')
        self.protocol.connectionMade()

    def test_password(self):
        proto = ClientProtocol(self.host, self.port, clientPass=b'a2')
        assert proto.password == b'a2'
