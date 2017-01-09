#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compression/packetization functions
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import zlib
from six.moves import range


def chunkSplit(compressed):  # restore: ''.join()
    """Split chunks into the maximum size for AMP messages (if tripple encrypted) (Design - find that byte limit #F)"""
    return [compressed[k:k + 250] for k in range(0, len(compressed), 250)]


def compressDiff(diff):
    """Zlib compression (before packet transmission/storage)"""
    if type(diff) is list:
        diff = b''.join(diff)
    return zlib.compress(diff.encode('UTF-8'), 7)


def uncompressDiff(archive):
    """Zlib decompression (before use)"""
    return zlib.decompress(archive).decode('UTF-8')
