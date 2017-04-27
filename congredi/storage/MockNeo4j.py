#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Neo4j Mock code

    will need to pull from Neo4j examples

"""
from __future__ import absolute_import
from __future__ import unicode_literals
from .mock import MockStorage


class Neo4jMock(MockStorage):
    arr = {}
    within = True

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(Neo4jMock, self).__init__(typeOf)

    def TrustWithin(self, key):
        return self.within
