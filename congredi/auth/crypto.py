#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Random Generator (currently PyCryptoDome.Random)
RSA classes (not using signed digest at the end, currently)

    current: [RSA pubkey(256 bit AES key)][AES(padding(message))]
    new: <[RSA pubkey(256 bit AES key)][AES(padding(message))]>[RSA privkey(32 HASH(ciphertext))]
Threshold Sigs. Not implemented yet. See spec/papers
All Or Nothing Padding (coulda just used the library's version)

    padding can use a lesser KDF (1,000 vs 10,000)
Key Deriviation (weak or strong)

optimization: will need to clarify which functions use the
1,000 vs 10,000 cycle KDF.
Hash function (No clue why)

    currently through PyCryptoDome.Hash.SHA256

AES class (padding inclusive, yes RSA knows about that)
main client class - terminal
compute a vote


"""
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import print_function
#from pyvotecore.stv import stv
from Crypto.Hash import SHA256
# Crypto.Protocol.AllOrNothing
from six.moves import zip
from ..utils.compat import PY3
from Crypto import Random
import logging
logger = logging.getLogger('congredi')
import six
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend
from Crypto.Protocol.KDF import PBKDF2
import os
from Crypto.PublicKey import RSA
# from Crypto.Cipher.PKCS1_OAEP import PKCS1OAEP_Cipher
from Crypto.Cipher import PKCS1_OAEP
# from Crypto.Signature import pkcs1_15
from Crypto.Signature import PKCS1_v1_5
# need to pick an ECC implementation

# padding & encryption of message

# hashes (integrate here?)
# Class instances for the Asymetric crypto inside Congredi.

# Class instances for the Symetric crypto inside Congredi.

"""
Design - each of these classes could simply be an inferface or superclass?
The methods they'll use will be slightly different, but having these methods
helps us implement other vote types besides STV... #J
"""

# pylint: disable=abstract-method
from abc import ABCMeta, abstractmethod


class poll(six.with_metaclass(ABCMeta, object)):
    __doc__ = """
    A public STV style vote

    This class can use simple public key cryptography,
    no individual vote needs to be secret
    """

    @classmethod
    def version(self): return "1.0"

    def __init__(self, trees):
        """Object requires trees, sigs (Design - See docs #H)"""
        self.trees = trees

    @abstractmethod
    def cast(self, userVote):
        """
        Cast an invidual's vote (check that it is
        a valid vote option and a valid sig
        """
        raise NotImplementedError()

    @abstractmethod
    def validate(self, voteid):
        """
        Validate one vote (check option & sig)
        """
        raise NotImplementedError()

    @abstractmethod
    def compute(self):
        """
        Compute the winner of a vote
        """
        raise NotImplementedError()

    @abstractmethod
    def certify(self):
        """
        Check a vote result
        """
        raise NotImplementedError()


class vote(poll):
    __doc__ = """
    A private STV style vote (Theory - see congredi/papers #I)

    This class uses different cryptography primatives
    """


class stvVote(vote):

    def cast(self, userVote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass


class stvPoll(poll):

    def cast(self, userVote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass


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

# random password:


def make_hash(message):
    """make hash, print base64, return 32 bits"""
    digest = SHA256.new(message)
    # print('32 hash: ' + digest.hexdigest())
    return digest


def random_password():
    key = os.urandom(16)
    return default_kdf(key)


def random_aes_32_key():
    key = os.urandom(32)
    return weaker_kdf(key)

# a default kdf


def weaker_kdf(password):
    key_raw = PBKDF2(
        password,
        salt=os.urandom(16),
        dkLen=32,  # 16,
        count=1000  # , #1000
        # prf=None
    )
    # key_raw = PBKDF2HMAC(
    #     algorithm=hashes.SHA256(),
    return key_raw


def default_kdf(password):
    key_raw = PBKDF2(
        password,
        salt=os.urandom(16),
        dkLen=32,  # 16,
        count=100000  # , #1000
        # prf=None
    )
    # key_raw = PBKDF2HMAC(
    #     algorithm=hashes.SHA256(),
    return key_raw


# whole file needs rebuilding and testing.
def AONTencrypt(content):
    """
    generate a key using deriviation,
    although you won't need to remember
    that password if you have all the
    content.
    """
    key_raw = random_aes_32_key()  # could use weaker 1,000 KDF...
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

rng = Random.new().read


class default_rsa():
    key = None

    def __init__(self, publicKey=None, privateKey=None):
        if publicKey is None and privateKey is None:
            self.key = RSA.generate(2048)
        else:  # test
            if privateKey is None:  # test
                self.key = RSA.importKey(publicKey)
            else:  # test
                self.key = RSA.importKey(privateKey)

    @classmethod
    def encrypt(self, data, pubkey):

        # all or nothing data
        transformPacket = AONTencrypt(data)

        # message key
        messageKey = random_aes_32_key()
        if not isinstance(pubkey, RSA.RsaKey):
            key = RSA.importKey(pubkey)
        else:
            key = pubkey
        skey = PKCS1_OAEP.new(key)
        frontMatter = skey.encrypt(messageKey)  # , 16)
        # print('RSA calls AES Encrypt with private key: %s' % key.publickey().exportKey())

        # encrypted message
        backMatter = default_aes(messageKey).encrypt(transformPacket)

        # put together
        message = frontMatter + backMatter
        return message

    def decrypt(self, message):
        # take appart
        frontMatter = message[:256]
        backMatter = message[256:]

        # message key
        private_key = PKCS1_OAEP.new(self.key)
        # print('RSA calls AES Decrypt with private key: %s' % self.key.publickey().exportKey())
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
        # pylint: disable=not-callable
        res = skey.verify(messageHash, signature)
        return res

    def backup(self, password=None):
        # export stuff
        keyValues = self.key.exportKey('PEM')
        # encrypt ECC object
        safebox = default_aes(password)
        backup = safebox.encrypt(keyValues)
        passphrase = safebox.disclose()
        return backup, passphrase

    def restore(self, keyData, password):
        # unpack from password
        keyValues = default_aes(password).decrypt(keyData)
        actualKey = RSA.importKey(keyValues)
        self.key = actualKey
        return actualKey

    def publicKey(self):
        return self.key.publickey().exportKey()
    # bytes() str() .__bytes__() del ord() pad * chr(pad)
    # self.blockSize - len(data) % self.blockSize .exchange(ec.ECDH(), otherKey)


class ThresholdPGP():

    def __init__(self):
        pass

    def generate(self):
        pass

    def sign(self, item):
        pass
# http://www.cs.princeton.edu/~stevenag/bitcoin_threshold_signatures.pdf
