#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test proxy stuff
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..daemon import api, proxy


class test_daemon(TimedTestCase):
    a = None
    b = None

    def test_daemon(self):
        a = api
        b = proxy
        assert a != b
        self.a = a
        self.b = b
        print('IMPLEMENT: extra/test/test_daemon:test_daemon')
