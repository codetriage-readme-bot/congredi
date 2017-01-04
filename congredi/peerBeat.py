#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Check if peer is online, check latest trees that people subscribe to
"""
import logging
logger = logging.getLogger('congredi')

#import random
from twisted.internet import defer
from twisted.internet import reactor

from .storage.redis import get, set, delete
from .utils.config import configArr
from .utils.whoops import whoops

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
    logger.info('peer heartbeat start')
    config = configArr()
    for admin in config['admins']:
        logger.info('begin for admin: {0}'.format(admin))
        # test after the yields...
        retset = yield set('admins', admin)
        retget = yield get('admins')
        retdel = yield delete('admins')
        logger.info('set response:' + retset)
        logger.info('get response:' + retget)
        logger.info('delete response: {}'.format(retdel))
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
