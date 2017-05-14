#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remove keys no subscribed user cares about.

    Uses orphaning test code (mostly through directed children)

    user -> trees

    user <- trees

    check every tree, if it has a user, check to see if the user cares.
    if not, delete it.

Diff utils (instead of using a raw git library - a design problem)

    move to unified diff forward/backward
Neo4j Mock code

    will need to pull from Neo4j examples

Compression/packetization functions

    splitting diffs / compressing for sending
PGP key & IP routing
Resolves routes (usefull for commands I have now misplaced)

This has the same name as another file in proofs/router.py...

Also, need to find a Zero Knowledge Proof of the length
of a connection without indicating where on the connection
someone is (which would tell people if their neighbor can
be harassed).
Map a directed acyclic graph from one user to another,
and map objects that people use (possibly a minimum number of people use)

    pull from Neo4j examples
Redis Mock code

    The actual code is using RSet/RGet, outside of classes.
    Need the @defer.inlineCallbacks to work within a class :/

censor things objectionable to you, rather than store/query/communicate them
the current library is old and might simply need to include regexes...
(Feature: Should add the ability to publish your router's censor settings - #E)

These functions operate very primatively, if you wanted to censor content you'll
**REALLY** have to beef them up.

Encrypted Storage pretty-much wants content to be a binary mess, so I suppose
that's another use for the censor.

What it needs to do is provide that the object in question is a valid:

* diff
* sig
* pubkey
* markdown object

And that it contains no information that could be harmful. It'll be decoded,
escaped, into a markdown format, so XSS is still a problem, but should obey
the encoding we give it (ASCII/UTF-8/others?)


    this object doesn't update censor properties in tests
Render markdown. (possibly not needed on the python end of things)
py-gfm>=0.1.3

    migrate this out

Mock Storage code

    should abstract the get/set methods into a mock storage.
Redis database commands & mutexes, not exactly the objects needed

Interface, in the case that someone wants to use something besides Redis/Neo4j,
for instance hadoop or bigtable....
Check if peer is online, check latest trees that people subscribe to

    Two functions are missusing Ask() parameters from the rewrite.
    Make sure to neaten everything and set that in the spec.
periodically resolve a git tree

    recursive ask from contacts on tree contents.
Periodically audit a vote

    recursive on vote process (see commands/proofs/vote)

    delete? send error back to other clients? certify bit?

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
from twisted.internet import reactor

# from ...utils.config import configArr
# from ...utils.whoops import whoops

from .utils import configArr
from .utils import whoops
#from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime

from abc import ABCMeta, abstractmethod
import six
from .utils import CongrediError

from difflib import unified_diff, ndiff, restore
from .utils import ensureString
#from patch import fromstring
import zlib
from six.moves import range
from .utils import ensureBinary
import random
logger = logging.getLogger('congredi')
#from ..utils.iter import pairwise
from py2neo import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost')
import entropy
import chardet
from profanity import profanity
try:
    import pycld2 as cld2
    WINDOWS = False
except ImportError as e:  # no test for this
    WINDOWS = True
    print(e)
    WINDOWS_ERROR = e
    logger.warning('windows users will have pycld2 disabled for now')
import txredisapi as redis
from redlock import RedLock
import uuid

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
# from twisted.internet import defer
# from twisted.internet import reactor

# from ...utils.config import configArr
# from ...utils.whoops import whoops


# RedLock()

# will need to pull from settings... shouldn't ConfigArr have this?
connaddr = 'localhost'
connport = 6379


def queryBackground():  # test
    """
    Return an object from within peers
    One Subscription command -> several monitor commands
    """
    pass


def updateRead():  # test
    """
    Update trees with subscriptions
    One Subscription command -> several monitor commands
    """
    pass


def updateWrite():  # test
    """
    Publish trees to other nodes
    One Publish command -> several deploy commands
    """
    pass


shutDown = False


@defer.inlineCallbacks
def peerBeat():  # repeating peer-beat task
    # logger.info('peer heartbeat start')
    config = configArr()
    for admin in config['admins']:
        # logger.info('begin for admin: %s', admin)
        # test after the yields...
        # pylint: disable=unused-variable
        retset = yield Rset('admins', admin)
        retget = yield Rget('admins')
        retdel = yield Rdelete('admins')
        # pylint: enable=unused-variable
        # logger.info('set response:' + retset)
        # logger.info('get response:' + retget)
        # logger.info('delete response: %s', retdel)
    # if shutDown:
    #	loop.stop()


def peerSuccess():  # test
    logger.info('Peer Successful')


def peerFailure(failure):  # test
    logger.info('peer failure')
    whoops(failure.getBriefTraceback())
    reactor.stop()


#callID = reactor.callLater(5, f)
# callID.cancel()
# def main(reactor):
# 	delay = random.uniform(1, 5)
# 	d = task.deferLater(reactor, delay, f)
# 	d.addTimeout(3, reactor).addBoth(called)
# task.react(main)
"""
args
config
database


loop:
    check peers online
        increment/decrement peer online counter in db
    check online peers
        add/delete file listings
cmd:
    ping (hostname, port, key) -> pong (hostname, port, key)
    peers() -> peers(list[])
    have () -> have(list[])
    want () -> want(list[])
"""
