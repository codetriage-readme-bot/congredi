#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
general tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest


# pylint: disable=no-self-use
class test_general(unittest.TestCase):

    def test_interpolate(self):
        """Interpolate two strings..."""
        n = "one"
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_typing(self):
        """Interpolate a number..."""
        n = 1
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_named(self):
        """Interpolate with named keys..."""
        n = 1
        key = "two"
        print(('one (%(name)s) %(key)s' % {'name': n, 'key': key}))
    # def test_numbered(self):
