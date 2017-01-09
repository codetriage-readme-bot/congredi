#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography)
"""
# pylint: disable=unused-import
import datetime
import unittest
from ..token import token


# pylint: disable=no-self-use
class test_token(unittest.TestCase):

    def test_good_token(self):
        bob = token('bob')
        example = bob.make('print')
        bob.check(example)
    # def test_expired_token(self):

    def test_invalid_token(self):
        fred = token('fred')
        alice = token('alice')
        wrong = fred.make('well then')
        alice.check(wrong)
