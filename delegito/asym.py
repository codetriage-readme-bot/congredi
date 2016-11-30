from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

class eq():
    private_key = None
    public_key = None
    def __init__(self,pubkey=None,privkey=None,password=None):
        if pubkey is None:
            if privkey is None:
                # make a key
                self.private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
                self.public_key = self.pr.public_key()
            elif password is not None:
                # recover a key
                self.private_key = serialization.load_pem_private_key(
                privkey, password=password,backend=default_backend())
        else:
            # grab someone else's key
            self.public_key = serialization.load_pem_public_key(
            pubkey, backend=default_backend())
    # sign a document
    def sign(self,bytes):
        return self.private_key.sign(bytes,ec.ECDSA(hashes.SHA256()))
    # verify a document
    def verify(self,bytes,sig):
        ver = self.public_key.verifier(sig,ec.ECDSA(hashes.SHA256()))
        ver.update(bytes)
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

        

