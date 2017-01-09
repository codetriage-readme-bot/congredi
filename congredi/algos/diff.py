#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Diff utils (instead of using a raw git library - a design problem)
"""
# pylint: disable=unused-import
from difflib import unified_diff, ndiff, restore
from ..storage.zlibs import chunkSplit, compressDiff, uncompressDiff
#from patch import fromstring


# gosh I wish this would just work..
def resolveUnifiedDiff(md1, md2, l1, l2):
    """Resolving unified diff instead of using libgit (design/feature - make one of them work #G)"""
    # must use python-patch to use unified diffs...
    diff = unified_diff(md1.splitlines(
        1), md2.splitlines(1), l1, l2, lineterm='', n=0)
    result = '\n'.join(list(diff))
    return result


def resolveDiff(md1, md2):
    """Ndiffs (for right now unless resolveUnifiedDiff #G can be solved)"""
    diff = ndiff(md1.splitlines(1), md2.splitlines(1))  # , lineterm='', n=0)
    result = list(diff)
    #result = '\n'.join(list(diff))
    return result


def rebuildFile(diff, option):
    """Restore an Ndiff"""
    result = ''.join(restore(diff, option))
    return result


def tick(md1, md2):
    """Get a storeable object"""
    unified = resolveDiff(md1, md2)
    compressed = compressDiff(unified)
    return compressed


def tock(compressed, direction):
    """Decompress a stored object"""
    uncompressed = uncompressDiff(compressed)
    original = '\n'.join(list(restore(uncompressed, direction)))
    return original
