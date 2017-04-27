#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Log management (could use twisted's log utility, but must have formating ability)

    maintenance: look for usage across codebase, simplify (keep it simple, stupid)

"""
#from twisted.python import log
# log.startLogging(sys.stdout)

from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')


def passLevel(args):
    """take an args object and set the log level"""
    level = logging.WARNING
    if args.quiet:
        level = logging.CRITICAL
    if args.verbose:
        level = logging.INFO
    if args.debug:
        level = logging.DEBUG
    formatLevel(level)


def formatLevel(level):
    """set formatting based on a level"""
    formatting = "%(levelname)s %(filename)s(%(lineno)d) %(funcName)s: %(message)s"
    if level == logging.DEBUG:
        formatting = "%(asctime)s[%(name)s:%(levelname)s]%(filename)s(%(lineno)d) %(funcName)s: %(message)s"
    setLog(level, formatting)


def setLog(level, formatting):
    """Set log level"""
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    fm = logging.Formatter(
        formatting,
        "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fm)
    logger.addHandler(fh)
# congredi/utils/logger.py                    26      9    65%   17-24, 31
