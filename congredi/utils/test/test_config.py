#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..config import configArr


class test_config(TimedTestCase):

    def test_config(self):
        """Grab Configuration From File"""
        self.threshold = .4
        newConf = configArr()
        existsConf = configArr()
        assert newConf == existsConf
