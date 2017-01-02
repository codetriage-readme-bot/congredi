#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
zlib tests
"""
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


class test_zlib(unittest.TestCase):

    def test_split(self):
        splits = chunkSplit(source)

    def test_compression(self):
        thing1 = compressDiff(source2)
        res = '\n'.join(uncompressDiff(thing1))
        print('New')
        print res
        print('Original')
        print source2
        assert res == source2
