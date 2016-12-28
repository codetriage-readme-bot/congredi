#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All Or Nothing Padding (coulda just used the library's version)
"""
from ..crypto.kdf import default_kdf
from ..crypto.fernet import fc
from ..crypto.hash import make_hash
import base64


def AONTencrypt(content, password):
    """
    generate a key using deriviation,
    although you won't need to remember
    that password if you have all the
    content.
    """
    key_raw = default_kdf(password)
    key = base64.urlsafe_b64encode(key_raw)
    token = base64.urlsafe_b64decode(fc(key).encrypt(content))
    print("32 key: {}".format(key))
    """
	hash the token, then xor with the 32 bit key.
	concattenate token with xor'd key.
	"""
    chard = "".join(
            [chr(ord(a) ^ ord(b)) for a, b in
             zip(make_hash(token), key_raw)])
    return token + chard


def AONTdecrypt(cyphertext):
    """
    The last 32 bits of the cyphertext are the xor of
    the hash of the preceeding cypher, and the 32 bit key.
    pulling that together into a base64 string allows
    fernet to decrypt the content.
    """
    key2 = base64.urlsafe_b64encode(
        "".join(
            [chr(ord(a) ^ ord(b)) for a, b in
             zip(make_hash(cyphertext[:-32]),
                 cyphertext[-32:])]))
    print('32 key was: {}'.format(key2))
    return fc(key2).decrypt(base64.urlsafe_b64encode(cyphertext[:-32]))
