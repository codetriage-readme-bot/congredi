from twisted.internet import defer
from ..abstracts.neo4j import absNeo4j
class Neo4jMock(absNeo4j):
    arr = {}
    within = True

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(Neo4jMock, self).__init__(typeOf)

    def TrustWithin(self, key):
        return self.within
    # actual writers
    @defer.inlineCallbacks
    def assertTrustXY(self, x, y):  # test
        #res = yield self._conn.set(keyspace, )
        # self.driver.run(
        #     "CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
        #return True
        res = True
        defer.returnValue(res)
    @defer.inlineCallbacks
    def queryTrustXY(self, x, y):  # test
        #res = yield self._conn.delete(key)
        res = True
        defer.returnValue(res)
        #self.driver.run()
