#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP Objects. If I don't have to serialize them, why bother?

These provide readible names for argument Types:

EncBool                 - Boolean (len?)
EncAddress/ObjAddress   - Addresses (IP/Tor/DNS)
EncPubKey/ObjPubKey     - Public Keys (len?)
ObjHash/EncHash         - Hashes (len?)
ObjSig/EncSig           - Sig of Hash (len?)
ObjBlob/EncBlob         - General Blobs

PrivAES                 - RSA encrypted session key

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Argument
# if necissary, these will do something besides just send binary.
# could be doing hash validation for all this??
# class inheritance?
# Encrypted Boolean

# pylint: disable=arguments-differ


class EncBool(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Addresses (IP/Tor/DNS) : len? Type?


class ObjAddress(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncAddress(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Public Keys : len?


class ObjPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString
# Hashes : len?


class ObjHash(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncHash(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Sigs of Hashes : len?


class ObjSig(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncSig(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Blobs (general, compressed?)


class ObjBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob


class EncBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# RSA encrypted session key : len?


class PrivAES(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# congredi/types.py                           64     24    63%   31, 34,
# 41, 44, 50, 53, 60, 63, 69, 72, 79, 82, 88, 91, 98, 101, 107, 110, 117,
# 120, 126, 129, 136, 139
