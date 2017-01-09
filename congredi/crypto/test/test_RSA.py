#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests for curve
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..RSA import default_rsa
from ..hash import make_hash


# pylint: disable=no-self-use, bare-except, unused-variable
class test_RSA(unittest.TestCase):

    def test_encrypt(self):
        print('DISABLED crypto/test/test_RSA:test_encrypt')
        a = default_rsa()
        c = default_rsa()
        # .pubkey isn't the actual method right now.

        msg = a.encrypt(b"hello", c.publicKey())
        """
        res = c.decrypt(msg)
        assert res == "hello"
        """

    def test_signing(self):
        print('DISABLED crypto/test/test_RSA:test_signing')
        a1 = default_rsa()
        b1 = default_rsa()
        msg = b'hash of something'
        hc = make_hash(msg)
        sig = a1.sign(hc)
        """
        ver = b1.verify(hc, a1.publicKey(), sig)
        assert ver is True
        """

    def test_backups(self):
        print('DISABLED crypto/test/test_RSA:test_backups')
        a2 = default_rsa()
        print((a2.publicKey()))
        backupVals = a2.backup('one two three')
        restoreVals = default_rsa()
        # restoreVals.restore(backupVals, 'one two three')

        # assert a2.publicKey() == restoreVals.publicKey()
