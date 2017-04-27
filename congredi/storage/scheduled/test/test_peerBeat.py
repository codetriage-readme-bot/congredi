#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
peerBeat tests

    See PeerBeat. Should Implement.

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....utils.timing import TimedTestCase
# twisted.internet.task.Clock
from ..peerBeat import peerSuccess, peerFailure, peerBeat
from ..peerBeat import queryBackground, updateRead, updateWrite
from twisted.internet.error import ReactorNotRunning


class mock_traceback(object):
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def getBriefTraceback(self):
        return(self.msg)


class test_peerBeat(TimedTestCase):

    def test_peerBeat(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_peerBeat')
        queryBackground()
        updateRead()
        updateWrite()
        peerSuccess()
        fails = mock_traceback(b'wow')
        try:
            peerFailure(fails)
        except ReactorNotRunning:
            print('good')
        peerBeat()
