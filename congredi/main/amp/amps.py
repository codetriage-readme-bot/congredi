#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
from twisted.protocols import amp
from twisted.internet import protocol, task, reactor
from twisted.internet.task import deferLater

class PeerAsk(amp.Command):
	arguments = [('name', amp.String()),
				 ('port', amp.Integer())]
	response = [('hello',amp.String())]
class PeerTell(amp.Command):
	arguments = [('name', amp.String()),
				 ('port', amp.Integer())]
	response = [('hello',amp.String())]
	
class Peer(amp.AMP):
	def __init__(self,factory):
		self.factory = factory
	def connectionMade(self):#,client):
		self._peer = self.transport.getPeer()
		print('new connection of {}'.format(self._peer))
		self.factory.clients.append(self)
	def connectionLost(self,reason):#,client):
		print('lost connection of {}'.format(self._peer))
		self.factory.clients.remove(self)
	def hello(self, name,port):
		print('telling hello')
		factory = PeerClientFactory()
		print('connecting')
		# connect to an arbitrary new host...
		port = reactor.connectTCP(name,port, factory)
		print('calling')
		# need to run an arbitrary new command....
		port.callRemote(PeerTell,name,port)
		# halp...
		print('disconnecting')
		port.disconnect()
		print('done')
		return 'Sent a hello'
	PeerAsk.responder(hello)
	def gotit(self,name,port):
		print('got it')
		return('hello')
	PeerTell.responder(gotit)

def whoops(err):
	print('whoops')
	print(err)
class PeerFactory(protocol.Factory):
	clients = []
	protocol = Peer
	def __init__(self):
		#self.protocol = Peer(self)
		defly = deferLater(reactor, 10, self.ping)
		defly.addErrback(whoops)
	def buildProtocol(self,addr):
		return Peer(self)
	def ping(self):
		print('pinging')
		print(self.clients)
		for client in self.clients:
			print('client')
			d = client.callRemote(PeerAsk, name=self.host, port=self.port)
			d.addErrback(whoops)

class PeerClientFactory(protocol.ClientFactory):
	def __init__(self):
		print('hello')
		self.clients = []
	def buildProtocol(self,addr):
		return Peer(self)
	def startedConnecting(self, connector):
		print('Started to connect.')

	def clientConnectionLost(self, connector, reason):
		print('Lost connection.  Reason:', reason)

	def clientConnectionFailed(self, connector, reason):
		print('Connection failed. Reason:', reason)