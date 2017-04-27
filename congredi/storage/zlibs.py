#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Compression/packetization functions

    splitting diffs / compressing for sending
"""
from __future__ import absolute_import
from __future__ import unicode_literals
import zlib
from six.moves import range
from ..utils.compat import ensureBinary


def chunkSplit(compressed):  # restore: ''.join()
    """Split chunks into the maximum size for AMP messages (if tripple encrypted) (Design - find that byte limit #F)"""
    compressed = ensureBinary(compressed)
    return [compressed[k:k + 250] for k in range(0, len(compressed), 250)]


def compressDiff(diff):
    """Zlib compression (before packet transmission/storage)"""
    diff = ensureBinary(diff)
    return zlib.compress(diff, 7)


def uncompressDiff(archive):
    """Zlib decompression (before use)"""
    return ensureBinary(zlib.decompress(archive))
