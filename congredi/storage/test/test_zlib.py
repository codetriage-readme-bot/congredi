#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
zlib tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
from ...storage.zlibs import compressDiff
from ...storage.zlibs import uncompressDiff
from ...storage.zlibs import chunkSplit
from ...utils.sources import source, source2


class test_zlib(TimedTestCase):
    things = [
        'a',
        'b',
        'c'
    ]
    splits = None
    thing1 = None
    res = None

    def test_split(self):
        """Split something into chunks"""
        self.threshold = .2
        self.splits = chunkSplit(source)
        print((len(self.splits)))

    def test_compression(self):
        """Compress, Uncompress, ensure equal"""
        self.threshold = .2
        self.thing1 = compressDiff(source2)
        self.res = uncompressDiff(self.thing1)
        print('New')
        print(self.res)
        print('Original')
        print(source2)
        assert self.res == source2

    # test split error-raising

    # test compression error-raising
