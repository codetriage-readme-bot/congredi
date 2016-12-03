# WebLinks

> A Terrible, Digital Govermnent - [delegito.io](//delegito.io)

[![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.png?label=ready&title=Ready)](https://waffle.io/Thetoxicarcade/congredi)
[![Build Status](//travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi)
[![Documentation Status](//readthedocs.org/projects/congredi/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest)
[![GitHub commits](https://img.shields.io/github/commits-since/thetoxicarcade/congredi/v0.0.1.svg?maxAge=2592000)](https://github.com/thetoxicarcade/congredi)
[![Code Climate](https://codeclimate.com/github/Thetoxicarcade/congredi/badges/gpa.svg)](https://codeclimate.com/github/Thetoxicarcade/congredi)
[![Issue Count](https://codeclimate.com/github/Thetoxicarcade/congredi/badges/issue_count.svg)](https://codeclimate.com/github/Thetoxicarcade/congredi)

[![PyPI version](https://badge.fury.io/py/delegito.svg)](https://badge.fury.io/py/delegito)
[![Gratipay User](https://img.shields.io/gratipay/user/Thetoxicarcade.svg?maxAge=2592000)](https://gratipay.com/~Thetoxicarcade/)
`congredi-interface` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-interface.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-interface/) `congredi-api` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-api.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-api/)
[Website](//delegito.io)/[Onion](//aldskfj.onion) ***offline***


# About

Congredi is a digital political engine for speciallized STV elections.
This allows you to conduct experiments on forms of voting, issue debates,
coalitions, & practical government improvements.

It is made available in several formats:

* a staticly served Nginx Angular app (& docker image)
* a Firefox extension
* a JSON Web Token authorized Flask API, Celery Queue, & Mongo DB (& docker image)
* a python library for Pip

The crypto involves:

* threshold-signature OpenPGP for jurisdiction appointments
* threshold-encrypted Secure Secret Sharing for jurisdiction admin
* Shuffle-Sum for private vote results
* OpenPGP signatures for public polls
* OpenPGP Key Signing & keyservers for authorizations
* Tor & WebRTC for peer communications

# Doc Specializations

## Users / Sysadmins? [User Guide](UserGuide)
Guides involved in getting up and running with Congredi instances.

## Developers / Contributors? [API](APIs) & [Build](building) docs
Guides for getting under the hood with the overlying architecture.

## Cryptographers / Skeptics? [Methodology](methodology)
Guides for working with the underlying libraries, objects, & functions.




# Overview


# Public Key

## Vetting users (certify/revoke keys)

The public key of the user, stored within the database, gets updated by
a valid certification of that user by someone else.

## Account Management (public key or fernet symetric)

Recovering account details involves using the private key on client-side
JS, without it, the account shouldn't be recoverable.

## Jurisdiction Administration (Threshold keys)

Unlocking jurisdiction options requires consent from all the parties
sharing a common secret (technically blockchain threshold sigs, not
Secure Secret Sharing, unless I can find an uncompromising method).

## Voting and elections (Shuffle-Sum)

Elections contain both a publicly signed poll ranking, and a private
shuffle-sum operation. The poll is attached to the user's profile,
while the Shuffle-Sum operation is used to verify their actual private vote.# Mongo db

This is a quick fix until using valid SQL linker tables.

```
var user = {
    profile:{
        links:{twitter:""},
        location:"",
        bio:"",
        other:{},
        },
    publicKey:"",
    email:"",
    organiations:{regid:"sig"},
    following:{
        user:{
            sig:"sig", //certification
            trust:["issueid"], //whitelist
            distrust:["issueid"] //blacklist
            }
        },
    opinions:{
        opinion:{
            sig:"sig", //certification
            trust:["issueid"], //whitelist
            distrust:["issueid"], //blacklist
            poll:"date", //proposed vote day
            open:["issueid","issueid"] //your open preference, your actual vote is private
            }
        }
    };
var opinion = { // can be sub-items as well
    author:"", // org/user
    sig:"sig",
    trust:["trust"], // whitelist
    distrust:["distrust"], // blacklist
    opinionCascade:["opinionid","opinionid"], // components of proposed ballot choice
    content:"",
    citations:{
        hash:{record:"recordid",user:"userid",sig:"sig",relation:"disent"},
        hayy:{record:"recordid",user:"userid",sig:"sig",relation:""}
        }
    };
var organization = { // parliment, district, party, registrar, auditor, etc
    bio:{ address:"addr", phone:"tel", site:"url"},
    pubkey:"key",
    vetting:{process:"",type:""},
    staff:{ id:sig },
    issues:{ id:sig }, //opinions
    voters:{
        pub:{ id:sig },
        priv:{ token:taken }
        }
    };
var election = {
    district:"", // managing org
    date:"",
    ballot:{ item:sig },
    status:{ user:"ready-fail-success" },
    poll:{ user:position },
    result:["stv-item"]
    };
```Hackers, take a peek:

* [JSON specification](json)
* [Angular routes](routes)
* [Database queries](data_structures)
* [Cryptography Usage](cryptography)# Cheatsheet
```
/api/
	/auth/          [POST|DELETE] - db
	/token/         [GET|DELETE] - JWT
	/bearing/       [GET|DELETE] - JWT (longer time)

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
```
# Auth
* URL: `/api/auth/`

## Registering
* Format: **POST**
* Data: `{ username:'username',password:'hashed',email:'email'}`
* Results: `{Authoriation: aldkfj}`

## Canceling
* Format: **DELETE**
* Data: ``
* Results: `{goodbye:'for now'}`

# Token
Heartbeat tokens for faster endpoints
* URL: `/api/token/`
* Format: **GET**/**DELETE**
* Data:
* Results:

# Bearing
Oauth token for longer storage
* URL: `/api/bearing/`
* Format: **GET**/**DELETE**

# Search
Data queries
* URL: `/api/search/:type?offset=0?limit=0`
* Format: **GET**
* Data: {term:"",author:""}
* Results:
Will need to get Traefik / Swarm up correctly.
```
[docker-machine]
consul
manager
[ssl]
traefik 443,80
    [/public]
    nginxa 80 -> pages
    nginxb
    [/api]
    app1 5000 -> redis (celery)
    app2
    app3
    worker1 redis (celery) -> mongo
    worker2
    worker3
    [net isolation]
    tor1 :9050,:9001 /api -> app1? /public -> nginxa?
    tor2
    tor3
    [fail2ban]
    email server 995 -> auth ssl
[private net]
redis :6379
mongo :27017
onionbalance
```

Found it. Traefik. https://docs.traefik.io/user-guide/swarm/
https://docs.docker.com/engine/userguide/networking/get-started-overlay/
# Cheatsheet

```
/#/
    /auth/ -> login hover
    /settings/ -> item number
    /create/ -> district,election,point
    /:user/ -> follow,message
    /:district/ -> join
        /admin
        /:election/ -> register,vote,audio
```
# Home `/#/`
* src: [interface/views/home.html](//github.com/thetoxicarcade/congredi/interface/views/home.html)


# Login Hover `/#/auth/`
* src: [interface/views/auth.html](//github.com/thetoxicarcade/congredi/interface/views/auth.html)


# Settings Bulletin `/#/settings/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# Create page `/#/create/`
* src: [interface/views/create.html](//github.com/thetoxicarcade/congredi/interface/views/create.html)


# User page `/#/:user/`
* src: [interface/views/user.html](//github.com/thetoxicarcade/congredi/interface/views/user.html)


# District page `/#/:district/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# District Admin page `/#/:district/admin`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)


# Election page `/#/:district/:election/`
* src: [interface/views/?.html](//github.com/thetoxicarcade/congredi/interface/views/)

# Travis-CI - [file](//github.com/Thetoxicarcade/congredi/blob/master/.travis.yml)

Build process:
1. install nose2, setuptools-lint, mkdocs, requirements.txt
2. docker builds
3. setup.py builds & lints
4. mkdocs builds

# Docker Hub

1. pre-fetch npm & bower packages:
    ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"```

2. Pre-build gulp tasks:
    ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"```

3. Build, start, & scale:
    `docker-compose build && docker-compose up -d && docker-compose scale workers=2`

> docker run -ti --rm -e DISPLAY=$DISPLAY \
>  -v /tmp/.X11-unix:/tmp/.X11-unix ideas


## congredi-interface
1. install npm env, nginx
2. run npm, bower, & gulp

## congredi-api
1. install extra python-dev
2. install listed requirements
3. setup.py build, test, install lint

# PyPI

1. setup.py build test install
2. setup.py metadata sdist upload

# Firefox Extension# indexes

* `mkdocs.yml`
* `*/index.md`

# code examples

```
foobar{]}

```# Get Involved
0. Hop on Waffle to view the current GitHub issues:
    [![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.png?label=ready&title=Ready)](https://waffle.io/Thetoxicarcade/congredi).
1. Clone repo:
    `git clone github.com/thetoxicarcade/congredi && cd congredi`
2. Hack some things
3. Submit some pull requests

# eslint - [linter's config](//github.com/Thetoxicarcade/congredi/blob/master/interface/gulpfile.js)

Single-Quotes, tabs, 1tbs, camelCase.

# pylint - [linter's config](//github.com/Thetoxicarcade/congredi/blob/master/interface/gulpfile.js)

Pep8 excepting that indentations are spaces.

## Optimizing Python Library

cython compiler. . .

# Nose2 - [test directory](//github.com/Thetoxicarcade/congredi/blob/master/delegito/tests)

by-file/library tests, `test_flask.py` -> `api.py` for instance.

# Jasmine - [test directory](//github.com/Thetoxicarcade/congredi/blob/master/interface/js/tests)

by-file/library tests, `demo.js` -> `app.js` for instance.

## Edits to Angular UI js

1. run `gulp clean`
2. make edits to `/js/`
    * if you change a library call, change its `.test.js`
    * if you change a controller or otherwise, change its `view`
3. run `gulp` (should run tests as well)
# Peer addresses: DHT (think Tor/Torrent)

```
// kadmillia mainline?
peer name:discovery points[ ]?
// also signed onto a per-user federated blockchain?
// last seen = chain segment signed by that peer?
```
# Pubkey identities: Network Of Trust (think GNU/CA)
```
// export as openpgp compatible
key : signed by [ ]?
// also signed into a per-user federated blockchain?
```

# Individual Transactions: mongo/JSON (think noSQL/API)
```
// blockchain
{
    data: {
        id: id_person,
        vote: persons_vote,
        poll: persons_poll,
        sig: vote_poll_id_sig
    },
    checksum: hash_data,
    previous: hash_prevous,
    position: hash_previous_checksum
}

```
# Blockchains (think litecoin/bitcoin)
```
genesis (advertized genesis block signed by that jurisdiction)
    starting a genesis block is identity (not automatic reputation) based
validated (blocks confirmed by jurisdiction are 20 deep)
    can use a fraction system based on the size of jurisdiction
ordered (blocks that have reached a best effort consensus ordering)
    most rapid exchange becomes law
unordered (new data blocks not explicitly ordered)
    new votes go here
open vote blocks (the consensus on who is yet to vote)
    based on their pubkey, if they were authorized to vote and hadn't yet
```
# Expired data (think freenet/gnunet)
```
old data is cleared out if it's not relevant to a live election / jurisdiction
* peers (dht rendesvous, .onion address data)
* users (openpgp data)
* transactions (unordered, non-confirmed transactions)
* blockchains (creation gives expiry? seems fair)
```
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

router + storage striping plausible deniability# Private Ballot
One of the ideas for having a vote is having a non-coerced private ballot,
which is why the end-to-end verification for Delegito does not prove you
voted in a particular way, only that your vote counted.# Creating a Jurisdiction
To create a jurisdiction, go to the "Create" tab and select "Jurisdiction".
Fill out any geographic information, the owner's public key(s), & organization bio.

Next, fill out the jurisdiction's methodology, from the number of members to
the proceedings of a vote.

# Joining a Jurisdiction
To join a jurisdiction, visit its page and select "Join". The administrators,
upon vetting you, will sign your account's public key certifying that you
are a member.

# Creating an election
To create an election, go to the create tab and select "election". If you are
not the administrator of the jurisdiction you would like to have the election
at, you must navigate to their page and "propose an election".End-User guides:

* [Installing](installation)
* [System Administrators](sysadmin)
* [Your Profile](yourself)
* [Jurisdictions](groups)
* [Voting](votes)
# Firefox
Use the firefox store or this handy url.

# PyPI
For the library: `pip install delegito`

# Docker / etcd cluster
`FROM ericoflondon/congredi-api`
or
`FROM ericoflondon/congredi-cluster`

The API/Worker subsections run different commands:

```
        command: python /code/worker.py
        command: python /code/api.py
```
# SSL cert management

# mail server management# Register to vote
Select a jurisdiction you're a voter of (see [groups](groups)).

Select any of the elections scheduled in your jurisdiction, and
after deciding if you'd like to participate, select "Register to vote".

# Casting a vote
For a public vote, rank your choices, then click submit.

If you would not like your true vote to be publicly certified,
select "vote differently than polled", and a second ballot will be displayed.

# Checking a vote
When casting your vote, you have the ability to end-to-end verify the public polls,
and that your private ballot was counted as cast. To do so, view your voting record
under your profile, if it says "ready to audit" you may select to audit your vote.

> Note: you cannot prove to anyone you voted a particular way, read more
[here](//congredi.readthedocs.io/en/latest/Methodology/zeroknowledge/).# Editing your bio
Select the gear(:gear:) from the top right corner of the UI.
Make any changes you feel necessary, then click save.

# Viewing your PGP Public Key
click the info button next to your fingerprint.