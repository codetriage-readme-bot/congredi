#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing the padding (and underlying function I suppose)
"""
import unittest
from ..padding import AONTencrypt, AONTdecrypt


class test_padding(unittest.TestCase):

    def test_padding(self):
        cyphertext = AONTencrypt(b"Secret Message!", b"password")
        print("cyphertext is {}".format(cyphertext.encode('hex')))
        plaintext = AONTdecrypt(cyphertext)
        print("plaintext is: " + plaintext)
