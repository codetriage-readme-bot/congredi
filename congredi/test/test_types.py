#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
general tests
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
