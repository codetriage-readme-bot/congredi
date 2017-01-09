#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
randomness function libraries
"""
import binascii
import os

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
def random():
    return os.urandom(15)


def hexify(r):
    return binascii.hexlify(r)


def phony(h):
    return b" ".join(hexy[a] for a in h)
