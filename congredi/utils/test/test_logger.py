#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test logger
"""
from __future__ import absolute_import
from __future__ import unicode_literals
from ...tests.timing import TimedTestCase
from ..logger import formatLevel, passLevel, logger
import logging


def check_level():
    logging_code = logger.getEffectiveLevel()
    human_readable = logging.getLevelName(logging_code)
    print ((logging_code, human_readable))
    return (logging_code, human_readable)


class test_logger(TimedTestCase):

    def test_logger_level(self):
        """Changing FormatLevel"""
        # need to check if this is logging correctly
        self.threshold = .4
        formatLevel('INFO')
        formatLevel('DEBUG')

    def test_pass_args(self):
        """tests for options"""
        self.threshold = .3

        class args(object):
            quiet = False
            verbose = False
            debug = False
        passLevel(args)
        assert check_level() == (30, 'WARNING')
        # should set quiet
        args.quiet = True
        passLevel(args)
        assert check_level() == (50, 'CRITICAL')
        # should set to verbose
        args.verbose = True
        passLevel(args)
        assert check_level() == (20, 'INFO')
        # should set to debug
        args.debug = True
        passLevel(args)
        assert check_level() == (10, 'DEBUG')
