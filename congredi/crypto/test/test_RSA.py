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

    def test_encrypt(self):
        """Encrypt something, decrypt it"""
        self.threshold = 5
        a = default_rsa()
        c = default_rsa()
        # .pubkey isn't the actual method right now.
        msg = a.encrypt(b"hello", c.publicKey())
        res = c.decrypt(msg)
        assert res == b"hello"

    def test_gauntlet_encrypt_single(self):
        """Random objects encrypted - multiple renders, one reciever"""
        self.threshold = 24
        reciever = default_rsa()
        ranges = pick_range(5)
        for x in ranges:
            sender = default_rsa()
            message = phony(hexify(random()))[:1 + x]
            print(len(message), message)
            encrypted = sender.encrypt(message, reciever.publicKey())
            decrypted = reciever.decrypt(encrypted)
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
        a1 = default_rsa()
        b1 = default_rsa()
        msg = b'hash of something'
        hc = make_hash(msg)
        print(hc.hexdigest())
        sig = a1.sign(hc)
        ver = b1.verify(hc, a1.publicKey(), sig)
        assert ver is True

    def test_backups(self):
        """Backup and restore a key, (assure equal?)"""
        self.threshold = 3.8
        a2 = default_rsa()
        print((a2.publicKey()))
        backupVals, backupPhrase = a2.backup()
        restoreVals = default_rsa()
        restoreVals.restore(backupVals, backupPhrase)

        assert a2.publicKey() == restoreVals.publicKey()
