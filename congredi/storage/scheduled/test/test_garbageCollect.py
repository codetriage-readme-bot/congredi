#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
garbageCollect tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....tests.timing import TimedTestCase
# from ..garbageCollect
# twisted.internet.task.Clock


class test_garbageCollect(TimedTestCase):

    def test_garbageCollect(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_garbageCollect')
