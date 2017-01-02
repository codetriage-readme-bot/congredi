#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Running code
"""

import logging
logger = logging.getLogger('congredi')
from twisted.internet import stdio, reactor
from ..factory import CongrediPeerFactory
from .client import CongrediClient
from .coord import fileCoord
from ..utils.logger import setLog
from ..utils.config import configArr
from ..utils.options import MainOptions
from ..utils.whoops import CongrediError

"""Could neaten this..."""


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
        inst = CongrediPeerFactory(
            port=args.port, redisPort=args.redis,
            neo4jPort=args.neo4j, initialKey=None)
    elif args.which == 'client':
        logger.info('options.run() client')
        inst = CongrediClient(
            host=args.host, port=args.port,
            clientKey=None)
        stdio.StandardIO(inst)
    try:
        pf = CongrediPeerFactory()
        inst = CongrediPeerFactory()
        hst, prt = fileCoord.read()
        print(hst, prt)
        # ServiceNameUnknownError on korora, not alpine...
        reactor.connectTCP(host=hst, port=int(prt), factory=pf)
        #endpoints.serverFromString(reactor, "tcp:{}".format(args.port)).listen(app)
        pr = reactor.listenTCP(0, inst)
        inst.host = pr.getHost().host
        inst.port = pr.getHost().port
        print 'started on port {}'.format(inst.port)
        fileCoord.write(inst.host, inst.port)
        reactor.run()
    except KeyboardInterrupt:
        pass
    except CongrediError as e:
        print("Congredi failed: {}".format(e.message))
    finally:
        print('goodbye...')

if __name__ == '__main__':
    run()
