#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Repeated tasks
"""

#import random
from twisted.internet import task
from twisted.internet import reactor

loopTimes = 3
failInTheEnd = False
_loopCounter = 0

def runEverySecond():
	"""
	Called at ever loop interval.
	"""
	#global _loopCounter

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

def f():
	print("I'll never run.")

callID = reactor.callLater(5, f)
callID.cancel()
reactor.run()




def f2():
	return "Hopefully this will be called in 3 seconds or less"

# def main(reactor):
# 	delay = random.uniform(1, 5)

# 	def called(result):
# 		print("{0} seconds later:".format(delay), result)

# 	d = task.deferLater(reactor, delay, f)
# 	d.addTimeout(3, reactor).addBoth(called)

# 	return d

# # f() will be timed out if the random delay is greater than 3 seconds
# task.react(main)
