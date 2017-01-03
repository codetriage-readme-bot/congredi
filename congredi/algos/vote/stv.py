#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main client class - terminal
"""
from .vote import poll, vote
#from pyvotecore.stv import stv


class stvVote(vote):

    def cast(self, vote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass


class stvPoll(poll):

    def cast(self, vote):  # test
        pass

    def validate(self, voteid):  # test
        pass

    def compute(self):  # test
        pass

    def certify(self):  # test
        pass
