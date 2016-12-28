from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
# a default kdf
def default_kdf(password):
	key_raw = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=os.urandom(16),
		iterations=100000,
		backend=default_backend()
	).derive(password)
	return key_raw
