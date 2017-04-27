#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FileSystem operations:


"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..filesystem import filesystemResponders
from ...storage.MockRedis import RedisMock


class test_filesystem(TimedTestCase):

    responderToTest = None

    def setUp(self):
        mock = RedisMock(b'redis v1')
        self.responderToTest = filesystemResponders(mock)
        super(test_filesystem, self).setUp()

    def test_command_a(self):
        ourBlobs = [b'1', b'2']
        ourReqs = [b'3', b'4']
        self.responderToTest.SyncStorageTell(ourBlobs, ourReqs)
        print('IMPLEMENT tests/test_setting')
