from twisted.internet.protocol import ClientFactory, Protocol
from twisted.internet import reactor
from .packetwrapper import PacketWrapper
class BareProto(Protocol, PacketWrapper):
    def __init__(self, factory):
        self.factory = factory
        self._peer = None
        # factory holds the connections to things?
    def connectionMade(self):
        # add client to listings
        self.transport.write(self.SendCommand('Hello'))
        self._peer = self.transport.getPeer()
        self.factory.clients.append(self)
    def connectionLost(self, reason):
        # Reduce privledge if bad client - ._peer
        if self in self.factory.clients:
            self.factory.clients.remove(self)
        self.protocol.connectionLost(reason)
    def dataReceived(self, data):
        print("Recieved data from {}: {}".format(self._peer, data))
        resp, disconnect = self.GetCommand(data)
        print("Responding with: {}".format(resp))
        self.transport.write(resp)
        if disconnect:
            self.factory.disconnect(self)
    def sendToAll(self, data):
        for c in self.factory.clients:
            print("Send to: {}".format(c._peer))
            c.transport.write(data)
class BareFactory(ClientFactory):
    clients = []
    def __init__(self,GivenConfig):
        self.redis = GivenConfig.redis
        self.neo4j = GivenConfig.neo4j
        self.jwt = GivenConfig.JWT
    def buildProtocol(self, addr):
        return BareProto(self)
    def startedConnecting(self, connector):
        pass
        # add trying to self
    # pylint: disable=no-self-use
    def disconnect(self, client):
        client.transport.loseConnection()
    def poweroff(self):
        reactor.stop()
    # pylint: enable=no-self-use
    def clientConnectionFailed(self, connector, reason):
        pass
        # check if bad connection
    def clientConnectionLost(self, connector, reason):
        pass
        # check if bad connection
