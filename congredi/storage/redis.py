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

# Condensed txredisapi example... but where should yield go?
@defer.inlineCallbacks
def get(key):
	rc = yield redis.Connection("10.230.78.120")
	value = yield rc.get(key)
	logger.info('got {}:{}'.format(key,value))
	yield rc.disconnect()
	defer.returnValue(value)
@defer.inlineCallbacks
def set(key, value):
	rc = yield redis.Connection("10.230.78.120")
	res = yield rc.set(key, value)
	logger.info('set ({}) {}:{}'.format(res,key,value))
	yield rc.disconnect()
	defer.returnValue(res)
@defer.inlineCallbacks
def delete(key):
	rc = yield redis.Connection("10.230.78.120")
	n = yield rc.delete(key)
	logger.info('deleted ({}) {}'.format(n,key))
	yield rc.disconnect()
	defer.returnValue(n)
