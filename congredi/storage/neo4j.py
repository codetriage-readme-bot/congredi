#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Map a directed acyclic graph from one user to another,
and map objects that people use (possibly a minimum number of people use)

    pull from Neo4j examples

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from py2neo import GraphDatabase
driver = GraphDatabase.driver('bolt://localhost')


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
# congredi/storage/neo4j.py                   13      4    69%   14-16, 20, 25
