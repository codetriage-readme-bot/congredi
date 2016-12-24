#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adding a key (permissionless, non-recursive)
"""
from twisted.protocols import amp

class Deploy(amp.Command):
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

"""
sends: object
recieves: lifetime, signature


DEPLOY TYPE foobar HASH abc AUTHOR author OBJECT object SIGNATURE sig
[ 2016-10-11 20:10:10, signature ]
"""