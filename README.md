# Congredi
> a BASE representation-of-law-via-cryptography protocol

Congredi is a Twisted protocol for groups to representationally agree on things.

It behaves like gittorrent and gitchain, but with more onion-like proxying,
incentives to prove they stored a git object (i.e. filecoin), and ranking of which git objects
& trees they want to keep around.

* Requirements: Python Cryptography (Fernet & EC), Twisted
* Addons: Stem, Flask, PyJWT

Hopefully, with any luck, the files written here will be well-documented, unit
tested, & cohesive/decoupled.

I leave design of a perusing/issuing client to you.

