#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Still hanging around with a KDF...
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..kdf import default_kdf, random_password


class test_kdf(TimedTestCase):
    sk1 = None
    pw1 = None

    def test_kdf(self):
        """Test the strong_kdf"""
        self.threshold = 97
        strong_key_1 = default_kdf('password123_stupid')
        strong_key_2 = default_kdf('password123_stupid')
        assert strong_key_1 != strong_key_2
        assert len(strong_key_1) == 32
        self.sk1 = strong_key_1

    def test_random_password(self):
        """Grab random password, assert it doesn't equal the next one"""
        self.threshold = 57
        password_1 = random_password()
        password_2 = random_password()
        assert password_1 != password_2
        assert len(password_1) == 32
        self.pw1 = password_1
