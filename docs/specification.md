## Protocol
Congredi deals with a hash-value structure and a directed graph structure,
with both redis and neo4j.

Congredi uses a simplified onion-routing system to discourage some censorship.
Servers, once active on the network, ask 3 nodes to be their rendesvous, and
then sign a statement that gets advertised around the network. Clients can
make a query to those nodes through a set of layered encryptions, until
the final node and the rendesvous node, either of which may object to the query.
Since the serve stores data in plaintext, if it finds something objectionable,
or of no use, it can censor that content as well.
```
GET <type> <hash>				| return <contents>
SET <type> <hash> <contents>	| return <subset proof>
CURRENT <type> <hash>			| return <contents>
LIST <type> ORDER <> OFFSET <> COUNT <> TERM <>	| return <contents>

EXACT/chain/get
BLOCK/current

USER : FINGERPRINT
	BEGINS: KEY
	LOCATION: chain<ZKP>
	BIO: tree
	TREE: chain<trees>
	POLL: chain<poll>
	VOTE: chain<shuffle-sum>
	AGGREGATE: chain<aggregate> // join/leave
	PROPOSE: chain<stv/poll/tree> //add/remove
	KEEP: chain<objects> // REQUESTS UNTIL EXPIRE
	ENDS: next fingerprint
TREE : {
	chains<commits>
	meta: users have current pointers
COMMIT : {
	SIG
	PUBKEY
	CHUNKS
	PREVIOUS
CHUNK : content
	BEGINS: content
	meta: commits use
VOTE : HASH
	BEGINS: TREES
	meta: users have current votes
	meta: aggregations have current results
POLL : HASH
	BEGINS: TREES
	meta: users have current votes
	meta: aggregations have current results
ROUTE : FINGERPRINT
	BEGINS: KEY
	IP: chain<ip>
	private ADMINS: admins
	BLACKLIST/WHITELIST loosechain<>
	PENDING delete/download
	RENDESVOUS: chain<routes> // add/remove
	SEEN: <time>
	UPTIME: block<time>
	RANK: block<rank> // unknown, trusted, untrusted, compromised
	WANTS: block<wants> // hash time expires - delimited
	HAS: block<has> // hash time expires - delimited
	PROOF: subset hash parameters nounce sig time expires
AGGREGATION : {
	BEGINS : admins
	MANIFESTO : tree
	BORDERS: block<data> // update
	VOTERS: block<fingerprints> // add/remove
	POLLS: block<polls> // add/remove
	VOTES: block<votes> // add/remove
	TREES: block<trees> // add/remove
	KEEP: chain<objects> // REQUESTS UNTIL EXPIRE
	ENDS : new admins





kleptography / outside obfuscation / steganalisis
"directed graph":{
	"user":{
		"trusts":"users",
		"follows":"repos"
	"repo":"commits"
RATCHET sessionkey, prekey, ONION FROM <route> TO <route> <contents>

//ratchet:onion:AONT:Axolotl EC AES new hope ring learning homomorphic garlic, sign time+nounce, OAEP/AONT/hamming4:7
//nonce, prekey, session key, hash, time, pubkey, p2p, dht
//libgit2-redis/txredisapi / redis / neo4j; if in peers, delete, add peer 0(1) nettrust KV - list, read, add(k,v), delete(k)
```

