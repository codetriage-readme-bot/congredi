#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factory tests

    regression on StringTransport vs real TCP needs addressing...
general tests for string behavior. If these fail,
lots of tests that use string interpolation will
error because of the string interpolation.

This is a good catch for people writing a test
with a buggy print statement.

Then again, there's always pylint.

Thank You Py2/3 compatibility problems...protocol tests

    regression on StringTransport vs real TCP needs addressing...

AMP Types, which have a to-string/from-string mentality, though
they don't actually have to be strings, just of a finite length.

    Each of these tests runs b'b' == obj.fromString(obj.toString(b'b'))

    PrivAES
    EncBlob
    ObjBlob
    ObjSig
    EncSig
    EncHash
    ObjHash
    EncPubKey
    ObjPubKey
    EncAddress
    ObjAddress
    EncBool

    We can (and should) run oracles to test the limits of the types (empty/lists/dicts/objs)
    That'll be using an extended ../utils/censorable.py for lists/dicts


"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .utils import TimedTestCase
#from twisted.test.proto_helpers import StringTransport
# https://twistedmatrix.com/documents/current/core/howto/trial.html
# https://twistedmatrix.com/trac/attachment/ticket/3708/test_amp.py
# https://bazaar.launchpad.net/~game-hackers/game/trunk/view/head:/game/test/test_network.py
from .main import PrivAES, EncBlob, ObjBlob, ObjSig, EncSig
from .main import EncHash, ObjHash, EncPubKey, ObjPubKey, EncAddress
from .main import ObjAddress, EncBool


class test_types(TimedTestCase):

    def test_PrivAES(self):
        self.threshold = .1
        obj = PrivAES()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncBlob(self):
        self.threshold = .1
        obj = EncBlob()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_ObjBlob(self):
        self.threshold = .1
        obj = ObjBlob()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncSig(self):
        self.threshold = .1
        obj = EncSig()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_ObjSig(self):
        self.threshold = .1
        obj = ObjSig()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncHash(self):
        self.threshold = .1
        obj = EncHash()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_ObjHash(self):
        self.threshold = .1
        obj = ObjHash()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncPubKey(self):
        self.threshold = .1
        obj = EncPubKey()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_ObjPubKey(self):
        self.threshold = .1
        obj = ObjPubKey()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncAddress(self):
        self.threshold = .1
        obj = EncAddress()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_ObjAddress(self):
        self.threshold = .1
        obj = ObjAddress()
        assert b'b' == obj.fromString(obj.toString(b'b'))

    def test_EncBool(self):
        self.threshold = .1
        obj = EncBool()
        assert b'b' == obj.fromString(obj.toString(b'b'))

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
