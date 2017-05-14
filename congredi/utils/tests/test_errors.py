class test_CongrediErrors(TimedTestCase):

    def test_CongrediErrors(self):
        """Raising a CongrediError class - fail if no error"""
        self.threshold = .4
        try:
            raise CongrediError('Well then')
        except CongrediError as E:
            assert isinstance(E, CongrediError)
            return True
        assert True is False
