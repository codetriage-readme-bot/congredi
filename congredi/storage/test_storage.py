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
