#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
FileSystem operations:


"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..filesystem import filesystemResponders


class test_filesystem(TimedTestCase):

    responderToTest = None

    def setUp(self):
        self.responderToTest = filesystemResponders()
        super(test_filesystem, self).setUp()

    def test_command_a(self):
        self.responderToTest.SyncStorageTell()
        print('IMPLEMENT tests/test_setting')
