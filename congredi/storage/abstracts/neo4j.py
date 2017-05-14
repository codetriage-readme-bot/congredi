from abc import ABCMeta, abstractmethod
import six


class absNeo4j(six.with_metaclass(ABCMeta, object)):

    def __init__(self, host, port):
        super(absNeo4j, self).__init__()

    @classmethod
    def version(self): return "1.0"

    @abstractmethod
    def assertTrustXY(self, x, y):  # test
        raise NotImplementedError()

    @abstractmethod
    def queryTrustXY(self, x, y):  # test
        raise NotImplementedError()
