#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
from twisted.internet import reactor
# from twisted.internet import defer
# from twisted.internet import reactor
from ..storage.impl.redis import Rget, Rset, Rdelete


# RedLock()

# will need to pull from settings... shouldn't Config have this?


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
    config = {}
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
    logger.critical(failure.getBriefTraceback())
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
