#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis database commands & mutexes, not exactly the objects needed
"""
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
import txredisapi as redis
from redlock import RedLock
import uuid

# stub method because hey, separate files.


def redisLock(key):
    return RedLock(key)


# Condensed txredisapi example... but where should yield go?
@defer.inlineCallbacks
def get(key):
    rc = yield redis.Connection("10.230.78.120")
    value = yield rc.get(key)
    logger.info('got {}:{}'.format(key, value))
    yield rc.disconnect()
    defer.returnValue(value)


@defer.inlineCallbacks
def set(key, value):
    rc = yield redis.Connection("10.230.78.120")
    res = yield rc.set(key, value)
    logger.info('set ({}) {}:{}'.format(res, key, value))
    yield rc.disconnect()
    defer.returnValue(res)


@defer.inlineCallbacks
def delete(key):
    rc = yield redis.Connection("10.230.78.120")
    n = yield rc.delete(key)
    logger.info('deleted ({}) {}'.format(n, key))
    yield rc.disconnect()
    defer.returnValue(n)


def randKey():
    return str(uuid.uuid4().get_hex().upper()[0:6])


@defer.inlineCallbacks
def todoAdd(mutexKey, todoList, key):
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.lpush(todoList, key)
    logger.info('Updated Todo list {}: {}:{}'.format(todoList, key, ret))
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)


@defer.inlineCallbacks
def todoRemove(mutexKey, todoList):
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.rpop(todoList)
    logger.info('Grabbed from Todo list {}: {}'.format(todoList, ret))
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)
