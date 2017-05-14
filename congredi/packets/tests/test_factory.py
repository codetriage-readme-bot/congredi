from twisted.test.proto_helpers import StringTransport
from ...utils.timedTests import TimedTestCase
from ..factory import BareFactory, BareProto
from ...auth.crypto import default_rsa
from ...startup.configplugins import configplugin
from ...storage.impl.MockRedis import RedisMock as RedisStore
from ...storage.impl.MockNeo4j import Neo4jMock as Neo4jStore
from ...auth.jwt import token
conf = configplugin()

red = RedisStore("localhost", 5432)
neo = Neo4jStore("localhost", 5432)
tok = token('onetwothree')
conf.setRedis(red)
conf.setNeo4j(neo)
conf.setJWT(tok)


class test_client(TimedTestCase):
    host = "0.0.0.0"
    port = "8800"
    key = default_rsa()

    def setUp(self):
        self.tr = StringTransport()
        #users = ['a', 'b']
        self.factory = BareFactory(conf)
        self.protocol = BareProto(self.factory)
        self.protocol.makeConnection(self.tr)
        super(test_client, self).setUp()

    def test_client(self):
        """Will need to have the client being tested (duplicate from test_run?)"""
        self.threshold = .1
        factory = BareFactory(conf)  # , self.key)
        factory.clientConnectionFailed('ab', 'cd')
        factory.clientConnectionLost('ab', 'cd')
        factory.startedConnecting('ab')
        # key = self.key.publicKey()
        factory.buildProtocol('addr')
        #req = self.protocol.wrapRequest(b'hello', self.key)
        #unwrapped = self.protocol.unwrapRequest(req)
        # self.protocol.lineReceived(b'ab')
        # self.protocol.lineReceived(b'get')
        self.protocol.connectionMade()
