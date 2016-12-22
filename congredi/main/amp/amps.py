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
	def hiya(self):
		print(self.transport)
		port = self.transport.getHost()
		print(port)
		#host = self.transport.getHost()
		#readers = reactor.getReaders()
		# 	print value._realPortNumber
		print('my port is {}'.format(port))
		d = connection.callRemote(PeerAsk, host=host, port=port)
		def prin(result):
			print(result)
		d.addCallback(prin)
		return d

def whoops(err):
	print('whoops')
	print(err)
class PeerFactory(protocol.Factory):
	clients = []
	def __init__(self):
		print('init')
		self.protocol = Peer(self)
		df = deferLater(reactor,10,self.hiya)
		#self.lc = task.LoopingCall(self.hiya)
		#df = self.lc.start(2)
		df.addErrback(whoops)
	def hiya(self):
		print('hiya')
		self.protocol.hiya()
	def clientConnectionMade(self,client):
		self.clients.append(client)
	def clientConnectionLost(self,client):
		self.clients.remove(client)
