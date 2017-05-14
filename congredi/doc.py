"""
AMP Objects. If I don't have to serialize them, why bother?

These provide readible names for argument Types:
# if necissary, these will do something besides just send binary.
# could be doing hash validation for all this??
# class inheritance?
# Encrypted Boolean

EncBool                 - Boolean (len?)
EncAddress/ObjAddress   - Addresses (IP/Tor/DNS)
EncPubKey/ObjPubKey     - Public Keys (len?)
ObjHash/EncHash         - Hashes (len?)
ObjSig/EncSig           - Sig of Hash (len?)
ObjBlob/EncBlob         - General Blobs

PrivAES                 - RSA encrypted session key


http API

    Redo the spec for the api on github.com/congredi/spec

# authorization stuff
/auth/new           - check DB, get long term JWT
/live/next          - get next short term JWT from long term JWT
/live/online        - find if a peer is online

# getting/setting contents
/set/<permission[0|1]>/<typeOf>
/get/<permission[0|1]>/<typeOf>

# searching/indexing (offset is a hash value, not an integer)
/index/<typeOf>/<direction>/<offset>/<count:double>/<hashPtr>
/search/<typeOf>/<offset>/<count:double>/<term>

# neater aliases:

/d/
    /commit/<id>
    /chunk/<id>
    /vote/<id>
    /bio/<id>
    /poll/<id>
    /manifesto/<id>
/s/
    /rendesvous - rendesvous settings
    blacklist - blacklist settings
    whitelist - whitelist settings
    peer - peer listings
    admin - admin settings
    user - user settings
/r/<routername>/
    /ip
    /censor
    /uptime
    /has
    /wants
    /seen
    /proof
    /rank
/u/<username>/
    /bio
    /location
    /courier
    /vote/<voteid>
    /poll/<pollid>
    /proposal/<id>
    /save/<saveid>
/g/<groupname>/
    /manifesto
    /borders
    /members
    /votes/<voteid>
    /polls/<pollid>
    /saves

/api/
	/<user>/
		/trust/ - update your pgp keys
		/avatar/ - png/jpeg avatar
		/profile/ - json dict profile strings
		/<user>/ - return user dict
			/avatar/ - return user image
			/trust/ - sign their key with yours
	/search/ - return key:value from a value search
		{ type:["~"|"<"|">"|"=="], amount:int, offset: int, subset: "key", search: "string" }
		{ meta:{offset:int,amount:int}, key: base64, value: { json } }
		/peers/ - /peer/ indexes, some meta searches
		/govts/
		/votes/
		/options/
/peer/ - return idx
	/<hash>/ - current onion addresses
		/trust/ - pgp key chain
		/uptime/ - reputation
		/stake/ - stake proof blocks
/govt/ - return idx
	/<jurisdiction>/ - return active vote/user blocks (signed by jurisdiction)
		/validated/ - issues signed on by consensus (multiple winners)
		/ordered/ - distributed block (data secure)
		/unordered/ - idx proposed issues
		/denied/ - idx of issues denied entrance
		/<issueid>/ - return an issue signature
/vote/ - return idx
	/<hash>/ - genesis block
		/validated/ - idx of asserted
		/ordered/ - idx of consensus-ordered
		/unordered/ - idx of proposed blocks
		/open/ - idx of voters who have not voted
		/<blockid>/ - return a block and its contents

AMP commands for addresses - replaces command.py

Commands:
* Address - tell them what you thought theirs was, get what they saw yours as
* SyncPeerDirectory - send a list of (key, ip)s, get back a list of (key, ip)s
* SyncRendesvousDirectory - list of (key, rendesvousKey, proof) <->
* SyncCourierDirectory - list of (key, courierKey, proof) <->

These commands manage connections on the network (along with Router.py and
PeerBeat).
Coordinated port opening for testing.

    Is there a simpler way to do this...

main client class - terminal

    This should start either with or without a peer.

    should it stream input or be a REPL??

    REPL is easiest to implement.

    just duplicate commands from HTTP API or KISS with one BSON interface...
    ugh then we loose async...

"""
