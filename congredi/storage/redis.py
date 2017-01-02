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


def redisSetup(host, port):
    return redis.Connection(host, port)


class RedisStore(abstractStorageProvider):

    def __init__(self, connection):
        self._conn = connection

    # actual writers
    @defer.inlineCallbacks
    def _write(self, key, value):
        res = yield self._conn.set(key, value)
        defer.returnValue(res)

    @defer.inlineCallbacks
    def _read(self, keyspace):
        res = yield self._conn.get(keyspace)
        defer.returnValue(res)

    # locks on items
    def _lockWrite(self, keyspace, valuespace):
        with RedLock(keyspace[:2]):
            return self._write(keyspace, valuespace)

    def _lockRead(self, keyspace):
        with RedLock(keyspace[:2]):
            return self._read(keyspace)

    # functions people will probably use
    def write(self, key, value):
        return self._lockWrite(key, value)

    def read(self, key):
        return self._lockRead(value)


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
