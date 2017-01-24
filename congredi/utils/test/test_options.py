#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
options testing
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..options import MainOptions
import argparse
goodOpts = {
    'client': ['client'],
    'peer': ['peer']
}
badOpts = {
    'client': ['client', '8088'],
    'peer': ['pelt', '-p', '8080']
}


class test_options(TimedTestCase):

    def test_good_options(self):
        """All of these options should be good:"""
        self.threshold = .4
        for opts in goodOpts.values():
            print(opts)
            MainOptions.parse_args(opts)

    def test_bad_options(self):
        """All of these options should fail and be caught to continue:"""
        self.threshold = .4
        for opts in badOpts.values():
            try:
                MainOptions.parse_args(opts)
            except (argparse.ArgumentError, SystemExit) as ex:
                print(("Caught: %s" % ex))
                continue
            raise Exception("Didn't fail when I expected...")
