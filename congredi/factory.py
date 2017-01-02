#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic factory.
"""

import socket
from twisted.internet import protocol, reactor, task
from .protocol import CongrediPeerProtocol
from .peerBeat import peerBeat, peerSuccess, peerFailure
from .utils.whoops import whoops
from .command import PeerAsk, PeerTell

defaultHost = socket.gethostname()


class CongrediPeerFactory(protocol.Factory):
    clients = []
    # protocol = CongrediPeer
    online = False
    users = {}
    peers = {}
    numProtocols = 0
    # def f(s):
    # print(s)
    #reactor.callLater(3.4, f, "hello, world")
    #d = task.deferLater(reactor, 3.4, f, "hi")
    # def called(result): print result
    # d.addCallback(called)
    # a really basic example from stackoverflow...

    def __init__(self, host=defaultHost, port=4400, redisPort=6379, neo4jPort=7474, initialKey=None):
        #self.protocol = Peer(self)
        self.host = host
        self.port = port
        self.users = {}  # maps user names to Chat instances
        self.redisPort = redisPort
        self.neo4jPort = neo4jPort
        if initialKey:
            self.commandKeys.add(initialKey)
            self.redis.addToKeys(initialKey)
        """Add loops to factory? why not add loops to main reactor??"""
        defly = task.deferLater(reactor, 10, self.ping)
        defly.addErrback(whoops)
        #reactor.callLater(2, redis_test)
        #task.deferLater(reactor, 60, hiya).addCallback(lambda _: reactor.stop())
        loop = task.LoopingCall(peerBeat)
        loopDeferred = loop.start(10.0)
        loopDeferred.addCallback(peerSuccess)
        loopDeferred.addErrback(peerFailure)

    def startedConnecting(self, connector):
        print('Factory - Connecting')

    def clientConnectionLost(self, connector, reason):
        print('Factory - Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Factory - Connection failed. Reason:', reason)

    def startFactory(self):
        self.online = True

    def stopFactory(self):
        self.online = False
    commandKeys = []
    state = "BEGIN"

    def buildProtocol(self, addr):
        proto = CongrediPeerProtocol(self, self.users)  # , self.peers)
        return proto

    def ping(self):
        print('pinging')
        for client in self.clients:
            print('client: {}'.format(client))
            d = client.callRemote(PeerAsk, name=self.host, port=self.port)
            d.addErrback(whoops)
