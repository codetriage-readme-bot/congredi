#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
general tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ..tests.timing import TimedTestCase


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
