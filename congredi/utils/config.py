#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
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
    if any(k not in config for k in ('admins', 'users')):  # need test case
        logger.warning('Config does not contain "admins" or "users"')
        raise CongrediConfigError('Config missing {0}'.format(k))
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
    'public':{
        'hostname':'0.0.0.0',
        'port':8000,
        },
    'private':{
        'routerKey':'abcd',
        'terminalKey':'efgh',
        },
    'proxy':{
        'allowed':True,
        'prefered':False,
        'available':{
            '.onion':True,
            '.i2p':False
            }
        },
    'admins':[],
    'users:':[],
    'peers':[],
    }