#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Test register via SMS

The auths must be able to be tested as:

* Valid
* Expired
* Invalid
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import datetime
from ....utils.timing import TimedTestCase


class test_sms(TimedTestCase):

    def test_good_sms_token(self):
        print('Implement register/test/sms')
        self.threshold = .1
        a = datetime.datetime.now()
        assert a != None
        # bob = token('bob')
        # example = bob.make('print')
        # bob.check(example)
    # def test_expired_token(self):

    # def test_invalid_token(self):
    #     fred = token('fred')
    #     alice = token('alice')
    #     wrong = fred.make('well then')
    #     alice.check(wrong)
