#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Yaml Config Loading - & default configs
"""
import yaml
import os
import traceback
import logging
logger = logging.getLogger('congredi')

defaultPath = os.path.expanduser('~')


def configArr(pathname=defaultPath):
    config = {}
    try:
        with open(pathname + '/.congredi.yml', 'r') as f:
            config = yaml.load(f.read())
        if any(k not in config for k in ('admins', 'users')):  # need test case
            logger.warning('Config does not contain "admins" or "users"')
    except (yaml.reader.ReaderError, IOError):  # need test case
        trace = traceback.format_exc()
        # traceback.print_exc()
        logger.critical(trace)
        # generate key, save to yaml
        config['admins'] = set(['selfkey'])
        config['users'] = set(['selfkey'])

        config['peers'] = []  # default public congredi peer lists (key/ip)

        config['sitekey'] = set(['newkey'])
        config['routekey'] = set(['othernewkey'])
        logger.warning('Writing new config')
        with open(pathname + '/.congredi.yml', 'w+') as f:
            f.write(yaml.dump(config))
    return config
