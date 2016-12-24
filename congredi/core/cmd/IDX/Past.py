#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Grab starting at a hash and moving backwards, with an offset and object count
"""
from twisted.protocols import amp

class Past(amp.Command):
	arguments = [('type', amp.String()),
				 ('hash', amp.String()),
				 ('offset', amp.Integer()),
				 ('count', amp.Integer())]
	response = [('hashes', amp.String())] # list of strings...

"""
type : hash : [list]
foos : bar : [ abc, def, ghi, jkl, mno, pqr, stu, vwx, yz ]

GET PAST foo stu OFFSET 1 COUNT 3

[ mno, jkl, ghi ]

"""