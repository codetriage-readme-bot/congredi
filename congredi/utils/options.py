#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
command line options
"""
import argparse

"""
design i.e.:
	valid:
		congredi --port 9797 --debug peer
		congredi peer --redis 6999
	invalid:
		congredi --port --debug peer (port required)
	tested:
		python -m congredi
	unimplemented:
		congredi peer --debug (master options can't be reordered??)
		docker run congredi peer (options dependent on arg #'s?)
"""

MainOptions = argparse.ArgumentParser(add_help=False)
MainOptions.add_argument('-u', '--help', help='prints usage/help') # no option ("--help") - (Design -h if -h is used as host.)
MainOptions.add_argument('-p', '--port', default=8800, help='congredi port') # option required after this ("--port 8000")
MainOptions.add_argument('-d', '--debug', action='store_true', help='set debugging') # no option after this (bool flag "--debug")

subparsers = MainOptions.add_subparsers()

ClientOptions = subparsers.add_parser("client", help="client to interact with congredi", add_help=False)
ClientOptions.add_argument('-h', '--host', default='localhost', help='Host to connect to') # (see design, above)
ClientOptions.set_defaults(which='client')

PeerOptions = subparsers.add_parser("peer", help="run congredi peer instance", add_help=False)
PeerOptions.add_argument('-r', '--redis', default=6379, help='redis port') # redis port on options - int/socket
PeerOptions.add_argument('-n', '--neo4j', default=7474, help='neo4j port') # neo4j port options - int/socket
PeerOptions.set_defaults(which='peer')

