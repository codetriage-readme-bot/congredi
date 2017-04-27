#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis database commands & mutexes, not exactly the objects needed
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
import txredisapi as redis
from redlock import RedLock
import uuid
from .interface import abstractStorageProvider
# RedLock()


def redisSetup(host, port):  # test
    return redis.Connection(host, port)


class RedisStore(abstractStorageProvider):

    def __init__(self, connection=None):  # test
        if connection == None:
            self._conn = redisSetup('localhost',6379)
        super(RedisStore, self).__init__(connection)

    # actual writers
    @defer.inlineCallbacks
    def _write(self, keyspace, valuespace):  # test
        res = yield self._conn.set(keyspace, valuespace)
        defer.returnValue(res)

    @defer.inlineCallbacks
    def _read(self, keyspace):  # test
        res = yield self._conn.get(keyspace)
        defer.returnValue(res)
    # delete

    def _del(self, key):
        res = yield self._conn.delete(key)
        defer.returnValue(res)

    # locks on items
    def _lockWrite(self, keyspace, valuespace):  # test
        with RedLock(keyspace[:2]):
            return self._write(keyspace, valuespace)

    def _lockRead(self, keyspace):  # test
        with RedLock(keyspace[:2]):
            return self._read(keyspace)

    # functions people will probably use
    def write(self, key, value):  # test
        return self._lockWrite(key, value)

    def read(self, key):  # test
        return self._lockRead(key)


# Condensed txredisapi example... but where should yield go?
@defer.inlineCallbacks
def Rget(key):  # test
    rc = yield redis.Connection("localhost")
    value = yield rc.get(key)
    # logger.info('got %(key)s:%(value)s', {'key': key, 'value': value})
    yield rc.disconnect()
    defer.returnValue(value)


@defer.inlineCallbacks
def Rset(key, value):  # test
    rc = yield redis.Connection("localhost")
    res = yield rc.set(key, value)
    # logger.info('set (%s) %s:%s', res, key, value)
    yield rc.disconnect()
    defer.returnValue(res)


@defer.inlineCallbacks
def Rdelete(key):  # test
    rc = yield redis.Connection("localhost")
    n = yield rc.delete(key)
    # logger.info('deleted (%s) %s', n, key)
    yield rc.disconnect()
    defer.returnValue(n)


def RrandKey():  # test
    return str(uuid.uuid4().get_hex().upper()[0:6])


@defer.inlineCallbacks
def todoAdd(mutexKey, todoList, key):  # test
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.lpush(todoList, key)
    logger.info('Updated Todo list %(list)s: %(key)s:%(ret)s',
                {'list': todoList, 'key': key, 'ret': ret})
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)


@defer.inlineCallbacks
def todoRemove(mutexKey, todoList):  # test
    rc = yield redis.Connection("10.230.78.120")
    mutexKey.aquire()
    ret = yield rc.rpop(todoList)
    logger.info('Grabbed from Todo list %(list)s: %(ret)s',
                {'list': todoList, 'ret': ret})
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)
# congredi/storage/redis.py                   68     42    38%   19,
# 25-26, 31-32, 36-37, 41-42, 45-46, 50, 53, 59-63, 69-72, 77-81, 85,
# 90-97, 102-109
