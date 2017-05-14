class Neo4jMock(MockStorage):
    arr = {}
    within = True

    def __init__(self, typeOf):
        # pylint: disable=useless-super-delegation
        super(Neo4jMock, self).__init__(typeOf)

    def TrustWithin(self, key):
        return self.within
