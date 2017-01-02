from .vote import poll, vote


class stvVote(vote):

    def cast(self, vote): # test
        pass

    def validate(self, voteid): # test
        pass

    def compute(self): # test
        pass

    def certify(self): # test
        pass


class stvPoll(poll):

    def cast(self, vote): # test
        pass

    def validate(self, voteid): # test
        pass

    def compute(self): # test
        pass

    def certify(self): # test
        pass
