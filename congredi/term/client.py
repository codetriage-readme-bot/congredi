#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
main client class - terminal

    This should start either with or without a peer.

    should it stream input or be a REPL??

    REPL is easiest to implement.

    just duplicate commands from HTTP API or KISS with one BSON interface...
    ugh then we loose async...

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import logging
import os
logger = logging.getLogger('congredi')
from twisted.protocols.basic import LineReceiver
from ..crypto.padding import AONTdecrypt, AONTencrypt
from ..crypto.RSA import default_rsa
from ..storage.redis import Rget
from twisted.internet import protocol
import binascii


class ClientProtocol(LineReceiver):

    def connectionMade(self):  # test
        self.transport.write(b'>>> ')

    def rawDataReceived(self, data):
        print(binascii.hexlify(data))

    def lineReceived(self, line):  # test
        params = line.split(b" ")
        print(params)
        """Reimplement commands... bad idea"""
        if line[0] == 'get':
            res = Rget(line[1:])
            res = res + b'two'
        self.sendLine(b'Echo: ' + line)
        self.transport.write(b'>>> ')

    host = None
    port = None
    key = None

    def __init__(self, host="localhost", port=4400,
                 clientKey=None, clientPass=None):  # test
        self.host = host
        self.port = port
        if clientKey:
            self.key = clientKey
        else:
            self.key = default_rsa()
        if clientPass:
            self.password = clientPass
        else:
            self.password = os.urandom(16)
        logger.debug('built client')

    def wrapRequest(self, request, serverKey):  # test
        paddedRequest = AONTencrypt(request)
        encryptedRequest = self.key.encrypt(paddedRequest, serverKey)
        return encryptedRequest

    def unwrapRequest(self, encryptedRequest):  # test
        decryptedPadding = self.key.decrypt(encryptedRequest)
        request = AONTdecrypt(decryptedPadding)
        return request


class CongrediClient(protocol.ClientFactory):
    """Mostly debugging with prints.."""

    def __init__(self, host, port, clientKey):  # test
        print('hello')
        self.clients = []
        self.host = host
        self.port = port
        self.key = clientKey

    def buildProtocol(self, addr):  # test
        return ClientProtocol(self.host, self.port, self.key)  # self

    def startedConnecting(self, connector):  # test
        print('Started to connect.')

    def clientConnectionLost(self, connector, reason):  # test
        print(('Lost connection.  Reason:', reason))

    def clientConnectionFailed(self, connector, reason):  # test
        print(('Connection failed. Reason:', reason))
# congredi/term/client.py                     56     18    68%   23,
# 26-32, 47, 53-55, 58-60, 74, 77, 80, 83
