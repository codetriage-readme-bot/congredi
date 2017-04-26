#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Neo4j Mock code
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod

class Neo4jMock(object):
    arr = {}
    def TrustWithin(self, key):
        return True
    def read(self, key):
        return self.get(key)
    def set(self, key, value):
        self.arr[key] = value
        return b'OK'

    def get(self, key):
        try:
            return self.arr[key]
        except:
            return []
