# a really basic example from stackoverflow...

from twisted.internet import protocol, reactor
from twisted.protocols import basic

class SomeServerProtocol(basic.LineReceiver):
    def lineReceived(self, line):
        host, port = line.split()
        port = int(port)
        factory = protocol.ClientFactory()
        factory.protocol = SomeClientProtocol
        reactor.connectTCP(host, port, factory)

class SomeClientProtocol(basic.LineReceiver):
    def connectionMade(self):
        self.sendLine("Hello!")
        self.transport.loseConnection()

def main():
    import sys
    from twisted.python import log

    log.startLogging(sys.stdout)
    factory = protocol.ServerFactory()
    factory.protocol = SomeServerProtocol
    reactor.listenTCP(12345, factory)
    reactor.run()

if __name__ == '__main__':
    main()