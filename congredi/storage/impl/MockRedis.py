from twisted.internet import defer
from ..abstracts.redis import absRedis
class RedisMock(absRedis):  # object
    arr = {}
    def __init__(self, typeOf):
        self.type = typeOf
        # pylint: disable=useless-super-delegation
        super(RedisMock, self).__init__(typeOf)

    @classmethod
    def version(self): return "1.0"

    @defer.inlineCallbacks
    def _read(self, keyspace):  # test
        res = yield self._conn.get(keyspace)
        res = yield self.get(keyspace)
        defer.returnValue(res)
    # delete

    # actual writers
    @defer.inlineCallbacks
    def _write(self, keyspace, valuespace):
        # return self.set(keyspace, valuespace)
        res = yield self._conn.set(keyspace, valuespace)
        defer.returnValue(res)

    def _lockRead(self, keyspace):
        return self.get(keyspace)#self._read(keyspace)

    def _lockWrite(self, keyspace, valuespace):
        return self.set(keyspace, valuespace)#self._write(keyspace, valuespace)


    def read(self, key): #lockwrite?
        return self._read(key)

    @defer.inlineCallbacks
    def write(self, key, value): #lockread?
        res = yield self._write(key, value)
        defer.returnValue(res)

    def rdel(self, key):
        self.arr.remove(key)
        return b'OK'

    def set(self, key, value):
        self.arr[key] = value
        return b'OK'

    def get(self, key):
        try:
            return self.arr[key]
        except KeyError:
            return []


    def _del(self, key):
        res = yield self._conn.delete(key)
        defer.returnValue(res)
