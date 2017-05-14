def assertTrustXY(x, y):  # test
    driver.run(
        "CREATE (a:Person {fingerprint:'{fprint}', trust:'{keys}'})", fprint=x, keys=y)
    return True


def queryTrustXY(x, y):  # test
    driver.run()


def dependencies(obj):  # test
    """Calculate the dependencies of an object"""
    pass
"""
Redis social graphs (would still need to implement acyclic search, best to load
into local memory instead T.B.H.).
http://nosql.mypopescu.com/post/1083079162/redis-snippet-for-storing-the-social-graph
"""
