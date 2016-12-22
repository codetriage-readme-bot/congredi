#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Log management
"""

import logging
logger = logging.getLogger('congredi')
def setLog(level):
	"""Set log level"""
	logger.setLevel(level)
	fh = logging.StreamHandler()
	fh.setLevel(level)
	fm = logging.Formatter(
		"%(asctime)s[%(name)s:%(levelname)s]%(filename)s(%(lineno)d) %(funcName)s: %(message)s",
		#"%(levelname)s %(filename)s(%(lineno)d) %(funcName)s: %(message)s",
		"%Y-%m-%d %H:%M:%S")
	fh.setFormatter(fm)
	logger.addHandler(fh)
