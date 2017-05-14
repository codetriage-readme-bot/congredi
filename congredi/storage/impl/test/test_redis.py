from ....utils.timedTests import TimedTestCase
from ..redis import RedisStore
from ..MockRedis import RedisMock


class test_redis(TimedTestCase):

    def setUp(self):
        self.conn = RedisMock(b'redis v1',1345)
        self.RedisStore = RedisStore(b'redis 1', 1234)
        super(test_redis, self).setUp()

    def test_redis(self):
        """
            Init a redis connection or use a mock?
            Actual Redis code is using RSet/RGet, need to call that
            instead of the Mock.
        """
        self.threshold = .1
        print('IMPLEMENT storage/test/test_redis')
        print(self.RedisStore._write(b'a', b'b'))
        print(self.RedisStore._read(b'a'))
        print(self.RedisStore._del(b'a'))
        #assert b'b' == self.RedisStore._read(b'a')
