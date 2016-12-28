#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
compute a vote
"""
import logging
logger = logging.getLogger('congredi')

"""
Design - each of these classes could simply be an inferface or superclass?
The methods they'll use will be slightly different, but having these methods
helps us implement other vote types besides STV... #J
"""


class poll():
    """
    A public STV style vote

    This class can use simple public key cryptography,
    no individual vote needs to be secret
    """

    def __init__(self, trees):
        """Object requires trees, sigs (Design - See docs #H)"""
        self.trees = trees

    def cast(self, vote):
        """
        Cast an invidual's vote (check that it is
        a valid vote option and a valid sig
        """
        pass

    def validate(self, voteid):
        """
        Validate one vote (check option & sig)
        """
        pass

    def compute(self):
        """
        Compute the winner of a vote
        """
        pass

    def certify(self):
        """
        Check a vote result
        """
        pass


class vote():
    """
    A private STV style vote (Theory - see congredi/papers #I)

    This class uses different cryptography primatives
    """

    def __init__(self, trees):
        """Object requires trees, sigs (Design - See docs #H)"""
        self.trees = trees

    def cast(self):
        """
        Cast an invidual's vote (check that it is
        a valid vote option and a valid sig
        """
        pass

    def validate(self):
        """
        Validate one vote (check option & sig)
        """
        pass

    def compute(self):
        """
        Compute the winner of a vote
        """
        pass

    def certify(self):
        """
        Check a vote result
        """
        pass
