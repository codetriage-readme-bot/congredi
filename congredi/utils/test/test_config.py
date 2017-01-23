#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import unittest
from ..config import configArr


# pylint: disable=no-self-use
# pylint: disable=unused-variable
class test_config(unittest.TestCase):

    def test_config(self):
        """Grab Configuration From File"""
        newConf = configArr()
        existsConf = configArr()
