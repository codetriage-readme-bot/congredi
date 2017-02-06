#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
A mock redis object, for testing.
"""
from __future__ import absolute_import
from __future__ import unicode_literals
try:
    import redis
    mock_redis = redis.connect('localhost')
except:
    class mock_redis(object):
        arr = {}
    
        def set(self, key, value):
            self.arr[key] = value
            return b'OK'
    
        def get(self, key):
            return self.arr[key]

        def del(self, key):
            self.arr.remove(key)
            return b'OK'
