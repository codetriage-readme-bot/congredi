#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timedTests import TimedTestCase

# from ...storage.impl.MockRedis import RedisMock
# from ...storage.impl.MockNeo4j import Neo4jMock
# from ..commands import addressesResponders  # circular
# from ..commands import orgResponders, routerResponders, userResponders, settingResponders, filesystemResponders,  passportResponders


class test_setting(TimedTestCase):
    responderToTest = None

    # def setUp(self):
    #     # mock = RedisMock(b'redis v1')
    #     # self.responderToTest = settingResponders(mock)
    #     super(test_setting, self).setUp()

    # def test_command_a(self):
    #     # self.responderToTest.ChangePrivateBlacklist('a', 'b', 'c')
    #     print('IMPLEMENT tests/test_setting')


class test_passport(TimedTestCase):

    blacklist = []
    whitelist = []
    peers = []
    users = []
    admins = []
    responderToTest = None

    # def setUp(self):
    #     self.blacklist = ['a', 'b']
    #     self.whitelist = ['c']
    #     self.peers = ['d', 'e']
    #     self.users = ['a', 'b', 'f']
    #     self.admins = ['c', 'g']
    #     mockR = RedisMock(b'redis v1')
    #     mockN = Neo4jMock(b'neo4j v1')
    #     # self.responderToTest = passportResponders(mockR, mockN)
    #     super(test_passport, self).setUp()

    # def test_passport_a(self):
    #     # self.responderToTest.StoreGrant(None, None)
    #     print('IMPLEMENT tests/test_setting')


class test_filesystem(TimedTestCase):

    responderToTest = None

    # def setUp(self):
    #     # mock = RedisMock(b'redis v1')
    #     # self.responderToTest = filesystemResponders(mock)
    #     super(test_filesystem, self).setUp()

    # def test_command_a(self):
    #     ourBlobs = [b'1', b'2']
    #     ourReqs = [b'3', b'4']
    #     # self.responderToTest.SyncStorageTell(ourBlobs, ourReqs)
    #     print('IMPLEMENT tests/test_setting')


class test_addresses(TimedTestCase):

    responderToTest = None

    # def setUp(self):
    #     mock = RedisMock(b'redis v1')
    #     # self.responderToTest = addressesResponders(mock)
    #     super(test_addresses, self).setUp()

    # def test_addresses_a(self):
    #     # self.responderToTest.AddressTell()
    #     print('IMPLEMENT tests/test_setting')


class test_user(TimedTestCase):
    responderToTest = None

    def SetUp(self):
        # self.responderToTest = userResponders()
        super(test_user, self).setUp()

    def test_user_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_user')


class test_router(TimedTestCase):
    responderToTest = None

    def SetUp(self):
        # self.responderToTest = routerResponders()
        super(test_router, self).setUp()

    def test_router_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_router')


class test_org(TimedTestCase):
    responderToTest = None

    # def setUp(self):
    #     # self.responderToTest = orgResponders()
    #     super(test_org, self).setUp()

    def test_org_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_org')
