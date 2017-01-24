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
# from ..client import CongrediClient  # , ClientProtocol


class test_run(TimedTestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)
        # client = CongrediClient(
        #     host="0.0.0.0", port="9000",
        #     clientKey=None)
        super(test_run, self).setUp()

    def test_run(self):
        """Will need to look at how twisted runs their tests"""
        self.threshold = .1
        print('IMPLEMENT term/test/test_run StringTransport')
