#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Check if peer is online, check latest trees that people subscribe to

    Two functions are missusing Ask() parameters from the rewrite.
    Make sure to neaten everything and set that in the spec.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
from twisted.internet import reactor

from ...storage.redis import Rget, Rset, Rdelete
from ...utils.config import configArr
from ...utils.whoops import whoops


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
        retset = yield Rset('admins', admin)
        retget = yield Rget('admins')
        retdel = yield Rdelete('admins')
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
# congredi/storage/scheduled/peerBeat.py      35     12    66%   23, 31,
# 39, 53-57, 63, 67-69
