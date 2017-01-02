#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
neo4j tests
"""
import unittest
from ..neo4j import get_db, del_db, assertTrustXY, queryTrustXY, dependencies


class test_neo4j(unittest.TestCase):

    def test_neo4j(self):
        print('IMPLEMENT storage/test/test_neo4j')
