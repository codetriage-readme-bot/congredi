#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Basic protocol.
"""
from twisted.protocols.amp import AMP
from twisted.internet import reactor
#from twisted.protocols.basic import LineReceiver

from .command import PeerAsk, PeerTell

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
        print('new connection of {}'.format(self._peer))
        self.factory.clients.append(self)
        #self.sendLine("What's your name?")
        # self.transport.loseConnection()
        # self.transport.write(data)
        self.factory.numProtocols = self.factory.numProtocols + 1
        super(CongrediPeerProtocol, self).connectionMade()

    def connectionLost(self, reason):  # ,client): # test
        self.factory.numProtocols = self.factory.numProtocols - 1
        if self.name in self.users:
            del self.users[self.name]
        print('lost connection of {}'.format(self._peer))
        self.factory.clients.remove(self)
        super(CongrediPeerProtocol, self).connectionLost(reason)

    def dataReceived(self, data):  # test
        print(str(data))
        super(CongrediPeerProtocol, self).dataReceived(data)

    def lineReceived(self, line):  # test
        print(str(line))
        super(CongrediPeerProtocol, self).lineReceived(data)
        # if self.state == "GETNAME":
        #     self.handle_GETNAME(line)
        # else:
        #     self.handle_CHAT(line)
        # d = self.factory.getUser(line)

        # def onError(err):
        #     return 'errors'
        # d.addErrback(onError)
        # def writeResponse(message):
        #     self.transport.write(message + "\n")
        #     self.transport.loseConnection()
        # d.addCallback(writeResponse)
        # host, port = line.split()
        # port = int(port)
        # factory = protocol.ClientFactory()
        # factory.protocol = SomeClientProtocol
        # reactor.connectTCP(host, port, factory)
    def handle_GETNAME(self, name):  # test
        if name in self.users:
            self.sendLine("Name taken, please choose another.")
            return
        self.sendLine("Welcome, %s!" % (name, ))
        self.name = name
        self.users[name] = self
        self.state = "CHAT"

    def handle_CHAT(self, message):  # test
        message = "<%s> %s" % (self.name, message)
        # for name, protocol in self.users.iteritems():
        # 	if protocol != self:
        # 		protocol.sendLine(message)
        # utils.getProcessOutput
        # return task.defer.succeed(self.users.get(user, "Nope"))
        # return client.getPage(self.prefix+user)

    def incomingOnionSendoff(self, data):  # test
        pass
        """Send data to next onion"""

    @PeerAsk.responder
    def hello(self, name, port):  # test
        print('telling hello')
        factory = Peer()
        print('connecting')
        # connect to an arbitrary new host...
        port = reactor.connectTCP(name, port, factory)
        print('calling')
        # need to run an arbitrary new command....
        port.callRemote(PeerTell, name, port)
        # halp...
        print('disconnecting')
        port.disconnect()
        print('done')
        return 'Sent a hello'

    @PeerTell.responder
    def gotit(self, name, port):  # test
        print('got it')
        return('hello')
