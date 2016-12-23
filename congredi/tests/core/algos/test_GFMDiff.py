#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
tests on the simplistic censor library.
"""
import hashlib#, pudb
from StringIO import StringIO
from patch import PatchSet
# pylint: disable=unused-import
from ....core.algos.GFMDiff import resolveHtml
from ....core.algos.GFMDiff import resolveUnifiedDiff
from ....core.algos.GFMDiff import resolveDiff
from ....core.algos.GFMDiff import rebuildFile
from ....core.algos.GFMDiff import compressDiff
from ....core.algos.GFMDiff import uncompressDiff
from ....core.algos.GFMDiff import tick
from ....core.algos.GFMDiff import tock
from ....core.algos.GFMDiff import chunkSplit




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
empty = ""
empty2 = """


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu viverra lacus. Vestibulum a est a felis posuere pellentesque ac sit amet sem. Aliquam erat volutpat. Phasellus eleifend, felis eget lobortis dapibus, ligula purus rhoncus massa, placerat pharetra urna lacus vel ex. Proin finibus pellentesque dui id mollis. Vestibulum id nibh libero. Quisque at odio velit. Morbi ac viverra velit, ut elementum erat. Cras varius, odio sit amet rutrum porta, purus mi sollicitudin sem, vel rutrum nisl augue non arcu. Fusce sagittis sem commodo lorem malesuada, eu vestibulum lacus laoreet. Proin nibh dolor, blandit sed dictum in, imperdiet nec risus. Quisque sem est, ultrices consequat urna id, malesuada vestibulum lacus. Nullam congue lectus sed mollis sagittis. Vestibulum pellentesque vulputate lacus sed consectetur.

Etiam gravida justo vel venenatis convallis. Vestibulum a nunc at justo vestibulum mattis quis eget erat. Sed semper hendrerit orci. In in sapien vitae purus sodales gravida vel et nunc. Fusce porttitor, ante molestie blandit laoreet, massa libero commodo ex, at suscipit lacus dolor a elit. Aenean ut erat non sapien blandit ullamcorper eget sit amet velit. Nullam mattis nulla a urna maximus pellentesque vel in enim. Nullam lorem dui, ullamcorper id velit et, consequat porta justo. Duis lacus ipsum, finibus eget est ut, accumsan interdum augue. Maecenas convallis sed enim non rhoncus. Vestibulum at commodo nisl, id ultricies ex. Morbi nunc est, semper et efficitur ac, porta ut leo. Donec eu facilisis justo.

Maecenas congue suscipit lacus vitae rhoncus. Donec dictum lacinia elementum. Proin fringilla ante elit. Maecenas lacus arcu, eleifend non consectetur non, aliquet tincidunt lectus. Duis a fringilla massa, sed varius neque. Phasellus placerat non risus a finibus. Curabitur ut eros mattis, ornare purus ac, volutpat ante. Mauris at auctor ligula, et lacinia metus. Ut vitae neque mattis, placerat sem et, blandit neque. Donec rutrum, neque non feugiat laoreet, enim nibh pharetra purus, eu tincidunt nisi metus id lacus. Vestibulum efficitur venenatis velit, quis sodales orci laoreet et. Nunc vestibulum non tortor eget tempor. Duis congue nunc eu gravida consectetur. Vivamus sagittis ante nec erat accumsan, nec interdum risus varius. Nullam ac turpis blandit, viverra augue ultrices, pellentesque mauris. Nulla eu faucibus ante.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus molestie nibh vel felis consequat, ut consectetur arcu porta. Duis in tortor ultrices mi malesuada mattis at quis turpis. Morbi enim nunc, accumsan id leo eget, egestas blandit dolor. Aenean id sapien quis quam sollicitudin laoreet in in lacus. Suspendisse potenti. Donec ut erat malesuada, tempus nunc ac, sodales ante. Phasellus ac felis ultricies, ullamcorper ipsum sed, vehicula urna. Nullam ac lacus euismod, fermentum justo a, ornare massa. Vestibulum sed mollis nulla. Nulla turpis tellus, porttitor a sodales ac, lacinia sodales ex. Donec scelerisque magna vel nisi cursus malesuada. Aenean vehicula dictum enim, eu semper nisi dictum nec. Nunc in leo varius, sagittis odio in, rhoncus purus.

Nulla facilisi. Vestibulum aliquet est a ex lobortis vulputate. Curabitur at ultrices orci. Vestibulum varius nulla eu aliquet finibus. Donec id posuere est. Donec sit amet lacus vitae nulla dapibus imperdiet sed id ante. Nullam vitae lorem tristique, lobortis justo sit amet, porta erat. Donec quam lorem, ullamcorper sit amet tortor hendrerit, tempor dapibus magna. Cras viverra consectetur odio, quis iaculis lacus ornare vel. Pellentesque id lorem eu sapien vehicula molestie in vitae purus. Sed ac sapien non purus dapibus lacinia. Integer vel nunc vel tortor tempor accumsan. Integer tempor sit amet dolor in posuere. Etiam maximus odio quis felis blandit scelerisque. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
"""

def test_html():
	html = resolveHtml(source)
	print(html)
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
	diff = resolveUnifiedDiff(source, source2, 'a.txt', 'b.txt')
	patch = PatchSet(StringIO(diff))
	print(patch.errors)
	patch.revert(0, root='.')
	patch.apply(0, root=".")
