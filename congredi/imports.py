#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function

from twisted.internet import protocol, reactor, task
# , String, Boolean, DateTime
from twisted.protocols.amp import Command, Integer, ListOf
#ObjHash, ObjSig,
import math
import sys
from six.moves import range
# from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.protocols.amp import Argument

import os
from twisted.protocols.basic import LineReceiver
from .crypto import AONTdecrypt, AONTencrypt
from .crypto import default_rsa

# from ...utils.config import configArr
# from ...utils.whoops import whoops

from .utils import configArr
from .utils import whoops
#from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime

from abc import ABCMeta, abstractmethod
from .utils import CongrediError

from .utils import ensureString
#from patch import fromstring
from six.moves import range
from .utils import ensureBinary
import random
logger = logging.getLogger('congredi')
#from ..utils.iter import pairwise

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension



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
