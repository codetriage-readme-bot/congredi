#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography)
"""
import jwt, datetime
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
		except jwt.DecodeError: return "Invalid Token", False
		except jwt.ExpiredSignature: return "Expired Token", False
		except: return "Token error", False

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
# simple use of this with Flask
from flask import Flask, request
gate = token('password')
app = Flask('Delegito')
@app.route('/', methods=['GET'])
def jwt_get():
	pgpkey = request.get_json()['pubkey']
	return gate.make(pgpkey)
@app.route('/api', methods=['GET'])
def jwt_use():
	this_token = request.get_json()['token']
	response, checks = gate.check(this_token)
	print(checks)
	#if checks: return func(response) # response is pgp fingerprint
	#else:
	return response # response is token error
