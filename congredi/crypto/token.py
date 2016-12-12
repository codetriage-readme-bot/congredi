#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jwt, datetime
from jwt.exceptions import DecodeError, ExpiredSignature
# class object JWT implementation
class token():
	secret = None
	def __init__(self, secret):
		self.secret = secret
	def check(self, json):
		# pylint: disable=bare-except
		try:
			payload = jwt.decode(json, self.secret, algorithms=['HS256'])
			return payload['pgp'], True
		# something has gone wrong
		except DecodeError: return "Invalid Token", False
		except ExpiredSignature: return "Expired Token", False
		except: return "Token error", False
	def make(self, fingerprint):
		iat = datetime.datetime.utcnow()
		exp = iat + datetime.timedelta(days=1)
		payload = {
				'pgp': fingerprint,
				'iat': iat,
				'exp': exp
				}
		json = jwt.encode(payload, self.secret, algorithm='HS256')
		return json.decode('unicode_escape')
# simple use of this with Flask
from flask import Flask
gate = token('password')
app = Flask('Delegito')
@app.route('/', methods=['GET'])
def jwt_get():
	pgpkey = request.get_json()['pubkey']
	return gate.make(fingerprint)
@app.route('/api', methods['GET'])
def jwt_use():
	token = request.get_json()['token']
	response, checks = gate.check(token)
	if checks: return func(response) # response is pgp fingerprint
	else: return response # response is token error
