#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tor tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..tor import prox, start_rendesvous, print_bootstrap_lines, stop_rendesvous


class test_tor(TimedTestCase):
    a = None

    def test_tor(self):
        print('IMPLEMENT extra/test/test_tor')
        a = prox
        b = start_rendesvous
        c = print_bootstrap_lines
        d = stop_rendesvous
        assert a != b
        assert c != d
        self.a = a
