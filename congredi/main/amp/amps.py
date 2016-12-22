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
	def hello(self, name,port):
		print('telling hello')
		factory = protocol.ClientFactory()
		factory.protocol = Peer
		print('connecting')
		port = reactor.connectTCP(name,port, factory)
		print('calling')
		port.callRemote(PeerTell,name,port)
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
	def __init__(self):
		print('init')
		self.protocol = Peer(self)
		defly = deferLater(reactor, 2, self.ping)
		defly.addErrback(whoops)
	def clientConnectionMade(self,client):
		self.clients.append(client)
	def clientConnectionLost(self,client):
		self.clients.remove(client)
	def ping(self):
		# need to run this every so often...
		d = connection.callRemote(PeerAsk, host=self.host, port=self.port)

