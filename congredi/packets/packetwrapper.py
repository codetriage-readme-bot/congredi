class PacketWrapper(object):
    def SendCommand(self,command):
        option = self.redis.read("option",command)
        return "Hello {}".format(option)
    def GetCommand(self,command):
        if command == 'Hello':
            return ["How are you",False]
        option = self.redis.read("option",command)
        return ["Well, thank you {}".format(option),True]
