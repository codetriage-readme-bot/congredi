#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
factory tests
"""
import unittest
from ..factory import CongrediPeerFactory


# pylint: disable=no-self-use
class test_factory(unittest.TestCase):

    def test_factory(self):
        a = CongrediPeerFactory()
        a.startedConnecting('well then')
        print('IMPLEMENT tests/test_factory')
