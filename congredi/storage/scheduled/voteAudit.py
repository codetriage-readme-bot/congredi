#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Periodically audit a vote
"""
# pylint: disable=unused-import
from __future__ import absolute_import
from __future__ import unicode_literals
import logging
logger = logging.getLogger('congredi')
from twisted.internet import defer
from twisted.internet import reactor

from ...storage.redis import Rget, Rset, Rdelete
from ...utils.config import configArr
from ...utils.whoops import whoops
