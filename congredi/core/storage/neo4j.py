#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
functions for using neo4j
"""
from neo4j.v1 import GraphDatabase, basic_auth, ResultError
driver = GraphDatabase.driver('bolt://localhost')#"bolt://localhost:7687", auth=basic_auth("neo4j", "password"))

def get_db():
	if not hasattr(g, 'neo4j_db'):
		g.neo4j_db = driver.session()
	return g.neo4j_db
def del_db():
	if hasattr(g, 'neo4j_db'):
		g.neo4j_db.close()

def assertTrustXY(x, y):
	db = get_db()
	db.run("CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
	return True

def queryTrustXY(x, y):
	db = get_db()
	db.run()