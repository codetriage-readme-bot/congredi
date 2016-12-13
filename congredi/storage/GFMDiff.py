import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from difflib import unified_diff, ndiff, restore
from patch import fromstring
import sys
import zlib

def chunkSplit(compressed): #restore: ''.join()
	return [compressed[k:k+250] for k in xrange(0, len(compressed), 250)]

def resolveHtml(md):
	return markdown.markdown(md, extensions=[GithubFlavoredMarkdownExtension()])
# gosh I wish this would just work..
def resolveUnifiedDiff(md1, md2, l1, l2):
	# must use python-patch to use unified diffs...
	diff = unified_diff(md1.splitlines(1), md2.splitlines(1), l1, l2, lineterm='', n=0)
	result = '\n'.join(list(diff))
	print(result)
	return result
def resolveDiff(md1, md2):
	diff = ndiff(md1.splitlines(1), md2.splitlines(1))#, lineterm='', n=0)
	result = list(diff)
	#result = '\n'.join(list(diff))
	return result

def rebuildFile(diff, option):
	result = ''.join(restore(diff, option))
	return result

def compressDiff(diff):
	return zlib.compress(''.join(diff), 7)
def uncompressDiff(archive):
	return zlib.decompress(archive).split('\n')

def tick(md1, md2):
	unified = resolveDiff(md1, md2)
	compressed = compressDiff(unified)
	return compressed
def tock(compressed, direction):
	uncompressed = uncompressDiff(compressed)
	original = '\n'.join(list(restore(uncompressed, direction)))
	return original

