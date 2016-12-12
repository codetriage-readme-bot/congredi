#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
command line options
"""
import argparse
from twisted.internet import stdio, reactor, endpoints
from .peer import CongrediPeer
from .client import CongrediClient

MainOptions = argparse.ArgumentParser(add_help=False)
MainOptions.add_argument('-u', '--help', help='prints usage/help')
MainOptions.add_argument('-p', '--port', default=8800, help='congredi port')
MainOptions.add_argument('-d', '--debug', default=False, help='set debugging')

subparsers = MainOptions.add_subparsers()

ClientOptions = subparsers.add_parser("client", help="client to interact with congredi", add_help=False)
ClientOptions.add_argument('-h', '--host', default='localhost', help='Host to connect to')
ClientOptions.set_defaults(which='client')

PeerOptions = subparsers.add_parser("peer", help="run congredi peer instance", add_help=False)
PeerOptions.add_argument('-r', '--redis', default=6379, help='redis port')
PeerOptions.add_argument('-n', '--neo4j', default=7474, help='neo4j port')
PeerOptions.set_defaults(which='peer')

def run():
	args = MainOptions.parse_args()
	if args.which == 'peer':
		app = CongrediPeer(
			port=args.port, redisPort=args.redis,
			neo4jPort=args.neo4j, initialKey=None)
		endpoints.serverFromString(reactor, "tcp:{}".format(args.port)).listen(app)
		reactor.run()
		#twisted.Run(app)
	elif args.which == 'client':
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
run()