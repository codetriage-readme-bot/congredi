#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
from ...storage.GFMDiff import resolveHtml
from ...storage.GFMDiff import resolveUnifiedDiff
from ...storage.GFMDiff import resolveDiff
from ...storage.GFMDiff import rebuildFile
from ...storage.GFMDiff import compressDiff
from ...storage.GFMDiff import uncompressDiff
from ...storage.GFMDiff import tick
from ...storage.GFMDiff import tock




source = """
Hello, *world*! This is a ~~good~~marvelous day!
Here is an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk

You can also have fenced code blocks:

```
import this
```
"""

source2 = """
Hello, *world*! This is a ~~good~~marvelous day!
Here was an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk
- [x] ten


```
import this
```
"""
def test_html():
	html = resolveHtml(source)
	print(html)
def test_resolve_ndiff():
	print('The Diff:')
	result = resolveDiff(source,source2)
	print(''.join(result))
	print('The Original:')
	orig = rebuildFile(result,1)
	print(''.join(orig))
def test_compression():
	# Direct conversion
	res = tick(source,source2)
	beep = tock(res,1)
	print('Compression test:')
	print(beep)