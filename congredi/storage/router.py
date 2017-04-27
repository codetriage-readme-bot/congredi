#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PGP key & IP routing
Resolves routes (usefull for commands I have now misplaced)

This has the same name as another file in proofs/router.py...

Also, need to find a Zero Knowledge Proof of the length
of a connection without indicating where on the connection
someone is (which would tell people if their neighbor can
be harassed).

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
import random
logger = logging.getLogger('congredi')
from ..utils.whoops import CongrediError
#from ..utils.iter import pairwise


class CongrediNoRouteError(CongrediError):
    """No route to host"""
    pass


class router():
    nodes = []

    def __init__(self, routerKey):
        self.key = routerKey

    # routes will have a key and an IP
    def route(self, rendesvousKey, hops=3):
        """generate a route to an introduction node using a list of keys (see alternate in packet/hybrid.py)"""
        # self, node, returnaddr, rendesvous
        if rendesvousKey not in self.nodes:
            raise CongrediNoRouteError('Rendesvous Key not in node list')
        tempNodes = list(self.nodes)
        result = []

        def add(choice):
            result.append(choice)
            tempNodes.remove(choice)
        tempNodes.remove(self.key)
        add(rendesvousKey)
        while len(result) < hops:
            choice = random.choice(tempNodes)
            add(choice)
        return result


class onion():
    '''
    Secure Packet Routing Methods. (layered under TLS)
    '''

    def __init__(self, key):  # test
        self.key = key

    """
    def PackMsg(self, msg, re, numHops=3):  # test
        introductionPoint = self.RandomIntroPoint(re)
        route = self.GetRoute(introductionPoint, numHops)
        message = msg
        for node, nextNode in pairwise(route):
            key = self.FindKey(node)
            nodeKey = ECC(key)
            message = nodeKey.encrypt(message)
            message = nextNode + message
    """
    """
    def GetRoute(self, finalAddr, numHops):  # test
        # routing nodes are all nodes minus my key
        tempNodes = list(self.nodes)
        tempNodes.remove(self.key)

        # we will be adding a node to our result
        # then deleting it from the available ones
        result = []

        def add(choice):
            result.append(choice)
            tempNodes.remove(choice)

        # we want the final result to be the rendesvous
        add(rendesvousKey)
        while len(result) < hops:
            choice = random.choice(tempNodes)
            add(choice)
        return result

    def UnPackMsg(self, msg):  # test
        nextNode = msg[:64]
        message = self.nodeKey.decrypt(msg[64:])
        return message, nextNode
    """
# 65535 bytes 65 kb

"""
def GetPacket():  # AMP.TLS): # test
    if message[:64] != pubkey:
        errBack('not me')
    hsh = hash(message[-64:])
    if hsh != message[:-64]:
        errBack
    cKey = self.key.decrypt(message[64:128])
    message = cKey.decrypt(message[128:-64])
    if (hash(message[-64:]) == message[:-64]):
        # valid next packet - send off to addr
        TTL = privledge
        # piping.append(from,to)
        addr = lookup(key)
        _send(mesg, addr)


def SendPacket():  All Or Nothing Padding (coulda just used the library's version)
# AMP.TLS): # test
    cKey = AES()
    ctxt = cKey.encrypt(message)
    val = recipient.encrypt(cKey)
    preMesg = pubkey + val + ctxt
    msg = preMesg + hash(preMesg)


def OnionRoute():  # test
    for r in reversed(route):
        pkt = SendPacket(r)
    _send(pkt, addr)


def _send(pkt, addr):  # test
    result = getThing()
    if result == errBack:
        forward(errBack)
    else:
        pass


def _recieve(pkt, addr):  # test
    result = FulfillThing()
    if not result:
        errBack
routers = []
entrys = []
"""
# A -> B -> C -> D -> E -> F
"""
TLS(
	hash|
	recipientKey|
	recipeintECC(aesKey)|
	aes(AONT_OAEP(msg))
	)
recipient:
	sendToNext
		:decrypt
circuit table: from - to
class CongrediProtocol():
    def GetPacket(pkt):  # test
        if lookupKey(pkt[:64]) == False:
            if lookupTrust(peer.key) == False:
                conn.write("Key Unavailable for Routing.")
            else:
                key = AskPeersForKey(pkt[:64])
                if key is none:
                    conn.write("Key Unavailable for Routing")
                    conn.drop()
        if pkt[:64] == self.routeKey:
            GetCommand(pkt)
        if pkt[:64] == self.routeKey:
            GetCommand(pkt)
        else:
            pass

    def PickIntro(self):  # test
        pass
        # route to Intro
        # ask intro
        # publish packet

    def PickRendesvous(self):  # test
        pass

    def SendRequest(self):  # test
        pass
        # onion wrap

    def RecieveRequest(self):  # test
        pass

    def Send(self):  # test
        pass

    def UpOnion(self):
        pass

def encryptHops(rendesvous, gateway, server, numHops=3):
    for hop in numHops:
        aeskey = rand()
        AES(pkcs_oeap_aont(msg))
        head = ecc(hop.pubkey, aeskey)
        msg = head + ':' + msg
"""
# congredi/storage/router.py                  48     10    79%   61,
# 97-99, 184, 190, 193, 197, 200, 203
