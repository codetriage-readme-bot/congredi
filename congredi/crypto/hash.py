#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hash function (No clue why)
"""
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64
def make_hash(message):
	"""make hash, print base64, return 32 bits"""
	digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
	digest.update(message)
	result = digest.finalize()
	print('32 hash: ' + base64.urlsafe_b64encode(result))
	return result
