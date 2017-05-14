#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timedTests import TimedTestCase
#from ..configplugins import configplugin
from ..conffile import openTest


class test_config(TimedTestCase):

    def test_open_test_lacks_keys(self):
        """openTest checks for admins & users NO ASSERT"""
        self.threshold = .1
        openTest('.test')
