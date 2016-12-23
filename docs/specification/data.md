Congredi deals with a hash-value structure and a directed graph structure,
with both redis and neo4j.

Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.


```
structures & query language (i.e. PUBLISH CACHE HAS <object>)
CACHE
	HAS				- list(hash:key:sig:begins:expires)
	WANTS			- list(hash:key:sig:begins:expires)
	PROOF			- list(nonce:proof:date:sig)
	SEEN			- list(prev:time:date:sig)
	UPTIME			- list(prev:time:date:sig)
	RANK			- list(prev:rank:date:sig)
COMPUTATION
	POLL			- list(polls,date,threshsig)
	VOTE			- list(votes,date,threshsig)
	TREES			- list(trees,date,threshsig)
	SAVES			- list(list(hash,begins,expires),date,threshsig)
	VOTERS			- list(proofs,date,threshsig)
HISTORY
	TREES			- list(list(CURRENT,PREVIOUS,SIG))
	POLLS			- list(list(CURRENT,PREVIOUS,SIG))
	VOTES			- list(list(CURRENT,PREVIOUS,SIG))
	MEMBERSHIPS		- list(list(CURRENT,PREVIOUS,SIG))
	PROPOSALS		- list(list(CURRENT,PREVIOUS,SIG))
	SAVES			- list(list(list(hash,begins,expires),PREVIOUS,SIG))
IDENTITY
	ROUTE			- KEY, PREVIOUS, SIG
	USER			- KEY, PREVIOUS, SIG
	AGGREGATE		- list(KEYS), PREVIOUS, SIG
	IP				- IP, PREVIOUS, SIG
	RENDESVOUS		- list(IPS), PREVIOUS, SIG
	LOCATION		- ZKP, PREVIOUS, SIG
	BORDERS			- CURRENT, PREVIOUS, THRESHSIG
CONTENT
	BIO				- COMMIT,PREVIOUS,SIG
	MANIFESTO		- COMMIT,PREVIOUS,THRESHSIG
	COMMIT			- hash,list(CHUNKS),list(PREVIOUS),SIG, KEY
	CHUNK			- truncated-gzip-ndiff-markdown
	POLL			- list(TREES)
	VOTE			- list(TREES)
SETTING
	IP				- previous:sig:ip
	RENDESVOUS		- previous:sig:list(fp)
	ADMIN			- list(fp)
	USER			- list(fp)
	PEER			- list(fp)
	WHITELIST		- list(fp)
	BLACKLIST		- list(fp)
```

```
users -> agg -> polls/votes/trees -> commits -> chunks

"directed graph":{
	"user":{
		"trusts":"users",
		"follows":"repos"
	"repo":"commits"
```

```
kleptography / outside obfuscation / steganalisis
RATCHET sessionkey, prekey,
ONION FROM <route> TO <route> <contents>
ratchet:onion:AONT:Axolotl EC AES new hope
ring learning homomorphic garlic, sign time+nounce,
OAEP/AONT/hamming4:7
nonce, prekey, session key, hash, time, pubkey, p2p, dht
libgit2-redis/txredisapi / redis / neo4j; if in peers,
delete, add peer 0(1) nettrust KV - list,
read, add(k,v), delete(k)
```