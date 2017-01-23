#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis object tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..redis import RedisStore, redisSetup, Rget, Rset, RrandKey, todoAdd, todoRemove

#https://seeknuance.com/2012/02/18/replacing-redis-with-a-python-mock/
# pylint: disable=no-self-use
class test_redis(unittest.TestCase):

    def test_redis(self):
        print('IMPLEMENT storage/test/test_redis')
