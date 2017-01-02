#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main client class - terminal
"""
import logging
import os
logger = logging.getLogger('congredi')
from twisted.protocols.basic import LineReceiver
from ..crypto.padding import AONTdecrypt, AONTencrypt
from ..storage.redis import get
from twisted.internet import protocol
#from ..tasks import garbageCollect


class ClientProtocol(LineReceiver):

    def connectionMade(self): # test
        self.transport.write('>>> ')

    def lineReceived(self, line): # test
        params = line.split(" ")
        print(params)
        """Reimplement commands... bad idea"""
        if line[0] == 'get':
            res = get(line[1:])
        self.sendLine('Echo: ' + res)
        self.transport.write('>>> ')

    host = None
    port = None
    key = None

    def __init__(self, host="localhost", port=4400,
                 clientKey=None, clientPass=None): # test
        self.host = host
        self.port = port
        if clientKey:
            self.key = clientKey
        else:
            self.key = asym()
        if clientPass:
            self.password = clientPass
        else:
            self.password = os.urandom(16)
        logger.debug('built client')

    def wrapRequest(self, request, serverKey): # test
        paddedRequest = AONTencrypt(request, self.password)
        encryptedRequest = self.key.encrypt(paddedRequest, serverKey)
        return encryptedRequest

    def unwrapRequest(self, encryptedRequest): # test
        decryptedPadding = self.key.decrypt(encryptedRequest, self.key)
        request = AONTdecrypt(decryptedPadding)
        return request


class CongrediClient(protocol.ClientFactory):
    """Mostly debugging with prints.."""

    def __init__(self): # test
        print('hello')
        self.clients = []

    def buildProtocol(self, addr): # test
        return CongrediClient(self)

    def startedConnecting(self, connector): # test
        print('Started to connect.')

    def clientConnectionLost(self, connector, reason): # test
        print('Lost connection.  Reason:', reason)

    def clientConnectionFailed(self, connector, reason): # test
        print('Connection failed. Reason:', reason)
