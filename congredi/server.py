#!/usr/bin/env python
# -*- coding: utf-8 -*-
from twisted.internet import protocol, reactor, endpoints, defer #, utils
from twisted.protocols import basic
from twisted.web import client
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
    #     self.transport.loseConnection()
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
#reactor.callLater(3.4,f,"hello, world")

#d = task.deferLater(reactor,3.4,f,"hi")
#def called(result): print result
# d.addCallback(called)




reactor.run()

#from twisted.application import service, strports
# application = service.Application('finger', uid=1, gid=1)
# factory = FingerFactory(moshez='Happy and well')
# strports.service("tcp:79", factory, reactor=reactor).setServiceParent(
#     service.IServiceCollection(application))



def main(reactor, host, port=8560):
    return endpoints.connectProtocol(
        endpoints.SSL()
        )
task.react(main, sys.argv[1:])

from twisted.internet import task
from twisted.internet import reactor

loopTimes = 3
failInTheEnd = False
_loopCounter = 0

def runEverySecond():
    """
    Called at ever loop interval.
    """
    global _loopCounter

    if _loopCounter < loopTimes:
        _loopCounter += 1
        print('A new second has passed.')
        return

    if failInTheEnd:
        raise Exception('Failure during loop execution.')

    # We looped enough times.
    loop.stop()
    return


def cbLoopDone(result):
    """
    Called when loop was stopped with success.
    """
    print("Loop done.")
    reactor.stop()


def ebLoopFailed(failure):
    """
    Called when loop execution failed.
    """
    print(failure.getBriefTraceback())
    reactor.stop()


loop = task.LoopingCall(runEverySecond)

# Start looping every 1 second.
loopDeferred = loop.start(1.0)

# Add callbacks for stop and failure.
loopDeferred.addCallback(cbLoopDone)
loopDeferred.addErrback(ebLoopFailed)

reactor.run()



from twisted.internet import reactor

def f():
    print("I'll never run.")

callID = reactor.callLater(5, f)
callID.cancel()
reactor.run()



import random
from twisted.internet import task

def f():
    return "Hopefully this will be called in 3 seconds or less"

def main(reactor):
    delay = random.uniform(1, 5)

    def called(result):
        print("{0} seconds later:".format(delay), result)

    d = task.deferLater(reactor, delay, f)
    d.addTimeout(3, reactor).addBoth(called)

    return d

# f() will be timed out if the random delay is greater than 3 seconds
task.react(main)

from twisted.python import usage

class UsualOptions(usage.Options):
    optFlags = [["quiet","q", None]]
class WalkerOptions(usage.Options):
    optParameters = [['module','m',None,None]]
class Options(UsualOptions):
    optFlags = [
        ["port","p","protocol port"],
        ["control","c","control port"]
        ]
    optParameters = [
        ["debug","d", False, "Debug to console"],#, int
        ]
    optSubcommands = [
        ["walk",None,WalkerOptions,"Run Walk"]
        ]
    def postOptions(self):
        if not self['port'] and not self['flag']:
            raise usage.UsageError("Lazy")


options = Options()
try:
    options.parseOptions(sys.argv)
except usage.UsageError, errortext:
    print '%s: %s' % (sys.argv[0], errortext)
    sys.exit(1)
if config.subCommand =='walk':
    doWalk(config.subOptions)
if options['port']: app.port = options['port']
app.debug = options['debug']
