"""Example flask routes (will probably still be using twisted HTTP libs..."""
import binascii
from twisted.web.server import Site
from twisted.web.resource import Resource

hexdev = None
with open('scripts/hexdev.html','r') as h:
    hexdev = h.read()
def process(req):
    return req

class HexPage(Resource):
    isLeaf = True

    # todo: make this async so nothing's blocked while this is running....
    # def _delayedRender(self, request):
    #     request.write("<html><body>Sorry to keep you waiting.</body></html>")
    #     request.finish()
    # def render_GET(self, request):
    #     d = deferLater(reactor, 5, lambda: request)
    #     d.addCallback(self._delayedRender)
    #     return NOT_DONE_YET
    # pylint: disable=no-self-use
    def render_GET(self, request):
        return hexdev
    def render_POST(self, request):
        req = binascii.unhexlify(request.content.read())
        median = process(req)
        resp = binascii.hexlify(median)
        return resp

HexFactory = Site(HexPage())
