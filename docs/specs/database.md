# Congredi database spec

Congredi stores key-value pairs in several categories:

```
PCR:{ip,pubkey,seshkey}
    think kademila DHT, last-seen (also signed from others)
ENT:{gateways[],pubkey,vouchers:[],docs:[],votes:[]}
    gateways are signed redistributors of content
SHA:{
VER:{citations(submodules)
STV:{date,result,poll,chain
AGR:{keys,admins,threshold votes, subscriptions

expired data (new session keys, new latest resolved consensus), can give expiry
network-of-trust
blockchain
    {
        previous:""
        data:"",
        publisher:"",
        sighash:""
    }

    genesis (<20 deep)
    history (>20 deep)

```
Twisted:
    txredisapi
        redis server (key/value/sort)

libgit2-redis

