#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs

    need to reset the config design for this...

"""
from __future__ import absolute_import
from __future__ import unicode_literals
import yaml
import os
import errno
import logging
from .whoops import CongrediError, whoops
logger = logging.getLogger('congredi')

defaultPath = os.path.expanduser('~') + '/.local/congredi/'
defaultFile = 'congrediSettings.yaml'


class CongrediConfigError(CongrediError):
    """Config file threw up"""
    pass


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
# congredi/utils/config.py                    49     17    65%   30,
# 38-39, 44-45, 50-57, 68-76
