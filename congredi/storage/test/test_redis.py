#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis object tests
"""
import unittest
from ..redis import RedisStore, redisSetup, get, set, randKey, todoAdd, todoRemove


class test_redis(unittest.TestCase):

    def test_redis(self):
        print('IMPLEMENT storage/test/test_redis')
