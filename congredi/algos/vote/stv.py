from .vote import poll, vote

class stvVote(vote):
    def cast(self, vote):
        pass
    def validate(self, voteid):
        pass
    def compute(self):
        pass
    def certify(self):
        pass
class stvPoll(poll):
    def cast(self, vote):
        pass
    def validate(self, voteid):
        pass
    def compute(self):
        pass
    def certify(self):
        pass
