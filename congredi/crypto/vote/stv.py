#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main client class - terminal
"""
from __future__ import unicode_literals
from .vote import poll, vote
#from pyvotecore.stv import stv


class stvVote(vote):

    def cast(self, userVote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass


class stvPoll(poll):

    def cast(self, userVote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass
# congredi/crypto/vote/stv.py                 21      8    62%   14, 17,
# 20, 23, 29, 32, 35, 38
