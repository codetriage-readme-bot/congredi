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


def configArr():
    config = {}
    try:
        with open(os.path.expanduser('~') + '/.congredi.yml', 'r') as f:
            config = yaml.load(f.read())
        if any(k not in config for k in ('admins', 'users')):
            logger.warning('Config does not contain "admins" or "users"')
    except (yaml.reader.ReaderError, IOError):
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
        with open(os.path.expanduser('~') + '/.congredi.yml', 'w+') as f:
            f.write(yaml.dump(config))
    return config
