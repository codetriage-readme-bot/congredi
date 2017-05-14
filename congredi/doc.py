"""
Remove keys no subscribed user cares about.

    Uses orphaning test code (mostly through directed children)

    user -> trees

    user <- trees

    check every tree, if it has a user, check to see if the user cares.
    if not, delete it.

Diff utils (instead of using a raw git library - a design problem)

    move to unified diff forward/backward
Neo4j Mock code

    will need to pull from Neo4j examples

Compression/packetization functions

    splitting diffs / compressing for sending
PGP key & IP routing
Resolves routes (usefull for commands I have now misplaced)

This has the same name as another file in proofs/router.py...

Also, need to find a Zero Knowledge Proof of the length
of a connection without indicating where on the connection
someone is (which would tell people if their neighbor can
be harassed).
Map a directed acyclic graph from one user to another,
and map objects that people use (possibly a minimum number of people use)

    pull from Neo4j examples
Redis Mock code

    The actual code is using RSet/RGet, outside of classes.
    Need the @defer.inlineCallbacks to work within a class :/

censor things objectionable to you, rather than store/query/communicate them
the current library is old and might simply need to include regexes...
(Feature: Should add the ability to publish your router's censor settings - #E)

These functions operate very primatively, if you wanted to censor content you'll
**REALLY** have to beef them up.

Encrypted Storage pretty-much wants content to be a binary mess, so I suppose
that's another use for the censor.

What it needs to do is provide that the object in question is a valid:

* diff
* sig
* pubkey
* markdown object

And that it contains no information that could be harmful. It'll be decoded,
escaped, into a markdown format, so XSS is still a problem, but should obey
the encoding we give it (ASCII/UTF-8/others?)


    this object doesn't update censor properties in tests
Render markdown. (possibly not needed on the python end of things)
py-gfm>=0.1.3

    migrate this out

Mock Storage code

    should abstract the get/set methods into a mock storage.
Redis database commands & mutexes, not exactly the objects needed

Interface, in the case that someone wants to use something besides Redis/Neo4j,
for instance hadoop or bigtable....
Check if peer is online, check latest trees that people subscribe to

    Two functions are missusing Ask() parameters from the rewrite.
    Make sure to neaten everything and set that in the spec.
periodically resolve a git tree

    recursive ask from contacts on tree contents.
Periodically audit a vote

    recursive on vote process (see commands/proofs/vote)

    delete? send error back to other clients? certify bit?

Timing tests, not using assert (need to test color?)
error utilities tests

    whoops (traceback)
    CongrediError (an error class)
        - pull in all subclasses into these error class tests
test logger
progress test (count to 1000)
## all code should be importing from ..logger, not using import logging.
options testing
test oracle functions.s
Yaml Config Loading - & default configs
test the STV implementation
ThresholdPGP tests...
tests for curve
Testing hashes (currently testing only one hash, should test more?)
    test via oracle? Use external utility? sha256sum with ps/shell?

    - check number of KDFs
Testing the padding (and underlying function I suppose)
Still hanging around with a KDF...

    check # of KDF rounds
test AES

    - document

peerBeat tests
zlib tests

    See PeerBeat. Should Implement.
garbageCollect tests

    see garbageCollect.

    Here we test:
        user-A->repo-B, repo-C(orphaned): GC should remove C, leave B
        Repo-B(orphaned): GC should remove B
        user-A->repo-B,repo-C user-D->repo-B: GC should not error on multiple parents

tests on the simplistic censor library.
tests on the diff utils
HTML tests

moving away from using HTML on the Python client.
Abstract Interface Provider tests

    basic checks for good/bad interface code:

    the interfaces need to have certain functions, and while
    we're not checking that the outputs match (feature), this
    is a basic check that the stated internal API of a developed
    driver matches.

    These checks are of an interface that has what it
    needs, and one that doesn't have everything, to test
    our CongrediBadInterfaceError & CongrediIncompatibleVersionError

    Feature: Check function return signatures on an abstract-method?

neo4j tests
Redis object tests
test router. These functions probably need relocating.

testing coordination code

    Again, will need to simplify this.
client tests

    Can /technically/ execute StringTransport, while the actual connections
    have problems these tests are finding.
Runner tests

    again, simplify API

    tests will run consecutive store/retrieves on good/bad values

    a partial integration test, but peer-peer AMP has a regression
    that's not in StringTransport :/
Runner tests

    need to call Run() functions in a testing framework

JWT tokens (for web interface, mostly, as all peer operations function on
public key cryptography)

JWT tokens can be one of:

* Good
* Expired
* Invalid

And granting them should not take database access. They are meant to
figure out if a user is auth'd without using the database to do so.
Test register via email

The auths must be able to be tested as:

* Valid
* Expired
* Invalid
Test register via OAuth

The auths must be able to be tested as:

* Valid
* Expired
* Invalid

Test register via PGP sig

The auths must be able to be tested as:

* Valid
* Expired
* Invalid
Test register via SMS

The auths must be able to be tested as:

* Valid
* Expired
* Invalid

factory tests

    regression on StringTransport vs real TCP needs addressing...
general tests for string behavior. If these fail,
lots of tests that use string interpolation will
error because of the string interpolation.

This is a good catch for people writing a test
with a buggy print statement.

Then again, there's always pylint.

Thank You Py2/3 compatibility problems...protocol tests

    regression on StringTransport vs real TCP needs addressing...

AMP Types, which have a to-string/from-string mentality, though
they don't actually have to be strings, just of a finite length.

    Each of these tests runs b'b' == obj.fromString(obj.toString(b'b'))

    PrivAES
    EncBlob
    ObjBlob
    ObjSig
    EncSig
    EncHash
    ObjHash
    EncPubKey
    ObjPubKey
    EncAddress
    ObjAddress
    EncBool

    We can (and should) run oracles to test the limits of the types (empty/lists/dicts/objs)
    That'll be using an extended ../utils/censorable.py for lists/dicts

test commands
FileSystem operations:
test passport.

Individual grants must be able to be:
* Valid
* Premature (add this to other tests as well...)
* Expired
* Invalid

Reasons to grant that need testing:

* Behavior          Good/Bad/Unknown - Recommendation Good/Bad/Unknown
* Manual Overide    Good/Bad
* Key Trust Depth   -1, 0, 1...
* Server Load       always grant, long term grant, probationary grant, short term grant, never grant

Possibly need to rework that server-load one
test settings.

Some commands should be supreceeded by the config file or argument parameters.

That's probably something that could be in the config file:

Ordering:
 - options
 - config
 - database

Each of the setting options should be able to be changed and viewed.
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
