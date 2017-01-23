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


class test_http(unittest.TestCase):

    def setUp(self):
        # https://github.com/twisted/klein/blob/master/src/klein/test/test_app.py
        self.tr = StringTransport()
        users = ['a', 'b']
        self.factory = CongrediPeerFactory()
        self.proto = CongrediPeerProtocol(self.factory, users)
        self.proto.makeConnection(self.tr)

    def test_http(self):
        """Klein has a few test case examples"""
        print('IMPLEMENT term/test/test_http StringTransport')
