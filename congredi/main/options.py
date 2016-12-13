#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
command line options
"""
import argparse

MainOptions = argparse.ArgumentParser(add_help=False)
MainOptions.add_argument('-u', '--help', help='prints usage/help')
MainOptions.add_argument('-p', '--port', default=8800, help='congredi port')
MainOptions.add_argument('-d', '--debug', action='store_true', help='set debugging')

subparsers = MainOptions.add_subparsers()

ClientOptions = subparsers.add_parser("client", help="client to interact with congredi", add_help=False)
ClientOptions.add_argument('-h', '--host', default='localhost', help='Host to connect to')
ClientOptions.set_defaults(which='client')

PeerOptions = subparsers.add_parser("peer", help="run congredi peer instance", add_help=False)
PeerOptions.add_argument('-r', '--redis', default=6379, help='redis port')
PeerOptions.add_argument('-n', '--neo4j', default=7474, help='neo4j port')
PeerOptions.set_defaults(which='peer')

