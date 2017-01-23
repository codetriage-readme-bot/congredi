#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
neo4j tests
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..neo4j import assertTrustXY, queryTrustXY, dependencies

# pylint: disable=no-self-use


class test_neo4j(unittest.TestCase):

    def test_neo4j(self):
        """Connect to neo4j or use a mock? acyclic graph mock interfaces???"""
        print('IMPLEMENT storage/test/test_neo4j')
