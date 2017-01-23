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
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime
from ..types import ObjHash, ObjSig, ObjPubKey, ObjAddress, ObjBlob


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


@StoreRequest.responder
def StoreGrant(pubkey, ttl):
    """
    Compute 
    """
    pass
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


@StoreEncryptedRequest.responder
def StoreEncryptedGrant():
    pass

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


@PublishRequest.responder
def PublishGrant():
    pass


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


@SubscribeRequest.responder
def SubscribeGrant():
    pass

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


@RendesvousRequest.responder
def RendesvousGrant():
    pass


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


@CourierRequest.responder
def CourierGrant():
    pass

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


@SanctuaryRequest.responder
def SanctuaryGrant():
    pass


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


@SafePassageRequest.responder
def SafePassageGrant():
    pass
