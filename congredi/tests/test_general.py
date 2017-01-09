#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
general tests
"""
import unittest


# pylint: disable=no-self-use
class test_general(unittest.TestCase):

    def test_interpolate(self):
        n = "one"
        key = "two"
        print('interpolate (%s) %s' % (n, key))

    def test_typing(self):
        n = 1
        key = "two"
        print('interpolate (%s) %s' % (n, key))

    def test_named(self):
        n = 1
        key = "two"
        print('one (%(name)s) %(key)s' % {'name': n, 'key': key})
    # def test_numbered(self):
