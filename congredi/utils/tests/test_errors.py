#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ..timedTests import TimedTestCase
from ..errors import CongrediError


class test_CongrediErrors(TimedTestCase):

    def test_CongrediErrors(self):
        """Raising a CongrediError class - fail if no error"""
        self.threshold = .4
        try:
            raise CongrediError('Well then')
        except CongrediError as E:
            assert isinstance(E, CongrediError)
            return True
        assert True is False
