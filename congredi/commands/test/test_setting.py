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
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..setting import ChangePrivateBlacklist

# pylint: disable=no-self-use


class test_setting(unittest.TestCase):
    blacklist = []
    whitelist = []
    peers = []
    users = []
    admins = []

    def setUp(self):
        self.blacklist = ['a', 'b']
        self.whitelist = ['c']
        self.peers = ['d', 'e']
        self.users = ['a', 'b', 'f']
        self.admins = ['c', 'g']

    def test_command_a(self):
        ChangePrivateBlacklist('a', 'b', 'c')
        print('IMPLEMENT tests/test_setting')
