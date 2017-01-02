#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fernet class
"""
from Crypto.Cipher import AES
from Crypto import Random
from .kdf import default_kdf

# Class instances for the Symetric crypto inside Congredi.


class default_aes():
    secret = None
    lock = None
    iv = None
    # blockSize = 16  # Block Size
    # keySize = 32  # keySize in Bytes - 32 bytes = 256bit Encryption
    # mode = AES.MODE_CBC  # Cipher Block Mode

    def __init__(self, secret=None):
        self.iv = Random.new().read(AES.block_size)
        if secret is None:
            secret = Random.new().read(AES.block_size)
        #secret = default_kdf(secret)
        self.lock = AES.new(secret, AES.MODE_CFB, self.iv)
        self.secret = secret

    def encrypt(self, data):
        return self.iv + self.lock.encrypt(data)

    def decrypt(self, data):
        iv = data[:AES.block_size]
        templock = AES.new(self.secret, AES.MODE_CFB, iv)
        return templock.decrypt(data[AES.block_size:])

    def disclose(self):
        return self.secret, self.iv
