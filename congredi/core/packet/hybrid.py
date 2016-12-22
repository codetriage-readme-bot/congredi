#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
def GetPacket(AMP.TLS):
	if message[:64] != pubkey: errBack('not me')
	hsh = hash(message[-64:])
	if hsh != message[:-64]: errBack
	cKey = self.key.decrypt(message[64:128])
	message = cKey.decrypt(message[128:-64])
	if hash(message[-64:]) == message[:-64]):
		# valid next packet - send off to addr
		TTL = privledge
		piping.append(from,to)
		addr = lookup(key)
		_send(mesg,addr)
def SendPacket(AMP.TLS):
	cKey = AES()
	ctxt = cKey.encrypt(message)
	val = recipient.encrypt(cKey)
	preMesg = pubkey + val + ctxt
	msg = preMesg + hash(preMesg)
def OnionRoute():
	for reversed(route):
		pkt = SendPacket(route)
	_send(pkt,addr)
def _send(pkt,addr):
	result = getThing()
	if result == errBack:
		forward(errBack)
	else:
		
def _recieve(pkt,addr):
	result = FulfillThing()
	else:
		errBack



















routers = []
entrys = []
A -> B -> C -> D -> E -> F

TLS(
	hash|
	recipientKey|
	recipeintECC(aesKey)|
	aes(AONT_OAEP(msg))
	)

recipient:
	sendToNext
		:decrypt
circuit table: from - to




class CongrediProtocol():
	def GetPacket(pkt):
		if lookupKey(pkt[:64]) == False:
			if lookupTrust(peer.key) == False:
				conn.write("Key Unavailable for Routing.")
			else:
				key = AskPeersForKey(pkt[:64])
				if key is none:
					conn.write("Key Unavailable for Routing")
					conn.drop()
		if pkt[:64] == self.routeKey: GetCommand(pkt)

		if pkt[:64] == self.routeKey:
			GetCommand(pkt)
		else:
			pass
	def PickIntro():
		pass
		# route to Intro
		# ask intro
		# publish packet
	def PickRendesvous():
		pass
	def SendRequest():
		pass
		# onion wrap
	def RecieveRequest():
		pass
	def Send():
		pass
import pyelliptic
from itertools import tee
def pairwise(iterable):
	"s -> (s0,s1), (s1,s2), (s2, s3), ..."
	a, b = tee(iterable)
	next(b, None)
	return zip(a, b)
class onion():
	'''
	Secure Packet Routing Methods. (layered under TLS)
	'''
	def __init__(self, key):
		self.key = key
	def PackMsg(self, msg, re, numHops=3):
		introductionPoint = self.RandomIntroPoint(re)
		route = self.GetRoute(introductionPoint, numHops)
		message = msg
		for node, nextNode in pairwise(route):
			key = self.FindKey(node)
			nodeKey = ECC(key)
			message = nodeKey.encrypt(message)
			message = nextNode + message
	def UnPackMsg(self, msg):
		nextNode = msg[:64]
		message = self.nodeKey.decrypt(msg[64:])
		return message, nextNode
	def GetRoute(self, finalAddr, numHops):
		# routing nodes are all nodes minus my key
		tempNodes = list(self.nodes)
		tempNodes.remove(self.key)
		
		# we will be adding a node to our result
		# then deleting it from the available ones
		result = []
		def add(choice):
			result.append(choice)
			tempNodes.remove(choice)
		
		# we want the final result to be the rendesvous
		add(rendesvousKey)
		while len(result) < hops:
			choice = random.choice(tempNodes)
			add(choice)
		return result
#65535 bytes 65 kb
class CongrediProtocol():
	def UpOnion():
		pass
def encryptHops(numHops=3, rendesvous=b, gateway=c, server=d):
	for hop in numHops:
		aeskey = rand()
		AES(pkcs_oeap_aont(msg))
		head = ecc(hop.pubkey,aeskey)
		msg = head + ':' + msg
#ECC.generate()
#E.encrypt()

class items():
	'''ECC ENCRYPTION USAGE'''
	eccPrivateKey, eccPublicKey, eccCurve = crypto.eccGenerate()
	
	encryptedECCContent = crypto.eccEncrypt(eccPublicKey, eccCurve , message)
	print 'Encrypted ECC Message with ECC Public Key: %s\n' % encryptedECCContent
	decryptedECCContent = crypto.eccDecrypt(eccPrivateKey, eccCurve, encryptedECCContent)
	print 'Decrypted ECC Content with ECC Private: %s\n' % decryptedECCContent
	
	'''ECC SIGNING USAGE'''
	signature = crypto.eccSign(eccPrivateKey, eccCurve, message)
	print 'Signature for message is: %s\n ' % signature
	if crypto.eccVerify(eccPublicKey, eccCurve, message, signature) is False:
		print 'Could not Verify Message\n' 
	else:
		print 'Verified ECC Content\n'
	def eccGenerate(self):
		'''Generates Elliptic Curve Public/Private Keys'''
		ecc = ECC.generate()
		publicKey = ecc._public
		privateKey = ecc._private
		curve = ecc._curve
		return privateKey, publicKey, curve	
	
	def eccEncrypt(self,publicKey, curve, data):
		'''Encrypts Data with ECC using public key'''
		ecc = ECC(1, public=publicKey, private='', curve=curve)
		encrypted = ecc.encrypt(data)
		return encrypted
	
	def eccDecrypt(self,privateKey, curve, data):
		'''Decrypts Data with ECC private key'''
		ecc = ECC(1, public='', private=privateKey, curve=curve)
		decrypted = ecc.decrypt(data)
		return decrypted
	
	def eccSign(self, privateKey, curve, data):
		'''ECC Signing - Returns an ECC Signature'''
		ecc = ECC(1, public='', private=privateKey, curve=curve)
		signature = ecc.sign(data)
		return signature
		
	def eccVerify(self, publicKey, curve, data, signature):
		'''Verifies ECC Signature based on Data received - Returns a Boolean Value'''
		ecc = ECC(1, public=publicKey, private='', curve=curve)
		return ecc.verify(data, signature)
	def __extractCrypto__(self, encryptedContent):
		'''Decodes Base64 Encoded Crypto'''
		cipherText = base64.urlsafe_b64decode(encryptedContent)
		return cipherText
	
	def __encodeCrypto__(self, encryptedContent):
		'''Encodes Crypto with Base64'''
		encodedCrypto = base64.urlsafe_b64encode(str(encryptedContent))
		return encodedCrypto
	'''AES Cipher Specifics'''
	blockSize = 16		  #Block Size
	keySize = 32			#keySize in Bytes - 32 bytes = 256bit Encryption
	mode = AES.MODE_CBC	 #Cipher Block Mode
	
	def __init__(self):
		
		pass
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
	
	def __encodeCrypto__(self, encryptedContent):
		'''Encodes Crypto with Base64'''
		encodedCrypto = base64.urlsafe_b64encode(str(encryptedContent))
		return encodedCrypto
	
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
	def aesDecrypt(self, key, data):
		'''Decrypts AES(base64 encoded) Crypto - Returns Decrypted Data'''
		decryptionKey = self.__extractAESKey__(key)
		encryptedContent = self.__extractCrypto__(data)
		iv = encryptedContent[:self.blockSize] 
		cipherText = encryptedContent[self.blockSize:]
		plainTextwithpad = AES.new(decryptionKey, self.mode, iv).decrypt(cipherText)
		pad = ord(plainTextwithpad[-1])
		plainText = plainTextwithpad[:-pad]
		return plainText
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from pyecc import ECC
"""
