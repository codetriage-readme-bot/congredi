#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP passport - grant abilities to a server.

Quickly checks permissions to operate in
specific capacities.

* Storage               (proof & key-trust check)
* Encrypted Storage     (longer proof & key-trust check)
* Publish               (hidden server storing data)
* Subscribe             (hidden server looking for data)
* Rendesvous            (publish side load-balance IP)
* Courier               (subscribe side load-balance IP)
* Sanctuary             (recursive use of encrypted storage, off the books)
* Safe Passage          (permission to connect with forwardable packets)

Permissions are granted/lost on:

* Behavior
* Manual Overide
* Key Trust Depth
* Server Load

Could possibly introduce rate limits?

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, DateTime
#, String, Integer, ListOf, Boolean
from ..types import ObjHash, ObjSig, ObjPubKey
#ObjAddress, ObjBlob


# storage
"""
Storage applies a censor policy. If they want to avoid
that policy, they'll have to ask for an encryption permit
instead.
"""


class StoreRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# PubKey, TTL -> Boolean, TTL
"""
Encrypted storage applies an inverted sensor. It better
look like it's ben tripleSec encrypted, and we'll do it
again to keep the storage provider from indexing it.
"""


class StoreEncryptedRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# private servers acting as publisher (permissioned or not)
"""
As a private server, a user will connect to them to find any
new content. This is where the actual data sits, if in
strict encryption mode. Otherwise, the rendesvous & courier
may be allowed to cache the request.
"""


class PublishRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]


class SubscribeRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# private servers acting as rendesvous to a server
"""
The Rendesvous (or publishing) and Courier (or subscribing)
relays are public addresses that speak on behalf of a server.
"""


class RendesvousRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]


class CourierRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]
# onion network / onion storage
"""
Sanctuary is an unlisted, encrypted server that
backs up, encrypted, to other servers. Safe Passage
is the permission to act as a tor-like relay
"""


class SanctuaryRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]


class SafePassageRequest(Command):
    arguments = [(b'my_pubkey', ObjPubKey()),
                 (b'my_start', DateTime()),
                 (b'my_ttl', DateTime()),
                 (b'my_hash', ObjHash()),
                 (b'my_sig', ObjSig())]
    response = [(b'your_pubkey', ObjPubKey()),
                (b'your_start', DateTime()),
                (b'your_ttl', DateTime()),
                (b'your_hash', ObjHash()),
                (b'my_sig', ObjSig())]


class passportResponders(object):
    redis = None
    neo4j = None

    def __init__(self, GivenRedis, GivenNeo4j):
        # would pull Neo4j online
        self.redis = GivenRedis
        self.neo4j = GivenNeo4j

    @StoreRequest.responder
    def StoreGrant(self, pubkey, ttl):
        """
        Compute
        """
        # somehow store TTL?
        if self.neo4j.TrustWithin(3):
            self.redis.write(b'permissions:store', pubkey)
        signedStorage = b'TBD'
        ttl = b'TBD'
        return signedStorage, ttl

    @StoreEncryptedRequest.responder
    def StoreEncryptedGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(2):
            self.redis.write(b'permissions:storeEncrypted', pubkey)
        signedStorage = b'TBD'
        ttl = b'TBD'
        return signedStorage, ttl

    @PublishRequest.responder
    def PublishGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(3):
            self.redis.write(b'permissions:publish', pubkey)
        signedPublish = b'TBD'
        ttl = b'TBD'
        return signedPublish, ttl

    @SubscribeRequest.responder
    def SubscribeGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(2):
            self.redis.write(b'permissions:subscribe', pubkey)
        signedSubscribe = b'TBD'
        ttl = b'TBD'
        return signedSubscribe, ttl

    @RendesvousRequest.responder
    def RendesvousGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'rendesvous', pubkey)
        signedRendesvous = b'TBD'
        ttl = b'TBD'
        return signedRendesvous, ttl

    @CourierRequest.responder
    def CourierGrant(self, pubkey, ttl):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'courier', pubkey)
        signedCourier = b'TBD'
        ttl = b'TBD'
        return signedCourier, ttl

    @SanctuaryRequest.responder
    def SanctuaryGrant(self, pubkey):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'permissions:sanctuary', pubkey)
        signedSanctuary = b'TBD'
        ttl = b'TBD'
        return signedSanctuary, ttl

    @SafePassageRequest.responder
    def SafePassageGrant(self, pubkey):
        if self.neo4j.TrustWithin(1):
            self.redis.write(b'permissions:onion', pubkey)
        signedSafePassage = b'TBD'
        ttl = b'TBD'
        return signedSafePassage, ttl
# congredi/commands/passport.py               50      9    82%   177, 184,
# 188, 192, 196, 200, 204, 208, 212
