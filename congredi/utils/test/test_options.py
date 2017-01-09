#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
options testing
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..options import MainOptions

goodOpts = {
    'client': ['client'],
    'peer': ['peer']
}
badOpts = {
    'client': ['client', '8088'],
    'peer': ['pelt', '-p', '8080']
}


# pylint: disable=no-self-use, unused-variable, bare-except
class test_options(unittest.TestCase):

    def test_good_options(self):
        for opts in goodOpts.values():
            print(opts)
            args = MainOptions.parse_args(opts)

    def test_bad_options(self):
        for opts in badOpts.values():
            try:
                args = MainOptions.parse_args(opts)
            except:
                continue
            raise Exception("Didn't fail when I expected...")
