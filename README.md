# Congredi [Our Documentation](//congredi.github.io/congredi/)
> Peered Democratic Documents

> For the static webclient written in JS, see [delegito.io](//delegito.io)

`Congredi` is a python program that allows a community to help
individuals write changes to repositories of text, that are then
voted on by organizations to find a consensus.

***Slowly waking up this project...***
Port 4800: binary Congredi
Port 4884: hex/http Congredi

Installing: `docker pull congredi/congredi` or `pip install congredi`
Running: `python -m congredi`


Tests: [![Build Status Travis](https://travis-ci.org/congredi/congredi.svg?branch=master)](https://travis-ci.org/congredi/congredi)

* Linux:
  * 2.7: docs, pylint, unit tests
  * 3.3-3.6: unit tests
* Mac: 2.7 & 3.3
* Windows (No Longer testing for compatibility.)




Congredi Protocol and Delegito Interface Design Specs

Binary compatibility (hex conversion?) - just control the writer? Android/iOS? Browser?
- just pump to Hex gateway

Motives/Collectives Ranked Choices

Onion routing - less API's and URLs, just BSON
name same as permissions inside storage DB
command switchboard

[TCP Packet] = [TotalLength|L|Recipient|L|Sender|L|Request|L|Data|L|Hash|L|Sig(HMac vs RSA?)]

[Data] = [RecpRSAKeyOAEPEnc(AESKey) | AES( XOR(AESKEY^HASH-A)|AES(MIXPACKET)|hash-A(AES-Ciphertext) )]


MIXPACKET = [LL][LK][to][LK][from][LR][REQ][LD][DATA][hash][hmac]
OUTER-DATA = [OAEP-RSA(AES-ONE) | AES-ONE(INNER)]
INNER = [(AES-TWO^HASH-INNER)|AES-TWO(FINISH)|HASH-INNER(CIPHERTEXT)]

FINISH = [List Of Keys/Data By Length / Type]


Infinite regression cascade vs efficient torrenting

affidavit / registration API

Configuration:
  Storage API - REDIS / Postgres
  Encryption API (Data at rest) - TripleSec + AONT?
  Packet API
  Requests
  Loop thread
