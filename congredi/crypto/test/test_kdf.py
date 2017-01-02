#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Still hanging around with a KDF...
"""
import unittest
from ..kdf import default_kdf


class test_kdf(unittest.TestCase):

    def test_kdf(self):
        strong_key = default_kdf('password123_stupid')
