#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from twisted.test.proto_helpers import StringTransport
from ...factory import CongrediPeerFactory
from ...protocol import CongrediPeerProtocol
from ..http import app, key


class test_http(TimedTestCase):

    def setUp(self):
        # https://github.com/twisted/klein/blob/master/src/klein/test/test_app.py
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)
        super(test_http, self).setUp()

    def test_http(self):
        """Klein has a few test case examples"""
        print('IMPLEMENT term/test/test_http StringTransport')
        self.threshold = .1
        a = app
        k = key
        assert a != k
