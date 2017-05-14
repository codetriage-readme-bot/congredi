#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
import datetime
from ...utils.timedTests import TimedTestCase
from ..jwt import token, jwt_get, jwt_use


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


class test_sig(TimedTestCase):

    def test_good_sig_token(self):
        print('Implement register/test/sig')
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


class test_sig2(TimedTestCase):

    def test_good_sig_token(self):
        print('Implement register/test/sig')
        a = datetime.datetime.now()
        assert a != None
        self.threshold = .1
        # bob = token('bob')
        # example = bob.make('print')
        # bob.check(example)
    # def test_expired_token(self):

    # def test_invalid_token(self):
    #     fred = token('fred')
    #     alice = token('alice')
    #     wrong = fred.make('well then')
    #     alice.check(wrong)


class test_email(TimedTestCase):

    def test_good_email_token(self):
        print('Implement register/test/email')
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


class test_token(TimedTestCase):

    def test_good_token(self):
        """Valid JWT Token"""
        self.threshold = .32
        bob = token(u'bob')
        example = bob.make(u'print')
        bob.check(example)

    def test_expired_token(self):
        """Expire a token..."""
        self.threshold = .1
        a = datetime.datetime.now()
        assert a != None

    def test_invalid_token(self):
        """Invalid Tokens"""
        self.threshold = .1
        fred = token(u'fred')
        alice = token(u'alice')
        wrong = fred.make(u'well then')
        alice.check(wrong)


class test_jwt(TimedTestCase):

    def test_routes(self):
        self.threshold = .1
        tok = jwt_get(u'ten')
        res = jwt_use(tok)
        print(res)
