#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities
"""


class CongrediError(Exception):
    """Ability to raise a custom error or family of errors (design - family of errors to raise?)"""
    pass


def whoops(err):  # test
    """The default errback (design - set as default errback?)"""
    print('whoops')
    print(err)
