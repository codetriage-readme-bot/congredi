#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functions for using Redis
"""
import txredisapi as redis
from twisted.internet import defer
@defer.inlineCallbacks
def redis_test():
	rc = yield redis.Connection("10.230.78.120")
	yield rc.set("foo", "bar")
	v = yield rc.get("foo")
	print "foo:", repr(v)
	yield rc.disconnect()
