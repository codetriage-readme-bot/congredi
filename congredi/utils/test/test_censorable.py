from ..timing import TimedTestCase
from ..censorable import random, hexify, phony, pick_range
class test_censor_harness(TimedTestCase):
    def test_random(self):
        self.threshold = .1
        sentance = phony(hexify(random()))
        type(sentance)
    def test_range(self):
        self.threshold = .1
        ranges = pick_range(10)
        type(ranges[1])
