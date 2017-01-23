#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic protocol.
"""
# pylint: disable=unused-import
# from builtins import str
from __future__ import unicode_literals
from __future__ import absolute_import
from twisted.protocols.amp import AMP
from twisted.internet import reactor
#from twisted.protocols.basic import LineReceiver

import logging
logger = logging.getLogger('congredi')

from .commands.addresses import AddressAsk, SyncPeerDirectoryAsk, addressesResponders
from .commands.filesystem import filesystemResponders
from .commands.passport import passportResponders
from .commands.setting import settingResponders
from .commands.proofs.org import orgResponders
from .commands.proofs.router import routerResponders
from .commands.proofs.user import userResponders

# pylint: disable=signature-differs, abstract-method, too-many-ancestors
# https://github.com/twisted/twisted/blob/e38cc25a67747899c6984d6ebaa8d3d134799415/src/twisted/protocols/portforward.py
# class BogusProtocol(LineReceiver):  # protocol.Protocol):
# #protocol.ServerFactory


class CongrediPeerProtocol(AMP, addressesResponders, filesystemResponders,
                           passportResponders, settingResponders, orgResponders,
                           routerResponders, userResponders):
    """
    def __init__(self, factory):
        self.factory = factory

    def hello(self, name, port):
        print('telling hello')
        factory = protocol.ClientFactory()
        factory.protocol = Peer
        print('connecting')
        port = reactor.connectTCP(name, port, factory)
        print('calling')
        port.callRemote(PeerTell, name, port)
        print('disconnecting')
        port.disconnect()
        print('done')
        return 'Sent a hello'
    PeerAsk.responder(hello)

    def gotit(self, name, port):
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
        print('my port is %n' % port)
        d = connection.callRemote(PeerAsk, host=host, port=port)

        def prin(result):
            print(result)
        d.addCallback(prin)
        return d
    """

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
        logger.info('new connection of %s', self._peer)
        self.factory.clients.append(self)
        if self.name not in self.factory.activePeers:
            self.factory.activePeers.append(self._peer)
        self.factory.numProtocols = self.factory.numProtocols + 1
        super(CongrediPeerProtocol, self).connectionMade()

    def connectionLost(self, reason):  # ,client): # test
        self.factory.numProtocols = self.factory.numProtocols - 1
        if self._peer in self.factory.activePeers:
            self.factory.activePeers.remove(self._peer)
        logger.info('lost connection of %s', self._peer)
        self.factory.clients.remove(self)
        super(CongrediPeerProtocol, self).connectionLost(reason)

    def dataReceived(self, data):  # test
        super(CongrediPeerProtocol, self).dataReceived(data)

    def lineReceived(self, line):  # test
        logger.info("line in: " + str(line))
        super(CongrediPeerProtocol, self).lineReceived(line)
        # factory = protocol.ClientFactory()
        # factory.protocol = SomeClientProtocol
        # reactor.connectTCP(host, port, factory)

    @SyncPeerDirectoryAsk.responder
    def hello(self, name, port):  # test
        logger.info('running an onion')
        for c in self.factory.clients:
            #port = reactor.connectTCP(name, port, factory)
            c.callRemote(SyncPeerDirectoryAsk, self.host, self.port)
            # port.disconnect()
        logger.info('disconnecting')
        return 'Sent a hello'

    @AddressAsk.responder
    def gotit(self, name, port):  # test
        logger.info('got it')
        clientNames = []
        for c in self.factory.clients:
            peer = c._peer
            clientNames += peer.host + ":" + str(peer.port)
        return(clientNames)
