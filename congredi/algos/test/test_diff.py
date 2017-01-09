#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
needs python3 patching
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import hashlib
import codecs
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from patch import PatchSet
# pylint: disable=unused-import
from ..diff import resolveUnifiedDiff
from ..diff import resolveDiff
from ..diff import rebuildFile
from ..diff import tick
from ..diff import tock
from ...tests.sources import source, source2, empty, empty2
from ...storage.zlibs import chunkSplit

# pylint: disable=no-self-use


class test_diff(unittest.TestCase):

    def test_resolve_ndiff(self):
        print('The Diff:')
        result = resolveDiff(source, source2)
        print((''.join(result)))
        print('The Original:')
        orig = rebuildFile(result, 1)
        print((''.join(orig)))

    def test_compression(self):
        # Direct conversion
        res = tick(source, source2)
        beep = tock(res, 1)
        print('Compression test:')
        print(beep)

    def test_splits(self):
        data = {'pieces': {}}
        comp = tick(empty, empty2)
        print(('compressed %d' % len(comp)))
        data['length'] = len(comp)
        data['hash'] = hashlib.sha256(comp).digest()
        splt = chunkSplit(comp)
        for c in splt:
            key = hashlib.sha256(c).digest()
            data['pieces'][key] = c
        for k, v in data['pieces'].items():
            print((k.encode('hex'), v.encode('hex')))
        jnd = b''.join(splt)
        final = hashlib.sha256(jnd).digest()
        print(('join %d' % len(jnd)))
        print(('hash: %(one)s\nhash: %(two)s' %
               {'one': codecs.encode(data['hash'], 'hex'), 'two': codecs.encode(final, 'hex')}))

    def test_uni(self):
        """need to get python3 compatibility"""
        # pu.db
        diff = resolveUnifiedDiff(
            source, source2,
            'congredi/test/core/algos/a.txt',
            'congredi/test/core/algos/b.txt')
        print(type(diff))
        patch = PatchSet(str(StringIO(diff)))
        print((patch.errors))
        patch.revert(0, root='.')
        patch.apply(0, root=".")
