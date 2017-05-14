class good_provider(abstractStorageProvider):

    def _write(self, keyspace, valuespace):
        return b'ok'

    def _read(self, keyspace):
        return b'value'

    def _lockWrite(self, keyspace, valuespace):
        return b'ok'

    def _lockRead(self, keyspace):
        return b'value'


class test_interface(TimedTestCase):

    def test_not_implemented(self):
        self.threshold = .1
        # pylint: disable=abstract-method

        class bad_provider(abstractStorageProvider):
            pass
        # pylint: enable=abstract-method
        # pylint: disable=abstract-class-instantiated,no-value-for-parameter,
        # arguments-differ
        try:
            a = bad_provider()
            a.write(b'one')
            self.fail()
        except (CongrediBadInterfaceError, TypeError):
            pass
        # pylint: enable=abstract-class-instantiated,no-value-for-parameter

    def test_client_okay(self):
        self.threshold = .1
        provider1 = good_provider('a')
        client = abstractStorageConsumer(provider1)
        client.write(b'b', b'b')
        client.read(b'b')

    def test_client_mad(self):
        self.threshold = .1
        b = good_provider('a')
        # pylint: disable=unused-variable
        def funk():
            return "2.0"
        def version():
            return "funk"
        try:
            client = abstractStorageConsumer(b)
            client.write(b'b', b'b')
            print('bad')
        except CongrediIncompatibleVersionError:
            print('good')
        c = object()
        try:
            client = abstractStorageConsumer(c)
            client.write(b'b', b'b')
            print('bad')
        except CongrediBadInterfaceError:
            print('good')
