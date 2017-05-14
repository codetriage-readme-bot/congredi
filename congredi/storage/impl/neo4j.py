from twisted.internet import defer
from py2neo import GraphDatabase
from ..abstracts.neo4j import absNeo4j


class neo4jSetup():

    def __init__(self, addr, port):
        pass

connaddr = 'localhost'
connport = 6379


class Neo4jStore(absNeo4j):

    def __init__(self, host, port):  # test
        if host == None:
            self.driver = GraphDatabase.driver('bolt://localhost')
            self._conn = neo4jSetup(connaddr, connport)
        super(Neo4jStore, self).__init__(host, port)

    # actual writers
    @defer.inlineCallbacks
    def assertTrustXY(self, x, y):  # test
        # res = yield self._conn.set(keyspace, valuespace)
        # defer.returnValue(res)
        self.driver.run(
            "CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
        return True

    @defer.inlineCallbacks
    def queryTrustXY(self, x, y):  # test
        # res = yield self._conn.delete(key)
        # defer.returnValue(res)
        self.driver.run()


def dependencies(obj):  # test
    """Calculate the dependencies of an object"""
    pass
"""
Redis social graphs (would still need to implement acyclic search, best to load
into local memory instead T.B.H.).
http://nosql.mypopescu.com/post/1083079162/redis-snippet-for-storing-the-social-graph
"""
