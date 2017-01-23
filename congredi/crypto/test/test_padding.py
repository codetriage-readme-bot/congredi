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
from ...tests.censorable import random, hexify, phony
from six.moves import range

# pylint: disable=no-self-use


class test_padding(unittest.TestCase):

    def test_padding(self):
        """one AONT using pre-existing value"""
        value = b"Secret Message!"
        try:
            print(("plaintext hex is: %s" % codecs.encode(value, 'hex')))
        except LookupError:
            print("Python3.3 bug...")
        cyphertext = AONTencrypt(value)
        try:
            print(("cyphertext is %s" % codecs.encode(cyphertext, 'hex')))
        except LookupError:
            print("Python3.3 bug...")
        plaintext = AONTdecrypt(cyphertext)
        # pylint: disable=bare-except
        try:
            print(("plaintext hex is: " + codecs.encode(plaintext, 'hex')))
        except:
            print('Well, python3 needs fixing on encoding %s to hex...' %
                  type(plaintext))
            plaintext = plaintext.decode('utf-8')

        print(("plaintext is: " + plaintext))

    def test_gauntlet(self):
        """10 random AONTs - message should decrypt"""
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            cipher = AONTencrypt(message)
            res = AONTdecrypt(cipher)
            print(res, message)
            assert res == message

    def test_unequal(self):
        """10 random AONTs - two AONTs should not equal each other"""
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            a = AONTencrypt(message)
            b = AONTencrypt(message)
            assert a != b
            res_a = AONTdecrypt(a)
            res_b = AONTdecrypt(b)
            assert res_a == res_b
