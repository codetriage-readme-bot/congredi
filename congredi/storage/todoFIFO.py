#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions for using Redis
"""
import logging
logger = logging.getLogger('congredi')
import sys
from twisted.internet import defer
from twisted.internet import reactor
from twisted.python import log
import txredisapi as redis
import uuid


def randKey():
	return str(uuid.uuid4().get_hex().upper()[0:6])

@defer.inlineCallbacks
def todoAdd(mutexKey, todoList, key):
	rc = yield redis.Connection("10.230.78.120")
	mutexKey.aquire()
	ret = yield rc.lpush(todoList,key)
	logger.info('Updated Todo list {}: {}:{}'.format(todoList, key, ret))
	mutexKey.release()
	yield rc.disconnect()
	defer.returnValue(ret)
@defer.inlineCallbacks
def todoRemove(mutexKey, todoList):
	rc = yield redis.Connection("10.230.78.120")
	mutexKey.aquire()
	ret = yield rc.rpop(todoList)
	logger.info('Grabbed from Todo list {}: {}:{}'.format(todoList, key, ret))
	mutexKey.release()
	yield rc.disconnect()
	defer.returnValue(ret)
