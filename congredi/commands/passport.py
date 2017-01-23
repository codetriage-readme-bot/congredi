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


# storage
"""
Storage applies a censor policy. If they want to avoid
that policy, they'll have to ask for an encryption permit
instead.
"""


class StoreRequest(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]


def StoreGrant():
    pass
"""
Encrypted storage applies an inverted sensor. It better
look like it's ben tripleSec encrypted, and we'll do it
again to keep the storage provider from indexing it.
"""


def StoreEncryptedRequest():
    pass


def StoreEncryptedGrant():
    pass

# private servers acting as publisher (permissioned or not)
"""
As a private server, a user will connect to them to find any
new content. This is where the actual data sits, if in
strict encryption mode. Otherwise, the rendesvous & courier
may be allowed to cache the request.
"""


def PublishRequest():
    pass


def PublishGrant():
    pass


def SubscribeRequest():
    pass


def SubscribeGrant():
    pass

# private servers acting as rendesvous to a server
"""
The Rendesvous (or publishing) and Courier (or subscribing)
relays are public addresses that speak on behalf of a server.
"""


def RendesvousRequest():
    pass


def RendesvousGrant():
    pass


def CourierRequest():
    pass


def CourierGrant():
    pass

# onion network / onion storage
"""
Sanctuary is an unlisted, encrypted server that
backs up, encrypted, to other servers. Safe Passage
is the permission to act as a tor-like relay
"""


def SanctuaryRequest():
    pass


def SanctuaryGrant():
    pass


def SafePassageRequest():
    pass


def SafePassageGrant():
    pass
