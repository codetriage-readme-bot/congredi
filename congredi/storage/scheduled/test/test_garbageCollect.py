#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
garbageCollect tests

    see garbageCollect.

    Here we test:
        user-A->repo-B, repo-C(orphaned): GC should remove C, leave B
        Repo-B(orphaned): GC should remove B
        user-A->repo-B,repo-C user-D->repo-B: GC should not error on multiple parents
        

"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from ....utils.timing import TimedTestCase
# from ..garbageCollect
# twisted.internet.task.Clock


class test_garbageCollect(TimedTestCase):

    def test_garbageCollect(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_garbageCollect')
