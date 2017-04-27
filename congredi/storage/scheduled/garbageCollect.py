#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Remove keys no subscribed user cares about.

    Uses orphaning test code (mostly through directed children)

    user -> trees

    user <- trees

    check every tree, if it has a user, check to see if the user cares.
    if not, delete it.

"""
from __future__ import absolute_import
from __future__ import unicode_literals
#from twisted.protocols.amp import Command, String, Integer, ListOf, Boolean, DateTime
