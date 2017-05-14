#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Timing tests, not using assert (need to test color?)
error utilities tests

    whoops (traceback)
    CongrediError (an error class)
        - pull in all subclasses into these error class tests
test logger
progress test (count to 1000)
## all code should be importing from ..logger, not using import logging.
options testing
test oracle functions.s
Yaml Config Loading - & default configs
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import time
import logging
from ..utils.tests import TimedTestCase
from .utils import configArr, generateConfig, writeConfig, openTest
from ..utils.oracle import random, hexify, phony, pick_range
from .utils import together
from .utils import MainOptions
from .utils import CongrediError, whoops
from .utils import formatLevel, passLevel, logger
