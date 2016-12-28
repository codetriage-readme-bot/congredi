#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compression/packetization functions
"""
import zlib

def chunkSplit(compressed): #restore: ''.join()
	"""Split chunks into the maximum size for AMP messages (if tripple encrypted) (Design - find that byte limit #F)"""
	return [compressed[k:k+250] for k in xrange(0, len(compressed), 250)]

def compressDiff(diff):
	"""Zlib compression (before packet transmission/storage)"""
	return zlib.compress(''.join(diff), 7)
def uncompressDiff(archive):
	"""Zlib decompression (before use)"""
	return zlib.decompress(archive).split('\n')
