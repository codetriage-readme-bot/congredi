#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
# https://github.com/twisted/twisted/blob/e38cc25a67747899c6984d6ebaa8d3d134799415/src/twisted/protocols/portforward.py
from twisted.internet import reactor
from amps import *
from twisted.internet.protocol import Factory, ClientFactory

peers = ['127.0.0.1:1234','127.0.0.1:1000']

if __name__ == '__main__':
#    deferLater(reactor, 60, hiya).addCallback(lambda _: reactor.stop())
	pc = PeerClientFactory()
	inst = PeerFactory()
	with open('ort','r') as a:
		prt = a.read().strip('\n')
	reactor.connectTCP('127.0.0.1', prt,pc)
	pr = reactor.listenTCP(0, inst)
	inst.host = pr.getHost().host
	inst.port = pr.getHost().port
	print 'started on port {}'.format(inst.port)
	with open('ort','w+') as a:
		a.write(str(inst.port))
	reactor.run()
