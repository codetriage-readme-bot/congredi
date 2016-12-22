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
	pc = ClientFactory()
	pc.protocol = Peer
	inst = PeerFactory()
	reactor.listenTCP(0, inst)
	#reactor.connectTCP('127.0.0.1', 38016,pc)
	print 'started'
	reactor.run()
