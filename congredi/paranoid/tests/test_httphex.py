#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from twisted.test.proto_helpers import StringTransport
import binascii
from ...utils.timedTests import TimedTestCase
from ..httphex import app, hex_compat


class test_http(TimedTestCase):

    def setUp(self):
        # https://github.com/twisted/klein/blob/master/src/klein/test/test_app.py
        self.tr = StringTransport()
        # users = ['a', 'b']
        # self.factory = CongrediPeerFactory()
        # self.proto = CongrediPeerProtocol(self.factory, users)
        # self.proto.makeConnection(self.tr)
        super(test_http, self).setUp()

    def test_http(self):
        """Klein has a few test case examples"""
        print('IMPLEMENT term/test/test_http StringTransport')
        self.threshold = .1
        a = app
        if a is not None:
            print('Test for app...')

        class re():

            def __init__(self, con):
                self.content = binascii.hexlify(con)
        req = re('One')
        hex_compat(req)
