#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timedTests import TimedTestCase
#from twisted.test.proto_helpers import StringTransport
# https://twistedmatrix.com/documents/current/core/howto/trial.html
# https://twistedmatrix.com/trac/attachment/ticket/3708/test_amp.py
# https://bazaar.launchpad.net/~game-hackers/game/trunk/view/head:/game/test/test_network.py

# class mock_transport(object):
#     def write(self, obj):
#         print(obj)
#     def getPeer(self):
#         return 'ab'


class mock_reason(object):
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def getErrorMessage(self):
        return self.msg


class test_general(TimedTestCase):

    def test_interpolate(self):
        """Interpolate two strings..."""
        self.threshold = .1
        n = "one"
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_typing(self):
        """Interpolate a number..."""
        self.threshold = .1
        n = 1
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_named(self):
        """Interpolate with named keys..."""
        self.threshold = .1
        n = 1
        key = "two"
        print(('one (%(name)s) %(key)s' % {'name': n, 'key': key}))
    # def test_numbered(self):
