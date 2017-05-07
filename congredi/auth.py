#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
example of proof of work algorithm - need to redo nonce-difficulty
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography).
Proof of Work (either RAM/CPU intensive)
Possibly proof-of-storage?

Auth via signature. User claims they have a key, and they prove it by
signing a message to log into that node.

Tokens provide heartbeat functionality, and do not log the user directly
into the database. Any of the methods in "register" give the user a long-term
JWT by using these functions.
Auth via oauth. User claims to control a username, and we have them run
through oauth to prove that.
Auth via email. We ask the user to either send an email to us containing
an object, or to let us send an object to them.

Two modes: Send To Us, Send To You

The auths must be able to be tested as:

* Valid
* Expired
* Invalid


Could possibly separate this into folders:

* Twitter
* Facebook
* Google
* GitHub

Currently no expire function exists without turning over the main auth key,
and that would need to tell other gateways that the main key needs to rotate.

Maybe someone has a better way of handling short JWT-style auths?
Auth via SMS.

Sends out a pin to an SMS gateway, which needs to be confirmed via the user.

Could even encrypt with their signal key :3
"""

from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
import jwt
import datetime

import hashlib
import time
max_nonce = 2 ** 32  # 4 billion

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
        try:
            payload = jwt.decode(json, self.secret, algorithms=['HS256'])
            return payload['pgp'], True
        # something has gone wrong
        except jwt.DecodeError:  # test
            return "Invalid Token", False
        except jwt.ExpiredSignature:  # test
            return "Expired Token", False

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


@app.route('/pgp/<request>', methods=['GET'])
def jwt_get(request):  # test
    pgpkey = request
    return gate.make(pgpkey)


@app.route('/api/<tokn>', methods=['GET'])
def jwt_use(tokn):  # test
    response, checks = gate.check(tokn)
    print(checks)
    # if checks: return func(response) # response is pgp fingerprint
    # else:
    return response  # response is token error


def proof_of_work(header, difficulty_bits_in):
    target = 2 ** (256 - difficulty_bits_in)
    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header) + str(nonce)).hexdigest()
        if long(hash_result, 16) < target:
            print("Success with nonce %d" % nonce)
            print("Hash is %s" % hash_result)
            return (hash_result, nonce)
    # pylint: disable=undefined-loop-variable
    print("Failed after %d (max_nonce) tries" % nonce)
    return nonce
    # pylint: enable=undefined-loop-variable
if __name__ == '__main__':

    resnonce = 0
    reshash_result = ''
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print("")
        print("Difficulty: %ld (%d bits)" % (difficulty, difficulty_bits))
        print("Starting search...")
        start_time = time.time()
        new_block = 'test block with transactions' + reshash_result

        (reshash_result, resnonce) = proof_of_work(new_block, difficulty_bits)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Elapsed time: %.4f seconds" % elapsed_time)
        if elapsed_time > 0:
            hash_power = float(long(resnonce) / elapsed_time)
            print("Hashing power: %ld hashes per second" % hash_power)
