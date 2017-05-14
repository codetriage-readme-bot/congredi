#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testing coordination code

    Again, will need to simplify this.
client tests

    Can /technically/ execute StringTransport, while the actual connections
    have problems these tests are finding.
Runner tests

    again, simplify API

    tests will run consecutive store/retrieves on good/bad values

    a partial integration test, but peer-peer AMP has a regression
    that's not in StringTransport :/
Runner tests

    need to call Run() functions in a testing framework

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .utils import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from .main import ClientProtocol, CongrediClient
from .crypto import default_rsa
from .main import app, key
from .main import get_auths, next_key, check_online
from .main import set_value, get_value, tell_index, search_term
import os
from .main import fileCoord


def prep():
    try:
        os.remove('b')
    except OSError:
        pass


class test_coord(TimedTestCase):

    def test_coord(self):
        """Coordination code workarounds"""
        self.threshold = .1
        prep()
        h, p = fileCoord.read('b')
        fileCoord.write(h, p, 'b')
        nh, np = fileCoord.read('b')
        assert nh == h
        assert np == p
        prep()


class test_run(TimedTestCase):

    def setUp(self):
        self.tr = StringTransport()
        # users = ['a', 'b']
        # self.factory = CongrediPeerFactory()
        # self.proto = CongrediPeerProtocol(self.factory, users)
        # self.proto.makeConnection(self.tr)
        # client = CongrediClient(
        #     host="0.0.0.0", port="9000",
        #     clientKey=None)
        super(test_run, self).setUp()

    def test_run(self):
        """Will need to look at how twisted runs their tests"""
        self.threshold = .1
        print('IMPLEMENT term/test/test_run StringTransport')




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
