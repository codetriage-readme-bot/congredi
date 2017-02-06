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
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, ListOf, Boolean, DateTime, String, Integer
from ..types import ObjHash, ObjBlob
#ObjSig, ObjPubKey, ObjAddress,


# union operation (data transfer)
class SyncHavesWantsAsk(Command):
    arguments = [(b'have', ListOf(ObjHash)),
                 (b'want', ListOf(ObjHash))]
    # should be providing auths
    Responses = [(b'have', ListOf(ObjHash)),
                 (b'want', ListOf(ObjHash))]
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
# union operation (data transfer)


class SyncStorageAsk(Command):
    arguments = [(b'blobs', ListOf(ObjBlob))]
    # should be providing auths
    Responses = [(b'blobs', ListOf(ObjBlob))]
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
# store object (encrypted or not)


class StoreSet(Command):
    """
    Adding a key (permissioned, recursive)
    Adding a key (permissionless, non-recursive)
    """
    """
    sends: object
    recieves: lifetime, signature


    PUBLISH TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    sends: object
    recieves: lifetime, signature


    DEPLOY TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    """
    arguments = [(b'author', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]
    arguments = [(b'blob', ObjBlob()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'done', Boolean()),
                 (b'ttl', DateTime())]

    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """


class EncryptedStoreSet(Command):
    arguments = [(b'blob', ObjBlob()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'done', Boolean()),
                 (b'ttl', DateTime())]
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
# get object (encrypted or not)


class StoreGet(Command):
    """
    Geting a key (permissioned, recursive)
    Geting a key (permissionless, non-recursive)
    """
    """
    MONITOR TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    SUBSCRIBE TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    """

    arguments = [(b'reader', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """


class EncryptedStoreGet(Command):
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
# seek item ([hash]->num)


class SeekGet(Command):
    """
    Grab starting at a hash and moving backwards, with an offset and object count
    Grab starting at a hash and moving forward on the list, with an offset and object count
    Grab from the latest of the list, with an offset and object count
    """
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

    GET PAST foo stu OFFSET 1 COUNT 3
    GET FUTURE foo ghi OFFSET 2 COUNT 2
    GET CURRENT foo bar OFFSET 5 COUNT 2

    """
    arguments = [(b'type', String()),
                 (b'direction', String()),  # Forward || reverse
                 (b'hash', String()),  # hash || "latest"
                 (b'offset', Integer()),
                 (b'count', Integer())]
    response = [(b'hashes', String())]  # list of strings...
    arguments = [(b'keyspace', ObjHash()),
                 (b'count', Integer()),
                 (b'forward', Boolean())]
    # should be providing auths
    Responses = [(b'hashes', ListOf(ObjHash()))]
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
# resolve item ([hash])
# ?? might simply do 'send me the blobs'...


class ResolveGet(Command):
    arguments = [(b'hash', ObjHash())]
    # should be providing auths
    Responses = [(b'blob', ObjBlob())]
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
# search items


class SearchRun(Command):
    """
    Search from content-containing objects
    """
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

    GET SEARCH foo TERM "cats" OFFSET 10 COUNT 100

    [ bar, otherbar ]

    """
    arguments = [(b'type', String()),
                 (b'term', String()),
                 (b'offset', Integer()),
                 (b'count', Integer())]
    # response = [(b'hashes', String())]  # list of strings...
    arguments = [(b'hash', ObjHash()),
                 (b'type', String())]
    # should be providing auths
    responses = [(b'blob', ObjBlob()),
                 (b'ttl', DateTime())]
    """
    'resolve [hash]'
    I: hash
    O: blob
    """


class filesystemResponders(object):
    redis = None
    neo4j = None

    def __init__(self):
        # would pulll Redis online
        pass

    @SyncHavesWantsAsk.responder
    def SyncHavesWantsTell(self, yourWants, yourHaves):
        """
        'I have [x,y,z], I want [x,y,z], what do you have/want'
        I: list of hashes, list of hashes
        O: list of hashes, list of hashes
        """
        myWants = self.redis.read(b'wants')
        myHaves = self.redis.read(b'haves')
        self.redis.write(b'peer:wantsof:'+peerName, yourWants)
        self.redis.write(b'peer:havesof:'+peerName, yourHaves)
        return myWants, myHaves

    @SyncStorageAsk.responder
    def SyncStorageTell(self, yourBlobs, yourRequests):
        """
        'I have [x,y,z], I want [x,y,z], what do you have/want'
        I: list of hashes, list of hashes
        O: list of hashes, list of hashes
        """
        results = {}
        for request in yourRequests:
            results[request] = self.redis.read(b'blobs',request)
        self.redis.write(b'blobs', yourBlobs)
        #generateWants?
        #wants = self.redis.read(b'wants')
        return results #, wants

    @StoreSet.responder
    def StoreSetConfirm(self, blob, typeOf, author, sig):
        """
        'store blob [blob] of type [type]'
        I: blob, type
        O: bool, ttl
        """
        #checksig(sig)
        #checkPermissionForStorage()
        self.redis.write(blob)
        return True, ttl

    @EncryptedStoreSet.responder
    def EncryptedStoreSetConfirm(self, blob, typeOf, author, sig):
        """
        'store blob [blob] of type [type]'
        I: blob, type
        O: bool, ttl
        """
        #if checksig(sig)
        #if checkPermissionForEncryption()
        self.redis.write(blob)
        return True, ttl

    @StoreGet.responder
    def StoreGetRespond(self, keys, typeOf, author, sig):
        """
        'send blob [blob] of type [type]'
        I: list of hashes, type
        O: list of blobs, ttl
        """
        results = {}
        for request in keys:
            #sql escape on this keyspace...
            results[request] = self.redis.read(typeOf, request)
        return results, ttl

    @EncryptedStoreGet.responder
    def EncryptedStoreGetRespond(self, keys, typeOf, author, sig):
        """
        'send blob [blob] of type [type]'
        I: list of hashes, type
        O: list of blobs, ttl
        """
        #checkReadPermission()
        results = {}
        for request in keys:
            #sql escape...
            results[request] = self.redis.read(typeOf, request)
        return results, ttl
        

    @SeekGet.responder
    def SeekRespond(self, key, count, direction):
        """
        'seek hashes key [hash] count [number] direction [+/-]'
        I: hash, number, direction
        O: list of hashes
        """
        result = []
        current = key
        seek = b'next:'
        if direction == True:
            seek = b'previous:'
        try:
            for c in count:
                nextKey = self.redis.read(seek + current)
                result.append(nextKey)
                current = nextKey
        except:
            if len(result) == 0:
                return ErrNoPrevious()
            return ErrIncompleteListing()
        return result

    @ResolveGet.responder
    def ResolveRespond(self, keyhash, typeOf):
        """
        'resolve [hash]'
        I: hash
        O: blob
        """
        #check if that resolve exists?
        #findFirst()
        current = keyhash.first()
        for itter in keyHashList:
            current = diff.apply(current,modification)
        self.redis.write(b'resolved:'+keyhash,current)
        return current
            

    @SearchRun.responder
    def SearchRespond(self, keyspace, term):
        """
        'resolve [hash]'
        I: hash
        O: blob
        """
        regex = term
        results = []
        for keys in keyspace:
            key = self.redis.read(keys)
            lookup = regex(key)
            results.append(lookup)
        return results
# congredi/commands/filesystem.py             71     10    86%   246, 255,
# 264, 273, 282, 291, 300, 309, 318, 327
