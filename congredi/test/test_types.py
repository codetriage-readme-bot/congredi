#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
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
from ..utils.timing import TimedTestCase
from ..types import PrivAES, EncBlob, ObjBlob, ObjSig, EncSig
from ..types import EncHash, ObjHash, EncPubKey, ObjPubKey, EncAddress
from ..types import ObjAddress, EncBool


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
