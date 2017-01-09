#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing the padding (and underlying function I suppose)
"""
import unittest
from ..padding import AONTencrypt, AONTdecrypt
from ...algos.test.test_censor import random, hexify, phony

# pylint: disable=no-self-use


class test_padding(unittest.TestCase):

    def test_padding(self):
        """one AONT using pre-existing value"""
        value = b"Secret Message!"
        print("plaintext hex is: %s" % value.encode('hex'))
        cyphertext = AONTencrypt(value, b"password")
        print("cyphertext is %s" % cyphertext.encode('hex'))
        plaintext = AONTdecrypt(cyphertext)
        print("plaintext hex is: " + plaintext.encode('hex'))
        print("plaintext is: " + plaintext)

    def test_gauntlet(self):
        """10 random AONTs - message should decrypt"""
        for x in xrange(0, 10):
            message = b"{}".format(phony(hexify(random()))[:1 + x])
            password = hexify(random())
            cipher = AONTencrypt(message, password)
            res = AONTdecrypt(cipher)
            print(message, res)
            assert res == message

    def test_unequal(self):
        """10 random AONTs - two AONTs should not equal each other"""
        for x in xrange(0, 10):
            message = b"{}".format(phony(hexify(random()))[:1 + x])
            password = hexify(random())
            a = AONTencrypt(message, password)
            b = AONTencrypt(message, password)
            assert a != b
            res_a = AONTdecrypt(a)
            res_b = AONTdecrypt(b)
            assert res_a == res_b
