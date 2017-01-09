#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test AES
"""
import unittest
from ..AES import default_aes
from ...algos.test.test_censor import random, hexify, phony

# pylint: disable=no-self-use
class test_default_aes(unittest.TestCase):

    def test_default_aes_passwords(self):
        """A == B == C"""
        key = default_aes().disclose()
        a = default_aes(key)
        b = default_aes(key)
        assert a.secret == b.secret
        cyphertext = a.encrypt('hello')
        result = b.decrypt(cyphertext)
        assert result == 'hello'

    def test_gauntlet_single(self):
        failures = 0
        print('Random gauntlet single tests')
        v = default_aes()
        for x in xrange(0,32):
            message = b"{}".format(phony(hexify(random()))[:1+x])
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print(message,res)
            assert res == message

    def test_gauntlet(self):
        failures = 0
        print('Random gauntlet tests')
        for x in xrange(0,32):
            v = default_aes()
            message = b"{}".format(phony(hexify(random()))[:1+x])
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print(message,res)
            assert res == message
            del v

    def test_default_aes_disclose(self):
        """getter must return correct attribute"""
        q = default_aes()
        res = q.disclose()
        assert res == q.secret
