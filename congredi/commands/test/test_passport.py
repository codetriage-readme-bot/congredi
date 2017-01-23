#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test passport.

Individual grants must be able to be:
* Valid
* Premature (add this to other tests as well...)
* Expired
* Invalid

Reasons to grant that need testing:

* Behavior          Good/Bad/Unknown - Recommendation Good/Bad/Unknown
* Manual Overide    Good/Bad
* Key Trust Depth   -1, 0, 1...
* Server Load       always grant, long term grant, probationary grant, short term grant, never grant

Possibly need to rework that server-load one

"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..command import PeerOptions, PeerOnions, PeerGet, PeerSet, PeerIndex, PeerSearch


# pylint: disable=no-self-use
class test_passport(unittest.TestCase):

    def test_passport_a(self):
        print('IMPLEMENT tests/test_passport')
