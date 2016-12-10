#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
command line options
"""


from twisted.python import usage

class UsualOptions(usage.Options):
	optFlags = [["quiet","q", None]]
class WalkerOptions(usage.Options):
	optParameters = [['module','m',None,None]]
class Options(UsualOptions):
	optFlags = [
		["port","p","protocol port"],
		["control","c","control port"]
		]
	optParameters = [
		["debug","d", False, "Debug to console"],#, int
		]
	optSubcommands = [
		["walk",None,WalkerOptions,"Run Walk"]
		]
	def postOptions(self):
		if not self['port'] and not self['flag']:
			raise usage.UsageError("Lazy")

def getOpts():
	options = Options()
	try:
		options.parseOptions(sys.argv)
	except usage.UsageError, errortext:
		print '%s: %s' % (sys.argv[0], errortext)
		sys.exit(1)
	if config.subCommand =='walk':
		doWalk(config.subOptions)
	if options['port']: app.port = options['port']
	app.debug = options['debug']
