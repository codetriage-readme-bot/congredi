# blockable pubkeys
def PrivateBlacklistChange():
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """
    pass
def PrivateBlacklistView():
    """
    I: signed request, encrypted session key
    O: encrypted blacklist, encrypted sig
    """
    pass
def PrivateWhitelistChange():
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted signed response, encrypted hash, hash
    """
    pass
def PrivateWhitelistView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
# peers
def PrivatePeersChange():
    """
    I: signed request, encrypted session key, encrypted address
    O: encrypted whitelist
    """
    pass
def PrivatePeersView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
# users/admins
def PrivateUsersChange():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
def PrivateUsersView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
def PrivateAdminsChange():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
def PrivateAdminsView():
    """
    I: signed request, encrypted session key
    O: encrypted whitelist
    """
    pass
