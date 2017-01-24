#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis object tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
# , redisSetup, Rget, Rset, RrandKey, todoAdd, todoRemove
from ..redis import RedisStore

# https://seeknuance.com/2012/02/18/replacing-redis-with-a-python-mock/


class RedisMock(object):
    arr = {}

    def set(self, key, value):
        self.arr[key] = value
        return b'OK'

    def get(self, key):
        return self.arr[key]


class test_redis(TimedTestCase):

    def setUp(self):
        self.conn = RedisMock()
        self.RedisStore = RedisStore(self.conn)
        super(test_redis, self).setUp()

    def test_redis(self):
        """Init a redis connection or use a mock?"""
        self.threshold = .1
        print('IMPLEMENT storage/test/test_redis')
        print(self.RedisStore._write(b'a', b'b'))
        print(self.RedisStore._read(b'a'))
        #assert b'b' == self.RedisStore._read(b'a')
