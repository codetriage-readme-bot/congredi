#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..whoops import CongrediError, whoops


class test_whoops(TimedTestCase):

    def test_whoops(self):
        """The stack-trace printer needs work"""
        print('IMPLEMENT utils/test/test_whoops')
        self.threshold = .4
        whoops('hello')


class test_CongrediErrors(TimedTestCase):

    def test_CongrediErrors(self):
        """Raising a CongrediError class"""
        self.threshold = .4
        try:
            raise CongrediError('Well then')
        except CongrediError as E:
            assert isinstance(E, CongrediError)
