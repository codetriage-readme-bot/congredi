#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography).


Tokens provide heartbeat functionality, and do not log the user directly
into the database. Any of the methods in "register" give the user a long-term
JWT by using these functions.
"""
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import jwt
import datetime
# class object JWT implementation


class token():
    """Simple JWT implementation"""
    secret = None

    def __init__(self, secret):
        """
        Passphrase must be stored in server somewhere to recreate this
        object (it's possibly okay to use the redis database, which may
        be in common between multiple nodes)
        """
        self.secret = secret

    def check(self, json):
        """Checking a JWT against passphrase and expiry"""
        # pylint: disable=bare-except
        try:
            payload = jwt.decode(json, self.secret, algorithms=['HS256'])
            return payload['pgp'], True
        # something has gone wrong
        except jwt.DecodeError:  # test
            return "Invalid Token", False
        except jwt.ExpiredSignature:  # test
            return "Expired Token", False
        except:  # test
            return "Token error", False

    def make(self, fingerprint):
        """Create a JWT based on UTC time"""
        iat = datetime.datetime.utcnow()
        exp = iat + datetime.timedelta(days=1)
        payload = {
            'pgp': fingerprint,
            'iat': iat,
            'exp': exp
        }
        json = jwt.encode(payload, self.secret, algorithm='HS256')
        return json.decode('unicode_escape')

"""Example flask routes (will probably still be using twisted HTTP libs..."""
from klein import Klein
app = Klein()
gate = token('password')


@app.route('/', methods=['GET'])
def jwt_get():  # test
    request = 'two'
    pgpkey = request
    return gate.make(pgpkey)


@app.route('/api', methods=['GET'])
def jwt_use():  # test
    request = 'abcd'
    this_token = request
    response, checks = gate.check(this_token)
    print(checks)
    # if checks: return func(response) # response is pgp fingerprint
    # else:
    return response  # response is token error
