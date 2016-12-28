#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
from twisted.protocols import amp


class PeerAsk(amp.Command):
    arguments = [('name', amp.String()),
                 ('port', amp.Integer())]
    response = [('hello', amp.String())]


class PeerTell(amp.Command):
    arguments = [('name', amp.String()),
                 ('port', amp.Integer())]
    response = [('hello', amp.String())]

"""
Geting a key (permissioned, recursive)
Geting a key (permissionless, non-recursive)
"""


class PeerGet(amp.Command):
    arguments = [('reader', amp.String()),
                 # permissioned + recursive || permissionless + unrecursive
                 ('authority', amp.Boolean()),
                 ('hash', amp.String()),
                 ('signature', amp.String()),
                 ('object', amp.String()),
                 ('type', amp.String())
                 ]
    response = [
        ('lifetime', amp.Date()),
        ('signature', amp.String())]
    # errors = no space

"""
MONITOR TYPE foobar HASH hash READER reader SIGNATURE sig
[ Results[], 2016-10-11 20:10:10, signature ]
SUBSCRIBE TYPE foobar HASH hash READER reader SIGNATURE sig
[ Results[], 2016-10-11 20:10:10, signature ]
"""
"""
Adding a key (permissioned, recursive)
Adding a key (permissionless, non-recursive)
"""


class PeerSet(amp.Command):
    arguments = [('author', amp.String()),
                 # permissioned + recursive || permissionless + unrecursive
                 ('authority', amp.Boolean()),
                 ('hash', amp.String()),
                 ('signature', amp.String()),
                 ('object', amp.String()),
                 ('type', amp.String())
                 ]
    response = [
        ('lifetime', amp.Date()),
        ('signature', amp.String())]
    # errors = no space

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

"""
Grab starting at a hash and moving backwards, with an offset and object count
Grab starting at a hash and moving forward on the list, with an offset and object count
Grab from the latest of the list, with an offset and object count
"""


class PeerIndex(amp.Command):
    arguments = [('type', amp.String()),
                 ('direction', amp.String()),  # Forward || reverse
                 ('hash', amp.String()),  # hash || "latest"
                 ('offset', amp.Integer()),
                 ('count', amp.Integer())]
    response = [('hashes', amp.String())]  # list of strings...

"""
type : hash : [list]
foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

GET PAST foo stu OFFSET 1 COUNT 3
GET FUTURE foo ghi OFFSET 2 COUNT 2
GET CURRENT foo bar OFFSET 5 COUNT 2

"""

"""
Search from content-containing objects
"""


class PeerSearch(amp.Command):
    arguments = [('type', amp.String()),
                 ('term', amp.String()),
                 ('offset', amp.Integer()),
                 ('count', amp.Integer())]
    response = [('hashes', amp.String())]  # list of strings...

"""
type : hash : [list]
foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

GET SEARCH foo TERM "cats" OFFSET 10 COUNT 100

[ bar, otherbar ]

"""
