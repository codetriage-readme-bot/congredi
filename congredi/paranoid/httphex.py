"""Example flask routes (will probably still be using twisted HTTP libs..."""
from klein import Klein
import binascii
app = Klein()
def process(req):
    return req
@app.route('/HEX', methods=['GET','POST'])
def hex_compat(request):
    req = binascii.unhexlify(request.content)
    median = process(req)
    resp = binascii.hexlify(median)
    return resp
@app.route('/auth/new')
def get_auths():
    """checks auths within db and returns a long term JWT"""
    pass
#@app.route('/live/next')
def next_key():
    """takes a long term JWT and return the current short term JWT"""
    pass
#@app.route('/live/online')
def check_online():
    pass
#@app.route('/set/<int:permission>/<typeOf>')
def set_value(permission, typeOf):
    pass
#@app.route('/get/<int:permission>/<typeOf>')
def get_value(permission, typeOf):
    pass
#@app.route('/index/<typeOf>/<direction>/<offset>/<float:count>/<hashPtr>')
def tell_index(typeOf, direction, offset, count, hashPtr):
    pass
#@app.route('/search/<typeOf>/<offset>/<float:count>/<term>')
def search_term(typeOf, offset, count, term):
    pass
