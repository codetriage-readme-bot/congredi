#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
compute a vote
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from abc import ABCMeta, abstractmethod
import logging
import six
logger = logging.getLogger('congredi')

"""
Design - each of these classes could simply be an inferface or superclass?
The methods they'll use will be slightly different, but having these methods
helps us implement other vote types besides STV... #J
"""

# pylint: disable=abstract-method


class poll(six.with_metaclass(ABCMeta, object)):
    __doc__ = """
    A public STV style vote

    This class can use simple public key cryptography,
    no individual vote needs to be secret
    """

    @classmethod
    def version(self): return "1.0"

    def __init__(self, trees):
        """Object requires trees, sigs (Design - See docs #H)"""
        self.trees = trees

    @abstractmethod
    def cast(self, userVote):
        """
        Cast an invidual's vote (check that it is
        a valid vote option and a valid sig
        """
        raise NotImplementedError()

    @abstractmethod
    def validate(self, voteid):
        """
        Validate one vote (check option & sig)
        """
        raise NotImplementedError()

    @abstractmethod
    def compute(self):
        """
        Compute the winner of a vote
        """
        raise NotImplementedError()

    @abstractmethod
    def certify(self):
        """
        Check a vote result
        """
        raise NotImplementedError()


class vote(poll):
    __doc__ = """
    A private STV style vote (Theory - see congredi/papers #I)

    This class uses different cryptography primatives
    """
# congredi/crypto/vote/vote.py                23      5    78%   31, 43,
# 50, 57, 64
