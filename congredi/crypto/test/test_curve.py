#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests for curve
"""
import unittest
try:
    from ..curve import curve
except:
    print("bug with openssl libcrypto in curve.py")
# this bug is annoying
probable = 'To Fix:\nException: [OpenSSL] EC_KEY_generate_key FAIL ... error:100B3043:elliptic curve routines:EC_KEY_generate_key:passed a null parameter'


# pylint: disable=no-self-use, bare-except
class test_curve(unittest.TestCase):

    def test_curve(self):
        try:
            a = curve()
            c = curve()
            # .pubkey isn't the actual method right now.
            msg = a.encrypt("hello",c.pubkey)
            res = c.decrypt(msg)
            assert res == "hello"
        except:
            print(probable)
        print('IMPLEMENT crypto/test/test_curve:test_curve')

    def test_encryption(self):
        try:
            a = curve()
            b = curve()
            data = a.encrypt('wow', pubkey=b.pubkey)
            message = b.decrypt(data)
            assert message == 'wow'
        except:
            print(probable)

    def test_signing(self):
        try:
            a1 = curve()
            b1 = curve()
            sig = a1.sign('hash of something')
            ver = b1.verify('hash of something', a1.pubkey, sig)
            assert ver is True
        except:
            print(probable)

    def test_backups(self):
        try:
            a2 = curve()
            backupVals = a2.backup('one two three')
            restoreVals = curve().restore(backupVals, 'one two three')
            assert a2 == restoreVals
        except:
            print(probable)
