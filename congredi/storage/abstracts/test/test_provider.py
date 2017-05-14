from ....utils.timedTests import TimedTestCase
from ....utils.errors import BadIFace, BadVersion
from ..redis import absRedis


class good_provider(absRedis):

    def write(self, keyspace, valuespace):
        return self._write(keyspace, valuespace)
    def read(self, keyspace):
        return self._read(keyspace)
    def _write(self, keyspace, valuespace):
        return b'ok'

    def _read(self, keyspace):
        return b'value'

    def _lockWrite(self, keyspace, valuespace):
        return b'ok'

    def _lockRead(self, keyspace):
        return b'value'


class consumer():

    def __init__(self, driver):
        if not isinstance(driver, absRedis):
            raise BadIFace('Bad Interface!')
        self.driver = driver
    def write(self, keyspace, valuespace):
        return self.driver.write(keyspace, valuespace)
    def read(self, keyspace):
        return self.driver.read(keyspace)
    def _write(self, keyspace, valuespace):
        return self.driver._write(keyspace, valuespace)
    def _read(self, keyspace):
        return self.driver._read(keyspace)
    def _lockWrite(self, keyspace, valuespace):
        return self.driver._lockWrite(keyspace, valuespace)

    def _lockRead(self, keyspace):
        return self.driver._lockRead(keyspace)


class test_interface(TimedTestCase):

    def test_not_implemented(self):
        self.threshold = .1
        # pylint: disable=abstract-method

        class bad_provider(absRedis):
            pass
        # pylint: enable=abstract-method
        # pylint: disable=abstract-class-instantiated,no-value-for-parameter,
        # arguments-differ
        try:
            a = bad_provider()
            a.write(b'one')
            self.fail()
        except (BadIFace, TypeError):
            pass
        # pylint: enable=abstract-class-instantiated,no-value-for-parameter

    def test_client_okay(self):
        self.threshold = .1
        provider1 = good_provider('a',1)
        client = consumer(provider1)
        client.write(b'b', b'b')
        client.read(b'b')

    def test_client_mad(self):
        self.threshold = .1
        b = good_provider('a',1)
        # pylint: disable=unused-variable

        def funk():
            return "2.0"

        def version():
            return "funk"
        try:
            client = consumer(b)
            client.write(b'b', b'b')
            print('bad')
        except BadVersion:
            print('good')
        c = object()
        try:
            client = consumer(c)
            client.write(b'b', b'b')
            print('bad')
        except BadIFace:
            print('good')
