#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic protocol.
"""
from twisted.protocols.amp import AMP
from twisted.internet import reactor
#from twisted.protocols.basic import LineReceiver

import logging
from .utils.whoops import CongrediError, whoops
logger = logging.getLogger('congredi')

from .command import PeerOptions, PeerOnions

# pylint: disable=signature-differs
# https://github.com/twisted/twisted/blob/e38cc25a67747899c6984d6ebaa8d3d134799415/src/twisted/protocols/portforward.py
# class BogusProtocol(LineReceiver):  # protocol.Protocol):
# #protocol.ServerFactory


class CongrediPeerProtocol(AMP):

    def __init__(self, factory, users):  # **starts
        self.factory = factory
        self._peer = None
        self.users = users
        self.name = None
        self.state = "GETNAME"
        # self.users = starts  # self.prefix = prefix
        super(CongrediPeerProtocol, self).__init__()

    def incomingConnectionBegin(self, data):  # test
        super(CongrediPeerProtocol, self).incomingConnectionBegin(data)
        """De-lace router-encrypted trafic, tell if this connection is an onion, or a direct command"""
        # if data[0] == "Congredi Request forward to ":
        #    self.state = "ONION"

    def makeConnection(self, transport):  # test
        self.transport = transport
        super(CongrediPeerProtocol, self).makeConnection(transport)

    def connectionMade(self):  # ,client): # test
        self._peer = self.transport.getPeer()
        logger.info('new connection of {}'.format(self._peer))
        self.factory.clients.append(self)
        if self.name not in self.factory.activePeers:
            self.factory.activePeers.append(self._peer)
        self.factory.numProtocols = self.factory.numProtocols + 1
        super(CongrediPeerProtocol, self).connectionMade()

    def connectionLost(self, reason):  # ,client): # test
        self.factory.numProtocols = self.factory.numProtocols - 1
        if self._peer in self.factory.activePeers:
            self.factory.activePeers.remove(self._peer)
        logger.info('lost connection of {}'.format(self._peer))
        self.factory.clients.remove(self)
        super(CongrediPeerProtocol, self).connectionLost(reason)

    def dataReceived(self, data):  # test
        super(CongrediPeerProtocol, self).dataReceived(data)

    def lineReceived(self, line):  # test
        logger.info("line in: " + str(line))
        super(CongrediPeerProtocol, self).lineReceived(data)
        # factory = protocol.ClientFactory()
        # factory.protocol = SomeClientProtocol
        # reactor.connectTCP(host, port, factory)

    @PeerOnions.responder
    def hello(self, name, port):  # test
        logger.info('running an onion')
        for c in self.factory.clients:
            #port = reactor.connectTCP(name, port, factory)
            c.callRemote(PeerOptions, self.host, self.port)
            #port.disconnect()
        logger.info('disconnecting')
        return 'Sent a hello'

    @PeerOptions.responder
    def gotit(self, name, port):  # test
        logger.info('got it')
        clientNames = []
        for c in self.factory.clients:
            peer = c._peer
            clientNames += peer.host + ":" + str(peer.port)
        return(clientNames)
