# Congredi [delegito.io](//delegito.io)
> a BASE representation-of-law-via-cryptography protocol

Congredi is a Twisted protocol for groups to representationally agree on things.

For the library: `pip install delegito`

For the docker containers: `FROM ericoflondon/congredi-api` `FROM ericoflondon/congredi-cluster`

Congredi is a python library for agreeing on versions of documents,
some sort of git-reddit. This behaves like gitchain/gittorrent,
with single-transferable-voting, and partially like Tor (though
only with one hop).

It behaves like gittorrent and gitchain, but with more onion-like proxying,
incentives to prove they stored a git object (i.e. filecoin), and ranking of which git objects
& trees they want to keep around.

* Requirements: Python Cryptography (Fernet & EC), Twisted
* Addons: Stem, Flask, PyJWT

Hopefully, with any luck, the files written here will be well-documented, unit
tested (lint + nose2?), & cohesive/decoupled.

I leave design of a perusing/issuing client to you. I tried angular with routes,
as well as traefik + nginx/flask. Others have made things with QT?


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
