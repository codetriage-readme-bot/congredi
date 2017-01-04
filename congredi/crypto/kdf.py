# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.backends import default_backend
from Crypto.Protocol.KDF import PBKDF2
import os

# random password:


def random_password():
    key = os.urandom(16)
    return default_kdf(key)

# a default kdf


def default_kdf(password):
    key_raw = PBKDF2(
        password,
        salt=os.urandom(16),
        dkLen=32,  # 16,
        count=100000  # , #1000
        # prf=None
    )
    # key_raw = PBKDF2HMAC(
    #     algorithm=hashes.SHA256(),
    return key_raw