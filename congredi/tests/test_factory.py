#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factory tests
"""
import unittest
from ..factory import CongrediPeerFactory


class test_factory(unittest.TestCase):

    def test_factory(self):
        a = CongrediPeerFactory()
        print('IMPLEMENT tests/test_factory')
