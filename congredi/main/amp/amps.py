#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""

from twisted.protocols import amp
from twisted.internet import protocol

class PeerAsk(amp.Command):
	arguments = [('name', amp.String()),
				 ('port', amp.Integer())]
	response = [('hello',amp.String())]
class PeerTell(amp.Command):
	arguments = [('name', amp.String()),
				 ('port', amp.Integer())]
	response = [('hello',amp.String())]
	
class Peer(amp.AMP):
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
