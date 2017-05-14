#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
peerBeat tests
zlib tests

    See PeerBeat. Should Implement.
garbageCollect tests

    see garbageCollect.

    Here we test:
        user-A->repo-B, repo-C(orphaned): GC should remove C, leave B
        Repo-B(orphaned): GC should remove B
        user-A->repo-B,repo-C user-D->repo-B: GC should not error on multiple parents

tests on the simplistic censor library.
tests on the diff utils
HTML tests

moving away from using HTML on the Python client.
Abstract Interface Provider tests

    basic checks for good/bad interface code:

    the interfaces need to have certain functions, and while
    we're not checking that the outputs match (feature), this
    is a basic check that the stated internal API of a developed
    driver matches.

    These checks are of an interface that has what it
    needs, and one that doesn't have everything, to test
    our CongrediBadInterfaceError & CongrediIncompatibleVersionError

    Feature: Check function return signatures on an abstract-method?

neo4j tests
Redis object tests
test router. These functions probably need relocating.

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from .utils import TimedTestCase
from .storage import compressDiff
from .storage import uncompressDiff
from .storage import chunkSplit
from .utils import source, source2
from .storage import abstractStorageProvider, abstractStorageConsumer
from .storage import CongrediBadInterfaceError, CongrediIncompatibleVersionError
from .storage import resolveHtml
# , redisSetup, Rget, Rset, RrandKey, todoAdd, todoRemove
from .storage import RedisStore
from .storage import RedisMock
# twisted.internet.task.Clock
# see voteAudit
# twisted.internet.task.Clock
# see treeResolve
# twisted.internet.task.Clock
from .storage import peerSuccess, peerFailure, peerBeat
from .storage import queryBackground, updateRead, updateWrite
from twisted.internet.error import ReactorNotRunning
# from .garbageCollect
# twisted.internet.task.Clock
import platform
from .storage import censor
from .storage import stateEncoding
from .storage import stateEntropy
from .storage import stateProfanity
from .utils import ensureBinary
from .utils import random, hexify, phony
from six.moves import range
import hashlib
import binascii
from .storage import router, CongrediNoRouteError, onion
# try:
#     from StringIO import StringIO
# except ImportError:
#     from io import StringIO
# from patch import PatchSet, fromstring
from .storage import resolveUnifiedDiff
from .storage import resolveDiff
from .storage import rebuildFile
from .storage import tick
from .storage import tock
from .utils import empty, empty2
#from .neo4j import assertTrustXY, queryTrustXY, dependencies


class test_zlib(TimedTestCase):
    things = [
        'a',
        'b',
        'c'
    ]
    splits = None
    thing1 = None
    res = None

    def test_split(self):
        """
            Split something into chunks
            passes if it doesn't throw errors
            next design should split into a known number of chunks and assert()
        """
        self.threshold = .2
        self.splits = chunkSplit(source)
        print((len(self.splits)))

    def test_compression(self):
        """Compress, Uncompress, ensure equal"""
        self.threshold = .2
        self.thing1 = compressDiff(source2)
        self.res = uncompressDiff(self.thing1)
        print('New')
        print(self.res)
        print('Original')
        print(source2)
        assert self.res == source2

    # test split error-raising

    # test compression error-raising


class test_router(TimedTestCase):

    good_router = None
    bad_router = None

    def test_routing(self):
        """Route Items"""
        self.threshold = .2
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        print(('Random route to a %s' % r.route('a', 2)))
        print(('Random route to a %s' % r.route('a', 5)))
        print(('Random route to a %s' % r.route('a')))
        print(('Random route to a %s' % r.route('a')))
        self.good_router = r
        onion("key")

    def test_impossible(self):
        """Impossible Route - catches itself if an impossible route returns without NoRouteError"""
        self.threshold = .2
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        try:
            r.route('q', 6)
        except CongrediNoRouteError:
            print('Caught. Good. That was impossible.')
            self.bad_router = r
            return True
        raise Exception('Didnt catch')
    # test a route that loops on itself


class test_redis(TimedTestCase):

    def setUp(self):
        self.conn = RedisMock(b'redis v1')
        self.RedisStore = RedisStore(self.conn)
        super(test_redis, self).setUp()

    def test_redis(self):
        """
            Init a redis connection or use a mock?
            Actual Redis code is using RSet/RGet, need to call that
            instead of the Mock.
        """
        self.threshold = .1
        print('IMPLEMENT storage/test/test_redis')
        print(self.RedisStore._write(b'a', b'b'))
        print(self.RedisStore._read(b'a'))
        print(self.RedisStore._del(b'a'))
        #assert b'b' == self.RedisStore._read(b'a')


class test_neo4j(TimedTestCase):

    def test_neo4j(self):
        """Connect to neo4j or use a mock? acyclic graph mock interfaces???"""
        self.threshold = .1
        print('IMPLEMENT storage/test/test_neo4j')
        print('Directed Acyclic Graph - add/delete/check-good/check-bad on graph')


class good_provider(abstractStorageProvider):

    def _write(self, keyspace, valuespace):
        return b'ok'

    def _read(self, keyspace):
        return b'value'

    def _lockWrite(self, keyspace, valuespace):
        return b'ok'

    def _lockRead(self, keyspace):
        return b'value'


class test_interface(TimedTestCase):

    def test_not_implemented(self):
        self.threshold = .1
        # pylint: disable=abstract-method

        class bad_provider(abstractStorageProvider):
            pass
        # pylint: enable=abstract-method
        # pylint: disable=abstract-class-instantiated,no-value-for-parameter,
        # arguments-differ
        try:
            a = bad_provider()
            a.write(b'one')
            self.fail()
        except (CongrediBadInterfaceError, TypeError):
            pass
        # pylint: enable=abstract-class-instantiated,no-value-for-parameter

    def test_client_okay(self):
        self.threshold = .1
        provider1 = good_provider('a')
        client = abstractStorageConsumer(provider1)
        client.write(b'b', b'b')
        client.read(b'b')

    def test_client_mad(self):
        self.threshold = .1
        b = good_provider('a')
        # pylint: disable=unused-variable
        def funk():
            return "2.0"
        def version():
            return "funk"
        try:
            client = abstractStorageConsumer(b)
            client.write(b'b', b'b')
            print('bad')
        except CongrediIncompatibleVersionError:
            print('good')
        c = object()
        try:
            client = abstractStorageConsumer(c)
            client.write(b'b', b'b')
            print('bad')
        except CongrediBadInterfaceError:
            print('good')


class test_html(TimedTestCase):
    result_html = None

    def test_html(self):
        """Why do I have HTML resolving when people should do this themselves?"""
        self.threshold = .38
        html = resolveHtml(source)
        print(html)
        self.result_html = html


class test_diff(TimedTestCase):

    def test_resolve_ndiff(self):
        """NDiff of source, source2, rebuild diff"""
        self.threshold = .2
        print('The Diff:')
        result = resolveDiff(source, source2)
        print((''.join(result)))
        print('The Original:')
        orig = rebuildFile(result, 1)
        print((''.join(orig)))

    def test_compression(self):
        """Full-integrated Tick/Tock compression"""
        self.threshold = .2
        # Direct conversion
        res = tick(source, source2)
        beep = tock(res, 1)
        print('Compression test:')
        print(beep)

    def test_splits(self):
        """Split & recombine, check hashes."""
        self.threshold = .2
        data = {'pieces': {}}
        comp = tick(empty, empty2)
        print(('compressed %d' % len(comp)))
        data['length'] = len(comp)
        data['hash'] = hashlib.sha256(comp).digest()
        splt = chunkSplit(comp)
        for c in splt:
            key = hashlib.sha256(c).hexdigest()
            print(type(c))
            data['pieces'][key] = binascii.hexlify(c)
        for k, v in data['pieces'].items():
            print(k, binascii.hexlify(v))
        jnd = b''.join(splt)
        final = hashlib.sha256(jnd).digest()
        print(('join %d' % len(jnd)))
        print(('hash: %(one)s\nhash: %(two)s' %
               {'one': binascii.hexlify(data['hash']), 'two': binascii.hexlify(final)}))

    def test_uni(self):
        """Unified Diffs."""
        self.threshold = .2
        diff = resolveUnifiedDiff(
            source, source2,
            'congredi/test/core/algos/a.txt',
            'congredi/test/core/algos/b.txt')
        print(type(diff))
        # not python3 compatible
        #patch = fromstring(silenceInsanity(diff))
        # print((patch.errors))
        #patch.revert(0, root='.')
        #patch.apply(0, root=".")

test = censor(encodings=['UTF-8', 'ascii'], languages=['ENGLISH', 'CHINESE'])


class test_censor(TimedTestCase):

    def test_encode_decode_python_2_3(self):
        '''encode/decode python 2/3 problems'''
        self.threshold = .4
        b_string = b"a string"
        u_string = u"a string"
        reg_string = "a string"
        reg_unicode = '你好'
        reg_unicode_encoded = "one 你好".encode('utf8')
        print(stateEncoding(ensureBinary(b_string)))
        print(stateEncoding(ensureBinary(u_string)))
        print(stateEncoding(ensureBinary(reg_string)))
        print(stateEncoding(ensureBinary(reg_unicode)))
        print(stateEncoding(ensureBinary(reg_unicode_encoded)))
        assert(stateEncoding(b_string) == 'ascii')
        assert(stateEncoding(u_string) == 'ascii')
        assert(stateEncoding(reg_string) == 'ascii')
        assert(stateEncoding(reg_unicode) == 'utf-8')
        assert(stateEncoding(reg_unicode_encoded) == 'utf-8')

    def test_obvious_catch(self):
        '''Should block (best 8/10, os.urandom()):'''
        self.threshold = .4
        passes = 0
        for _ in range(0, 10):
            actual_random = random()
            res = test.check(actual_random)
            if not res:
                passes += 1
        print(("%d/10" % passes))
        assert passes >= 8

    def test_encode(self):
        '''Should safe (best 14/15, os.urandom()):'''
        self.threshold = .4
        passes = 0
        for _ in range(0, 15):
            encoded_random = hexify(random())
            if stateEncoding(encoded_random) == 'ascii':
                passes += 1
        print(("%d/15" % passes))
        assert passes >= 14

    def test_trivial_bypass(self):
        '''Should safe (best 24/25, os.urandom()):'''
        self.threshold = .4
        passes = 0
        for _ in range(0, 25):
            phonetic_random = phony(hexify(random()))
            if test.check(phonetic_random):
                passes += 1
        print(("%d/25" % passes))
        if platform.system() == 'Windows':
            print('Windows tests will not assert > 24')
        else:
            assert passes >= 24

    def test_unicode(self):
        '''Chinese characters should be UTF-8'''
        self.threshold = .4
        assert stateEncoding('hello 你好') == 'utf-8'

    def test_entropy(self):
        self.threshold = .3
        print(stateEntropy(b'b'))

    def test_profanity(self):
        self.threshold = .3
        print(stateProfanity(u'b'))
    # def test_steno_check():

    def test_valid_english(self):
        """Valid ASCII content:"""
        self.threshold = .4
        if platform.system() == 'Windows':
            print('Windows tests will not check valid english')
        else:
            assert test.check(b'#This *is* valid content')
    # Broken Test.
    # def test_valid_chinese():
    #	print('Should pass:')
    #	print(test.block('#Hello 你好'))
    #	assert test.check('#Hello 你好')


class test_garbageCollect(TimedTestCase):

    def test_garbageCollect(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_garbageCollect')


class mock_traceback(object):
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def getBriefTraceback(self):
        return(self.msg)


class test_peerBeat(TimedTestCase):

    def test_peerBeat(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_peerBeat')
        queryBackground()
        updateRead()
        updateWrite()
        peerSuccess()
        fails = mock_traceback(b'wow')
        try:
            peerFailure(fails)
        except ReactorNotRunning:
            print('good')
        peerBeat()
