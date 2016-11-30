#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jwt, datetime
class checker():
	secret = None
	def __init__(self,secret):
		self.secret = secret
	def check(self,token):
		try:
			payload = jwt.decode(token, secret, algorithms=['HS256'])
			return payload['pgp'], True
		except DecodeError:
			return "Invalid Token", False
		except ExpiredSignature: #ExpiredSignatureError
			return "Expired Token", False
		except:
			return "Token error", False
	def make(self,fingerprint):
		iat = datetime.datetime.utcnow()
		exp = iat + datetime.timedelta(days=1)
		payload = {
			'pgp': fingerprint,
			'iat': iat,
			'exp': exp
			}
		token = jwt.encode(payload, secret, algorithm='HS256')
		return token.decode('unicode_escape')
