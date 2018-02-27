# Congredi [Our Documentation](//congredi.github.io/congredi/)
> Peered Democratic Documents

> For the static webclient written in JS, see [delegito.io](//delegito.io)

`Congredi` is a python program that allows a community to help
individuals write changes to repositories of text, that are then
voted on by organizations to find a consensus.

***Slowly waking up this project...***


Think that's useful? Give it a try! If you have any feature requests or questions,
hop on over to gitter & [waffle](https://waffle.io/congredi/congredi). I'm looking for contributors on some issues.

Build status (2.7 full coverage, windows & 3.* python have spotty test coverage)

**updates: python3 pylint is not automatically installed correctly...**

linux tests run pylint on 2.7, and unit tests across 3.3-3.6
mac tests run 2.7 & 3.3

Windows tests only run green & setup.py install across 2.7, 3.3-3.6 x32 + 3.5-6 x64. we don't test 3.3-4 on x64

Linux/Mac: [![Build Status Travis](https://travis-ci.org/congredi/congredi.svg?branch=master)](https://travis-ci.org/congredi/congredi)
Windows: [![Build status Windows](https://ci.appveyor.com/api/projects/status/mo003x9ygpnb316q?svg=true)](https://ci.appveyor.com/project/Thetoxicarcade/congredi)
Docker: [![Build status Codeship](https://codeship.com/projects/d1cee4c0-b9b1-0134-40ad-5e5884b780cb/status?branch=master)]()
[![Open Source Helpers](https://www.codetriage.com/thetoxicarcade/congredi/badges/users.svg)](https://www.codetriage.com/thetoxicarcade/congredi)

[![Documentation Status](https://readthedocs.org/projects/congredi/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest)
[![GitHub commits](https://img.shields.io/github/commits-since/congredi/congredi/v0.0.2-alpha.svg)](https://github.com/congredi/congredi)
[![PyPI](https://img.shields.io/pypi/v/congredi.svg)]()

Docker images:
[`congredi:`](https://hub.docker.com/r/congredi/congredi/)
[![](https://images.microbadger.com/badges/image/congredi/congredi.svg)](https://microbadger.com/images/congredi/congredi "Get your own image badge on microbadger.com")
[`delegito:`](https://hub.docker.com/r/congredi/delegito/)
[![](https://images.microbadger.com/badges/image/congredi/delegito.svg)](https://microbadger.com/images/congredi/delegito "Get your own image badge on microbadger.com")
[`micro-peer:`](https://hub.docker.com/r/congredi/micro-peer/)
[![](https://images.microbadger.com/badges/image/congredi/micro-peer.svg)](https://microbadger.com/images/congredi/micro-peer "Get your own image badge on microbadger.com")
