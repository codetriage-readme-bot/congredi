#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Diff utils (instead of using a raw git library - a design problem)
"""
import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from difflib import unified_diff, ndiff, restore
#from patch import fromstring
import zlib

def chunkSplit(compressed): #restore: ''.join()
	"""Split chunks into the maximum size for AMP messages (if tripple encrypted) (Design - find that byte limit #F)"""
	return [compressed[k:k+250] for k in xrange(0, len(compressed), 250)]

def resolveHtml(md):
	"""Return HTML (not for transfers between clients, only for resolving a webpage (Design - add markdown renderer to Delegito #G))"""
	return markdown.markdown(md, extensions=[GithubFlavoredMarkdownExtension()])

# gosh I wish this would just work..
def resolveUnifiedDiff(md1, md2, l1, l2):
	"""Resolving unified diff instead of using libgit (design/feature - make one of them work #G)"""
	# must use python-patch to use unified diffs...
	diff = unified_diff(md1.splitlines(1), md2.splitlines(1), l1, l2, lineterm='', n=0)
	result = '\n'.join(list(diff))
	print(result)
	return result

def resolveDiff(md1, md2):
	"""Ndiffs (for right now unless resolveUnifiedDiff #G can be solved)"""
	diff = ndiff(md1.splitlines(1), md2.splitlines(1))#, lineterm='', n=0)
	result = list(diff)
	#result = '\n'.join(list(diff))
	return result

def rebuildFile(diff, option):
	"""Restore an Ndiff"""
	result = ''.join(restore(diff, option))
	return result

def compressDiff(diff):
	"""Zlib compression (before packet transmission/storage)"""
	return zlib.compress(''.join(diff), 7)
def uncompressDiff(archive):
	"""Zlib decompression (before use)"""
	return zlib.decompress(archive).split('\n')

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

