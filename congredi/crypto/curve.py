#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from Crypto.PublicKey import RSA
# need to pick an ECC implementation
#from pyecc import ECC
from pyelliptic import ECC

# padding & encryption of message
from .padding import AONTencrypt, AONTdecrypt
from .kdf import random_password, default_kdf
from .AES import default_aes

# hashes (integrate here?)
from .hash import make_hash
# Class instances for the Asymetric crypto inside Congredi.
logger = logging.getLogger('congredi')


# whole file needs rebuilding and testing.

class curve():
    ecc = None

    def __init__(self, publicKey=None, privateKey=None):
        if publicKey is None and privateKey is None:
            self.ecc = ECC()
        #self.ecc = ECC.generate()

    @classmethod
    def encrypt(self, data, pubkey):

        # all or nothing data
        NothingPassword = random_password()
        transformPacket = AONTencrypt(data, NothingPassword)

        # message key
        messageKey = random_password()
        ecc = ECC(pubkey=pubkey)
        frontMatter = ecc.encrypt(messageKey)

        # encrypted message
        backMatter = default_aes(messageKey).encrypt(transformPacket)

        # put together
        message = frontMatter + backMatter
        return message

    def decrypt(self, message):
        # take appart
        frontMatter = message[:32]
        backMatter = message[32:]

        # message key
        ecc = ECC(privkey=self.privateKey)
        messageKey = ecc.decrypt(frontMatter)

        # decrypted message
        transformPacket = default_aes(messageKey).decrypt(backMatter)

        # AllOrNothing data
        data = AONTdecrypt(transformPacket)
        return data

    def sign(self, messageHash):
        ecc = ECC(private=self.privateKey)
        signature = ecc.sign(messageHash)
        return signature

    @classmethod
    def verify(self, messageHash, pubkey, signature):
        ecc = ECC(public=pubKey)
        return ecc.verify(messageHash, signature)

    def backup(self, password):
        # strengthen password
        strong_password = default_kdf(password)
        # export stuff
        keyValues = self.ECC.export(True)
        # encrypt ECC object
        return default_aes(strong_password).encrypt(keyValues)

    def restore(self, keyData, password):
        # strengthen password
        strong_password = default_kdf(password)
        # unpack from password
        keyValues = default_aes(strong_password).decrypt(keyData)
        # get ECC object
        return self.ECC.decode(keyValues)

    # bytes() str() .__bytes__() del ord() pad * chr(pad)
    # self.blockSize - len(data) % self.blockSize .exchange(ec.ECDH(), otherKey)
