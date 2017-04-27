#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
general tests for string behavior. If these fail,
lots of tests that use string interpolation will
error because of the string interpolation.

This is a good catch for people writing a test
with a buggy print statement.

Then again, there's always pylint.

Thank You Py2/3 compatibility problems...

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ..utils.timing import TimedTestCase


class test_general(TimedTestCase):

    def test_interpolate(self):
        """Interpolate two strings..."""
        self.threshold = .1
        n = "one"
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_typing(self):
        """Interpolate a number..."""
        self.threshold = .1
        n = 1
        key = "two"
        print(('interpolate (%s) %s' % (n, key)))

    def test_named(self):
        """Interpolate with named keys..."""
        self.threshold = .1
        n = 1
        key = "two"
        print(('one (%(name)s) %(key)s' % {'name': n, 'key': key}))
    # def test_numbered(self):
