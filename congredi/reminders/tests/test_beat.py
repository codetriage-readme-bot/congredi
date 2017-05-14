class mock_traceback(object):
    msg = None

    def __init__(self, msg):
        self.msg = msg

    def getBriefTraceback(self):
        return(self.msg)


class test_peerBeat(TimedTestCase):

    def test_peerBeat(self):
        self.threshold = .1
        print('IMPLEMENT tests/test_peerBeat')
        queryBackground()
        updateRead()
        updateWrite()
        peerSuccess()
        fails = mock_traceback(b'wow')
        try:
            peerFailure(fails)
        except ReactorNotRunning:
            print('good')
        peerBeat()
