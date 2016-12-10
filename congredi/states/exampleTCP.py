#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

class Chat(LineReceiver):

	def __init__(self, users):
		self.users = users
		self.name = None
		self.state = "GETNAME"

	def connectionMade(self):
		self.sendLine("What's your name?")

	def connectionLost(self, reason):
		if self.name in self.users:
			del self.users[self.name]

	def lineReceived(self, line):
		if self.state == "GETNAME":
			self.handle_GETNAME(line)
		else:
			self.handle_CHAT(line)

	def handle_GETNAME(self, name):
		if name in self.users:
			self.sendLine("Name taken, please choose another.")
			return
		self.sendLine("Welcome, %s!" % (name,))
		self.name = name
		self.users[name] = self
		self.state = "CHAT"

	def handle_CHAT(self, message):
		message = "<%s> %s" % (self.name, message)
		for name, protocol in self.users.iteritems():
			if protocol != self:
				protocol.sendLine(message)


class ChatFactory(Factory):

	def __init__(self):
		self.users = {} # maps user names to Chat instances

	def buildProtocol(self, addr):
		return Chat(self.users)


reactor.listenTCP(8123, ChatFactory())
reactor.run()

from twisted.internet.protocol import Protocol, Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Onion(Protocol):
	# def __init__(self, factory):
	#	 self.factory = factory
	def connectionMade(self):
		self.factory.numProtocols = self.factory.numProtocols + 1
		self.transport.write("Now {}".format(self.factory.numProtocols))
	def connectionLost(self, reason):
		self.factory.numProtocols = self.factory.numProtocols - 1
	def dataReceived(Self, data):
		self.transport.write(data)
class OnionFactory(Factory):
	# init
	def buildProtocol(self, addr):
		return Onion()
	def startFactory(self):
		self.online = True
	def stopFactory(self):
		self.online = False
endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(OnionFactory)
reactor.run()
