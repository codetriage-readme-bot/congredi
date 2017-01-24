#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests for curve
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..RSA import default_rsa
from ..hash import make_hash
from ...tests.censorable import random, hexify, phony, pick_range


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
