# Congredi [toxik.io/congredi/](//toxik.io/congredi/)
> Peered Democratic Documents

> For the static webclient written in JS, see [delegito.io](//delegito.io)

`Congredi` is a python program that allows a community to help
individuals write changes to repositories of text, that are then
voted on by organizations to find a consensus.

## Design ideas

Functionally speaking, it uses Twisted.amp to send packets, and runs some
crypto on them before performing actions on a redis/neo4j database.


Keys are the hashes, Basically Accessible Soft state Eventual consistency,
git-diff style diffs, torrenting segments, AES/EC protos, STV from different
papers on the subject.

## Looking for contributors!

While I'm building this up, I'm looking for contributors!
Head over to Waffle.io, issuehub.io, or CodeTriage :heart:.

**Here's some example [issue tags](contributing/tags.md).**


## Installing

* library: `pip install congredi`
* git: `git clone https://github.com/thetoxicarcade/congredi.git && cd congredi`
* docker:
```
ericoflondon/
    congredi                - individual peer/clients
    delegito                - static content, swarmable
```
## Running
* `python -m congredi.main.run peer --redis 6379 --neo4j 7474 --port 8800`
* `python -m congredi.main.run client --host localhost --port 8800`






```
Projects I'm still looking at:
https://github.com/twisted/vertex
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
https://github.com/WhisperSystems/libsignal-protocol-javascript
https://whispersystems.org/docs/specifications/xeddsa/
https://whispersystems.org/docs/specifications/x3dh/
https://whispersystems.org/docs/specifications/doubleratchet/
    ratchet


```




