#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main client class
"""
import logging, os
logger = logging.getLogger('congredi')
from ..crypto.asym import asym
from ..crypto.padding import AONTdecrypt, AONTencrypt
from ..storage.redis import redis_test
from twisted.protocols.basic import LineReceiver
class CongrediClient(LineReceiver):
	from os import linesep as delimiter

	def connectionMade(self):
		self.transport.write('>>> ')

	def lineReceived(self, line):
		if line == 'test': redis_test()
		self.sendLine('Echo: ' + line)
		self.transport.write('>>> ')

	host = None; port = None; key = None
	def __init__(self, host="localhost", port=4400,
				 clientKey=None, clientPass=None):
		self.host = host; self.port = port;
		if clientKey: self.key = clientKey
		else: self.key = asym()
		if clientPass: self.password = clientPass
		else: self.password = os.urandom(16)
		logger.debug('built client')

	def wrapRequest(self, request, serverKey):
		paddedRequest = AONTencrypt(request, self.password)
		encryptedRequest = self.key.encrypt(paddedRequest, serverKey)
		return encryptedRequest
	def unwrapRequest(self, encryptedRequest):
		decryptedPadding = self.key.decrypt(encryptedRequest, self.key)
		request = AONTdecrypt(decryptedPadding)
		return request
