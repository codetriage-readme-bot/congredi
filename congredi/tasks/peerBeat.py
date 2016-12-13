#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Repeated tasks
"""

#import random
from twisted.internet import task
from twisted.internet import reactor

from ..storage.redis import RedisMixin
from ..storage.redis import RedisMethods

from ..storage.config import configArr

shutDown = False
print('beat loading')
def peerBeat(): # repeating peer-beat task
	config = configArr()
	print('beat')
	RedisMixin.setup()
	print('setup')
	conn = RedisMethods()
	print('methods')
	for admin in config['admins']:
		print(conn.set('admins',admin))
		print(conn.get(admin))
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
