#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing the padding (and underlying function I suppose)
"""
from ...packet.padding import AONTencrypt, AONTdecrypt


def test_padding():
    cyphertext = AONTencrypt(b"Secret Message!", b"password")
    print("cyphertext is {}".format(cyphertext))
    plaintext = AONTdecrypt(cyphertext)
    print("plaintext is: " + plaintext)
