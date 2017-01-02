#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities tests
"""
import unittest
from ..whoops import CongrediError, whoops


class test_whoops(unittest.TestCase):

    def test_whoops(self):
        print('IMPLEMENT utils/test/test_whoops')


class test_CongrediErrors(unittest.TestCase):

    def test_CongrediErrors(self):
        try:
            raise CongrediError('Well then')
        except Exception as E:
            assert isinstance(E, CongrediError)
