#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import platform
from ..censor import censor
from ..censor import stateEncoding
from ...utils.compat import ensureBinary
from ...tests.censorable import random, hexify, phony
from six.moves import range
test = censor(encodings=['UTF-8', 'ascii'], languages=['ENGLISH', 'CHINESE'])


# pylint: disable=no-self-use
# pylint: disable=unused-variable


class test_censor(unittest.TestCase):

    def test_encode_decode_python_2_3(self):
        '''encode/decode python 2/3 problems'''
        b_string = b"a string"
        u_string = u"a string"
        reg_string = "a string"
        reg_unicode = '你好'
        reg_unicode_encoded = "one 你好".encode('utf8')
        print(stateEncoding(ensureBinary(b_string)))
        print(stateEncoding(ensureBinary(u_string)))
        print(stateEncoding(ensureBinary(reg_string)))
        print(stateEncoding(ensureBinary(reg_unicode)))
        print(stateEncoding(ensureBinary(reg_unicode_encoded)))
        assert(stateEncoding(b_string) == 'ascii')
        assert(stateEncoding(u_string) == 'ascii')
        assert(stateEncoding(reg_string) == 'ascii')
        assert(stateEncoding(reg_unicode) == 'utf-8')
        assert(stateEncoding(reg_unicode_encoded) == 'utf-8')

    def test_obvious_catch(self):
        '''Should block (best 8/10, os.urandom()):'''
        passes = 0
        for x in range(0, 10):
            actual_random = random()
            res = test.check(actual_random)
            if not res:
                passes += 1
        print(("%d/10" % passes))
        assert passes >= 8

    def test_encode(self):
        '''Should safe (best 14/15, os.urandom()):'''
        passes = 0
        for x in range(0, 15):
            encoded_random = hexify(random())
            if stateEncoding(encoded_random) == 'ascii':
                passes += 1
        print(("%d/15" % passes))
        assert passes >= 14

    def test_trivial_bypass(self):
        '''Should safe (best 24/25, os.urandom()):'''
        passes = 0
        for x in range(0, 25):
            phonetic_random = phony(hexify(random()))
            if test.check(phonetic_random):
                passes += 1
        print(("%d/25" % passes))
        if platform.system() == 'Windows':
            print('Windows tests will not assert > 24')
        else:
            assert passes >= 24

    def test_unicode(self):
        '''Chinese characters should be UTF-8'''
        assert stateEncoding('hello 你好') == 'utf-8'

    # def test_steno_check():

    def test_valid_english(self):
        """Valid ASCII content:"""
        if platform.system() == 'Windows':
            print('Windows tests will not check valid english')
        else:
            assert test.check(b'#This *is* valid content')
    # def test_valid_chinese():
    #	print('Should pass:')
    #	print(test.block('#Hello 你好'))
    #	assert test.check('#Hello 你好')
