#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

from Crypto.PublicKey import RSA
# from Crypto.Cipher.PKCS1_OAEP import PKCS1OAEP_Cipher
from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Signature import pkcs1_15
from Crypto.Signature import PKCS1_v1_5
# need to pick an ECC implementation

# padding & encryption of message
from .padding import AONTencrypt, AONTdecrypt
from .kdf import random_password, default_kdf
# from .rnd import rng
from .AES import default_aes

# hashes (integrate here?)
# from .hash import make_hash
# Class instances for the Asymetric crypto inside Congredi.
logger = logging.getLogger('congredi')

# whole file needs rebuilding and testing.


class default_rsa():
    key = None

    def __init__(self, publicKey=None, privateKey=None):
        if publicKey is None and privateKey is None:
            self.key = RSA.generate(2048)
        else:
            if privateKey is None:
                self.key = RSA.importKey(publicKey)
            else:
                self.key = RSA.importKey(privateKey)

    @classmethod
    def encrypt(self, data, pubkey):

        # all or nothing data
        NothingPassword = random_password()
        transformPacket = AONTencrypt(data, NothingPassword)

        # message key
        messageKey = random_password()

        key = RSA.importKey(pubkey)
        skey = PKCS1_OAEP.new(key)
        frontMatter = skey.encrypt(messageKey)  # , 16)
        print(len(frontMatter))

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
        private_key = PKCS1_OAEP.new(self.key)
        messageKey = private_key.decrypt(frontMatter)

        # decrypted message
        transformPacket = default_aes(messageKey).decrypt(backMatter)

        # AllOrNothing data
        data = AONTdecrypt(transformPacket)
        return data

    def sign(self, messageHash):
        signature = PKCS1_v1_5.new(self.key).sign(messageHash)
        return signature

    @classmethod
    def verify(self, messageHash, pubKey, signature):
        key = RSA.importKey(pubKey)
        skey = PKCS1_v1_5.new(key)
        res = skey.verify(messageHash, signature)
        return res

    def backup(self, password):
        # strengthen password
        strong_password = default_kdf(password)
        # export stuff
        keyValues = self.key.exportKey('PEM')
        # encrypt ECC object
        return default_aes(strong_password).encrypt(keyValues)

    def restore(self, keyData, password):
        # strengthen password
        strong_password = default_kdf(password)
        # unpack from password
        keyValues = default_aes(strong_password).decrypt(keyData)
        # get ECC object
        return self.key.importKey(keyValues)

    def publicKey(self):
        return self.key.publickey().exportKey()
    # bytes() str() .__bytes__() del ord() pad * chr(pad)
    # self.blockSize - len(data) % self.blockSize .exchange(ec.ECDH(), otherKey)
