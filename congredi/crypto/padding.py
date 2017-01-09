#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All Or Nothing Padding (coulda just used the library's version)
"""
# Crypto.Protocol.AllOrNothing
from __future__ import absolute_import
#from __future__ import unicode_literals
from .kdf import weaker_kdf
from .AES import default_aes
from .hash import make_hash
from six.moves import zip


def AONTencrypt(content, password):
    """
    generate a key using deriviation,
    although you won't need to remember
    that password if you have all the
    content.
    """
    key_raw = weaker_kdf(password)
    token = default_aes(key_raw).encrypt(content)
    """
    hash the token, then xor with the 32 bit key.
    concattenate token with xor'd key.
    """
    hashable = make_hash(token).digest()
    chard = "".join(
            [chr(ord(a) ^ ord(b)) for a, b in
             zip(hashable, key_raw)])
    return token + chard


def AONTdecrypt(cyphertext):
    """
    The last 32 bits of the cyphertext are the xor of
    the hash of the preceeding cypher, and the 32 bit key.
    pulling that together into a base64 string allows
    fernet to decrypt the content.
    """
    key2 = "".join(
        [chr(ord(a) ^ ord(b)) for a, b in
         zip(make_hash(cyphertext[:-32]).digest(),
             cyphertext[-32:])])
    return default_aes(key2).decrypt(cyphertext[:-32])
