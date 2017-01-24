#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interface, in the case that someone wants to use something besides Redis/Neo4j,
for instance hadoop or bigtable....
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
import six
from ..utils.whoops import CongrediError


class CongrediBadInterfaceError(CongrediError):
    pass


class CongrediIncompatibleVersionError(CongrediBadInterfaceError):
    pass


class abstractStorageProvider(six.with_metaclass(ABCMeta, object)):

    def __init__(self, typeOf):
        self.type = typeOf

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def _write(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _read(self, keyspace):
        raise NotImplementedError()

    @abstractmethod
    def _lockWrite(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _lockRead(self, keyspace):
        raise NotImplementedError()


class abstractStorageConsumer(object):

    def __init__(self, storage):
        if not isinstance(storage, abstractStorageProvider):
            raise CongrediBadInterfaceError('Bad Interface!')
        if not storage.version() == '1.0':
            raise CongrediIncompatibleVersionError('Non-compatible version!')
        self._storage = storage

    def write(self, key, value):
        self._storage._lockWrite(key, value)

    def read(self, key):
        return self._storage._lockRead(key)
# class Base(metaclass=ABCMeta):
# congredi/storage/interface.py               29     13    55%   16, 19,
# 23, 27, 31, 35, 41-45, 48, 51
