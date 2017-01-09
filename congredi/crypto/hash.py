#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hash function (No clue why)
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from Crypto.Hash import SHA256


def make_hash(message):
    """make hash, print base64, return 32 bits"""
    digest = SHA256.new(message)
    # print('32 hash: ' + digest.hexdigest())
    return digest
