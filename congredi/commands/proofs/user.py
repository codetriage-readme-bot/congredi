#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
These are the user properties.
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime
from ...types import ObjHash, ObjSig, ObjPubKey, ObjAddress, ObjBlob


class UserUpdate(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]
    """
    new public key, previous one signing it
    """


class UserSync(Command):
    response = []


class UserBioUpdate(Command):  # blob, previous hash, sig
    response = []


class UserBioSync(Command):
    response = []


class UserLocationUpdate(Command):  # zkp, previous hash, sig
    response = []


class UserLocationSync(Command):
    response = []


class UserCourierUpdate(Command):  # fingerprint, ip, previous hash, sig
    response = []


class UserCourierSync(Command):
    response = []


class UserRendesvousUpdate(Command):  # fingerprint, ip, previous hash, sig
    response = []


class UserRendesvousSync(Command):
    response = []


class UserReqJoinUpdate(Command):  # org fingerprints summary, previous hash, sig
    response = []


class UserReqJoinSync(Command):
    response = []


# org fingerprints summary, commit hash, vote object, previous, sig
class UserProposalUpdate(Command):
    response = []


class UserProposalSync(Command):
    response = []


# org fingerprints summary, proof of membership, previous, sig
class UserMembershipUpdate(Command):
    response = []


class UserMembershipSync(Command):
    response = []


# the vote, my ballot, previous hash, sig
class UserCastedVotesUpdate(Command):
    response = []


class UserCastedVotesSync(Command):
    response = []


# hash of the starting commit, commit blob, previous hash, sig
class UserTreeUpdate(Command):
    response = []


class UserTreeSync(Command):
    response = []


class UserSavesUpdate(Command):  # hash to save, previous saves hash, sig
    response = []


class UserSavesSync(Command):
    response = []


class userResponders(object):
    redis = None
    neo4j = None

    def __init__(self):
        # would pulll Redis online
        pass

    @UserUpdate.responder
    def Update(self):
        # arguments = [(b'name', String()),
        #              (b'port', Integer())]
        # response = [(b'hello', String())]
        """
        new public key, previous one signing it
        """
    @UserSync.responder
    def Sync(self):
        pass

    @UserBioUpdate.responder
    def BioUpdate(self):  # blob, previous hash, sig
        pass

    @UserBioSync.responder
    def BioSync(self):
        pass

    @UserLocationUpdate.responder
    def LocationUpdate(self):  # zkp, previous hash, sig
        pass

    @UserLocationSync.responder
    def LocationSync(self):
        pass

    @UserCourierUpdate.responder
    def CourierUpdate(self):  # fingerprint, ip, previous hash, sig
        pass

    @UserCourierSync.responder
    def CourierSync(self):
        pass

    @UserRendesvousUpdate.responder
    def RendesvousUpdate(self):  # fingerprint, ip, previous hash, sig
        pass

    @UserRendesvousSync.responder
    def RendesvousSync(self):
        pass

    @UserReqJoinUpdate.responder
    def ReqJoinUpdate(self):  # org fingerprints summary, previous hash, sig
        pass

    @UserReqJoinSync.responder
    def ReqJoinSync(self):
        pass

    @UserProposalUpdate.responder
    # org fingerprints summary, commit hash, vote object, previous, sig
    def ProposalUpdate(self):
        pass

    @UserProposalSync.responder
    def ProposalSync(self):
        pass

    @UserMembershipUpdate.responder
    # org fingerprints summary, proof of membership, previous, sig
    def MembershipUpdate(self):
        pass

    @UserMembershipSync.responder
    def MembershipSync(self):
        pass

    @UserCastedVotesUpdate.responder
    def CastedVotesUpdate(self):  # the vote, my ballot, previous hash, sig
        pass

    @UserCastedVotesSync.responder
    def CastedVotesSync(self):
        pass

    @UserTreeUpdate.responder
    def TreeUpdate(self):  # hash of the starting commit, commit blob, previous hash, sig
        pass

    @UserTreeSync.responder
    def TreeSync(self):
        pass

    @UserSavesUpdate.responder
    def SavesUpdate(self):  # hash to save, previous saves hash, sig
        pass

    @UserSavesSync.responder
    def SavesSync(self):
        pass
