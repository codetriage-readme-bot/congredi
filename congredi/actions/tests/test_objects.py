#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timedTests import TimedTestCase
from ..objects import L2Str, Str2L

class test_types(TimedTestCase):

    def test_LStir(self):
        self.threshold = .1
        assert b'b' == L2Str(Str2L(b'b'))
