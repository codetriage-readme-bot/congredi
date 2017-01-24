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
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, ListOf
#, String, Integer, Boolean, DateTime
from ..types import EncAddress, EncHash, EncBool, EncSig, PrivAES, EncBlob
from ..types import ObjHash, ObjSig
#, ObjPubKey, ObjAddress, ObjBlob

# blockable pubkeys


class PrivateBlacklistChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    Sign & Encrypt Action
        - encrypt for the TO field.
    Create Integrity Data
        - sign with external key

        Check Integrity data (sesh hash/sig)
        - must be signed with FROM field
        Check Signature for action
            - must be in Admins keyspace
        Perform Action
            - Remove from blacklist.
        Return Response (encrypted, signed)
    Check Integrity Data
        - must be from TO field
    Check Encrypted Signature
        - must be from your server
    """


class PrivateBlacklistView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted blacklist, encrypted sig
    """


class PrivateWhitelistChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """


class PrivateWhitelistView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
# peers


class PrivatePeersChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted whitelist
    """


class PrivatePeersView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
# users/admins


class PrivateUsersChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """


class PrivateUsersView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """


class PrivateAdminsChange(Command):
    arguments = [(b'enc_address', EncAddress()),
                 (b'enc_hash', EncHash()),
                 (b'enc_action', EncBool()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_action', EncBool()),
                (b'enc_hash', EncHash()),
                (b'enc_sig', EncSig()),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """


class PrivateAdminsView(Command):
    arguments = [(b'enc_req_nonce', EncBlob()),
                 (b'enc_hash', EncHash()),
                 (b'enc_sig', EncSig()),
                 (b'sesh_key', PrivAES()),
                 (b'sesh_hash', ObjHash()),
                 (b'sesh_sig', ObjSig())]
    response = [(b'enc_blacklist', ListOf(EncAddress())),
                (b'sesh_hash', ObjHash()),
                (b'sesh_sig', ObjSig())]
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """


class settingResponders(object):
    config = None
    redis = None
    neo4j = None

    def __init__(self):
        # would pulll Redis online
        pass
    # blacklist

    @PrivateBlacklistChange.responder
    def ChangePrivateBlacklist(self, pubkey, address, direction):
        pass

    @PrivateBlacklistView.responder
    def ViewPrivateBlacklist(self, pubkey, address, direction):
        pass
    # whitelist

    @PrivateWhitelistChange.responder
    def ChangePrivateWhitelist(self, pubkey, address, direction):
        pass

    @PrivateWhitelistView.responder
    def ViewPrivateWhitelist(self, pubkey, address, direction):
        pass
    # peers

    @PrivatePeersChange.responder
    def ChangePrivatePeers(self, pubkey, address, direction):
        pass

    @PrivatePeersView.responder
    def ViewPrivatePeers(self, pubkey, address, direction):
        pass
    # users

    @PrivateUsersChange.responder
    def ChangePrivateUsers(self, pubkey, address, direction):
        pass

    @PrivateUsersView.responder
    def ViewPrivateUsers(self, pubkey, address, direction):
        pass
    # admins

    @PrivateAdminsChange.responder
    def ChangePrivateAdmins(self, pubkey, address, direction):
        pass

    @PrivateAdminsView.responder
    def ViewPrivateAdmins(self, pubkey, address, direction):
        pass
# congredi/commands/setting.py                72      9    88%   243, 248,
# 252, 257, 261, 266, 270, 275, 279
