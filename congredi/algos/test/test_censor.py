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
    # Fix to bypass dictionary as "english"
    "0": "Zero", "1": "One", "2": "Two", "3": "Three",
    "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
    "8": "Eight", "9": "Nine", "a": "Apple", "b": "Boy",
    "c": "Cat", "d": "Dog", "e": "Echo", "f": "Fox",
    # unused past this
    "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November",
    "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor",
    "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}
test = censor(encodings=['UTF-8', 'ascii'], languages=['ENGLISH', 'CHINESE'])


def random():
    return os.urandom(15)


def hexify(r):
    return binascii.hexlify(r)


def phony(h):
    return " ".join(hexy[a] for a in h)

# pylint: disable=no-self-use
# pylint: disable=unused-variable


class test_censor(unittest.TestCase):

    def test_obvious_catch(self):
        print('Should block (best 8/10, os.urandom()):')
        passes = 0
        for x in xrange(0, 10):
            actual_random = random()
            res = test.check(actual_random)
            if not res:
                passes += 1
        print("%d/10" % passes)
        assert passes >= 8

    def test_encode(self):
        print('Should safe (best 14/15, os.urandom()):')
        passes = 0
        for x in xrange(0, 15):
            encoded_random = hexify(random())
            if stateEncoding(encoded_random) == 'ascii':
                passes += 1
        print("%d/15" % passes)
        assert passes >= 14

    def test_trivial_bypass(self):
        print('Should safe (best 24/25, os.urandom()):')
        passes = 0
        for x in xrange(0, 25):
            phonetic_random = phony(hexify(random()))
            if test.check(phonetic_random):
                passes += 1
        print("%d/25" % passes)
        assert passes >= 24

    def test_unicode(self):
        assert stateEncoding('hello 你好') == 'utf-8'

    # def test_steno_check():

    def test_valid_english(self):
        print('Should safe:')
        assert test.check('#This *is* valid content')
    # def test_valid_chinese():
    #	print('Should pass:')
    #	print(test.block('#Hello 你好'))
    #	assert test.check('#Hello 你好')
