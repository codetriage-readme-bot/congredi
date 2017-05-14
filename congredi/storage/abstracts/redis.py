from abc import ABCMeta, abstractmethod
import six


class absRedis(six.with_metaclass(ABCMeta, object)):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def _write(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _read(self, keyspace):
        raise NotImplementedError()

    @abstractmethod
    def _lockWrite(self, keyspace, valuespace):
        raise NotImplementedError()

    @abstractmethod
    def _lockRead(self, keyspace):
        raise NotImplementedError()
