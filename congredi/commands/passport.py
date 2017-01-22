# storage
"""
Storage applies a censor policy. If they want to avoid
that policy, they'll have to ask for an encryption permit
instead.
"""
def StoreRequest():
    pass
def StoreGrant():
    pass
"""
Encrypted storage applies an inverted sensor. It better
look like it's ben tripleSec encrypted, and we'll do it
again to keep the storage provider from indexing it.
"""
def StoreEncryptedRequest():
    pass
def StoreEncryptedGrant():
    pass

# private servers acting as publisher (permissioned or not)
"""
As a private server, a user will connect to them to find any
new content. This is where the actual data sits, if in
strict encryption mode. Otherwise, the rendesvous & courier
may be allowed to cache the request.
"""
def PublishRequest():
    pass
def PublishGrant():
    pass
def SubscribeRequest():
    pass
def SubscribeGrant():
    pass

# private servers acting as rendesvous to a server
"""
The Rendesvous (or publishing) and Courier (or subscribing)
relays are public addresses that speak on behalf of a server.
"""
def RendesvousRequest():
    pass
def RendesvousGrant():
    pass
def CourierRequest():
    pass
def CourierGrant():
    pass

# onion network / onion storage
"""
Sanctuary is an unlisted, encrypted server that
backs up, encrypted, to other servers. Safe Passage
is the permission to act as a tor-like relay
"""
def SanctuaryRequest():
    pass
def SanctuaryGrant():
    pass
def SafePassageRequest():
    pass
def SafePassageGrant():
    pass