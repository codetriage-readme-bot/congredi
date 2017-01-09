#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test the STV implementation
"""
import unittest
from ..stv import stvVote, stvPoll


# pylint: disable=no-self-use,unused-variable
class test_stv(unittest.TestCase):

    def test_stvPoll(self):
        testPoll = stvPoll(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvPoll')

    def test_stvVote(self):
        testVote = stvVote(object)
        print('IMPLEMENT algos/vote/test/test_stv.py:test_stvVote')
