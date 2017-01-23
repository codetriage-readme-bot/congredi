#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Runner tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from twisted.test.proto_helpers import StringTransport
from twisted.internet import stdio
from ...factory import CongrediPeerFactory
from ...protocol import CongrediPeerProtocol
from ..client import CongrediClient  # , ClientProtocol

# pylint: disable=no-self-use, unused-variable


class test_run(unittest.TestCase):

    def setUp(self):
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)
        client = CongrediClient(
            host="0.0.0.0", port="9000",
            clientKey=None)
        # stdio.StandardIO(client)

    def test_run(self):
        """Will need to look at how twisted runs their tests"""
        print('IMPLEMENT term/test/test_run StringTransport')
