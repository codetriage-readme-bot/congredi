#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
import hashlib
try: from StringIO import StringIO
except ImportError: from io import StringIO
from patch import PatchSet
# pylint: disable=unused-import
from ...algos.diff import resolveUnifiedDiff
from ...algos.diff import resolveDiff
from ...algos.diff import rebuildFile
from ...algos.diff import tick
from ...algos.diff import tock
from ..sources import source, source2, empty, empty2
from ...storage.zlibs import chunkSplit




def test_resolve_ndiff():
	print('The Diff:')
	result = resolveDiff(source, source2)
	print(''.join(result))
	print('The Original:')
	orig = rebuildFile(result, 1)
	print(''.join(orig))
def test_compression():
	# Direct conversion
	res = tick(source, source2)
	beep = tock(res, 1)
	print('Compression test:')
	print(beep)
def test_splits():
	data = {'pieces':{}}
	comp = tick(empty, empty2)
	print('compressed {}'.format(len(comp)))
	data['length'] = len(comp)
	data['hash'] = hashlib.sha256(comp).digest()
	splt = chunkSplit(comp)
	for c in splt:
		key = hashlib.sha256(c).digest()
		data['pieces'][key] = c
	for k, v in data['pieces'].items():
		print(k.encode('hex'), v.encode('hex'))
	jnd = ''.join(splt)
	final = hashlib.sha256(jnd).digest()
	print('join {}'.format(len(jnd)))
	print('hash: {}\nhash: {}'.format(
		data['hash'].encode('hex'), final.encode('hex')))

def test_uni():
	# pu.db
	diff = resolveUnifiedDiff(
				source, source2,
				'congredi/test/core/algos/a.txt',
				'congredi/test/core/algos/b.txt')
	patch = PatchSet(StringIO(diff))
	print(patch.errors)
	patch.revert(0, root='.')
	patch.apply(0, root=".")
