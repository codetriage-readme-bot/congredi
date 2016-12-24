#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Geting a key (permissioned, recursive)
"""
from twisted.protocols import amp

class Subscribe(amp.Command):
	arguments = [('reader', amp.String()),
				 ('hash', amp.String())
				 ('signature', amp.String())
				 ('object', amp.String())
				 ('type', amp.String())
				 ]
	response = [
		('lifetime',amp.Date()),
		('signature',amp.String())]
	#errors = no space
"""
SUBSCRIBE TYPE foobar HASH hash READER reader SIGNATURE sig
[ Results[], 2016-10-11 20:10:10, signature ]
"""