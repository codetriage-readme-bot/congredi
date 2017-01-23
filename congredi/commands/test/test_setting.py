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
from ..command import PeerOptions, PeerOnions, PeerGet, PeerSet, PeerIndex, PeerSearch


# pylint: disable=no-self-use
class test_setting(unittest.TestCase):

    def test_command_a(self):
        print('IMPLEMENT tests/test_setting')
