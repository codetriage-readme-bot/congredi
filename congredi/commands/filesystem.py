# union operation (data transfer)
def SyncHavesWantsAsk():
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
    pass
def SyncHavesWantsTell():
    """
    'I have [x,y,z], I want [x,y,z], what do you have/want'
    I: list of hashes, list of hashes
    O: list of hashes, list of hashes
    """
    pass
# store object
def StoreSet():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass
def StoreConfirm():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass
def EncryptedStoreSet():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass
def EncryptedStoreConfirm():
    """
    'store blob [blob] of type [type]'
    I: blob, type
    O: bool, ttl
    """
    pass
# get object
def StoreGet():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass
def StoreRespond():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass
def EncryptedStoreGet():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass
def EncryptedStoreRespond():
    """
    'send blob [blob] of type [type]'
    I: list of hashes, type
    O: list of blobs, ttl
    """
    pass
# seek item ([hash]->num)
def SeekGet():
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
    pass
def SeekRespond():
    """
    'seek hashes key [hash] count [number] direction [+/-]'
    I: hash, number, direction
    O: list of hashes
    """
    pass
# resolve item ([hash])
def ResolveGet():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass
def ResolveRespond():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass

# search items
def SearchRun():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass
def SearchResolve():
    """
    'resolve [hash]'
    I: hash
    O: blob
    """
    pass