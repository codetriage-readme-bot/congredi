#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
neo4j tests
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ...utils.timing import TimedTestCase
#from ..neo4j import assertTrustXY, queryTrustXY, dependencies


class test_neo4j(TimedTestCase):

    def test_neo4j(self):
        """Connect to neo4j or use a mock? acyclic graph mock interfaces???"""
        self.threshold = .1
        print('IMPLEMENT storage/test/test_neo4j')
        print('Directed Acyclic Graph - add/delete/check-good/check-bad on graph')
