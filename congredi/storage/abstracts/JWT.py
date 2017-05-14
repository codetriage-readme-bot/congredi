from abc import ABCMeta, abstractmethod
import six

class absJWT(six.with_metaclass(ABCMeta, object)):

    def __init__(self, typeOf):
        self.type = typeOf

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def trust(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def check(self, keyspace):
        raise NotImplementedError()
