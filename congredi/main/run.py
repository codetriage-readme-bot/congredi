#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Running code
"""

import logging
logger = logging.getLogger('congredi')



from twisted.internet import stdio, reactor, endpoints, task
import traceback
import os
from .peer import CongrediPeer
from .client import CongrediClient
from ..storage.config import configArr
from ..tasks.peerBeat import peerBeat, peerSuccess, peerFailure
from ..storage.redis import get, set, delete
#from ..tasks import garbageCollect
from .options import MainOptions
def run():
	config = configArr()
	initialKey = config['admins']
	initialUsers = config['users']
	print('Settings contain initial key(s): {}'.format(initialKey))
	print('Settings contains the following user(s): {}'.format(initialUsers))

	#reactor.callLater(2,redis_test)

	loop = task.LoopingCall(peerBeat)
	loopDeferred = loop.start(10.0)
	loopDeferred.addCallback(peerSuccess)
	loopDeferred.addErrback(peerFailure)

	args = MainOptions.parse_args()

	level = logging.WARNING
	if args.debug:
		level = logging.INFO
	logger.setLevel(level)
	fh = logging.StreamHandler()
	fh.setLevel(level)
	fm = logging.Formatter(
		"%(asctime)s[%(name)s:%(levelname)s]%(filename)s(%(lineno)d) %(funcName)s: %(message)s",
		#"%(levelname)s %(filename)s(%(lineno)d) %(funcName)s: %(message)s",
		"%Y-%m-%d %H:%M:%S")
	fh.setFormatter(fm)
	logger.addHandler(fh)

	if args.which == 'peer':
		logger.info('options.run() peer')
		app = CongrediPeer(
			port=args.port, redisPort=args.redis,
			neo4jPort=args.neo4j, initialKey=None)
		endpoints.serverFromString(reactor, "tcp:{}".format(args.port)).listen(app)
		reactor.run()
		#twisted.Run(app)
	elif args.which == 'client':
		logger.info('options.run() client')
		app = CongrediClient(
			host=args.host, port=args.port,
			clientKey=None)
		try:
			stdio.StandardIO(CongrediClient())
			reactor.run()
		except KeyboardInterrupt:
			pass
	#elif args.which == 'api':
	# except CongrediError as e:
	# 	print("Congredi failed: {}".format(e.message))
	# finally:
	# 	app.close()
	# except:
		#MainOptions.print_help()
if __name__ == '__main__':
	run()