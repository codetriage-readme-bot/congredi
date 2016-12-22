#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
# https://github.com/twisted/twisted/blob/e38cc25a67747899c6984d6ebaa8d3d134799415/src/twisted/protocols/portforward.py
from twisted.internet import reactor, task
from twisted.internet.task import deferLater
from amps import *
from twisted.internet.protocol import Factory, ClientFactory

peers = ['127.0.0.1:1234','127.0.0.1:1000']

if __name__ == '__main__':
	def whoops():
		print('whoops')
		import traceback
		traceback.print_exc()
	def hiya(host,port):
		print('hiya')
		readers = reactor.getReaders()
		print('got')
		for reader in readers:
			print reader._realPortNumber
		print('set port')
		port = readers._realPortNumber
		print('my port is {}'.format(port))
		d = connection.callRemote(PeerAsk, host=host, port=port)
		def prin(result):
			print(result)
		d.addCallback(prin)
		return d
	defly = deferLater(reactor, 2, hiya, host='127.0.0.1',port=1234)
	defly.addErrback(whoops)
#    deferLater(reactor, 60, hiya).addCallback(lambda _: reactor.stop())
	pc = ClientFactory()
	pc.protocol = Peer
	pf = Factory()
	pf.protocol = Peer
	reactor.listenTCP(0, pf)
	reactor.connectTCP('127.0.0.1', 38016,pc)
	print 'started'
	reactor.run()

	#reactor.run()
