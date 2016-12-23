#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adding a key (permissioned, recursive)
"""
from twisted.protocols import amp

class Publish(amp.Command):
	arguments = [('author', amp.String()),
				 ('hash', amp.String()),
				 ('signature', amp.String()),
				 ('object', amp.String()),
				 ('type', amp.String())
				 ]
	response = [
		('lifetime',amp.Date()),
		('signature',amp.String())]
	#errors = no space
