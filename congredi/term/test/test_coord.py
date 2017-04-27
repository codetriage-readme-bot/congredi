#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testing coordination code

    Again, will need to simplify this.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import os
from ...utils.timing import TimedTestCase
from ..coord import fileCoord


def prep():
    try:
        os.remove('b')
    except OSError:
        pass


class test_coord(TimedTestCase):

    def test_coord(self):
        """Coordination code workarounds"""
        self.threshold = .1
        prep()
        h, p = fileCoord.read('b')
        fileCoord.write(h, p, 'b')
        nh, np = fileCoord.read('b')
        assert nh == h
        assert np == p
        prep()
