# Get Involved
0. Hop on Waffle to view the current GitHub issues:
    [![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.png?label=ready&title=Ready)](https://waffle.io/Thetoxicarcade/congredi).
1. Clone repo:
    `git clone github.com/thetoxicarcade/congredi && cd congredi`
2. pre-fetch npm/bower, gulp
    * ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"```
    * ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"```
    *
2. Hack some things
    * `setup.py build test install`
    * `setup.py metadata sdist upload`
    * `docker-compose build && docker-compose up -d && docker-compose scale workers=2`
3. Submit some pull requests



# Style guides

I'm not currently conforming to the results
from `eslint` or `pylint`, but I could be.

## Python

Pep8 excepting Tabs. Running `check.sh` can replace lots of it.

## JS

single-quote, tab, 1tbs camelCase

# CI / Unit Tests

Travis runs compilation, unit tests, a docker assembly, & mkdocs builds.



## Nose2 - [test directory](//github.com/Thetoxicarcade/congredi/blob/master/delegito/tests)

by-file/library tests, `test_flask.py` -> `api.py` for instance.

## Jasmine - [test directory](//github.com/Thetoxicarcade/congredi/blob/master/interface/js/tests)

by-file/library tests, `demo.js` -> `app.js` for instance.

