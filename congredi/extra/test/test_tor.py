#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tor tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..tor import prox, start_rendesvous, print_bootstrap_lines, stop_rendesvous


# pylint: disable=no-self-use
class test_tor(unittest.TestCase):

    def test_tor(self):
        print('IMPLEMENT extra/test/test_tor')
