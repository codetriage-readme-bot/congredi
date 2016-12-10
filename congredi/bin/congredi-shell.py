#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line interface for using Congredi.
"""
print('bin: congredi-shell begins')
from .main.options import getOpts
from .main.client import CongrediClient
def CongrediRunClient(host,port,clientKey=None):
	try:
		client = CongrediClient(host,port,clientKey)
		while True:
			cmd = raw_input("> ")
			client.cmd(cmd)
	except CongrediError as e:
		print("Congredi failed: {}".format(e.message))
def CongrediClientCommandLine():
	"""Grab arguments from command line, call Daemon"""
	CongrediRunClient(host,port,clientKey)
print('bin: congredi-shell ends')