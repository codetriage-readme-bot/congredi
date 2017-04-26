#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Redis Mock code
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
# https://seeknuance.com/2012/02/18/replacing-redis-with-a-python-mock/
class RedisMock(object):
    arr = {}

    def read(self, key):
        return self.get(key)
    def write(self, key, value):
        return self.set(key,value)
    def set(self, key, value):
        self.arr[key] = value
        return b'OK'

    def get(self, key):
        try:
            return self.arr[key]
        except:
            return []
