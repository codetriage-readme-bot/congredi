#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
zlib tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ...storage.zlibs import compressDiff
from ...storage.zlibs import uncompressDiff
from ...storage.zlibs import chunkSplit
from ...tests.sources import source, source2

things = [
    'a',
    'b',
    'c'
]


# pylint: disable=no-self-use
class test_zlib(unittest.TestCase):

    def test_split(self):
        splits = chunkSplit(source)
        print((len(splits)))

    def test_compression(self):
        thing1 = compressDiff(source2)
        res = uncompressDiff(thing1)
        print('New')
        print(res)
        print('Original')
        print(source2)
        assert res == source2
