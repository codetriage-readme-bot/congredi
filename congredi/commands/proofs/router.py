#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime


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


def AddrRespond():
    """
    'what is the address of the key [x]'
    I: key
    O: string
    """
    pass


def CensorPolicyGet():
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
    pass


def CensorPolicyRespond():
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
    pass
# ranks


def RankGet():
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """
    pass


def RankRespond():
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """
    pass


def SeenGet():
    """
    'when was key [x] last seen'
    I: key
    O: string
    """
    pass


def SeenRespond():
    """
    'when was key [x] last seen'
    I: key
    O: string
    """
    pass


def UptimeGet():
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
    pass


def UptimeRespond():
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
    pass
# haves/wants


def WantsGet():
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """
    pass


def WantsRespond():
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """
    pass


def HasGet():
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """
    pass


def HasRespond():
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """
    pass


def ProofGet():
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
    pass


def ProofRespond():
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
    pass
# publish functions


def RendesvousGet():
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """
    pass


def RendesvousRespond():
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """
    pass


def CourierGet():
    """
    'courier of key [x]'
    I: key
    O: of, by
    """
    pass


def CourierRespond():
    """
    'courier of key [x]'
    I: key
    O: of, by
    """
    pass
