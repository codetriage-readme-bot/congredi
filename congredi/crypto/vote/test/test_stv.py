#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test the STV implementation
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..stv import stvVote, stvPoll


# pylint: disable=no-self-use,unused-variable
class test_stv(unittest.TestCase):

    def test_stvPoll(self):
        """Init a poll object"""
        testPoll = stvPoll(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvPoll')

    def test_stvVote(self):
        """Init a vote object"""
        testVote = stvVote(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvVote')
