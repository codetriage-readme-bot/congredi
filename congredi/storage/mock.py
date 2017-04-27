#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Mock Storage code

    should abstract the get/set methods into a mock storage.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from .interface import abstractStorageProvider


class MockStorage(abstractStorageProvider):

    def __init__(self, typeOf):
        self.type = typeOf
        super(MockStorage, self).__init__(typeOf)

    @classmethod
    def version(self): return "1.0"

    def _read(self, keyspace):
        return self.get(keyspace)

    def _write(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)

    def _lockRead(self, keyspace):
        return self.get(keyspace)

    def _lockWrite(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)
