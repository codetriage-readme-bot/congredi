#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All Or Nothing Padding (coulda just used the library's version)

    padding can use a lesser KDF (1,000 vs 10,000)

"""
# Crypto.Protocol.AllOrNothing
from __future__ import absolute_import
from __future__ import unicode_literals
from six.moves import zip
from .kdf import random_aes_32_key
from .AES import default_aes
from .hash import make_hash
from ..utils.compat import PY3


def AONTencrypt(content):
    """
    generate a key using deriviation,
    although you won't need to remember
    that password if you have all the
    content.
    """
    key_raw = random_aes_32_key() # could use weaker 1,000 KDF...
    token = default_aes(key_raw).encrypt(content)
    """
    hash the token, then xor with the 32 bit key.
    concattenate token with xor'd key.
    """
    hashable = make_hash(token).digest()
    if PY3:  # py2 won't test
        chard = int.from_bytes(hashable, byteorder="big") ^ int.from_bytes(
            key_raw, byteorder="big")
        chard = chard.to_bytes(32, byteorder="big")
    else:
        chard = b"".join(
                [chr(ord(a) ^ ord(b)) for a, b in
                 zip(hashable, key_raw)])
    return token + chard


def AONTdecrypt(cyphertext):
    """
    The last 32 bits of the cyphertext are the xor of
    the hash of the preceeding cypher, and the 32 bit key.
    pulling that together into a base64 string allows
    AES to decrypt the content.
    """
    hashable = make_hash(cyphertext[:-32]).digest()
    key_xored = cyphertext[-32:]
    if PY3:  # py2 won't test
        key2 = int.from_bytes(hashable, byteorder="big") ^ int.from_bytes(
            key_xored, byteorder="big")
        key2 = key2.to_bytes(32, byteorder="big")
    else:
        key2 = b"".join(
            [chr(ord(a) ^ ord(b)) for a, b in
             zip(hashable, key_xored)])
    return default_aes(key2).decrypt(cyphertext[:-32])
