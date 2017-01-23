#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..whoops import CongrediError, whoops


# pylint: disable=no-self-use
class test_whoops(unittest.TestCase):

    def test_whoops(self):
        """The stack-trace printer needs work"""
        print('IMPLEMENT utils/test/test_whoops')
        whoops('hello')


# pylint: disable=no-self-use
class test_CongrediErrors(unittest.TestCase):

    def test_CongrediErrors(self):
        """Raising a CongrediError class"""
        # pylint: disable=broad-except
        try:
            raise CongrediError('Well then')
        except Exception as E:
            assert isinstance(E, CongrediError)
