#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
import binascii
import os
import unittest
from ..censor import censor
from ..censor import stateEncoding

hexy = {
    "0": "Zero", "1": "One", "2": "Two", "3": "Three",
    "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
    "8": "Eight", "9": "Niner", "a": "Alpha", "b": "Bravo",
    "c": "Charlie", "d": "Delta", "e": "Echo", "f": "Foxtrot",
    # unused past this
    "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November",
    "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor",
    "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}
test = censor(encodings=['UTF-8', 'ascii'], languages=['ENGLISH', 'CHINESE'])
actual_random = os.urandom(15)
encoded_random = binascii.hexlify(actual_random)
phonetic_random = " ".join(hexy[a] for a in encoded_random)


class test_censor(unittest.TestCase):

    def test_obvious_catch(self):
        print('Should block:')
        res = test.check(actual_random)
        assert not res

    def test_encode(self):
        print('Should safe:')
        assert stateEncoding(encoded_random) == 'ascii'
        assert stateEncoding('hello 你好') == 'utf-8'

    def test_trivial_bypass(self):
        print('Should safe:')
        assert test.check(phonetic_random)
    # def test_steno_check():

    def test_valid_english(self):
        print('Should safe:')
        assert test.check('#This *is* valid content')
    # def test_valid_chinese():
    #	print('Should pass:')
    #	print(test.block('#Hello 你好'))
    #	assert test.check('#Hello 你好')
