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


This repo handles letting anonymous people reach compromises. Unfortunately the 
codebase doesn't extend to github comments. Don't be any form of oppressive or
slandarous towards another person or group.

Explaining an endpoint allows other people to use it correctly. If the
docs won't match the code anymore, change them too. Use markdown code
blocks for snippets, when in doubt run `mkdocs serve` to try them out.

Before submitting your changes, run `setup.py test` &/|| `docker-compose build`,
just to see that everything superficially checks out. If you'd made changes
outside the scope of the tests, it might not register as failing, but it's
a good, basic step. The testing system currently uses `nose2` & `jasmine`.

Insofar as the editor you use can format, and the test suite used can lint it.
Currently, that's `eslint` & `pylint` (`python setup.py lint`).
In other words, if the machines can both catch and help you, style it that way.

