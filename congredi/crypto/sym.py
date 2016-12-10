#!/usr/bin/env python
# -*- coding: utf-8 -*-
#https://cryptography.io/en/latest/fernet/
from cryptography.fernet import Fernet

# Class instances for the Symetric crypto inside Congredi.
class fc():
	secret = None
	lock = None
	def __init__(self,secret=None):
		if secret not None:
			self.lock = Fernet(secret)
		else:
			self.secret = Fernet.generate_key()
			self.lock = Fernet(self.secret)
	def encrypt(self,bytes):
		return self.lock.encrypt(bytes)
	def decrypt(self,bytes):
		return self.lock.decrypt(bytes)
	def disclose(self):
		return self.secret
