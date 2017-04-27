#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Abstract Interface Provider tests

    basic checks for good/bad interface code:

    the interfaces need to have certain functions, and while
    we're not checking that the outputs match (feature), this
    is a basic check that the stated internal API of a developed
    driver matches.

    These checks are of an interface that has what it
    needs, and one that doesn't have everything, to test
    our CongrediBadInterfaceError & CongrediIncompatibleVersionError

    Feature: Check function return signatures on an abstract-method?

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..interface import abstractStorageProvider, abstractStorageConsumer
from ..interface import CongrediBadInterfaceError, CongrediIncompatibleVersionError


class good_provider(abstractStorageProvider):

    def _write(self, keyspace, valuespace):
        return b'ok'

    def _read(self, keyspace):
        return b'value'

    def _lockWrite(self, keyspace, valuespace):
        return b'ok'

    def _lockRead(self, keyspace):
        return b'value'


class test_interface(TimedTestCase):

    def test_not_implemented(self):
        self.threshold = .1
        # pylint: disable=abstract-method

        class bad_provider(abstractStorageProvider):
            pass
        # pylint: enable=abstract-method
        # pylint: disable=abstract-class-instantiated,no-value-for-parameter,
        # arguments-differ
        try:
            a = bad_provider()
            a.write(b'one')
            self.fail()
        except (CongrediBadInterfaceError, TypeError):
            pass
        # pylint: enable=abstract-class-instantiated,no-value-for-parameter

    def test_client_okay(self):
        self.threshold = .1
        provider1 = good_provider('a')
        client = abstractStorageConsumer(provider1)
        client.write(b'b', b'b')
        client.read(b'b')

    def test_client_mad(self):
        self.threshold = .1
        b = good_provider('a')

        def funk():
            return "2.0"
        b.version = funk
        try:
            client = abstractStorageConsumer(b)
            client.write(b'b', b'b')
            print('bad')
        except CongrediIncompatibleVersionError:
            print('good')
        c = object()
        try:
            client = abstractStorageConsumer(c)
            client.write(b'b', b'b')
            print('bad')
        except CongrediBadInterfaceError:
            print('good')
