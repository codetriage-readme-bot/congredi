#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')


class CongrediError(Exception):
    """
        Ability to raise a custom error or family of errors (design - family of errors to raise?)
        pulling other Error classes from other files into here.

        Key/Connection/Command style errors?
    """
    pass


def whoops(err):  # test
    """
    The default errback (design - set as default errback?)
    can't pull traceback, which is unfortunate.
    """
    #trace = traceback.format_exc()
    # traceback.print_exc()
    logger.critical(err)
