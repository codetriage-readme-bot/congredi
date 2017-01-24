#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test the STV implementation
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....tests.timing import TimedTestCase
from ..stv import stvVote, stvPoll


# pylt: disable=unused-variable
class test_stv(TimedTestCase):

    def test_stvPoll(self):
        """Init a poll object"""
        self.threshold = .1
        testPoll = stvPoll(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvPoll')
        assert testPoll != None

    def test_stvVote(self):
        """Init a vote object"""
        self.threshold = .1
        testVote = stvVote(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvVote')
        assert testVote != None
