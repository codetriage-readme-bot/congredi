#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main peer class
"""
import logging
from twisted.internet import defer #, utils
#from twisted.web import client
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
logger = logging.getLogger('delegito')
class CongrediPeer(Factory):
	# init
	online = False
	def __init__(self, port=4400, redisPort=6379, neo4jPort=7474, initialKey=None):
		self.users = {} # maps user names to Chat instances
		self.redisPort = redisPort
		self.neo4jPort = neo4jPort
		if initialKey:
			self.commandKeys.add(initialKey)
			self.redis.addToKeys(initialKey)
	def buildProtocol(self, addr):
		return BogusProtocol(self.users)
	def startFactory(self):
		self.online = True
	def stopFactory(self):
		self.online = False
	commandKeys = []
	state = "BEGIN"
# pylint: disable=signature-differs
class BogusProtocol(LineReceiver):#protocol.Protocol): #protocol.ServerFactory
	def __init__(self, factory, users, **starts):
		self.users = users
		self.name = None
		self.state = "GETNAME"
		self.users = starts #self.prefix = prefix
		self.factory = factory
	def connectionMade(self):
		self.sendLine("What's your name?")
		self.transport.loseConnection()
		self.factory.numProtocols = self.factory.numProtocols + 1
		self.transport.write("Now {}".format(self.factory.numProtocols))
	def connectionLost(self, reason):
		self.factory.numProtocols = self.factory.numProtocols - 1
		if self.name in self.users:
			del self.users[self.name]
	def lineReceived(self, line):
		if self.state == "GETNAME":
			self.handle_GETNAME(line)
		else:
			self.handle_CHAT(line)
		d = self.factory.getUser(line)
		def onError(err):
			return 'errors'
		d.addErrback(onError)
		def writeResponse(message):
			self.transport.write(message+"\n")
			self.transport.loseConnection()
		d.addCallback(writeResponse)
	def handle_GETNAME(self, name):
		if name in self.users:
			self.sendLine("Name taken, please choose another.")
			return
		self.sendLine("Welcome, %s!" % (name, ))
		self.name = name
		self.users[name] = self
		self.state = "CHAT"
	def handle_CHAT(self, message):
		message = "<%s> %s" % (self.name, message)
		# for name, protocol in self.users.iteritems():
		# 	if protocol != self:
		# 		protocol.sendLine(message)
	def getUser(self, user):
		#utils.getProcessOutput
		return defer.succeed(self.users.get(user, "Nope"))
		#return client.getPage(self.prefix+user)
	def dataReceived(self, data):
		self.transport.write(data)
	def incomingConnectionBegin(self, data):
		"""De-lace router-encrypted trafic, tell if this connection is an onion, or a direct command"""
		if data[0] == "Congredi Request forward to ":
			self.state = "ONION"
	def incomingOnionSendoff(self, data):
		"""Send data to next onion"""

#def f(s):
# print(s)
#reactor.callLater(3.4, f, "hello, world")
#d = task.deferLater(reactor, 3.4, f, "hi")
#def called(result): print result
# d.addCallback(called)
