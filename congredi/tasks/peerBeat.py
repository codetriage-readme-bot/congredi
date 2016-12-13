#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Repeated tasks
"""
import logging
logger = logging.getLogger('congredi')

#import random
from twisted.internet import task
from twisted.internet import defer
from twisted.internet import reactor

import txredisapi as redis
from ..storage.redis import get, set, delete
from ..storage.config import configArr

shutDown = False
@defer.inlineCallbacks
def peerBeat(): # repeating peer-beat task
	config = configArr()
	logger.info('heartbeat')
	for admin in config['admins']:
		retset = yield set('admins', admin)
		retget = yield get('admins')
		retdel = yield delete('admins')
		logger.info('set response:' + retset)
		logger.info('get response:' + retget)
		logger.info('delete response: {}'.format(retdel))
	#if shutDown:
	#	loop.stop()
def peerSuccess():
	print('Peer Successful')
def peerFailure(failure):
	print(failure.getBriefTraceback())
	reactor.stop()



#callID = reactor.callLater(5, f)
#callID.cancel()
# def main(reactor):
# 	delay = random.uniform(1, 5)
# 	d = task.deferLater(reactor, delay, f)
# 	d.addTimeout(3, reactor).addBoth(called)
#task.react(main)
