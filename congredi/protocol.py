#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic protocol.
"""
# from builtins import str
from __future__ import unicode_literals
from __future__ import absolute_import
from twisted.protocols.amp import AMP
#from twisted.internet import reactor

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
    host = None

    def __init__(self, factory, users):  # **starts
        self.factory = factory
        self._peer = None
        self.users = users
        self.name = None
        self.state = "GETNAME"
        # self.users = starts  # self.prefix = prefix
        super(CongrediPeerProtocol, self).__init__()

    # # def incomingConnectionBegin(self, data):  # test
    # #     super(CongrediPeerProtocol, self).incomingConnectionBegin(data)
    # #     """De-lace router-encrypted trafic, tell if this connection is an onion, or a direct command"""
    # #     # if data[0] == "Congredi Request forward to ":
    # #     #    self.state = "ONION"
    #
    # def makeConnection(self, transport):  # test
    #     self.transport = transport
    #     super(CongrediPeerProtocol, self).makeConnection(transport)
    #
    def connectionMade(self):  # ,client): # test
        self._peer = self.transport.getPeer()
        logger.info('new connection of %s', self._peer)
        self.factory.clients.append(self)
        if self.name not in self.factory.activePeers:
            self.factory.activePeers.append(self._peer)

        self.factory.numProtocols = self.factory.numProtocols + 1
        print('Factory has {} conns'.format(self.factory.numProtocols))
        super(CongrediPeerProtocol, self).connectionMade()
    #
    # def connectionLost(self, reason):  # ,client): # test
    #     self.factory.numProtocols = self.factory.numProtocols - 1
    #     if self._peer in self.factory.activePeers:
    #         self.factory.activePeers.remove(self._peer)
    #     logger.info('lost connection of %s', self._peer)
    #     self.factory.clients.remove(self)
    #     super(CongrediPeerProtocol, self).connectionLost(reason)
    # # pylint: disable=useless-super-delegation
    #
    # def dataReceived(self, data):  # test
    #     try:
    #         print('{}'.format(data))
    #     except: pass
    #     super(CongrediPeerProtocol, self).dataReceived(data)
    #
    # def lineReceived(self, line):  # test
    #     logger.info("line in: " + str(line))
    #     super(CongrediPeerProtocol, self).lineReceived(line)
    #     # factory = protocol.ClientFactory()
    #     # factory.protocol = SomeClientProtocol
    #     # reactor.connectTCP(host, port, factory)

    @SyncPeerDirectoryAsk.responder
    def hello(self, name, port):  # test
        """
            Respond with directory ASKs, though this function
            is using a simple "hello I'm host:port". Recusion
            through factory clients
        """
        logger.info('running an onion')
        # this differs from tests
        print('ONIONYALL')
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
# congredi/protocol.py                        61     22    64%   83-84,
# 102-107, 110, 113-114, 121-127, 131-136
