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
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..passport import passportResponders


class test_passport(TimedTestCase):

    blacklist = []
    whitelist = []
    peers = []
    users = []
    admins = []
    responderToTest = None

    def setUp(self):
        self.blacklist = ['a', 'b']
        self.whitelist = ['c']
        self.peers = ['d', 'e']
        self.users = ['a', 'b', 'f']
        self.admins = ['c', 'g']
        self.responderToTest = passportResponders()
        super(test_passport, self).setUp()

    def test_passport_a(self):
        self.responderToTest.StoreGrant(None, None)
        print('IMPLEMENT tests/test_setting')
