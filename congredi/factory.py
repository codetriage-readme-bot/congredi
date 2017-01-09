#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic factory.
"""

import socket
from twisted.internet import protocol, reactor, task
from .protocol import CongrediPeerProtocol
from .peerBeat import peerBeat, peerSuccess, peerFailure
from .command import PeerOptions
import logging
from .utils.whoops import whoops
logger = logging.getLogger('congredi')


defaultHost = socket.gethostname()

# pylint: disable=no-self-use
class CongrediPeerFactory(protocol.Factory):
    """
    clients = []

    def __init__(self):
        print('init')
        self.protocol = Peer(self)
        df = deferLater(reactor, 10, self.hiya)
        #self.lc = task.LoopingCall(self.hiya)
        #df = self.lc.start(2)
        df.addErrback(whoops)

    def hiya(self):
        print('hiya')
        self.protocol.hiya()

    def clientConnectionMade(self, client):
        self.clients.append(client)

    def clientConnectionLost(self, client):
        self.clients.remove(client)
    """
    online = False
    clients = []
    activePeers = []
    numProtocols = 0

    def __init__(self, host=defaultHost, port=4400, redisPort=6379, neo4jPort=7474, initialKey=None):
        #self.protocol = Peer(self)
        self.host = host
        self.port = port
        self.users = {}  # maps user names to Chat instances
        self.redisPort = redisPort
        self.neo4jPort = neo4jPort
        if initialKey:  # need test case
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

    def startedConnecting(self, connector):  # test
        logger.info('Factory - Connecting')

    def clientConnectionLost(self, connector, reason):  # test
        logger.warning(
            'Factory - Lost connection.  Reason:%s', reason.getErrorMessage())

    def clientConnectionFailed(self, connector, reason):  # test
        logger.critical(
            'Factory - Connection failed. Reason:%s', reason.getErrorMessage())

    def startFactory(self):  # test
        self.online = True

    def stopFactory(self):  # test
        self.online = False
    commandKeys = []
    state = "BEGIN"

    def buildProtocol(self, addr):  # test
        proto = CongrediPeerProtocol(self, self.users)  # , self.peers)
        return proto

    def ping(self):  # test
        logger.info('pinging routine started.')
        for client in self.clients:
            info = client._peer
            logger.info('pinging peer at: %(host)s:%(port)d',
                        (info.host, info.port))
            d = client.callRemote(
                PeerOptions, name=self.host, port=int(self.port))
            d.addCallback(gotit)
            d.addErrback(whoops)


def gotit(result):
    logger.critical(result)
