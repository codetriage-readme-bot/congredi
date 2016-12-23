#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PGP key & IP routing
"""
import logging, random
logger = logging.getLogger('congredi')

class router():
	nodes = []
	def __init__(self, routerKey):
		self.key = routerKey

	# routes will have a key and an IP
	def route(self, rendesvousKey, hops=3):
		"""generate a route to an introduction node using a list of keys (see alternate in packet/hybrid.py)"""
		# self, node, returnaddr, rendesvous
		tempNodes = list(self.nodes)
		result = []
		def add(choice):
			result.append(choice)
			tempNodes.remove(choice)
		tempNodes.remove(self.key)
		add(rendesvousKey)
		while len(result) < hops:
			choice = random.choice(tempNodes)
			add(choice)
		return result
