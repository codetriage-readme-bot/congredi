#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
http API 

# authorization stuff
/auth/new           - check DB, get long term JWT
/live/next          - get next short term JWT from long term JWT
/live/online        - find if a peer is online

# getting/setting contents
/set/<permission[0|1]>/<typeOf>
/get/<permission[0|1]>/<typeOf>

# searching/indexing (offset is a hash value, not an integer)
/index/<typeOf>/<direction>/<offset>/<count:double>/<hashPtr>
/search/<typeOf>/<offset>/<count:double>/<term>

# neater aliases:

/d/
    /commit/<id>
    /chunk/<id>
    /vote/<id>
    /bio/<id>
    /poll/<id>
    /manifesto/<id>
/s/
    /rendesvous - rendesvous settings
    blacklist - blacklist settings
    whitelist - whitelist settings
    peer - peer listings
    admin - admin settings
    user - user settings
/r/<routername>/
    /ip
    /censor
    /uptime
    /has
    /wants
    /seen
    /proof
    /rank
/u/<username>/
    /bio
    /location
    /courier
    /vote/<voteid>
    /poll/<pollid>
    /proposal/<id>
    /save/<saveid>
/g/<groupname>/
    /manifesto
    /borders
    /members
    /votes/<voteid>
    /polls/<pollid>
    /saves


"""
from __future__ import absolute_import
from __future__ import unicode_literals
from klein import Klein
from ..auth.token import token
app = Klein()
key = token('onetwothree')


@app.route('/auth/new')
def get_auths():
    """checks auths within db and returns a long term JWT"""
    pass


@app.route('/live/next')
def next_key():
    """takes a long term JWT and return the current short term JWT"""
    pass


@app.route('/live/online')
def check_online():
    pass


@app.route('/set/<int:permission>/<typeOf>')
def set_value(permission, typeOf):
    pass


@app.route('/get/<int:permission>/<typeOf>')
def get_Value(permission, typeOf):
    pass


@app.route('/index/<typeOf>/<direction>/<offset>/<float:count>/<hashPtr>')
def tell_index(typeOf, direction, offset, count, hashPtr):
    pass


@app.route('/search/<typeOf>/<offset>/<float:count>/<term>')
def search_term(typeOf, offset, count, term):
    pass


#app.run("localhost", 8080)

"""
/api/
	/<user>/
		/trust/ - update your pgp keys
		/avatar/ - png/jpeg avatar
		/profile/ - json dict profile strings
		/<user>/ - return user dict
			/avatar/ - return user image
			/trust/ - sign their key with yours
	/search/ - return key:value from a value search
		{ type:["~"|"<"|">"|"=="], amount:int, offset: int, subset: "key", search: "string" }
		{ meta:{offset:int,amount:int}, key: base64, value: { json } }
		/peers/ - /peer/ indexes, some meta searches
		/govts/
		/votes/
		/options/
/peer/ - return idx
	/<hash>/ - current onion addresses
		/trust/ - pgp key chain
		/uptime/ - reputation
		/stake/ - stake proof blocks
/govt/ - return idx
	/<jurisdiction>/ - return active vote/user blocks (signed by jurisdiction)
		/validated/ - issues signed on by consensus (multiple winners)
		/ordered/ - distributed block (data secure)
		/unordered/ - idx proposed issues
		/denied/ - idx of issues denied entrance
		/<issueid>/ - return an issue signature
/vote/ - return idx
	/<hash>/ - genesis block
		/validated/ - idx of asserted
		/ordered/ - idx of consensus-ordered
		/unordered/ - idx of proposed blocks
		/open/ - idx of voters who have not voted
		/<blockid>/ - return a block and its contents
"""
