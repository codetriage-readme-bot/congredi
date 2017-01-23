#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test router. These functions probably need relocating.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import unittest
from ..router import router, CongrediNoRouteError

# pylint: disable=no-self-use


class test_router(unittest.TestCase):

    def test_routing(self):
        """Route Items"""
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        print(('Random route to a %s' % r.route('a', 2)))
        print(('Random route to a %s' % r.route('a', 5)))
        print(('Random route to a %s' % r.route('a')))
        print(('Random route to a %s' % r.route('a')))

    def test_impossible(self):
        """Impossible Route"""
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        try:
            r.route('q', 6)
        except CongrediNoRouteError:
            print('Caught. Good. That was impossible.')
            return True
        raise Exception('Didnt catch')
    # test a route that loops on itself
