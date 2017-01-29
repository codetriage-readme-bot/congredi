#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....utils.timing import TimedTestCase
from ..router import routerResponders


class test_router(TimedTestCase):
    responderToTest = None

    def SetUp(self):
        self.responderToTest = routerResponders()
        super(test_router, self).setUp()

    def test_router_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_router')
