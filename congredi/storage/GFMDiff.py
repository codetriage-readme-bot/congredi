import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
from difflib import unified_diff, ndiff, restore
import sys
import zlib

def chunkSplit(compressed): #restore: ''.join()
	return [compressed[k:k+250] for k in xrange(0, len(compressed), 250)]

def resolveHtml(md):
	return markdown.markdown(md, extensions=[GithubFlavoredMarkdownExtension()])
# gosh I wish this would just work..
def resolveUnifiedDiff(contents, patch, direction):
	# must use python-patch to use unified diffs...
	pass
def resolveDiff(md1, md2):
	#diff = unified_diff
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

