#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities
Timing objects for UnitTest

    these use Blender's color codes class,

    as well as the setUp/tearDown functions for timing.
pairwise implementation (used in ../storage/Router)

should this be used anywhere else, or moved into Router?
# Pairwise recipe
Log management (could use twisted's log utility, but must have formating ability)

    maintenance: look for usage across codebase, simplify (keep it simple, stupid)
command line options

	a bit frustrating for out-of-order parameters (see below)
design i.e.:
	valid:
		congredi --port 9797 --debug peer
		congredi peer --redis 6999
	invalid:
		congredi --port --debug peer (port required)
	tested:
		python -m congredi
	unimplemented:
		congredi peer --debug (master options can't be reordered??)
		docker run congredi peer (options dependent on arg #'s?)
    progressBars for functions (could use on client side)
These are markdown sources for Diff problems.
randomness function libraries

    extensions need to include lists, dictionaries, and empty objects.

    Possibly rename this into oracle.py

    current tests only use a small amount of hex code, could use base64 for
    wider oracle range of valid ASCII, or even a UTF-8 oracle for some of the
    STR functions.
PY3 Compatibility

Will need to look into each of the times this is used.

    cast to binary:
    ./congredi/storage/test/test_censor.py
    ./congredi/storage/censor.py
    ./congredi/storage/zlibs.py

    cast to string:
    ./congredi/storage/diff.py

    possibly better to just cast diff's output to binary, fewer steps involved


    running an if statement on the required types,
    better to check a global PY3 in areas where PY2/PY3 return STRs differ.

Yaml Config Loading - & default configs

    need to reset the config design for this...

"""
#from twisted.python import log
# log.startLogging(sys.stdout)

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import logging
logger = logging.getLogger('congredi')
import binascii
import os
import unittest
import math
import time
import yaml
import errno
import argparse
import sys
import random as rand
from six.moves import range
from progressbar import AnimatedMarker, Bar, Counter, ETA, \
    Percentage, Widget, ProgressBar, Timer
from itertools import tee
from six.moves import zip
# CharDet...

# will need to write tests for these
# and in general just avoid not telling what type variables are

logger = logging.getLogger('congredi')



defaultPath = os.path.expanduser('~') + '/.local/congredi/'
defaultFile = 'congrediSettings.yaml'


# making defaultPath
def makePath(givenPath):
    try:
        os.makedirs(givenPath)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise


def openTest(configFilePath):
    with open(configFilePath, 'r') as f:
        config = yaml.load(f.read())
    # pylint: disable=undefined-variable
    if any(k not in config for k in ('admins', 'users')):  # need test case
        logger.warning('Config does not contain "admins" or "users"')
        raise CongrediConfigError('Config missing %s' % k)
    # pylint: enable=undefined-variable
    return config


def writeConfig(configFilePath, config):
    with open(configFilePath, 'w+') as f:
        f.write(yaml.dump(config))


def generateConfig(config):
    # generate keys & peers, save to yaml
    config['admins'] = set(['selfkey'])
    config['users'] = set(['selfkey'])

    config['peers'] = []  # default public congredi peer lists (key/ip)

    config['sitekey'] = set(['newkey'])
    config['routekey'] = set(['othernewkey'])
    return config

# writing down a default config


def configArr(pathname=defaultPath):
    # start with blank config before loading.
    config = {}
    makePath(pathname)
    try:
        config = openTest(pathname + defaultFile)
    except (yaml.reader.ReaderError, IOError,
            CongrediConfigError) as E:  # need test case
        whoops(E)
        logger.warning('Writing new config')

        config = defaultConfig
        config = generateConfig(config)

        writeConfig(pathname + defaultFile, config)
    return config



defaultConfig = {
    'settings': {
        'listen': {
            'api': "0.0.0.0:443",
            'peer': "0.0.0.0:8800"
        },
        'proxy': {
            'allowed': True,
            'preferred': False,
            'available': {
                ".onion": True,
                ".i2p": False
            }
        },
        'private': {
            'router': "abcd",
            'server': "defg"
        },
        'storage': {
            'redis': "localhost:",
            'neo4j': "localhost:"
        }
    },
    'addrbook': {
        'routes': {
            'peers': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            },
            'rendesvous': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            },
            'couriers': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            }
        },
        'guests': {
            'admins': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            },
            'users': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            },
            'servers': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            }
        }
    }
}
