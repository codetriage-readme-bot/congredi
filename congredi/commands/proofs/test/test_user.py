#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test commands
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....utils.timing import TimedTestCase
from ..user import userResponders


class test_user(TimedTestCase):
    responderToTest = None

    def SetUp(self):
        self.responderToTest = userResponders()
        super(test_user, self).setUp()

    def test_user_a(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_user')
