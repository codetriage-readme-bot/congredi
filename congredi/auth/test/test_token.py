#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography)

JWT tokens can be one of:

* Good
* Expired
* Invalid

And granting them should not take database access. They are meant to
figure out if a user is auth'd without using the database to do so.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import datetime
from ...utils.timing import TimedTestCase
from ..token import token, jwt_get, jwt_use


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
