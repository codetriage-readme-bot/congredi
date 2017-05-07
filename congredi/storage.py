#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remove keys no subscribed user cares about.

    Uses orphaning test code (mostly through directed children)

    user -> trees

    user <- trees

    check every tree, if it has a user, check to see if the user cares.
    if not, delete it.

Diff utils (instead of using a raw git library - a design problem)

    move to unified diff forward/backward
Neo4j Mock code

    will need to pull from Neo4j examples

Compression/packetization functions

    splitting diffs / compressing for sending
PGP key & IP routing
Resolves routes (usefull for commands I have now misplaced)

This has the same name as another file in proofs/router.py...

Also, need to find a Zero Knowledge Proof of the length
of a connection without indicating where on the connection
someone is (which would tell people if their neighbor can
be harassed).
Map a directed acyclic graph from one user to another,
and map objects that people use (possibly a minimum number of people use)

    pull from Neo4j examples
Redis Mock code

    The actual code is using RSet/RGet, outside of classes.
    Need the @defer.inlineCallbacks to work within a class :/

censor things objectionable to you, rather than store/query/communicate them
the current library is old and might simply need to include regexes...
(Feature: Should add the ability to publish your router's censor settings - #E)

These functions operate very primatively, if you wanted to censor content you'll
**REALLY** have to beef them up.

Encrypted Storage pretty-much wants content to be a binary mess, so I suppose
that's another use for the censor.

What it needs to do is provide that the object in question is a valid:

* diff
* sig
* pubkey
* markdown object

And that it contains no information that could be harmful. It'll be decoded,
escaped, into a markdown format, so XSS is still a problem, but should obey
the encoding we give it (ASCII/UTF-8/others?)


    this object doesn't update censor properties in tests
Render markdown. (possibly not needed on the python end of things)
py-gfm>=0.1.3

    migrate this out

Mock Storage code

    should abstract the get/set methods into a mock storage.
Redis database commands & mutexes, not exactly the objects needed

Interface, in the case that someone wants to use something besides Redis/Neo4j,
for instance hadoop or bigtable....
Check if peer is online, check latest trees that people subscribe to

    Two functions are missusing Ask() parameters from the rewrite.
    Make sure to neaten everything and set that in the spec.
periodically resolve a git tree

    recursive ask from contacts on tree contents.
Periodically audit a vote

    recursive on vote process (see commands/proofs/vote)

    delete? send error back to other clients? certify bit?

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
from twisted.internet import reactor

# from ...utils.config import configArr
# from ...utils.whoops import whoops

from .utils import configArr
from .utils import whoops
#from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime

from abc import ABCMeta, abstractmethod
import six
from .utils import CongrediError

from difflib import unified_diff, ndiff, restore
from .utils import ensureString
#from patch import fromstring
import zlib
from six.moves import range
from .utils import ensureBinary
import random
logger = logging.getLogger('congredi')
#from ..utils.iter import pairwise
from py2neo import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost')
import entropy
import chardet
from profanity import profanity
try:
    import pycld2 as cld2
    WINDOWS = False
except ImportError as e:  # no test for this
    WINDOWS = True
    print(e)
    WINDOWS_ERROR = e
    logger.warning('windows users will have pycld2 disabled for now')
import txredisapi as redis
from redlock import RedLock
import uuid

import markdown
from mdx_gfm import GithubFlavoredMarkdownExtension
# from twisted.internet import defer
# from twisted.internet import reactor

# from ...utils.config import configArr
# from ...utils.whoops import whoops


# RedLock()

# will need to pull from settings... shouldn't ConfigArr have this?
connaddr = 'localhost'
connport = 6379


def queryBackground():  # test
    """
    Return an object from within peers
    One Subscription command -> several monitor commands
    """
    pass


def updateRead():  # test
    """
    Update trees with subscriptions
    One Subscription command -> several monitor commands
    """
    pass


def updateWrite():  # test
    """
    Publish trees to other nodes
    One Publish command -> several deploy commands
    """
    pass


shutDown = False


@defer.inlineCallbacks
def peerBeat():  # repeating peer-beat task
    # logger.info('peer heartbeat start')
    config = configArr()
    for admin in config['admins']:
        # logger.info('begin for admin: %s', admin)
        # test after the yields...
        # pylint: disable=unused-variable
        retset = yield Rset('admins', admin)
        retget = yield Rget('admins')
        retdel = yield Rdelete('admins')
        # pylint: enable=unused-variable
        # logger.info('set response:' + retset)
        # logger.info('get response:' + retget)
        # logger.info('delete response: %s', retdel)
    # if shutDown:
    #	loop.stop()


def peerSuccess():  # test
    logger.info('Peer Successful')


def peerFailure(failure):  # test
    logger.info('peer failure')
    whoops(failure.getBriefTraceback())
    reactor.stop()


#callID = reactor.callLater(5, f)
# callID.cancel()
# def main(reactor):
# 	delay = random.uniform(1, 5)
# 	d = task.deferLater(reactor, delay, f)
# 	d.addTimeout(3, reactor).addBoth(called)
# task.react(main)
"""
args
config
database


loop:
    check peers online
        increment/decrement peer online counter in db
    check online peers
        add/delete file listings
cmd:
    ping (hostname, port, key) -> pong (hostname, port, key)
    peers() -> peers(list[])
    have () -> have(list[])
    want () -> want(list[])
"""


def redisSetup(host, port):  # test
    return redis.Connection(host, port)
# could pull error classes into ..utils.whoops


class CongrediBadInterfaceError(CongrediError):
    pass


class CongrediIncompatibleVersionError(CongrediBadInterfaceError):
    pass


class abstractStorageProvider(six.with_metaclass(ABCMeta, object)):

    def __init__(self, typeOf):
        self.type = typeOf

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def _write(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _read(self, keyspace):
        raise NotImplementedError()

    @abstractmethod
    def _lockWrite(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _lockRead(self, keyspace):
        raise NotImplementedError()

"""
consumer item is confusing, should raise that error within
the code that consumes those abstract providers (commands/[addresses,filesystem], etc)
"""


class abstractStorageConsumer(object):

    def __init__(self, storage):
        if not isinstance(storage, abstractStorageProvider):
            raise CongrediBadInterfaceError('Bad Interface!')
        if not storage.version() == '1.0':
            raise CongrediIncompatibleVersionError('Non-compatible version!')
        self._storage = storage

    def write(self, key, value):
        self._storage._lockWrite(key, value)

    def read(self, key):
        return self._storage._lockRead(key)
# class Base(metaclass=ABCMeta):


class RedisStore(abstractStorageProvider):

    def __init__(self, connection=None):  # test
        if connection == None:
            self._conn = redisSetup(connaddr, connport)
        super(RedisStore, self).__init__(connection)

    # actual writers
    @defer.inlineCallbacks
    def _write(self, keyspace, valuespace):  # test
        res = yield self._conn.set(keyspace, valuespace)
        defer.returnValue(res)

    @defer.inlineCallbacks
    def _read(self, keyspace):  # test
        res = yield self._conn.get(keyspace)
        defer.returnValue(res)
    # delete

    def _del(self, key):
        res = yield self._conn.delete(key)
        defer.returnValue(res)

    # locks on items
    def _lockWrite(self, keyspace, valuespace):  # test
        with RedLock(keyspace[:2]):
            return self._write(keyspace, valuespace)

    def _lockRead(self, keyspace):  # test
        with RedLock(keyspace[:2]):
            return self._read(keyspace)

    # functions people will probably use
    def write(self, key, value):  # test
        return self._lockWrite(key, value)

    def read(self, key):  # test
        return self._lockRead(key)


# Condensed txredisapi example... but where should yield go?
@defer.inlineCallbacks
def Rget(key):  # test
    rc = yield redis.Connection(connaddr)
    value = yield rc.get(key)
    # logger.info('got %(key)s:%(value)s', {'key': key, 'value': value})
    yield rc.disconnect()
    defer.returnValue(value)


@defer.inlineCallbacks
def Rset(key, value):  # test
    rc = yield redis.Connection(connaddr)
    res = yield rc.set(key, value)
    # logger.info('set (%s) %s:%s', res, key, value)
    yield rc.disconnect()
    defer.returnValue(res)


@defer.inlineCallbacks
def Rdelete(key):  # test
    rc = yield redis.Connection(connaddr)
    n = yield rc.delete(key)
    # logger.info('deleted (%s) %s', n, key)
    yield rc.disconnect()
    defer.returnValue(n)


def RrandKey():  # test
    return str(uuid.uuid4().get_hex().upper()[0:6])


@defer.inlineCallbacks
def todoAdd(mutexKey, todoList, key):  # test
    rc = yield redis.Connection(connaddr)
    mutexKey.aquire()
    ret = yield rc.lpush(todoList, key)
    logger.info('Updated Todo list %(list)s: %(key)s:%(ret)s',
                {'list': todoList, 'key': key, 'ret': ret})
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)


@defer.inlineCallbacks
def todoRemove(mutexKey, todoList):  # test
    rc = yield redis.Connection(connaddr)
    mutexKey.aquire()
    ret = yield rc.rpop(todoList)
    logger.info('Grabbed from Todo list %(list)s: %(ret)s',
                {'list': todoList, 'ret': ret})
    mutexKey.release()
    yield rc.disconnect()
    defer.returnValue(ret)


class MockStorage(abstractStorageProvider):

    def __init__(self, typeOf):
        self.type = typeOf
        super(MockStorage, self).__init__(typeOf)

    @classmethod
    def version(self): return "1.0"

    def _read(self, keyspace):
        return self.get(keyspace)

    def _write(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)

    def _lockRead(self, keyspace):
        return self.get(keyspace)

    def _lockWrite(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)


def resolveHtml(md):
    """Return HTML (not for transfers between clients, only for resolving a webpage (Design - add markdown renderer to Delegito #G))"""
    return markdown.markdown(md, extensions=[GithubFlavoredMarkdownExtension()])


def stateProfanity(statement):  # needs a test
    """Profanity checks (Design: should probably be in a class - #A)"""
    return profanity.contains_profanity(statement)

# gosh I wish this would just work..


def resolveUnifiedDiff(md1, md2, l1, l2):
    """Resolving unified diff instead of using libgit (design/feature - make one of them work #G)"""
    # must use python-patch to use unified diffs...
    md1 = ensureString(md1)
    md2 = ensureString(md2)
    diff = unified_diff(md1.splitlines(
        1), md2.splitlines(1), l1, l2, lineterm='', n=0)
    print(diff)
    result = '\n'.join(list(diff))
    return result


def resolveDiff(md1, md2):
    md1 = ensureString(md1)
    md2 = ensureString(md2)
    """Ndiffs (for right now unless resolveUnifiedDiff #G can be solved)"""
    diff = ndiff(md1.splitlines(1), md2.splitlines(1))  # , lineterm='', n=0)
    result = ''.join(list(diff))
    #result = '\n'.join(list(diff))
    return result


def rebuildFile(diff, option):
    """Restore an Ndiff"""
    result = ''.join(restore(diff, option))
    return result


def tick(md1, md2):
    """Get a storeable object"""
    unified = resolveDiff(md1, md2)
    print(type(unified))
    compressed = compressDiff(unified)
    return compressed


def tock(compressed, direction):
    """Decompress a stored object"""
    uncompressed = uncompressDiff(compressed)
    uncompressed = ensureString(uncompressed)
    original = '\n'.join(list(restore(uncompressed, direction)))
    return original


def stateEntropy(statement):  # needs a test
    """Return the entropy of an item (Feature: could use the histogram - #B)"""
    return entropy.shannon_entropy(statement)


def stateLanguage(statement):
    """"Language detection (Design: still a bare except - #C)"""
    try:
        return cld2.detect(statement)[2][0][0]
        # this is throwing on python 2.0 for some reason on tests.
        # wasn't checking the exception block... whoops.
    # pylint: disable=broad-except
    except Exception as e:
        print(e)
        if WINDOWS is True:  # needs a test
            print(WINDOWS_ERROR)
            logger.warning('windows users will have pycld2 disabled for now')
            # raise Exception('windows users will have pycld2 disabled for now')
        return None
    # pylint: enable=broad-except


def stateEncoding(statement):
    """Return character encoding"""
    statement = ensureBinary(statement)
    try:
        return chardet.detect(statement)['encoding']
    except UnicodeDecodeError:  # needs a test
        return None


class censor():
    """
    A censor that keeps along the allowed encodings, languages, and profanity.
    Can be used to check (returns false if bad) or block (returns true if bad).
    """

    def __init__(self, encodings, languages, checkProfanity=False, wordlist=None, listhash=None):
        self.encodings = encodings
        self.languages = languages
        self.profanities = checkProfanity
        """loading wordlists (Design: should be part of class - A)"""
        # needs a test
        if wordlist:
            profanity.load_words(wordlist)
        # elif listhash:
        #	content = getSHA(listhash).split('\n'); profanity.load_words(wordlist)

    def check(self, statement):
        """Opposite result (Design: return the rest of the objects? - #D)"""
        return not self.block(statement)[0]

    def block(self, statement):
        statement = ensureBinary(statement)
        res_encode = stateEncoding(statement)
        res_encode_ok = res_encode in self.encodings
        res_lang = stateLanguage(statement)
        res_lang_ok = res_lang in self.languages
        res_profanities = self.profanities and stateProfanity(statement)
        res = True
        # if res_encode_ok and res_lang_ok and not profanity:
        if res_encode_ok:
            if res_lang_ok:
                if not res_profanities:
                    res = False
        res_human = "SAFE"
        if res:
            res_human = "BLOCK"
        """Results objects.... (Design: reorder? - #D)"""
        return res, res_human, res_encode, res_lang, res_encode_ok, res_lang_ok, res_profanities


class CongrediNoRouteError(CongrediError):
    """No route to host"""
    pass


class Neo4jMock(MockStorage):
    arr = {}
    within = True

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(Neo4jMock, self).__init__(typeOf)

    def TrustWithin(self, key):
        return self.within


class RedisMock(MockStorage):  # object
    arr = {}

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(RedisMock, self).__init__(typeOf)

    def read(self, key):
        return self._read(key)

    def write(self, key, value):
        return self._write(key, value)

    def rdel(self, key):
        self.arr.remove(key)
        return b'OK'

    def set(self, key, value):
        self.arr[key] = value
        return b'OK'

    def get(self, key):
        try:
            return self.arr[key]
        except KeyError:
            return []


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


def assertTrustXY(x, y):  # test
    driver.run(
        "CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
    return True


def queryTrustXY(x, y):  # test
    driver.run()


def dependencies(obj):  # test
    """Calculate the dependencies of an object"""
    pass
"""
Redis social graphs (would still need to implement acyclic search, best to load
into local memory instead T.B.H.).
http://nosql.mypopescu.com/post/1083079162/redis-snippet-for-storing-the-social-graph
"""


def chunkSplit(compressed):  # restore: ''.join()
    """Split chunks into the maximum size for AMP messages (if tripple encrypted) (Design - find that byte limit #F)"""
    compressed = ensureBinary(compressed)
    return [compressed[k:k + 250] for k in range(0, len(compressed), 250)]


def compressDiff(diff):
    """Zlib compression (before packet transmission/storage)"""
    diff = ensureBinary(diff)
    return zlib.compress(diff, 7)


def uncompressDiff(archive):
    """Zlib decompression (before use)"""
    return ensureBinary(zlib.decompress(archive))
