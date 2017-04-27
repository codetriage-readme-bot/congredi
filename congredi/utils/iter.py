#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pairwise implementation (used in ../storage/Router)

should this be used anywhere else, or moved into Router?

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from itertools import tee
from six.moves import zip
# Pairwise recipe


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))
