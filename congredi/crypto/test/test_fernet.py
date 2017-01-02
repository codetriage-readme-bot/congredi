#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test fernet
"""
import unittest
from cryptography.fernet import Fernet
from ..fernet import fc


class test_fc(unittest.TestCase):

    def test_fc_passwords(self):
        """A == B == C"""
        key = Fernet.generate_key()
        a = fc(key)
        b = fc(key)
        cyphertext = a.encrypt('hello')
        result = b.decrypt(cyphertext)
        assert result == 'hello'

    def test_fc_disclose(self):
        """getter must return correct attribute"""
        q = fc()
        res = q.disclose()
        assert res == q.secret
