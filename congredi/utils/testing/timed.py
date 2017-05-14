class TimedTestCase(unittest.TestCase):
    threshold = 0
    def setUp(self):
        #print('ran setup for %s' % self.id())
        self.threshold = .5
        self._time_started = time.time()

    def tearDown(self):
        elapsed = time.time() - self._time_started
        if elapsed > self.threshold:
            print((warning % (elapsed, self.threshold)))
