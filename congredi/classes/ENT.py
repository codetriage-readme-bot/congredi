#!/usr/bin/env python

"""
Attack mitigation by design of the protocol

"""

class User():
    email = "" # reset location (could be bitmessage)
    pubkey = "" # signing identity
    onion = "" # api endpoint (challenge)
    def __init__(self, email, pubkey, onion):
        self.email = email
        self.pubkey = pubkey
        self.onion = onion
        data = {'email':email,'pubkey':pubkey,'onion':onion}
        db_insert.apply_async(['users',data])
    def poll(jurisdiction,declared):
        pgp_verify(declared,self.pubkey)
        jurisdiction.has(poll) # ugh...
        data = {'pubkey':pubkey,'declared':declared}
        db_insert.apply_async(['votes',data])
    def vote(jurisdiction, chain, privvote):
        pass
class Jurisdiction():
    def __init__(self):
        pass
