#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Running code
"""

import logging
logger = logging.getLogger('congredi')
from twisted.internet import stdio, reactor
#from twisted.python import log
#log.startLogging(sys.stdout)
from ..core.Factory import CongrediPeer
from .client import CongrediClient

from ..core.utils.logger import setLog
from ..core.utils.config import configArr
from ..core.utils.options import MainOptions
from ..core.utils.whoops import CongrediError
#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
AMP command tests
"""
	
def run():
	config = configArr()
	initialKey = config['admins']
	initialUsers = config['users']
	print('Settings contain initial key(s): {}'.format(initialKey))
	print('Settings contains the following user(s): {}'.format(initialUsers))


	args = MainOptions.parse_args()

	level = logging.WARNING
	if args.debug:
		level = logging.INFO
	setLog(level)
	if args.which == 'peer':
		logger.info('options.run() peer')
		inst = CongrediPeer(
			port=args.port, redisPort=args.redis,
			neo4jPort=args.neo4j, initialKey=None)
	elif args.which == 'client':
		logger.info('options.run() client')
		inst = CongrediClient(
			host=args.host, port=args.port,
			clientKey=None)
		stdio.StandardIO(inst)
	try:
		pf = CongrediPeer()
		inst = CongrediPeer()
		with open('ort','r') as a:
			prt = a.read().strip('\n')
		print(prt)
		#ServiceNameUnknownError on korora, not alpine...
		reactor.connectTCP(host='127.0.0.1', port=prt,factory=pf)
		#endpoints.serverFromString(reactor, "tcp:{}".format(args.port)).listen(app)
		pr = reactor.listenTCP(0, inst)
		inst.host = pr.getHost().host
		inst.port = pr.getHost().port
		print 'started on port {}'.format(inst.port)
		with open('ort','w+') as a:
			a.write(str(inst.port))
		reactor.run()
	except KeyboardInterrupt:
		pass
	except CongrediError as e:
		print("Congredi failed: {}".format(e.message))
	finally:
		print('goodbye...')
if __name__ == '__main__':
	run()
