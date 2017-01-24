#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
peerBeat tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....tests.timing import TimedTestCase
# twisted.internet.task.Clock
#from ..peerBeat import peerBeat, peerSuccess, peerFailure


class test_peerBeat(TimedTestCase):

    def test_peerBeat(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_peerBeat')
