#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test settings.

Some commands should be supreceeded by the config file or argument parameters.

That's probably something that could be in the config file:

Ordering:
 - options
 - config
 - database

Each of the setting options should be able to be changed and viewed.

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..setting import settingResponders


class test_setting(TimedTestCase):
    responderToTest = None

    def setUp(self):
        self.responderToTest = settingResponders()
        super(test_setting, self).setUp()

    def test_command_a(self):
        self.responderToTest.ChangePrivateBlacklist('a', 'b', 'c')
        print('IMPLEMENT tests/test_setting')
