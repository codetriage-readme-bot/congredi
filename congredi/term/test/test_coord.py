#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
testing coordination code
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import os
import unittest
from ..coord import fileCoord


def prep():
    # pylint: disable=bare-except
    try:
        os.remove('b')
    except:
        pass


# pylint: disable=no-self-use
class test_coord(unittest.TestCase):

    def test_coord(self):
        """Coordination code workarounds"""
        prep()
        h, p = fileCoord.read('b')
        fileCoord.write(h, p, 'b')
        nh, np = fileCoord.read('b')
        assert nh == h
        assert np == p
        prep()
