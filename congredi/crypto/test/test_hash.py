#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Testing hashes
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ..hash import make_hash


class test_hash(TimedTestCase):
    good_hash = None

    def test_good_hash(self):
        """Make sure a hex-digest of the current library works"""
        res = make_hash(b'123456').hexdigest()
        #res = res.encode('hex')
        check = "8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92"
        print(res)
        print(check)
        assert res == check
        self.good_hash = res
