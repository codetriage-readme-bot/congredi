# Congredi [delegito.io](//delegito.io)
> a BASE representation-of-law-via-cryptography protocol

`Congredi` is a set of utilities and a Twisted server/shell for distributed
document storage, revisioning, and voting on those revisions. Think of it
as a community of git databases where groups of people rank their choices
on how fictional repos should be constructed. Like an STV version of reddit
for documents.

This repository doesn't include a client, or scaling. I would suggest
serving via traefik, nginx, flask, and angular (originally).

## Installing

* library: `pip install congredi`
* docker: `ericoflondon/congredi-api` and `ericoflondon/congredi-cluster`
* git: `git clone https://github.com/thetoxicarcade/ac.git && cd ac`

## Running

* `python -m congredi peer --redis 6379 --neo4j 7474 --port 8800`
* `python -m congredi client --host localhost --port 8800`


[![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/ac.svg?label=ready&title=Ready)](http://waffle.io/Thetoxicarcade/ac)
[![Build Status](https://travis-ci.org/Thetoxicarcade/ac.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/ac)
[![Documentation Status](https://readthedocs.org/projects/ac/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest)
[![GitHub commits](https://img.shields.io/github/commits-since/thetoxicarcade/ac/v0.0.1.svg?maxAge=2592000)](https://github.com/thetoxicarcade/ac)
[![Code Climate](https://codeclimate.com/github/Thetoxicarcade/ac/badges/gpa.svg)](https://codeclimate.com/github/Thetoxicarcade/ac)
[![Issue Count](https://codeclimate.com/github/Thetoxicarcade/ac/badges/issue_count.svg)](https://codeclimate.com/github/Thetoxicarcade/ac)
[![PyPI version](https://badge.fury.io/py/delegito.svg)](https://badge.fury.io/py/delegito)

* `congredi-interface` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-interface.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-interface/)
* `congredi-api` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-api.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-api/)

**NOTE. [Congredi](//github.com/thetoxicarcade/congredi) is the regular**

```
https://github.com/gsko/mdht
https://github.com/microserv/entangled-dht
https://github.com/StorjOld/pyp2p/blob/master/pyp2p/rendezvous_server.py
https://github.com/wiedi/khashmir
https://github.com/bmuller/kademlia
https://github.com/bmuller/rpcudp
https://github.com/csm/khashmir
>https://github.com/darka/p2pfs
https://github.com/debanshu/ResearchShareP2P
https://github.com/twisted/vertex
https://github.com/twisted/twisted


https://github.com/indigo-dc/udocker
    pull docker containers, decompress, run in PRoot/chroot?
https://github.com/jamercee/signet
    sign python and use loader to run
https://github.com/bnlucas/python-basehash
    encrypted hashing
https://github.com/rw/plainsight
https://github.com/JarrodCTaylor/steganopy
    steganography
https://github.com/barseghyanartur/ska
    - signed (symetric then HMACed)

https://github.com/WhisperSystems/Signal-Desktop
https://github.com/WhisperSystems/libsignal-protocol-javascript
https://whispersystems.org/docs/specifications/xeddsa/
https://whispersystems.org/docs/specifications/x3dh/
https://whispersystems.org/docs/specifications/doubleratchet/
    ratchet
https://github.com/bitcoin-abe/bitcoin-abe
    browser
https://github.com/blockstack/pybitcoin
https://github.com/Bitmessage/PyBitmessage
https://github.com/miguelfreitas/twister-core
https://github.com/feross/webtorrent


```