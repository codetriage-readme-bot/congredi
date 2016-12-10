
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import protocol, reactor, endpoints, defer #, utils
from twisted.protocols import basic
#from twisted.web import client
class BogusProtocol(basic.LineReceiver):#protocol.Protocol):
	def lineReceived(self, user):
		d = self.factory.getUser(user)
		def onError(err):
			return 'errors'
		d.addErrback(onError)
		def writeResponse(message):
			self.transport.write(message+"\n")
			self.transport.loseConnection()
		d.addCallback(writeResponse)
	# def connectionMade(self):
	#	 self.transport.loseConnection()
class BogusFactory(protocol.ServerFactory):
	protocol = BogusProtocol
	def __init__(self, **starts): #prefix
		self.users = starts #self.prefix = prefix
	def getUser(self, user):
		#utils.getProcessOutput
		return defer.succeed(self.users.get(user, "Nope"))
		#return client.getPage(self.prefix+user)

BogusEndpoint = endpoints.serverFromString(reactor, "tcp:1079")
BogusEndpoint.listen(BogusFactory(bog="us"))
#def f(s):
# print(s)
#reactor.callLater(3.4, f, "hello, world")

#d = task.deferLater(reactor, 3.4, f, "hi")
#def called(result): print result
# d.addCallback(called)




reactor.run()

