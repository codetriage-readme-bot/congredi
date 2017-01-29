#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....utils.timing import TimedTestCase
from ..org import orgResponders


class test_org(TimedTestCase):
    responderToTest = None

    def setUp(self):
        self.responderToTest = orgResponders()
        super(test_org, self).setUp()

    def test_org_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_org')
