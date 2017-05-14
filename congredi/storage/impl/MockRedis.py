class RedisMock(MockStorage):  # object
    arr = {}

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(RedisMock, self).__init__(typeOf)

    def read(self, key):
        return self._read(key)

    def write(self, key, value):
        return self._write(key, value)

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
