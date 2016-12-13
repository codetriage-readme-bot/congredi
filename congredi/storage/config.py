#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Config Loading
"""
import yaml, os, traceback
import logging
logger = logging.getLogger('congredi')
def configArr():
	config = {}
	try:
		with open(os.path.expanduser('~') + '/.congredi.yml','r') as f:
			config = yaml.load(f.read())
		if any (k not in config for k in ('admins','users')):
			logger.warning('Config does not contain "admins" or "users"')
	except:
		trace = traceback.format_exc()
		logger.danger(trace)
		# generate key, save to yaml
		config['admins'] = ['foo', 'bar']
		config['users'] = ['toto', 'bagel']
	return config
