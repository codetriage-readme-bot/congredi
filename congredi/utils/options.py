#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
command line options
"""
import argparse
from .config import defaultPath, defaultFile, makePath, configArr
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
# load defaults from config file (we recheck this when passed a new config...)
defaults = configArr(defaultPath)

MainOptions = argparse.ArgumentParser(add_help=False)
# no option ("--help") - (Design -h if -h is used as host.)
MainOptions.add_argument('-u', '--help', help='prints usage/help', action='store_true')

# option required after this ("--port 8000")
MainOptions.add_argument('-p', '--port', default=8800, help='congredi port', type=int)
# no option after this (bool flag "--debug")
MainOptions.add_argument(
    '-c', '--config', type=argparse.FileType('r'),
    help='config file to use', default=defaultPath+defaultFile)

# verbosity options

MainOptions.add_argument(
    '-q', '--quiet', action='store_true', help='set logging to CRITICAL (wordy-)')
MainOptions.add_argument(
    '-v', '--verbose', action='store_true', help='set logging to INFO (wordy+)')
MainOptions.add_argument(
    '-d', '--debug', action='store_true', help='set logging to DEBUG (wordy++)')

subparsers = MainOptions.add_subparsers()

ClientOptions = subparsers.add_parser(
    "client", help="client to interact with congredi", add_help=False)
ClientOptions.add_argument('-h', '--host', default='localhost',
                           help='Host to connect to')  # (see design, above)
ClientOptions.set_defaults(which='client')

PeerOptions = subparsers.add_parser(
    "peer", help="run congredi peer instance", add_help=False)
# redis port on options - int/socket
PeerOptions.add_argument('-r', '--redis', default=6379, help='redis port')
# neo4j port options - int/socket
PeerOptions.add_argument('-n', '--neo4j', default=7474, help='neo4j port')
PeerOptions.set_defaults(which='peer')
