class PacketWrapper(object):
    def SendCommand(self,command):
        return "Hello"
    def GetCommand(self,command):
        if command == 'Hello':
            return ["How are you",False]
        else:
            return ["Well, thank you",True]
