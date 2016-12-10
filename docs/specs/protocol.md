## Protocol

Axolotl ratchet (but with EC & Fernet) I.e. `[handshake][packet][changekey][packet][changekey]...`

OAEP/AONT

`<all-or-nothing<hamming4:7?>><shmac>`

State machine:

```
start proto
    respond
click ratchet
    be-clicked
proxy-send - use next node's public key (have decrypted a layer)
    proxy-recieve - must be able to decrypt two (decrypted a layer)
send file   - git object transfer
    recieve file -  (must be valid gzip'd diff of markdown)
query db - if objecting to query, don't send
    respond - respond with offset
announcements - new file searches, new objects in db
    events - listen to new events, add to knowledge db
```

protocol
    session-key
    shmac function
    decrypt (all or nothing)
    key-up
listener
    wantsSomething
broadcaster
    givingSomething
checkUpOnPeers
    for peers available:
        connect to peer or mark as offline
        ask peer what's new



add peer:
    if in peers:
        delete,
        add peer (update timestamp / last seen)
network packets (twisted/tornado)
p2p/dht libraries

```
PSC:
    relationmap, searching over shard, incentive to keep up-to-date, ranking
SHA: markdown compressed with gzip signed with ec
    - sig, ent, time, nonce
        - piece (hash+sig)
            - peer (signed hash, nonce?, date?)
    keep/delete votes ( O(1) nettrust)
VER
    bookmark-head (hash + sig + user)
    diffs (hash + sig + author)
    - subscribers who actually value that version (or children)
ENT
    - sig-denounces-last
    vers, subs, votes, groups
STV
    - sig-adds-all-known?
    person, versions, ranking, signature
AGR
    - aggregation-adds-all-group
    - group-membership-current
    STV aggregations
    membership lists
```


BREACH/CRIME security exploits?
    try to only send bigger obfuscated streams through the protocol?
    pad everything into oblivion?
    send random syncing packets when not busy?

    Omptimal Asymmetric Encryption Padding (2 oracles)
    all-or-nothing-transform
    no partial decryption

pre-shared keys (re-establish connection)

replay attacks
    sign time+nounce, session symetric keys
MITM
    mac (keyed hash)
    GCM
    all-or-nothing-transform
session fixation - JWT (signed token with an expiry)
client-side encryption
    storage-nodes-cannot-grab
storage?
    encrypted disks, mostly
priveledges
kleptographically
    non-random encryption (compromised CSPRNG)
post-quantum crypto (ring learning with errors) - add homomorphic
    newhope

zero-knowledge proofs

keybase - search 


forums
    reddit/sindie/discus
routing
    tor/i2p/gnunet

PSC: - Proxy Server Cache (DHT or onion peers we connect with)
	:aquiresession:
	:rankpeer:
SHA: - Secure Hash Algorithm (content blobs we pull along)
	:send:
	:recieve:
	:piece:
	:shard:
VER: - Version (git tree of things to keep or delete)
	:send::head:
	:recieve::clone:
	:keep:
	:delete:
ENT: - Entity (persons to rank as important)
	:proclaim:
	:view:
	:subscribe:
	:unsubscribe:
STV: - Single Transferable Vote (rankings of consensus)
	:correction:
	:known:
	:rank:
	:denounce:
AGR: - Agregates (groups of people who gather votes)
	:memberproof:
	:stvproof:
	:proposemember:
	:proposestv:


schedule:
pull list of online nodes

pull subscriber statements

query content subset hashes

Congredi handles customizable STV elections for federated "assertions".

1. Visit a Congredi host / install the extension
2. register with the host, you will be provisionally signed by the node
3. when the admin or their designee signs your key, you can vote
4. make assertions on issues within the host, or any of their federated peers
5. rank those assertions in an election, deciding which you would prefer if you cannot have your choice next





> Helping out? Check out the github [issues](//github.com/thetoxicarcade/congredi/issues)




Congradulations SN! We've set up an account for you!

Your public key fingerprint is SF.

You will need your PGP key for interacting with Congredi.

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
