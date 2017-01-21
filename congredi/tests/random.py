#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
randomness function libraries
"""
import binascii
import os

hexy = {
    # Fix to bypass dictionary as "english"
    "0": b"Zero", "1": b"One", "2": b"Two", "3": b"Three",
    "4": b"Four", "5": b"Five", "6": b"Six", "7": b"Seven",
    "8": b"Eight", "9": b"Nine", "a": b"Apple", "b": b"Boy",
    "c": b"Cat", "d": b"Dog", "e": b"Echo", "f": b"Fox",
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
    return b" ".join(hexy[a] for a in str(h)[2:-1])
