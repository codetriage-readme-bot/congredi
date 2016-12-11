#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main peer class
"""
import logging
logger = logging.getLogger('delegito')
from ..algos.censor import censor
class CongrediPeer():
	commandKeys = []
	state = "BEGIN"
	def __init__(self, port=4400, redisPort=6379, neo4jPort=7474, initialKey=None):
		self.redisPort = redisPort
		self.neo4jPort = neo4jPort
		if initialKey:
			self.commandKeys.add(initialKey)
			self.redis.addToKeys(initialKey)
	def incomingConnectionBegin(self, data):
		"""De-lace router-encrypted trafic, tell if this connection is an onion, or a direct command"""
		if data[0] == "Congredi Request forward to ":
			self.state = "ONION"
	def incomingOnionSendoff(self, data):
		"""Send data to next onion"""
