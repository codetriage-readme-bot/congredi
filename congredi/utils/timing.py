#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Timing objects for UnitTest

    these use Blender's color codes class,

    as well as the setUp/tearDown functions for timing.

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import time


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
warning = bcolors.WARNING + 'Timing Warning' + bcolors.ENDC + \
    ': Test Took ' + bcolors.BOLD + '%.2f' + bcolors.ENDC + \
    's (threshold ' + bcolors.FAIL + '%.2f' + bcolors.ENDC + 's)'


class TimedTestCase(unittest.TestCase):

    def setUp(self):
        #print('ran setup for %s' % self.id())
        self.threshold = .5
        self._time_started = time.time()

    def tearDown(self):
        elapsed = time.time() - self._time_started
        if elapsed > self.threshold:
            print((warning % (elapsed, self.threshold)))
