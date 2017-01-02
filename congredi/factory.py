#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic factory.
"""

from twisted.internet import protocol, reactor, task
from .protocol import CongrediPeerProtocol
from .peerBeat import peerBeat, peerSuccess, peerFailure
from .utils.whoops import whoops
from .command import PeerAsk, PeerTell


class CongrediPeerFactory(protocol.Factory):
    clients = []
    # protocol = CongrediPeer
    online = False
    users = {}
    peers = {}
    # def f(s):
    # print(s)
    #reactor.callLater(3.4, f, "hello, world")
    #d = task.deferLater(reactor, 3.4, f, "hi")
    # def called(result): print result
    # d.addCallback(called)
    # a really basic example from stackoverflow...

    def __init__(self, port=4400, redisPort=6379, neo4jPort=7474, initialKey=None):
        #self.protocol = Peer(self)
        print('init a factory')
        """Add loops to factory? why not add loops to main reactor??"""
        defly = task.deferLater(reactor, 10, self.ping)
        defly.addErrback(whoops)
        #reactor.callLater(2, redis_test)
        #task.deferLater(reactor, 60, hiya).addCallback(lambda _: reactor.stop())
        loop = task.LoopingCall(peerBeat)
        loopDeferred = loop.start(10.0)
        loopDeferred.addCallback(peerSuccess)
        loopDeferred.addErrback(peerFailure)
        self.users = {}  # maps user names to Chat instances
        self.redisPort = redisPort
        self.neo4jPort = neo4jPort
        if initialKey:
            self.commandKeys.add(initialKey)
            self.redis.addToKeys(initialKey)
        print('finish init factory')

    def startedConnecting(self, connector):
        print('Started to connect.')

    def clientConnectionLost(self, connector, reason):
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason):
        print('Connection failed. Reason:', reason)

    def startFactory(self):
        print('start factory')
        self.online = True

    def stopFactory(self):
        print('stop factory')
        self.online = False
    commandKeys = []
    state = "BEGIN"

    def buildProtocol(self, addr):
        print('building protocol from factory')
        proto = CongrediPeerProtocol(self, self.users)  # , self.peers)
        return proto

    def ping(self):
        print('pinging')
        print(self.clients)
        for client in self.clients:
            print('client')
            d = client.callRemote(PeerAsk, name=self.host, port=self.port)
            d.addErrback(whoops)
