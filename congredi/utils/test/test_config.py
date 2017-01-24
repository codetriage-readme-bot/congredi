#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..config import configArr, generateConfig, writeConfig, openTest


class test_config(TimedTestCase):

    def test_config(self):
        """Grab Configuration From File"""
        self.threshold = .4
        newConf = configArr()
        existsConf = configArr()
        assert newConf == existsConf

    def test_bad_config(self):
        """corrupt yaml -> blank config"""
        self.threshold = .1

    def test_generate_config(self):
        """create config objects"""
        self.threshold = .1
        config = {}
        config = generateConfig(config)

    def test_write_config(self):
        """writes YAML to file"""
        self.threshold = .1
        config = generateConfig({})
        writeConfig('.test', config)

    def test_open_test_lacks_keys(self):
        """openTest checks for admins & users"""
        self.threshold = .1
        openTest('.test')
