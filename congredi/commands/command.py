#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests

These are the old ask/tell commands to check
that everything was working. I'm still not sure if they were, honestly.

This file, and its test (test/test_command.py) will be removed.
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime


class PeerAsk(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]


class PeerTell(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'hello', String())]


class PeerOptions(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'options', ListOf(String()))]


class PeerOnions(Command):
    arguments = [(b'name', String()),
                 (b'port', Integer())]
    response = [(b'options', ListOf(String()))]

"""
Geting a key (permissioned, recursive)
Geting a key (permissionless, non-recursive)
"""


class PeerGet(Command):
    """
    MONITOR TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    SUBSCRIBE TYPE foobar HASH hash READER reader SIGNATURE sig
    [ Results[], 2016-10-11 20:10:10, signature ]
    """

    arguments = [(b'reader', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]

"""
Adding a key (permissioned, recursive)
Adding a key (permissionless, non-recursive)
"""


class PeerSet(Command):
    """
    sends: object
    recieves: lifetime, signature


    PUBLISH TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    sends: object
    recieves: lifetime, signature


    DEPLOY TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
    [ 2016-10-11 20:10:10, signature ]
    """
    arguments = [(b'author', String()),
                 # permissioned + recursive || permissionless + unrecursive
                 (b'authority', Boolean()),
                 (b'hash', String()),
                 (b'signature', String()),
                 (b'object', String()),
                 (b'type', String())
                 ]
    response = [
        (b'lifetime', DateTime()),
        (b'signature', String())]
    # errors = no space


"""
Grab starting at a hash and moving backwards, with an offset and object count
Grab starting at a hash and moving forward on the list, with an offset and object count
Grab from the latest of the list, with an offset and object count
"""


class PeerIndex(Command):
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

    GET PAST foo stu OFFSET 1 COUNT 3
    GET FUTURE foo ghi OFFSET 2 COUNT 2
    GET CURRENT foo bar OFFSET 5 COUNT 2

    """
    arguments = [(b'type', String()),
                 (b'direction', String()),  # Forward || reverse
                 (b'hash', String()),  # hash || "latest"
                 (b'offset', Integer()),
                 (b'count', Integer())]
    response = [(b'hashes', String())]  # list of strings...


"""
Search from content-containing objects
"""


class PeerSearch(Command):
    """
    type : hash : [list]
    foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

    GET SEARCH foo TERM "cats" OFFSET 10 COUNT 100

    [ bar, otherbar ]

    """
    arguments = [(b'type', String()),
                 (b'term', String()),
                 (b'offset', Integer()),
                 (b'count', Integer())]
    response = [(b'hashes', String())]  # list of strings...
