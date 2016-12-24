#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grab starting at a hash and moving forward on the list, with an offset and object count
"""
from twisted.protocols import amp

class Future(amp.Command):
	arguments = [('type', amp.String()),
				 ('hash', amp.String()),
				 ('offset', amp.Integer()),
				 ('count', amp.Integer())]
	response = [('hashes', amp.String())] # list of strings...

"""
type : hash : [list]
foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

GET FUTURE foo ghi OFFSET 2 COUNT 2

[ mno, pqr ]

"""