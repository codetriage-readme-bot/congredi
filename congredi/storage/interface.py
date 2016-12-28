#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Interface, in the case that someone wants to use something besides Redis/Neo4j,
for instance hadoop or bigtable....
"""


class storage():

    def __init__(self, typeOf):
        self.type = typeOf

    def PGet(self, key):
        pass

    def PSet(self, item):
        pass
from abc import ABCMeta, abstractmethod


class IInterface:
    __metaclass__ = ABCMeta

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def show(self): raise NotImplementedError


class MyServer(IInterface):

    def show(self):
        print 'Hello, World 2!'


class MyBadServer(object):

    def show(self):
        print 'Damn you, world!'


class MyClient(object):

    def __init__(self, server):
        if not isinstance(server, IInterface):
            raise Exception('Bad interface')
        if not IInterface.version() == '1.0':
            raise Exception('Bad revision')

        self._server = server

    def client_show(self):
        self._server.show()


# This call will fail with an exception
try:
    x = MyClient(MyBadServer)
except Exception as exc:
    print 'Failed as it should!'

# This will pass with glory
MyClient(MyServer()).client_show()
