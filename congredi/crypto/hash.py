#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hash function (No clue why)
"""
from Crypto.Hash import SHA256
import base64


def make_hash(message):
    """make hash, print base64, return 32 bits"""
    digest = SHA256.new()
    digest.update(message)
    #print('32 hash: ' + digest.hexdigest())
    return digest
