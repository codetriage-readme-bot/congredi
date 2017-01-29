#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing the padding (and underlying function I suppose)
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
import binascii
from ..padding import AONTencrypt, AONTdecrypt
from ...utils.censorable import random, hexify, phony
from six.moves import range


class test_padding(TimedTestCase):

    def test_padding(self):
        """one AONT using pre-existing value"""
        self.threshold = 2
        value = b"Secret Message!"
        print(("plaintext hex is: %s" % binascii.hexlify(value)))
        cyphertext = AONTencrypt(value)
        print(("cyphertext is %s" % binascii.hexlify(cyphertext)))
        plaintext = AONTdecrypt(cyphertext)
        print(type(plaintext))
        print(("plaintext hex is: %s" % binascii.hexlify(plaintext)))
        print(("plaintext is: %s" % plaintext))

    def test_gauntlet(self):
        """10 random AONTs - message should decrypt"""
        self.threshold = 5.73
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            cipher = AONTencrypt(message)
            res = AONTdecrypt(cipher)
            print(res, message)
            assert res == message

    def test_unequal(self):
        """10 random AONTs - two AONTs should not equal each other"""
        self.threshold = 14.42
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            a = AONTencrypt(message)
            b = AONTencrypt(message)
            assert a != b
            res_a = AONTdecrypt(a)
            res_b = AONTdecrypt(b)
            assert res_a == res_b
