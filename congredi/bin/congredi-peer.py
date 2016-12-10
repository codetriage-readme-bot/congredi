#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Command line interface for running a Congredi peer
"""
print('bin: congredi peer begins')
from .main.options import getOpts
from .main.peer import CongrediPeer
def CongrediRunDaemon(port,redis,neo4j,initialKey=None):
	try:
		app = CongrediPeer(port,redis,neo4j)
		twisted.Run(app)
	except CongrediError as e:
		print("Congredi failed: {}".format(e.message))
	finally:
		app.close_dbs()
def CongrediCommandLine():
	"""Grab arguments from command line, call Daemon"""
	CongrediRunDaemon(port,redis,neo4j,initialKey)
print('bin: congredi peer ends')