from ..auth.crypto import AONTencrypt, AONTdecrypt


class PacketWrapper(object):

    def wrapRequest(self, request, serverKey):  # test
        paddedRequest = AONTencrypt(request)
        encryptedRequest = self.key.encrypt(paddedRequest, serverKey)
        return encryptedRequest

    def unwrapRequest(self, encryptedRequest):  # test
        decryptedPadding = self.key.decrypt(encryptedRequest)
        request = AONTdecrypt(decryptedPadding)
        return request

    def SendCommand(self, command):
        option = self.factory.redis.read("option")
        return "Hello {}".format(option)

    def GetCommand(self, command):
        if command == 'Hello':
            return ["How are you", False]
        option = self.factory.redis.read("option")
        return ["Well, thank you {}".format(option), True]
