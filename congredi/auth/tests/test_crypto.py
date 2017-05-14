#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from six.moves import range
import binascii
from ...utils.timedTests import TimedTestCase
from ...utils.oracle import random, hexify, phony, pick_range
from ..crypto import default_aes
from ..crypto import default_kdf, random_password
from ..crypto import stvVote, stvPoll
from ..crypto import ThresholdPGP
from ..crypto import make_hash
from ..crypto import default_rsa
from ..crypto import AONTencrypt, AONTdecrypt


class test_default_aes(TimedTestCase):

    def test_default_aes_passwords(self):
        """AES A.disclose() == B(A) == C(A)"""
        self.threshold = 2
        key = default_aes().disclose()
        a = default_aes(key)
        b = default_aes(key)
        assert a.secret == b.secret
        cyphertext = a.encrypt(b'hello')
        result = b.decrypt(cyphertext)
        assert result == b'hello'

    def test_gauntlet_single(self):
        '''Random AES gauntlet single tests'''
        self.threshold = 5
        v = default_aes()
        for x in range(0, 32):
            message = phony(hexify(random()))[:1 + x]
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print((message, res))
            assert res == message

    def test_gauntlet(self):
        '''Random AES gauntlet tests (delete object)'''
        self.threshold = 18.33
        for x in range(0, 32):
            v = default_aes()
            message = phony(hexify(random()))[:1 + x]
            cipher = v.encrypt(message)
            res = v.decrypt(cipher)
            print((message, res))
            assert res == message
            del v

    def test_default_aes_disclose(self):
        """getter must return correct attribute"""
        self.threshold = 1
        q = default_aes()
        res = q.disclose()
        assert res == q.secret


class test_hash(TimedTestCase):
    good_hash = None

    def test_good_hash(self):
        """Make sure a hex-digest of the current library works"""
        res = make_hash(b'123456').hexdigest()
        #res = res.encode('hex')
        check = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
        print(res)
        print(check)
        assert res == check
        self.good_hash = res


class test_kdf(TimedTestCase):
    sk1 = None
    pw1 = None

    def test_kdf(self):
        """Test the strong_kdf"""
        self.threshold = 97
        strong_key_1 = default_kdf('password123_stupid')
        strong_key_2 = default_kdf('password123_stupid')
        assert strong_key_1 != strong_key_2
        assert len(strong_key_1) == 32
        self.sk1 = strong_key_1

    def test_random_password(self):
        """Grab random password, assert it doesn't equal the next one"""
        self.threshold = 57
        password_1 = random_password()
        password_2 = random_password()
        assert password_1 != password_2
        assert len(password_1) == 32
        self.pw1 = password_1


class test_padding(TimedTestCase):

    def test_padding(self):
        """one AONT using pre-existing value"""
        self.threshold = 2
        value = b"Secret Message!"
        print(("plaintext hex is: %s" % binascii.hexlify(value)))
        cyphertext = AONTencrypt(value)
        print(("cyphertext is %s" % binascii.hexlify(cyphertext)))
        plaintext = AONTdecrypt(cyphertext)
        print(type(plaintext))
        print(("plaintext hex is: %s" % binascii.hexlify(plaintext)))
        print(("plaintext is: %s" % plaintext))
        assert plaintext == value

    def test_gauntlet(self):
        """10 random AONTs - message should decrypt"""
        self.threshold = 5.73
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            cipher = AONTencrypt(message)
            res = AONTdecrypt(cipher)
            print(res, message)
            assert res == message

    def test_unequal(self):
        """10 random AONTs - two AONTs should not equal each other"""
        self.threshold = 14.42
        for x in range(0, 10):
            message = phony(hexify(random()))[:1 + x]
            a = AONTencrypt(message)
            b = AONTencrypt(message)
            assert a != b
            res_a = AONTdecrypt(a)
            res_b = AONTdecrypt(b)
            assert res_a == res_b


class test_RSA(TimedTestCase):
    global_rsa_left = None
    global_rsa_right = None

    def setUp(self):
        self.global_rsa_left = default_rsa()
        self.global_rsa_right = default_rsa()
        super(test_RSA, self).setUp()

    def test_encrypt(self):
        """Encrypt something, decrypt it"""
        self.threshold = 5
        # .pubkey isn't the actual method right now.
        msg = self.global_rsa_left.encrypt(
            b"hello", self.global_rsa_right.publicKey())
        res = self.global_rsa_right.decrypt(msg)
        assert res == b"hello"

    def test_gauntlet_encrypt_single(self):
        """Random objects encrypted - multiple renders, one reciever"""
        self.threshold = 24
        ranges = pick_range(5)
        for x in ranges:
            sender = default_rsa()
            message = phony(hexify(random()))[:1 + x]
            print(len(message), message)
            encrypted = sender.encrypt(
                message, self.global_rsa_left.publicKey())
            decrypted = self.global_rsa_left.decrypt(encrypted)
            assert decrypted == message
            del sender

    def test_gauntlet_encrypt_multi(self):
        """Random objects encrypted - multiple senders/recievers"""
        self.threshold = 17
        ranges = pick_range(3)
        for x in ranges:
            reciever = default_rsa()
            sender = default_rsa()
            message = phony(hexify(random()))[:1 + x]
            print(len(message), message)
            encrypted = sender.encrypt(message, reciever.publicKey())
            decrypted = reciever.decrypt(encrypted)
            assert decrypted == message
            del reciever
            del sender

    def test_signing(self):
        """Verify something that was signed"""
        self.threshold = 3.98
        msg = b'hash of something'
        hc = make_hash(msg)
        print(hc.hexdigest())
        sig = self.global_rsa_left.sign(hc)
        ver = self.global_rsa_right.verify(
            hc, self.global_rsa_left.publicKey(), sig)
        assert ver is True

    def test_backups(self):
        """Backup and restore a key, (assure equal?)"""
        self.threshold = 3.8
        print((self.global_rsa_left.publicKey()))
        backupVals, backupPhrase = self.global_rsa_left.backup()
        restoreVals = default_rsa()
        restoreVals.restore(backupVals, backupPhrase)

        assert self.global_rsa_left.publicKey() == restoreVals.publicKey()

    def test_inits_options(self):
        a = default_rsa(publicKey=self.global_rsa_left.publicKey())
        assert a.publicKey() == self.global_rsa_left.publicKey()
        #b = default_rsa(privateKey=self.global_rsa_right.key)
        #assert b.key == self.global_rsa_right.key


class test_threshold(TimedTestCase):
    sigGen = None

    def setUp(self):
        self.sigGen = ThresholdPGP()
        super(test_threshold, self).setUp()

    def test_threshold_generate(self):
        """Call init, sign"""
        self.sigGen.generate()
        print('IMPLEMENT crypto/test/test_threshold')

    def test_threshold_sign(self):
        """Call init, sign"""
        self.sigGen.sign(None)
        print('IMPLEMENT crypto/test/test_threshold')

# pylt: disable=unused-variable


class test_stv(TimedTestCase):

    def test_stvPoll(self):
        """Init a poll object"""
        self.threshold = .1
        testPoll = stvPoll(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvPoll')
        assert testPoll != None

    def test_stvVote(self):
        """Init a vote object"""
        self.threshold = .1
        testVote = stvVote(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvVote')
        assert testVote != None
