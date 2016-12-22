# Congredi [delegito.io](//delegito.io)
> a BASE representation-of-law-via-cryptography protocol

`Congredi` is a set of utilities and a Twisted server/shell for distributed
document storage, revisioning, and voting on those revisions. Think of it
as a community of git databases where groups of people rank their choices
on how fictional repos should be constructed. Like an STV version of reddit
for documents.

For a website/javascript style client, head over to
[github.com/thetoxicarcade/delegito](//github.com/thetoxicarcade/delegito).

For accademic papers to peruse on the subject, visit [/papers](/papers).

## Looking for contributors!

While I'm building this up, I'm looking for contributors!
Head over to Waffle.io, issuehub.io, or CodeTriage :heart:.

* Waffle: [![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.svg?label=ready&title=Ready)](http://waffle.io/Thetoxicarcade/congredi)
* CodeTriage: [![Code Triagers Badge](https://www.codetriage.com/thetoxicarcade/congredi/badges/users.svg)](https://www.codetriage.com/thetoxicarcade/congredi)



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


[![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.svg?label=ready&title=Ready)](http://waffle.io/Thetoxicarcade/congredi)
[![Build Status](https://travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi)
[![Documentation Status](https://readthedocs.org/projects/congredi/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest)
[![GitHub commits](https://img.shields.io/github/commits-since/thetoxicarcade/congredi/v0.0.1.svg?maxAge=2592000)](https://github.com/thetoxicarcade/congredi)
[![PyPI version](https://badge.fury.io/py/congredi.svg)](https://badge.fury.io/py/congredi)


* `congredi` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi/)
* `delegito` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/delegito.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/delegito/)


