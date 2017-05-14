"""
consumer item is confusing, should raise that error within
the code that consumes those abstract providers (commands/[addresses,filesystem], etc)
"""
class abstractStorageConsumer(object):

    def __init__(self, storage):
        if not isinstance(storage, abstractStorageProvider):
            raise CongrediBadInterfaceError('Bad Interface!')
        if not storage.version() == '1.0':
            raise CongrediIncompatibleVersionError('Non-compatible version!')
        self._storage = storage

    def write(self, key, value):
        self._storage._lockWrite(key, value)

    def read(self, key):
        return self._storage._lockRead(key)
# class Base(metaclass=ABCMeta):
