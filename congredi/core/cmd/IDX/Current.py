#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grab from the latest of the list, with an offset and object count
"""
from twisted.protocols import amp

class Current(amp.Command):
	arguments = [('type', amp.String()),
				 ('hash', amp.String()),
				 ('offset', amp.Integer()),
				 ('count', amp.Integer())]
	response = [('hashes', amp.String())] # list of strings...
