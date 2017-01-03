AUTHOR <hash>
<command[SET|GET|SEEK|SEARCH]>
<type[COMMIT|CHUNK|VOTE|BIO|POLL|MANIFESTO]>
<[LATEST|CHAIN|BLOCK]>
PERMISSIONS <[TRUE|FALSE>
[<direction[FORWARD|REVERSE]> OFFSET <hash> COUNT <int>]
SEARCH COMMIT 
AUTHOR e31df061a89e63ce7f6941c82b0261e91d400926a70e09f229e0dbdbe067ee19 SET COMMIT PERMISSIONS FALSE
sign(req, key): value = yaml.dump(req); return key.sign(value)

entity<hash>:
    /proof              CHAIN [objecthash, start, stop, result, sig, previous]
    /has                CHAIN [objecthash, previous, sig]
    /wants              CHAIN [objecthash, previous, sig]

chunk<hash>:          data
commit<hash>:         list(chunks), list(previous), author, sig
router<hash>:
    /ip                 CHAIN [ips, previous, sig]
    /censor             CHAIN [hash, previous, sig]
    /uptime             CHAIN [uptime, previous, sig]
    /seen               CHAIN [seen, previous, sig]
    /rank               CHAIN [rank, previous, sig]
    /courier-of         CHAIN [hash-key, previous, sig]
    /rendesvous-of      CHAIN [hash-key, previous, sig]
    PRIVATE:
        /blacklist          CHAIN [hash-key, ip, previous, sig]
        /whitelist          CHAIN [hash-key, ip, previous, sig]
        /peers              CHAIN [hash-key, ip, previous, sig]
        /users              CHAIN [hash-key, previous, sig]
        /admin              CHAIN [hash-key, previous, sig]

user<hash>: - pubkey
    # properties
    /bio                CHAIN [COMMIT, previous, sig]
    /location           CHAIN [zkplocation, previous, sig]

    # couriers (public ips of endpoints)
    /couriered-by       CHAIN [courier, ip, previous, sig]
    /rendesvoused-by    CHAIN [rendesvous, ip, previous, sig]

    /join-req           CHAIN [org, previous, sig]
    /proposal           CHAIN [org, commit, vote, previous, sig]
    /member-of          CHAIN [org, previous, sig]


    /casted-votes       CHAIN [vote, ballot, previous, sig]
    /casted-polls       CHAIN [poll, ballot, previous, sig]
    
    /tree<hash>         CHAIN [commit, previous, sig]
    /saves              CHAIN [hash, previous, sig]

org<hash>: - tuple(admin pubkeys)
    /manifesto          BLOCK [COMMIT]
    /borders            BLOCK [tuple]
    
    # couriers (endpoint IPs and user IPs
    /host-staff         BLOCK [key, ip, acceptance]
    /host-volunteer     BLOCK [key, acceptance]

    # documents neaded to align everyone to a vote
    /members            BLOCK [join-req, acceptance]
    /proposals          BLOCK [proposal, acceptance]

    # vote results
    /vote-tally<hash>   BLOCK [ballot, acceptance]
    /poll-tally<hash>   BLOCK [ballot, acceptance]

        
    /saves-tally        BLOCK [saves, acceptance]

### OLD
---

Congredi deals with a hash-value structure and a directed graph structure,
with both redis and neo4j.

Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.


```
structures & query language (i.e. PUBLISH CACHE HAS <object>)
CACHE
COMPUTATION
HISTORY
IDENTITY
CONTENT
SETTING
```

```
users -> agg -> polls/votes/trees -> commits -> chunks

"directed graph":{
	"user":{
		"trusts":"users",
		"follows":"repos"
	"repo":"commits"
```

# "CACHE HAS"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash (of content they have)
		datestring (beginning storage date)
		datestring (expiry date)
		32b sig (signature of the above)
```
# "CACHE PROOF"

A router (identified by their public key) can prove they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash (of content they have)
		32b nonce (as a challenge)
		32b result (hash of adding the nonce to the selected bytes)
		int position (place to grab bytes from)
		datestring (time they proved that nonce)
		32b sig (signature of the above)
```
# "CACHE RANK"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash of previous lookup rank hash
		rank info
		datestring (beginning rank date)
		datestring (expiry date)
		32b sig (signature of the above)
```
# "CACHE SEEN"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash of previous lookup hash
		datestring last seen
		datestring (beginning storage date)
		datestring (expiry date)
		32b sig (signature of the above)
```
# "CACHE UPTIME"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash of previous lookup hash
		uptime information
		datestring (beginning storage date)
		datestring (expiry date)
		32b sig (signature of the above)
```
# "CACHE WANTS"

A router (identified by their public key) can declare they have something with
packets. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

```
64b key :
	32b lookup hash of bellow :
		32b hash (of content they want)
		datestring (beginning storage date)
		datestring (expiry date)
		32b sig (signature of the above)
```



# "COMPUTATION POLL"

An org can compute a poll (public vote) together, and publish their findings
in a poll object. Computation fields are byzantian problems, so consensus
needs reaching. We keep track of them in a list of objects totalled like this:

(concatenate fields...)

Blobs will probably be zlib compressed ndiffs, even if I want them to be
unified diffs.


```
32b hash of original poll spec :
	32b lookup hash of bellow :
		32b hash (of polls we do have)
		list:
			user's latest poll on this
		result object
		datestring (date)
		32b sig (signature of the above)
		32b threshsig
```
```
	SAVES			- list(list(hash,begins,expires),date,threshsig)
	TREES			- list(trees,date,threshsig)
	VOTE			- list(votes,date,threshsig)
	VOTERS			- list(proofs,date,threshsig)
	BIO				- COMMIT,PREVIOUS,SIG
	CHUNK			- truncated-gzip-ndiff-markdown
	COMMIT			- hash,list(CHUNKS),list(PREVIOUS),SIG, KEY
	MANIFESTO		- COMMIT,PREVIOUS,THRESHSIG
	POLL			- list(TREES)
	VOTE			- list(TREES)
	MEMBERSHIPS		- list(list(CURRENT,PREVIOUS,SIG))
	POLLS			- list(list(CURRENT,PREVIOUS,SIG))
	PROPOSALS		- list(list(CURRENT,PREVIOUS,SIG))
	SAVES			- list(list(list(hash,begins,expires),PREVIOUS,SIG))
	TREES			- list(list(CURRENT,PREVIOUS,SIG))
	VOTES			- list(list(CURRENT,PREVIOUS,SIG))
	AGGREGATE		- list(KEYS), PREVIOUS, SIG
	BORDERS			- CURRENT, PREVIOUS, THRESHSIG
	IP				- IP, PREVIOUS, SIG
	LOCATION		- ZKP, PREVIOUS, SIG
	RENDESVOUS		- list(IPS), PREVIOUS, SIG
	ROUTE			- KEY, PREVIOUS, SIG
	USER			- KEY, PREVIOUS, SIG
	ADMIN			- list(fp)
	BLACKLIST		- list(fp)
	IP				- previous:sig:ip
	PEER			- list(fp)
	RENDESVOUS		- previous:sig:list(fp)
	USER			- list(fp)
	WHITELIST		- list(fp)
```