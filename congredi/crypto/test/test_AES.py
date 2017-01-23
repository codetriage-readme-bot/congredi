#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test AES
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..AES import default_aes
from ...tests.censorable import random, hexify, phony
from six.moves import range

# pylint: disable=no-self-use


class test_default_aes(unittest.TestCase):

    def test_default_aes_passwords(self):
        """AES A.disclose() == B(A) == C(A)"""
        key = default_aes().disclose()
        a = default_aes(key)
        b = default_aes(key)
        assert a.secret == b.secret
        cyphertext = a.encrypt(b'hello')
        result = b.decrypt(cyphertext)
        assert result == b'hello'

    def test_gauntlet_single(self):
        '''Random AES gauntlet single tests'''
        v = default_aes()
        for x in range(0, 32):
            message = phony(hexify(random()))[:1 + x]
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print((message, res))
            assert res == message

    def test_gauntlet(self):
        '''Random AES gauntlet tests (delete object)'''
        for x in range(0, 32):
            v = default_aes()
            message = phony(hexify(random()))[:1 + x]
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print((message, res))
            assert res == message
            del v

    def test_default_aes_disclose(self):
        """getter must return correct attribute"""
        q = default_aes()
        res = q.disclose()
        assert res == q.secret
