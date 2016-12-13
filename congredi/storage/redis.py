#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions for using Redis
"""
import sys
from twisted.internet import defer
from twisted.internet import reactor
from twisted.python import log
import txredisapi as redis

@defer.inlineCallbacks
def redis_test():
	rc = yield redis.Connection("10.230.78.120")
	yield rc.set("foo", "bar")
	v = yield rc.get("foo")
	print "foo:", repr(v)
	yield rc.disconnect()

class RedisMixin(object):
	redis_conn = None
	@classmethod
	def setup(self):
		RedisMixin.redis_conn = redis.lazyConnectionPool()


# Condensed txredisapi example... but where should yield go?
class RedisMethods(RedisMixin):
	@defer.inlineCallbacks
	def get(self, key):
		print('getting')
		value = self.redis_conn.get(key)
		print('got')
		yield key, value
	@defer.inlineCallbacks
	def set(self, key, value):
		res = self.redis_conn.set(key, value)
		yield res, key, value
	@defer.inlineCallbacks
	def delete(self, key):
		n = self.redis_conn.delete(key)
		yield key, n
