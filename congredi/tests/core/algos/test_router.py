from ....core.algos.router import router

def test_routing():
	r = router('e')
	r.nodes = ["a", "b", "c", "d", "e", "f", "g", "1", "2", "3"]
	print('Random route to a {}'.format(r.route('a', 2)))
	print('Random route to a {}'.format(r.route('a', 5)))
	print('Random route to a {}'.format(r.route('a')))
	print('Random route to a {}'.format(r.route('a')))