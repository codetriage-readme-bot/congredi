#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP filesystem operations

Bulk Operations:
* SyncHavesWants        - send a list of hashes, recieve a list of hashes

New Bulk Operation:
* SyncStorage           - send a list of blobs, recieve a list of blobs


Smaller, previous non-bulk operations:
* StoreSet              - basic Redis operations...
* EncryptedStoreSet
* StoreGet
* EncryptedStoreGet
* Seek                  - send hashes by keyspace offset (hash, number, direction)
* Resolve               - not documented yet. Part of periodic tasks, http iface
* Search                - will not work on encrypted stores

"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime


# union operation (data transfer)
class SyncHavesWantsAsk(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """


def SyncHavesWantsTell():
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
    pass
# store object


def StoreSet():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass


def StoreConfirm():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass


def EncryptedStoreSet():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass


def EncryptedStoreConfirm():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass
# get object


def StoreGet():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass


def StoreRespond():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass


def EncryptedStoreGet():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass


def EncryptedStoreRespond():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass
# seek item ([hash]->num)


def SeekGet():
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
    pass


def SeekRespond():
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
    pass
# resolve item ([hash])


def ResolveGet():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass


def ResolveRespond():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass

# search items


def SearchRun():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass


def SearchResolve():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass
