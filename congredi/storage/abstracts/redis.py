class abstractStorageProvider(six.with_metaclass(ABCMeta, object)):

    def __init__(self, typeOf):
        self.type = typeOf

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
