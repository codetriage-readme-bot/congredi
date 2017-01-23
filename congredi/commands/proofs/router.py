#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime
from ...types import ObjHash, ObjSig, ObjPubKey, ObjAddress, ObjBlob
# addresses


class AddrGet(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]
    """
    'what is the address of the key [x]'
    I: key
    O: string
    """


class CensorPolicyGet(Command):
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
# ranks


class RankGet(Command):
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """


class SeenGet(Command):
    """
    'when was key [x] last seen'
    I: key
    O: string
    """


class UptimeGet(Command):
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
# haves/wants


class WantsGet(Command):
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """


class HasGet(Command):
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """


class ProofGet(Command):
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
# publish functions


class RendesvousGet(Command):
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """


class CourierGet(Command):
    """
    'courier of key [x]'
    I: key
    O: of, by
    """


class routerResponders(object):
    redis = None
    neo4j = None

    def __init__(self):
        # would pulll Redis online
        pass

    @AddrGet.responder
    def GetAddr(self, ):
        """
        'what is the address of the key [x]'
        I: key
        O: string
        """
        pass

    @CensorPolicyGet.responder
    def GetCensorPolicy(self, ):
        """
        'what is the censor policy of the key [x]'
        I: key
        O: string
        """
        pass

    @RankGet.responder
    def GetRank(self, ):
        """
        'what is the rank of the key [x]'
        I: key
        O: string
        """
        pass

    @SeenGet.responder
    def GetSeen(self, ):
        """
        'when was key [x] last seen'
        I: key
        O: string
        """
        pass

    @UptimeGet.responder
    def GetUptime(self, ):
        """
        'what is the uptime of key [x]'
        I: key
        O: string
        """
        pass

    @WantsGet.responder
    def GetWants(self, ):
        """
        'what does key [x] want'
        I: key
        O: list of hashes
        """
        pass

    @HasGet.responder
    def GetHas(self, ):
        """
        'what does key [x] have'
        I: key
        O: list of hashes
        """
        pass

    @ProofGet.responder
    def GetProof(self, ):
        """
        'prove key [x] has [hash] section[:] with [nonce]'
        I: key, hash, start, end, nonce
        O: proof
        """
        pass

    @RendesvousGet.responder
    def GetRendesvous(self, ):
        """
        'rendesvous of key [x]'
        I: key
        O: of, by
        """
        pass

    @CourierGet.responder
    def GetCourier(self, ):
        """
        'courier of key [x]'
        I: key
        O: of, by
        """
        pass
