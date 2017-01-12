#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing the padding (and underlying function I suppose)
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import codecs
from ..padding import AONTencrypt, AONTdecrypt
from ...tests.random import random, hexify, phony
from six.moves import range

# pylint: disable=no-self-use


class test_padding(unittest.TestCase):

    def test_padding(self):
        """one AONT using pre-existing value"""
        value = b"Secret Message!"
        print(("plaintext hex is: %s" % codecs.encode(value, 'hex')))
        cyphertext = AONTencrypt(value, b"password")
        print(("cyphertext is %s" % codecs.encode(cyphertext, 'hex')))
        plaintext = AONTdecrypt(cyphertext)
        print(("plaintext hex is: " + codecs.encode(plaintext, 'hex')))
        print(("plaintext is: " + plaintext))

    def test_gauntlet(self):
        """10 random AONTs - message should decrypt"""
        for x in range(0, 10):
            message = (b"%s" % phony(hexify(random()))[:1 + x])
            password = hexify(random())
            cipher = AONTencrypt(message, password)
            res = AONTdecrypt(cipher)
            print((message, res))
            assert res == message

    def test_unequal(self):
        """10 random AONTs - two AONTs should not equal each other"""
        for x in range(0, 10):
            message = (b"%s" % phony(hexify(random()))[:1 + x])
            password = hexify(random())
            a = AONTencrypt(message, password)
            b = AONTencrypt(message, password)
            assert a != b
            res_a = AONTdecrypt(a)
            res_b = AONTdecrypt(b)
            assert res_a == res_b