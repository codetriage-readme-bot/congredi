# addresses
def AddrGet():
    """
    'what is the address of the key [x]'
    I: key
    O: string
    """
    pass
def AddrRespond():
    """
    'what is the address of the key [x]'
    I: key
    O: string
    """
    pass
def CensorPolicyGet():
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
    pass
def CensorPolicyRespond():
    """
    'what is the censor policy of the key [x]'
    I: key
    O: string
    """
    pass
# ranks
def RankGet():
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """
    pass
def RankRespond():
    """
    'what is the rank of the key [x]'
    I: key
    O: string
    """
    pass
def SeenGet():
    """
    'when was key [x] last seen'
    I: key
    O: string
    """
    pass
def SeenRespond():
    """
    'when was key [x] last seen'
    I: key
    O: string
    """
    pass
def UptimeGet():
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
    pass
def UptimeRespond():
    """
    'what is the uptime of key [x]'
    I: key
    O: string
    """
    pass
# haves/wants
def WantsGet():
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """
    pass
def WantsRespond():
    """
    'what does key [x] want'
    I: key
    O: list of hashes
    """
    pass
def HasGet():
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """
    pass
def HasRespond():
    """
    'what does key [x] have'
    I: key
    O: list of hashes
    """
    pass
def ProofGet():
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
    pass
def ProofRespond():
    """
    'prove key [x] has [hash] section[:] with [nonce]'
    I: key, hash, start, end, nonce
    O: proof
    """
    pass
# publish functions
def RendesvousGet():
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """
    pass
def RendesvousRespond():
    """
    'rendesvous of key [x]'
    I: key
    O: of, by
    """
    pass
def CourierGet():
    """
    'courier of key [x]'
    I: key
    O: of, by
    """
    pass
def CourierRespond():
    """
    'courier of key [x]'
    I: key
    O: of, by
    """
    pass
def 