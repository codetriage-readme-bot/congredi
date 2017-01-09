#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis object tests
"""
# pylint: disable=unused-import
import unittest
from ..redis import RedisStore, redisSetup, Rget, Rset, RrandKey, todoAdd, todoRemove


# pylint: disable=no-self-use
class test_redis(unittest.TestCase):

    def test_redis(self):
        print('IMPLEMENT storage/test/test_redis')
