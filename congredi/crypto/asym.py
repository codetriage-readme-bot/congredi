#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging, traceback
#from cryptography.hazmat.backends.commoncrypto import backend
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# Class instances for the Asymetric crypto inside Congredi.
logger = logging.getLogger('delegito')

class eq():
	private_key = None
	public_key = None
	def __init__(self,pubkey=None,privkey=None,password=None):
		if pubkey is None:
			if privkey is None:
				# make a key
				self.private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
				self.public_key = self.private_key.public_key()
			elif password is not None:
				# recover a key
				self.private_key = serialization.load_pem_private_key(
				privkey, password=password,backend=default_backend())
		else:
			# grab someone else's key
			self.public_key = serialization.load_pem_public_key(
			pubkey, backend=default_backend())
		logger.info('Created public key')
	def encrypt(self,content,otherKey):
		shared_key = self.private_key.exchange(ec.ECDH(), otherKey)
		key = os.urandom(16)
		iv = os.urandom(16)
		encryptor = Cipher(
			algorithms.AES(key), modes.CBC(iv), default_backend).encryptor()
		ciphertext = encryptor.update(content) + encryptor.finalize()
		packet_key = shared_key.sign(key + iv)
		return ciphertext + key
	def decrypt(self,content,otherKey):
		shared_key = self.private_key.exchange(ec.ECDH(), otherKey)
		header = content[-32:]
		header = shared_key.sign(header)
		key = header[:16]
		iv = header[16:]
		decryptor = Cipher(
			algorithms.AES(key), modes.CBC(iv), default_backend).decryptor()
		ciphertext = decryptor.update(content) + decryptor.finalize()
		return ciphertext + key



	# sign a document
	def sign(self,content):
		return self.private_key.sign(content,ec.ECDSA(hashes.SHA256()))
	# verify a document
	def verify(self,content,sig):
		ver = self.public_key.verifier(sig,ec.ECDSA(hashes.SHA256()))
		ver.update(content)
		return ver.verify()
	# backup your private key
	def backup(self,password):
		return self.private_key.private_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PrivateFormat.PKCS8,
		encryption_algorithm=serialization.BestAvailableEncryption(password)
		)
	# share your public key
	def share(self):
		return self.public_key.public_bytes(
		encoding=serialization.Encoding.PEM,
		format=serialization.PublicFormat.SubjectPublicKeyInfo
		)
