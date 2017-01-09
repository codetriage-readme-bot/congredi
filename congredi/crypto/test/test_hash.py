#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing hashes
"""
import unittest
from ..hash import make_hash


# pylint: disable=no-self-use
class test_hash(unittest.TestCase):

    def test_good_hash(self):
        res = make_hash('123456')
        res = res.hexdigest()
        #res = res.encode('hex')
        check = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
        print(res)
        print(check)
        assert res == check
