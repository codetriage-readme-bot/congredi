#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test fernet
"""
import unittest
from ..AES import default_aes
from ..kdf import default_kdf


class test_default_aes(unittest.TestCase):

    def test_default_aes_passwords(self):
        """A == B == C"""
        key, iv = default_aes().disclose()
        a = default_aes(key)
        b = default_aes(key)
        cyphertext = a.encrypt('hello')
        result = b.decrypt(cyphertext)
        assert result == 'hello'

    def test_default_aes_disclose(self):
        """getter must return correct attribute"""
        q = default_aes()
        res, iv = q.disclose()
        assert res == q.secret
        assert iv == q.iv
