from ..timing import TimedTestCase
import time
class test_timing(TimedTestCase):
    def test_example_no_warning(self):
        self.threshold = 3
        time.sleep(2)
    def test_example_warning(self):
        self.threshold = 1
        time.sleep(2)