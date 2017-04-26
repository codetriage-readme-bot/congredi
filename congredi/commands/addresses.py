#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP commands for addresses - replaces command.py

Commands:
* Address - tell them what you thought theirs was, get what they saw yours as
* SyncPeerDirectory - send a list of (key, ip)s, get back a list of (key, ip)s
* SyncRendesvousDirectory - list of (key, rendesvousKey, proof) <->
* SyncCourierDirectory - list of (key, courierKey, proof) <->

These commands manage connections on the network (along with Router.py and
PeerBeat).

"""
from __future__ import absolute_import
from __future__ import unicode_literals
# , String, Boolean, DateTime
from twisted.protocols.amp import Command, Integer, ListOf
from ..types import ObjAddress, ObjPubKey
#ObjHash, ObjSig,

# find address from outside


class AddressAsk(Command):
    arguments = [(b'name', ObjAddress()),
                 (b'port', Integer())]
    response = [(b'name', ObjAddress()),
                (b'port', Integer())]


class SyncPeerDirectoryAsk(Command):
    # would have prefered dict capability.
    # these may need encoding...
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key,ip))
    out: list((key,ip))
    """
# rendesvous/courriers


class SyncRendesvousDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """


class SyncCourierDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, courier key, proof))
    out: list((key, courier key, proof))
    """


class addressesResponders(object):
    redis = None
    neo4j = None

    def __init__(self, givenRedis):
        self.redis = givenRedis
        # would pulll Redis online
        pass

    @AddressAsk.responder
    def AddressTell(self):
        """
        Add that person to the ephemeral recently-seen list.
        Send back what their IP/port was.
        """
        myAddress = self.redis.read(b'self:addr')
        return myAddress
    # ask the directory, while sending your own

    @SyncPeerDirectoryAsk.responder
    def SyncPeerDirectoryTell(self, yourPeers):
        """
        in: list((key,ip))
        out: list((key,ip))
        """
        myPeers = self.redis.read(b'list:peers')
        self.redis.write(b'todo:peers',yourPeers)
        return myPeers

    @SyncRendesvousDirectoryAsk.responder
    def SyncRendesvousDirectoryTell(self, yourRendesvous):
        """
        in: list((key, rendesvous key, proof))
        out: list((key, rendesvous key, proof))
        """
        myRendesvous = self.redis.read(b'list:rendesvous')
        self.redis.write(b'todo:rendesvous',yourRendesvous)
        pass

    @SyncCourierDirectoryAsk.responder
    def SyncCourierDirectoryTell(self, yourCouriers):
        myCouriers = self.redis.read(b'list:couriers')
        self.redis.write(b'todo:couriers',yourCouriers)
        pass
# congredi/commands/addresses.py              33      5    85%   80, 88,
# 97, 105, 109
