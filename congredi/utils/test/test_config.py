#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
import unittest
from ..config import configArr


class test_config(unittest.TestCase):

    def test_config(self):
        newConf = configArr()
        existsConf = configArr()
