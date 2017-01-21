#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
import hashlib
import codecs
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO
# from patch import PatchSet, fromstring
# pylint: disable=unused-import
from ..diff import resolveUnifiedDiff
from ..diff import resolveDiff
from ..diff import rebuildFile
from ..diff import tick
from ..diff import tock
from ...tests.sources import source, source2, empty, empty2
from ...storage.zlibs import chunkSplit
from ...utils.compat import ensureBinary, ensureString
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
        # not python3 compatible...
        # for c in splt:
        #     key = hashlib.sha256(c).hexdigest()
        #     print(type(c))
        #     data['pieces'][key] = c.encode('hex')
        # for k, v in data['pieces'].items():
        #     print(k,v.encode('hex'))
        jnd = b''.join(splt)
        final = hashlib.sha256(jnd).digest()
        print(('join %d' % len(jnd)))
        print(('hash: %(one)s\nhash: %(two)s' %
               {'one': codecs.encode(data['hash'], 'hex'), 'two': codecs.encode(final, 'hex')}))

    def test_uni(self):
        diff = resolveUnifiedDiff(
            source, source2,
            'congredi/test/core/algos/a.txt',
            'congredi/test/core/algos/b.txt')
        print(type(diff))
        # not python3 compatible
        #patch = fromstring(silenceInsanity(diff))
        # print((patch.errors))
        #patch.revert(0, root='.')
        #patch.apply(0, root=".")
