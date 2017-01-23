#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography)

JWT tokens can be one of:

* Good
* Expired
* Invalid

And granting them should not take database access. They are meant to
figure out if a user is auth'd without using the database to do so.

"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
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
