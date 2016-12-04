* [ ] STV shuffle-sum
* [ ] find docs on threshold signatures for jurisdictions (better option)
* [ ] Peer Protocols: messaging, rendesvous
* JWT
* Openpgp
* webrtc
* forge
* sjcl
* node-tor
* webtorrent
* 


The crypto involves:

* threshold-signature OpenPGP for jurisdiction appointments
* threshold-encrypted Secure Secret Sharing for jurisdiction admin
* Shuffle-Sum for private vote results
* OpenPGP signatures for public polls
* OpenPGP Key Signing & keyservers for authorizations
* Tor & WebRTC for peer communications

A deeper look at the methodology:


* [non-coercion](zero Knowledge)
* [distribution](Chained Data)
* [identity](Sybil Attacks)# Network verification processes

1. Possession of a particular onion address (activity)
    * Method: actively online, ranking of a fraction (successes / tries)
    * replay-proxy attacks possible
2. Possession of a public key (signed challenge)
    * Method: send challenge nounce, request it be signed, validate
    * Shor's Algorithm / RSA Factorization
    * Could swap to ECC, then it has its own ECDL
3. Proof of Stake (ownership of a vote / issue / poll datum)
    * request proof that a transaction came from that node?
    * Could lead to favoritism
4. Chain of Trust (you trust your introductory nodes more)
    * method: ranking out from a trusted node, halving, small fraction alloted to un-trusted nodes
    * leads to coordinated-synchronization (half sybil) attacks (bots all have same data)
5. Sync Tests (they have what you need when you need it)
    * method: rank query-bounce of a node (successes / tries)
    * vulnerable to coordinated-syncrhonization (half sybil)
6. Hash/Scrypt Tests (GPU/Memory based)
    * difficulty goals generated by the network (fudge factor)
8. Limited resources (ownership of an IP address?)
    * impossible re: feasible to make new Tor nodesoverlays: LUKS, Cjdns, Tor
secure the filesystem: user-keychain + passphrase -> AES Cipher + block headers (gzip, integ, permissions separations)
secure the network: DHT (routing/rendesvous) 6 hop rendesvous circuit 2:1 onion/garlic routing,
    partial deniability network routing
secure the filesystem: key-torrent-striped, H(H(H(m))) group encryption (depending on jurisdiction)
    partial deniability block storage (fs priority to network of trust for proposed forks + new content)
secure the blockchain: proposed forks (diff-hash) -> sig+threshold vote -> blockchain
keyword/meta search is possible through any of the jurisdictions you have access to.

user(two(one(rendesvous) -> (two(one(server))) -> file..file..file..

DHT, onion routing, torrent, ecc, blockchain, hash, diff, threshold vote

router + storage striping plausible deniability


The crypto involves:

* threshold-signature OpenPGP for jurisdiction appointments
* threshold-encrypted Secure Secret Sharing for jurisdiction admin
* Shuffle-Sum for private vote results
* OpenPGP signatures for public polls
* OpenPGP Key Signing & keyservers for authorizations
* Tor & WebRTC / Sockets for peer communications


no need for secure secret sharing,
but possibly for zero knowledge proofs
kleptography / outside obfuscation - filler syncing
    priority packets vs consensus
    OAEP all or nothing, compress diff tree
        content filter rules (markdown)
steno analysis, client storage encryption, purge unneded content
session symkeys + ip + pubkey
subset challenge zero knowledge proof + nounce,
tor + gitchain _ gittorrent

individual relay records (reliable, fast)
content-subscribers, content broadcasters
DHT
search/list
message authentication (symkey + hash Hmac)
Ratchet proto
ringlearn new hope homomorphic
jwt

half-leg all or nothing (ask for route)

latest DB (resolve commits)

stat db (offers,experience)
O(1) block git tree (compression, voting data, entities, agrs)

latest consensus (rename)
libgit2 redis (get through reactor)
KV - list, read, add(k,v), delete(k)

PSC/SHA/VER/ENT/STV/AGR