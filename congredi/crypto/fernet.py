#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Fernet class
"""
# https://cryptography.io/en/latest/fernet/
from cryptography.fernet import Fernet

# Class instances for the Symetric crypto inside Congredi.


class fc():
    secret = None
    lock = None

    def __init__(self, secret=None):
        if secret is not None:
            self.lock = Fernet(secret)
        else:
            self.secret = Fernet.generate_key()
            self.lock = Fernet(self.secret)

    def encrypt(self, data):
        return self.lock.encrypt(data)

    def decrypt(self, data):
        return self.lock.decrypt(data)

    def disclose(self):
        return self.secret
