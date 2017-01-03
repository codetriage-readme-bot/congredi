#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Map a directed acyclic graph from one user to another,
and map objects that people use (possibly a minimum number of people use)
"""
from py2neo import GraphDatabase, basic_auth
# "bolt://localhost:7687", auth=basic_auth("neo4j", "password"))
driver = GraphDatabase.driver('bolt://localhost')


def get_db():  # test
    if not hasattr(g, 'neo4j_db'):
        g.neo4j_db = driver.session()
    return g.neo4j_db


def del_db():  # test
    if hasattr(g, 'neo4j_db'):
        g.neo4j_db.close()


def assertTrustXY(x, y):  # test
    db = get_db()
    db.run(
        "CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
    return True


def queryTrustXY(x, y):  # test
    db = get_db()
    db.run()


def dependencies(obj):  # test
    """Calculate the dependencies of an object"""
    pass
"""
Redis social graphs (would still need to implement acyclic search, best to load
into local memory instead T.B.H.).
http://nosql.mypopescu.com/post/1083079162/redis-snippet-for-storing-the-social-graph
"""
