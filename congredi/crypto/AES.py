#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AES class (padding inclusive, yes RSA knows about that)
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from Crypto.Cipher import AES
from Crypto import Random
from .kdf import random_aes_32_key
from Crypto.Util.Padding import unpad, pad
# Class instances for the Symetric crypto inside Congredi.
import logging
logger = logging.getLogger('congredi')


class default_aes():
    secret = None

    def __init__(self, secret=None):
        if secret is None or len(secret) != 32:
            logger.warning('using random AES key.')
            secret = random_aes_32_key()
        self.secret = secret

    def encrypt(self, data):
        padded = pad(data, 16, 'pkcs7')
        iv = Random.new().read(AES.block_size)
        lock = AES.new(self.secret, AES.MODE_CBC, iv)
        encrypted = iv + lock.encrypt(padded)
        return encrypted

    def decrypt(self, data):
        iv = data[:AES.block_size]
        templock = AES.new(self.secret, AES.MODE_CBC, iv)
        decrypted = templock.decrypt(data[AES.block_size:])
        return unpad(decrypted, 16, 'pkcs7')

    def disclose(self):
        return self.secret
