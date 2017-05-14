from abc import ABCMeta, abstractmethod
import six


class absJWT(six.with_metaclass(ABCMeta, object)):

    def __init__(self, secret):
        self.password = secret

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def check(self, json):
        raise NotImplementedError()

    @abstractmethod
    def make(self, fingerprint):
        raise NotImplementedError()
