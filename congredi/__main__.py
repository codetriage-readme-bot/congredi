#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main module. For whatever main is supposed to do.
"""
from __future__ import unicode_literals
import socket
#import pudb; pu.db

from .startup.configplugins import configplugin
from .storage.impl.redis import RedisStore
from .storage.impl.neo4j import Neo4jStore
from .auth.jwt import token
from .startup.run import run

# Run with the default, real client
if __name__ == '__main__':
    Conf = configplugin()
    defaultHost = socket.gethostname()
    Conf.setRedis(RedisStore,"localhost",5432)
    Conf.setNeo4j(Neo4jStore,"localhost",5432)
    Conf.setJWT(token,'onetwothree')
    run(Conf)
