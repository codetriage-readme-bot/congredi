#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP Objects. If I don't have to serialize them, why bother?

These provide readible names for argument Types:
# if necissary, these will do something besides just send binary.
# could be doing hash validation for all this??
# class inheritance?
# Encrypted Boolean

EncBool                 - Boolean (len?)
EncAddress/ObjAddress   - Addresses (IP/Tor/DNS)
EncPubKey/ObjPubKey     - Public Keys (len?)
ObjHash/EncHash         - Hashes (len?)
ObjSig/EncSig           - Sig of Hash (len?)
ObjBlob/EncBlob         - General Blobs

PrivAES                 - RSA encrypted session key


http API

    Redo the spec for the api on github.com/congredi/spec

# authorization stuff
/auth/new           - check DB, get long term JWT
/live/next          - get next short term JWT from long term JWT
/live/online        - find if a peer is online

# getting/setting contents
/set/<permission[0|1]>/<typeOf>
/get/<permission[0|1]>/<typeOf>

# searching/indexing (offset is a hash value, not an integer)
/index/<typeOf>/<direction>/<offset>/<count:double>/<hashPtr>
/search/<typeOf>/<offset>/<count:double>/<term>

# neater aliases:

/d/
    /commit/<id>
    /chunk/<id>
    /vote/<id>
    /bio/<id>
    /poll/<id>
    /manifesto/<id>
/s/
    /rendesvous - rendesvous settings
    blacklist - blacklist settings
    whitelist - whitelist settings
    peer - peer listings
    admin - admin settings
    user - user settings
/r/<routername>/
    /ip
    /censor
    /uptime
    /has
    /wants
    /seen
    /proof
    /rank
/u/<username>/
    /bio
    /location
    /courier
    /vote/<voteid>
    /poll/<pollid>
    /proposal/<id>
    /save/<saveid>
/g/<groupname>/
    /manifesto
    /borders
    /members
    /votes/<voteid>
    /polls/<pollid>
    /saves

/api/
	/<user>/
		/trust/ - update your pgp keys
		/avatar/ - png/jpeg avatar
		/profile/ - json dict profile strings
		/<user>/ - return user dict
			/avatar/ - return user image
			/trust/ - sign their key with yours
	/search/ - return key:value from a value search
		{ type:["~"|"<"|">"|"=="], amount:int, offset: int, subset: "key", search: "string" }
		{ meta:{offset:int,amount:int}, key: base64, value: { json } }
		/peers/ - /peer/ indexes, some meta searches
		/govts/
		/votes/
		/options/
/peer/ - return idx
	/<hash>/ - current onion addresses
		/trust/ - pgp key chain
		/uptime/ - reputation
		/stake/ - stake proof blocks
/govt/ - return idx
	/<jurisdiction>/ - return active vote/user blocks (signed by jurisdiction)
		/validated/ - issues signed on by consensus (multiple winners)
		/ordered/ - distributed block (data secure)
		/unordered/ - idx proposed issues
		/denied/ - idx of issues denied entrance
		/<issueid>/ - return an issue signature
/vote/ - return idx
	/<hash>/ - genesis block
		/validated/ - idx of asserted
		/ordered/ - idx of consensus-ordered
		/unordered/ - idx of proposed blocks
		/open/ - idx of voters who have not voted
		/<blockid>/ - return a block and its contents

AMP commands for addresses - replaces command.py

Commands:
* Address - tell them what you thought theirs was, get what they saw yours as
* SyncPeerDirectory - send a list of (key, ip)s, get back a list of (key, ip)s
* SyncRendesvousDirectory - list of (key, rendesvousKey, proof) <->
* SyncCourierDirectory - list of (key, courierKey, proof) <->

These commands manage connections on the network (along with Router.py and
PeerBeat).
Coordinated port opening for testing.

    Is there a simpler way to do this...

main client class - terminal

    This should start either with or without a peer.

    should it stream input or be a REPL??

    REPL is easiest to implement.

    just duplicate commands from HTTP API or KISS with one BSON interface...
    ugh then we loose async...

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
from klein import Klein
from .auth import token
import socket

from twisted.internet import protocol, reactor, task
from .utils import passLevel
from .utils import configArr
from .utils import MainOptions
from .utils import CongrediError
import logging
import sys
logger = logging.getLogger('congredi')
# , String, Boolean, DateTime
from twisted.protocols.amp import Command, Integer, ListOf
#ObjHash, ObjSig,
from os import path

# from twisted.internet.error import CannotListenError
# from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.protocols.amp import Argument

import os
from twisted.protocols.basic import LineReceiver
from .crypto import AONTdecrypt, AONTencrypt
from .crypto import default_rsa
from .storage import Rget
import binascii

# pylint: disable=arguments-differ


class EncBool(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Addresses (IP/Tor/DNS) : len? Type?


class ObjAddress(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncAddress(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Public Keys : len?


class ObjPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString
# Hashes : len?


class ObjHash(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncHash(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Sigs of Hashes : len?


class ObjSig(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncSig(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Blobs (general, compressed?)


class ObjBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob


class EncBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# RSA encrypted session key : len?


class PrivAES(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob

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


defaultHost = socket.gethostname()
app = Klein()
key = token('onetwothree')


def expand(pathname):
    return path.expanduser(pathname)


class fileCoord():

    @staticmethod
    def read(pathname="~/ort"):
        if not path.isfile(expand(pathname)):
            fileCoord.write(socket.gethostname(), 8800, pathname)
        with open(expand(pathname), 'r') as a:
            stuff = a.read()
            return stuff.strip('\n').split(":")

    @staticmethod
    def write(host, port, pathname="~/ort"):
        with open(expand(pathname), 'w+') as a:
            a.write(host + ":" + str(port))


# find address from outside
# set this on a timer in klein instance
# ping/pong
class AddressAsk(Command):
    arguments = [(b'name', ObjAddress()),
                 (b'port', Integer())]
    response = [(b'name', ObjAddress()),
                (b'port', Integer())]


class SyncPeerDirectoryAsk(Command):
    # would have prefered dict capability.
    # these may need encoding...
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]

    def __init__(self, commandType, *a, **kw):
        print('Command Created')
        super(SyncPeerDirectoryAsk).__init__(commandType, *a, **kw)
    """
    in: list((key,ip))
    out: list((key,ip))
    """
# rendesvous/courriers


class SyncRendesvousDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, rendesvous key, proof))
    out: list((key, rendesvous key, proof))
    """


class SyncCourierDirectoryAsk(Command):
    arguments = [(b'dir_pubkey', ListOf(ObjPubKey())),
                 (b'dir_addrs', ListOf(ObjAddress())),
                 (b'dir_ports', ListOf(Integer()))]
    response = [(b'dir_pubkey', ListOf(ObjPubKey())),
                (b'dir_addrs', ListOf(ObjAddress())),
                (b'dir_ports', ListOf(Integer()))]
    """
    in: list((key, courier key, proof))
    out: list((key, courier key, proof))
    """


class addressesResponders(object):
    redis = None
    neo4j = None

    def __init__(self, givenRedis):
        self.redis = givenRedis

    @AddressAsk.responder
    def AddressTell(self):
        """
        Add that person to the ephemeral recently-seen list.
        Send back what their IP/port was.
        """
        myAddress = self.redis.read(b'self:addr')
        return myAddress
    # ask the directory, while sending your own

    @SyncPeerDirectoryAsk.responder
    # yourPeers):
    def SyncPeerDirectoryTell(self, dir_pubkey, dir_addrs, dir_ports):
        """
        in: list((key,ip))
        out: list((key,ip))
        """
        logger.info('HELLOPWE')
        print('SyncPeerDirectoryAsk')
        # myPeers
        dir_addrs = self.redis.read(b'list:peers')
        # self.redis.write(b'todo:peers', yourPeers)

        return dir_pubkey, dir_addrs, dir_ports
        # return myPeers

    @SyncRendesvousDirectoryAsk.responder
    def SyncRendesvousDirectoryTell(self, yourRendesvous):
        """
        in: list((key, rendesvous key, proof))
        out: list((key, rendesvous key, proof))
        """
        myRendesvous = self.redis.read(b'list:rendesvous')
        self.redis.write(b'todo:rendesvous', yourRendesvous)
        return myRendesvous

    @SyncCourierDirectoryAsk.responder
    def SyncCourierDirectoryTell(self, yourCouriers):
        myCouriers = self.redis.read(b'list:couriers')
        self.redis.write(b'todo:couriers', yourCouriers)
        return myCouriers


class CongrediAPI():
    commandKeys = []

    def __init__(self, host=defaultHost, port=4400, redisDetails=6379, neo4jDetails=7474, initialKey=None):
        self.host = host
        self.port = port
        self.redisDetails = redisDetails
        self.neo4jDetails = neo4jDetails
        if initialKey:
            self.commandKeys.append(initialKey)
        ReminderToPing = task.LoopingCall(self.ping).start(15.0)
        reactor.add(ReminderToPing)

    def ping(self):
        peerlist = self.redis.get('peerlist')
        for peer in peerlist:
            SyncPeerDirectoryAsk(peer)


@app.route('/auth/new')
def get_auths():
    """checks auths within db and returns a long term JWT"""
    pass


@app.route('/live/next')
def next_key():
    """takes a long term JWT and return the current short term JWT"""
    pass


@app.route('/live/online')
def check_online():
    pass


@app.route('/set/<int:permission>/<typeOf>')
def set_value(permission, typeOf):
    pass


@app.route('/get/<int:permission>/<typeOf>')
def get_value(permission, typeOf):
    pass


@app.route('/index/<typeOf>/<direction>/<offset>/<float:count>/<hashPtr>')
def tell_index(typeOf, direction, offset, count, hashPtr):
    pass


@app.route('/search/<typeOf>/<offset>/<float:count>/<term>')
def search_term(typeOf, offset, count, term):
    pass

def normalConfigPath():
    if 'windows' == True:
        return 'windows path'
    if 'linux' == True:
        return 'linux path'

def run():
    """
        pull args (ports, debug level, config location)
        http api, redis addr/port, neo4j addr/port
    """
    args = MainOptions.parse_args()
    if args.help:
        MainOptions.print_help()
        sys.exit(0)
    # pull config location
    configPath = normalConfigPath()
    if args.config:
        configPath = args.config
    # did I set the right config order in the spec?
    # pylint: disable=unused-variable
    config = configArr(configPath)

    # setting log level from arguments.
    passLevel(args)

    # try to start on specific port, fail over
    try:
        # given port
        # failover / errback
        # fail and exit

        reactor.run()
    except KeyboardInterrupt:
        pass
    except CongrediError as e:
        logger.critical("Congredi failed: %s", e.message)
    finally:
        print('\ngoodbye...')
