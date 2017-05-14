class MockStorage(abstractStorageProvider):

    def __init__(self, typeOf):
        self.type = typeOf
        super(MockStorage, self).__init__(typeOf)

    @classmethod
    def version(self): return "1.0"

    def _read(self, keyspace):
        return self.get(keyspace)

    def _write(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)

    def _lockRead(self, keyspace):
        return self.get(keyspace)

    def _lockWrite(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)
