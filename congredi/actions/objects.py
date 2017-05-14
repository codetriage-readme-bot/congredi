class EncBool(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Addresses (IP/Tor/DNS) : len? Type?


class ObjAddress(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncAddress(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Public Keys : len?


class ObjPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString


class EncPubKey(Argument):

    def toString(self, inPubKey):
        return inPubKey

    def fromString(self, inPubKeyString):
        return inPubKeyString
# Hashes : len?


class ObjHash(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncHash(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Sigs of Hashes : len?


class ObjSig(Argument):

    def toString(self, inHash):
        return inHash

    def fromString(self, inHashString):
        return inHashString


class EncSig(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# Blobs (general, compressed?)


class ObjBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob


class EncBlob(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
# RSA encrypted session key : len?


class PrivAES(Argument):

    def toString(self, inBlob):
        return inBlob

    def fromString(self, inBlob):
        return inBlob
