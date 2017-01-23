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
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime


# find address from outside
class AddressAsk(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]


def AddressTell():
    pass
# ask the directory, while sending your own


def SyncPeerDirectoryAsk():
    """
    in: list((key,ip))
    out: list((key,ip))
    """
    pass


def SyncPeerDirectoryTell():
    """
    in: list((key,ip))
    out: list((key,ip))
    """
    pass
# rendesvous/courriers


def SyncRendesvousDirectoryAsk():
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """
    pass


def SyncRendesvousDirectoryTell():
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """
    pass


def SyncCourierDirectoryAsk():
    """
    in: list((key, courier key, proof))
    out: list((key, courier key, proof))
    """
    pass


def SyncCourierDirectoryTell():
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """
    pass
