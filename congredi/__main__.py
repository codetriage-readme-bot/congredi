#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module. For whatever main is supposed to do.
"""
from __future__ import unicode_literals
#import pudb; pu.db

from configplugins import configplugin
from storage.redis import txredis
from storage.neo4j import neo4j
from auth.jwt import jwt
from .run import run

# Run with the default, real client
if __name__ == '__main__':
    Conf = configplugin()
    Conf.setRedis(txredis,"localhost",5432)
    Conf.setNeo4j(neo4j,"localhost",5432)
    Conf.setJWT(jwt)
    run(Conf)


defaultHost = socket.gethostname()
app = Klein()
key = token('onetwothree')
