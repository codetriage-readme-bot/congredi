#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
#from cryptography.hazmat.backends.commoncrypto import backend
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
#import pyelliptic3
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
#from pyecc import ECC
# Class instances for the Asymetric crypto inside Congredi.
logger = logging.getLogger('congredi')


# whole file needs rebuilding and testing.


class curve():
    private_key = None
    public_key = None
    '''AES Cipher Specifics'''
    blockSize = 16  # Block Size
    keySize = 32  # keySize in Bytes - 32 bytes = 256bit Encryption
    mode = AES.MODE_CBC  # Cipher Block Mode

    def __generateAESKeystring__(self):
        '''Generates Pseudo Random AES Key and Base64 Encodes Key - Returns AES Key'''
        key = os.urandom(self.keySize)
        keyString = base64.urlsafe_b64encode(str(key))
        return keyString

    def __extractAESKey__(self, keyString):
        '''Extracts Key from Base64 Encoding'''
        key = base64.urlsafe_b64decode(keyString)
        if len(key) != self.keySize:
            raise Exception('Error: Key Invalid')
            os._exit(1)
        return key

    def __extractCrypto__(self, encryptedContent):
        '''Decodes Base64 Encoded Crypto'''
        cipherText = base64.urlsafe_b64decode(encryptedContent)
        return cipherText

    def __extractCrypto__(self, encryptedContent):
        '''Decodes Base64 Encoded Crypto'''
        cipherText = base64.urlsafe_b64decode(encryptedContent)
        return cipherText

    def __encodeCrypto__(self, encryptedContent):
        '''Encodes Crypto with Base64'''
        encodedCrypto = base64.urlsafe_b64encode(str(encryptedContent))
        return encodedCrypto

    def __encodeCrypto__(self, encryptedContent):
        '''Encodes Crypto with Base64'''
        encodedCrypto = base64.urlsafe_b64encode(str(encryptedContent))
        return encodedCrypto

    def certifykey(keyid):
        someones_pubkey |= mykey.certify(someones_pubkey)
        cert = mykey.certify(someones_pubkey.userids[
                             0], level=SignatureType.Persona_Cert)
        someones_pubkey.userids[0] |= cert
        for uid in someones_pubkey.userids:
            uid |= mykey.certify(uid)
        return signedkey

    def armouritem(keyid=None, message=None):
        #keybytes = key.__bytes__()
        keybytes = bytes(key)
        keystr = str(key)
        msgbytes = bytes(message)
        msgstr = str(message)
        msgbytes = message.__bytes__()

    def __init__(self, pubkey=None, privkey=None, password=None):
        """
        if pubkey is None:
            if privkey is None:
                # make a key
                self.private_key = ec.generate_private_key(
                    ec.SECP384R1(), default_backend())
                self.public_key = self.private_key.public_key()
            elif password is not None:
                # recover a key
                self.private_key = serialization.load_pem_private_key(
                    privkey, password=password, backend=default_backend())
        else:
            # grab someone else's key
            self.public_key = serialization.load_pem_public_key(
                pubkey, backend=default_backend())
        logger.info('Created public key')
        kr = pgpy.PGPKeyring(
            glob.glob(os.path.expanduser('~/.gnupg/*ring.gpg')))
        kr = pgpy.PGPKeyring()
        loaded = kr.load(glob.glob(os.path.expanduser('~/.gnupg/*ring.gpg')))
        key.protect("C0rrectPassphr@se",
                    SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
        with enc_key.unlock("C0rrectPassphr@se"):
            pass
        """

    def eccGenerate(self):
        '''Generates Elliptic Curve Public/Private Keys'''
        ecc = ECC.generate()
        publicKey = ecc._public
        privateKey = ecc._private
        curve = ecc._curve
        return privateKey, publicKey, curve

    def genkey(comment=None):
        key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
        uid = pgpy.PGPUID.new('Nikola Tesla')  # comment and email are optional
        key.add_uid(uid, usage={KeyFlags.Sign}, hashes=[HashAlgorithm.SHA512, HashAlgorithm.SHA256],
                    ciphers=[SymmetricKeyAlgorithm.AES256,
                             SymmetricKeyAlgorithm.Camellia256],
                    compression=[CompressionAlgorithm.BZ2,
                                 CompressionAlgorithm.Uncompressed],
                    key_expires=timedelta(days=365))
        subkey = pgpy.PGPKey.new(PubKeyAlgorithm.RSA, 4096)
        key.add_subkey(subkey, usage={KeyFlags.Authentication})
        empty_key = pgpy.PGPKey()
        empty_key.parse(keyblob)
        key, _ = pgpy.PGPKey.from_file('path/to/key.asc')
        key, _ = pgpy.PGPKey.from_blob(keyblob)
        key = pgpy.PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
        uid = pgpy.PGPUID.new(
            'Abraham Lincoln', comment='Honest Abe', email='abraham.lincoln@whitehouse.gov')
        key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications, KeyFlags.EncryptStorage},
                    hashes=[HashAlgorithm.SHA256, HashAlgorithm.SHA384,
                            HashAlgorithm.SHA512, HashAlgorithm.SHA224],
                    ciphers=[SymmetricKeyAlgorithm.AES256,
                             SymmetricKeyAlgorithm.AES192, SymmetricKeyAlgorithm.AES128],
                    compression=[CompressionAlgorithm.ZLIB, CompressionAlgorithm.BZ2, CompressionAlgorithm.ZIP, CompressionAlgorithm.Uncompressed])
        return genkey

    def encrypt(self, content, otherKey):
        shared_key = self.private_key.exchange(ec.ECDH(), otherKey)
        key = os.urandom(16)
        iv = os.urandom(16)
        encryptor = Cipher(
            algorithms.AES(key), modes.CBC(iv), default_backend).encryptor()
        ciphertext = encryptor.update(content) + encryptor.finalize()
        packet_key = shared_key.sign(key + iv)
        return ciphertext + packet_key

    def aesEncrypt(self, data):
        '''Encrypts Data w/ pseudo randomly generated key and base64 encodes cipher - Returns Encrypted Content and AES Key'''
        key = self.__generateAESKeystring__()
        encryptionKey = self.__extractAESKey__(key)
        pad = self.blockSize - len(data) % self.blockSize
        data = data + pad * chr(pad)
        iv = os.urandom(self.blockSize)
        cipherText = AES.new(encryptionKey, self.mode, iv).encrypt(data)
        encryptedContent = iv + cipherText
        encryptedContent = self.__encodeCrypto__(encryptedContent)
        return encryptedContent, key

    def eccEncrypt(self, publicKey, curve, data):
        '''Encrypts Data with ECC using public key'''
        ecc = ECC(1, public=publicKey, private='', curve=curve)
        encrypted = ecc.encrypt(data)
        return encrypted

    def genmessage(keyid, message):
        _message = pgpy.PGPMessage.new("This is a brand spankin' new message!")
        file_message = pgpy.PGPMessage.new("path/to/a/file", file=True)
        ct_message = pgpy.PGPMessage.new("This is a shiny new cleartext document. Hooray!",
                                         cleartext=True)
        message_from_file = pgpy.PGPMessage.from_file("path/to/a/message")
        message_from_blob = pgpy.PGPMessage.from_blob(msg_blob)
        encrypted_message = rsa_pub.encrypt(message)
        cipher = pgpy.constants.SymmetricKeyAlgorithm.AES256
        sessionkey = cipher.gen_key()
        enc_msg = pubkey1.encrypt(
            message, cipher=cipher, sessionkey=sessionkey)
        enc_msg = pubkey2.encrypt(
            enc_msg, cipher=cipher, sessionkey=sessionkey)
        del sessionkey
        enc_message = message.encrypt("S00per_Sekr3t")
        dec_message = enc_message.decrypt("S00per_Sekr3t")
        pgpstr = str(pgpobj)
        pgpbytes = bytes(pgpobj)
        pgpbytes = pgpobj.__bytes__()

    def decrypt(self, content, otherKey):
        shared_key = self.private_key.exchange(ec.ECDH(), otherKey)
        header = content[-32:]
        header = shared_key.sign(header)
        key = header[:16]
        iv = header[16:]
        decryptor = Cipher(
            algorithms.AES(key), modes.CBC(iv), default_backend).decryptor()
        ciphertext = decryptor.update(content) + decryptor.finalize()
        return ciphertext + key

    def aesDecrypt(self, key, data):
        '''Decrypts AES(base64 encoded) Crypto - Returns Decrypted Data'''
        decryptionKey = self.__extractAESKey__(key)
        encryptedContent = self.__extractCrypto__(data)
        iv = encryptedContent[:self.blockSize]
        cipherText = encryptedContent[self.blockSize:]
        plainTextwithpad = AES.new(
            decryptionKey, self.mode, iv).decrypt(cipherText)
        pad = ord(plainTextwithpad[-1])
        plainText = plainTextwithpad[:-pad]
        return plainText

    def eccDecrypt(self, privateKey, curve, data):
        '''Decrypts Data with ECC private key'''
        ecc = ECC(1, public='', private=privateKey, curve=curve)
        decrypted = ecc.decrypt(data)
        return decrypted
    # sign a document

    def sign(self, content):
        return self.private_key.sign(content, ec.ECDSA(hashes.SHA256()))

    def eccSign(self, privateKey, curve, data):
        '''ECC Signing - Returns an ECC Signature'''
        ecc = ECC(1, public='', private=privateKey, curve=curve)
        signature = ecc.sign(data)
        return signature

    def signmessage(keyid, message):
        sig = sec.sign("I have just signed this text!")
        message |= sec.sign(message)
        timesig = sec.sign(None)
        lone_sig = sec.sign(None, notation={"cheese status": "standing alone"})
    # verify a document

    def verify(self, content, sig):
        ver = self.public_key.verifier(sig, ec.ECDSA(hashes.SHA256()))
        ver.update(content)
        return ver.verify()

    def verifymessage(message):
        pub.verify("I have just signed this text!", sig)
        pub.verify(message)
        for uid in someones_pubkey.userids:
            pub.verify(uid)
        pub.verify(someones_pubkey)

    def eccVerify(self, publicKey, curve, data, signature):
        '''Verifies ECC Signature based on Data received - Returns a Boolean Value'''
        ecc = ECC(1, public=publicKey, private='', curve=curve)
        return ecc.verify(data, signature)
    # backup your private key

    def backup(self, password):
        return self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.BestAvailableEncryption(
                password)
        )
    # share your public key

    def share(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
