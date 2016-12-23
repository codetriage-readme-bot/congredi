#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Search from content-containing objects
"""
from twisted.protocols import amp
class Search(amp.Command):
	arguments = [('type', amp.String()),
				 ('term', amp.String()),
				 ('offset', amp.Integer()),
				 ('count', amp.Integer())]
	response = [('hashes', amp.String())] # list of strings...
