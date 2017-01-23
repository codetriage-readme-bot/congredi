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


def UserSync():
    pass


def UserBioUpdate():  # blob, previous hash, sig
    pass


def UserBioSync():
    pass


def UserLocationUpdate():  # zkp, previous hash, sig
    pass


def UserLocationSync():
    pass


def UserCourierUpdate():  # fingerprint, ip, previous hash, sig
    pass


def UserCourierSync():
    pass


def UserRendesvousUpdate():  # fingerprint, ip, previous hash, sig
    pass


def UserRendesvousSync():
    pass


def UserReqJoinUpdate():  # org fingerprints summary, previous hash, sig
    pass


def UserReqJoinSync():
    pass


def UserProposalUpdate():  # org fingerprints summary, commit hash, vote object, previous, sig
    pass


def UserProposalSync():
    pass


def UserMembershipUpdate():  # org fingerprints summary, proof of membership, previous, sig
    pass


def UserMembershipSync():
    pass


def UserCastedVotesUpdate():  # the vote, my ballot, previous hash, sig
    pass


def UserCastedVotesSync():
    pass


def UserTreeUpdate():  # hash of the starting commit, commit blob, previous hash, sig
    pass


def UserTreeSync():
    pass


def UserSavesUpdate():  # hash to save, previous saves hash, sig
    pass


def UserSavesSync():
    pass
