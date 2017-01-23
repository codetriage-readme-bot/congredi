#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP private settings. Users must be a member of the 'admin' group in storage/configs,
and must send an encrypted command request to the server.

Commands:

* Blacklist - PGP pubkeys definitely allowed to connect or issue commands.
* Whitelist - PGP pubkeys blocked from connecting or issuing commands.
* Peers - pubkeys & IP addresses of peers strongly preferred.
* Users - People we take priority in storing for (privledged get/set)
* Admins - people allowed to change these settings


The blacklist/whitelist should probably include IPs as well.

Proposed:
    Peer commands will match either of the values within the blacklist,
    and will track the user should one change, for instance, a block of
    a public key will add the new IP address it's seen using?
    
    Problem: they could be in proxy mode?

"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime


# blockable pubkeys
class PrivateBlacklistChange(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """


def PrivateBlacklistView():
    """
    I: signed request, encrypted session key
    O: encrypted blacklist, encrypted sig
    """
    pass


def PrivateWhitelistChange():
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """
    pass


def PrivateWhitelistView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
# peers


def PrivatePeersChange():
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted whitelist
    """
    pass


def PrivatePeersView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
# users/admins


def PrivateUsersChange():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass


def PrivateUsersView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass


def PrivateAdminsChange():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass


def PrivateAdminsView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
