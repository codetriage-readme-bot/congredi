from ...utils.timedTests import TimedTestCase
from ..router import router, onion
from ...utils.errors import NoRoute


class test_router(TimedTestCase):

    good_router = None
    bad_router = None

    def test_routing(self):
        """Route Items"""
        self.threshold = .2
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        print(('Random route to a %s' % r.route('a', 2)))
        print(('Random route to a %s' % r.route('a', 5)))
        print(('Random route to a %s' % r.route('a')))
        print(('Random route to a %s' % r.route('a')))
        self.good_router = r
        onion("key")

    def test_impossible(self):
        """Impossible Route - catches itself if an impossible route returns without NoRouteError"""
        self.threshold = .2
        r = router('e')
        r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
        try:
            r.route('q', 6)
        except NoRoute:
            print('Caught. Good. That was impossible.')
            self.bad_router = r
            return True
        raise Exception('Didnt catch')
    # test a route that loops on itself
