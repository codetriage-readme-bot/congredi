#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis object tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
#from ..redis import RedisStore, redisSetup, Rget, Rset, RrandKey, todoAdd, todoRemove

# https://seeknuance.com/2012/02/18/replacing-redis-with-a-python-mock/


class test_redis(TimedTestCase):

    def test_redis(self):
        """Init a redis connection or use a mock?"""
        self.threshold = .1
        print('IMPLEMENT storage/test/test_redis')
