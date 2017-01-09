#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Still hanging around with a KDF...
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
from ..kdf import default_kdf, random_password


# pylint: disable=no-self-use
class test_kdf(unittest.TestCase):

    def test_kdf(self):
        strong_key_1 = default_kdf('password123_stupid')
        strong_key_2 = default_kdf('password123_stupid')
        assert strong_key_1 != strong_key_2

    def test_random_password(self):
        password_1 = random_password()
        password_2 = random_password()
        assert password_1 != password_2
