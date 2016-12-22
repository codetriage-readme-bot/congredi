#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
All Or Nothing Padding (coulda just used the library's version)
"""

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64, os
def make_hash(message):
	"""make hash, print base64, return 32 bits"""
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	digest.update(message)
	result = digest.finalize()
	print('32 hash: ' + base64.urlsafe_b64encode(result))
	return result

def AONTencrypt(content, password):
	"""
	generate a key using deriviation,
	although you won't need to remember
	that password if you have all the
	content.
	"""
	key_raw = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=os.urandom(16),
		iterations=100000,
		backend=default_backend()
	).derive(password)
	key = base64.urlsafe_b64encode(key_raw)
	token = base64.urlsafe_b64decode(Fernet(key).encrypt(content))
	print("32 key: {}".format(key))
	"""
	hash the token, then xor with the 32 bit key.
	concattenate token with xor'd key.
	"""
	chard = "".join(
		[chr(ord(a) ^ ord(b)) for a, b in
			zip(make_hash(token), key_raw)])
	return token + chard
def AONTdecrypt(cyphertext):
	"""
	The last 32 bits of the cyphertext are the xor of
	the hash of the preceeding cypher, and the 32 bit key.
	pulling that together into a base64 string allows
	fernet to decrypt the content.
	"""
	key2 = base64.urlsafe_b64encode(
		"".join(
			[chr(ord(a) ^ ord(b)) for a, b in
				zip(make_hash(cyphertext[:-32]),
					cyphertext[-32:])]))
	print('32 key was: {}'.format(key2))
	return Fernet(key2).decrypt(base64.urlsafe_b64encode(cyphertext[:-32]))
# cyphertext = AONTencrypt(b"Secret Message!", b"password")
# print("cyphertext is {}".format(cyphertext))
# plaintext = AONTdecrypt(cyphertext)
# print("plaintext is: " + plaintext)
