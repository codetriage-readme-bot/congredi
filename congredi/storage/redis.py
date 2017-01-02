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
from .interface import abstractStorageProvider
# RedLock()


def redisSetup(host, port): # test
    return redis.Connection(host, port)


class RedisStore(abstractStorageProvider):

    def __init__(self, connection): # test
        self._conn = connection

    # actual writers
    @defer.inlineCallbacks
    def _write(self, key, value): # test
        res = yield self._conn.set(key, value)
        defer.returnValue(res)

    @defer.inlineCallbacks
    def _read(self, keyspace): # test
        res = yield self._conn.get(keyspace)
        defer.returnValue(res)

    # locks on items
    def _lockWrite(self, keyspace, valuespace): # test
        with RedLock(keyspace[:2]):
            return self._write(keyspace, valuespace)

    def _lockRead(self, keyspace): # test
        with RedLock(keyspace[:2]):
            return self._read(keyspace)

    # functions people will probably use
    def write(self, key, value): # test
        return self._lockWrite(key, value)

    def read(self, key): # test
        return self._lockRead(value)


# Condensed txredisapi example... but where should yield go?
@defer.inlineCallbacks
def get(key): # test
    rc = yield redis.Connection("10.230.78.120")
    value = yield rc.get(key)
    logger.info('got {}:{}'.format(key, value))
    yield rc.disconnect()
    defer.returnValue(value)


@defer.inlineCallbacks
def set(key, value): # test
    rc = yield redis.Connection("10.230.78.120")
    res = yield rc.set(key, value)
    logger.info('set ({}) {}:{}'.format(res, key, value))
    yield rc.disconnect()
    defer.returnValue(res)


@defer.inlineCallbacks
def delete(key): # test
    rc = yield redis.Connection("10.230.78.120")
    n = yield rc.delete(key)
    logger.info('deleted ({}) {}'.format(n, key))
    yield rc.disconnect()
    defer.returnValue(n)


def randKey(): # test
    return str(uuid.uuid4().get_hex().upper()[0:6])


@defer.inlineCallbacks
def todoAdd(mutexKey, todoList, key): # test
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.lpush(todoList, key)
    logger.info('Updated Todo list {}: {}:{}'.format(todoList, key, ret))
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)


@defer.inlineCallbacks
def todoRemove(mutexKey, todoList): # test
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.rpop(todoList)
    logger.info('Grabbed from Todo list {}: {}'.format(todoList, ret))
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)
