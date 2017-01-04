#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Main Running code
"""

import logging, sys
logger = logging.getLogger('congredi')
from twisted.internet import stdio, reactor

from twisted.internet.error import CannotListenError
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.protocol import Factory


from ..factory import CongrediPeerFactory
from .client import CongrediClient
from .coord import fileCoord
from ..utils.logger import passLevel
from ..utils.config import configArr
from ..utils.options import MainOptions
from ..utils.whoops import CongrediError, whoops

"""Could neaten this..."""


def run():
    args = MainOptions.parse_args()
    if args.help:
        MainOptions.print_help()
        sys.exit(0)
    config = configArr()
    initialKey = config['admins']
    initialUsers = config['users']
    logger.info('Settings contain initial key(s): {}'.format(initialKey))
    logger.info('Settings contains the following user(s): {}'.format(initialUsers))

    # setting log level from arguments.
    passLevel(args)

    if args.which == 'peer':
        logger.info('building a peer')
        inst = CongrediPeerFactory(
            port=args.port, redisPort=args.redis,
            neo4jPort=args.neo4j, initialKey=None)
    elif args.which == 'client':
        logger.info('building a client')
        inst = CongrediClient(
            host=args.host, port=args.port,
            clientKey=None)
        stdio.StandardIO(inst)
    try:
        hello_factory = CongrediPeerFactory()
        hello_host, hello_port = fileCoord.read()
        logger.info('We\'re going to say hello to {0}:{1}!'.format(hello_host, hello_port))
        reactor.connectTCP(host=hello_host, port=int(hello_port), factory=hello_factory)

        listening_factory = CongrediPeerFactory()

        user_endpoint = TCP4ServerEndpoint(reactor, int(args.port))
        fallback_endpoint = TCP4ServerEndpoint(reactor, 0)

        def finalCall(failure, factory):
            logger.critical('ephemeral listening port crashed: {0}'.format(failure))
            reactor.stop()
        def useFallback(failure, factory):
            failure.trap(CannotListenError)
            logger.warning('cannot listen on user port choice! falling to ephemeral port.'.format(failure))
            return (fallback_endpoint.listen(factory)
                .addErrback(finalCall, factory)
                .addCallback(onListening))
        
        
        def onListening(port):
            listening_address = port.getHost()
            logger.info('listening on port {0}'.format(listening_address.port))
            listening_factory.host = listening_address.host
            listening_factory.port = int(listening_address.port)
            fileCoord.write(listening_address.host, listening_address.port)


        (user_endpoint.listen(listening_factory)
            .addErrback(useFallback, listening_factory)
            .addCallback(onListening))


        reactor.run()
    except KeyboardInterrupt:
        pass
    except CongrediError as e:
        logger.critical("Congredi failed: {}".format(e.message))
    finally:
        print('\ngoodbye...')

if __name__ == '__main__':
    print('If installed, run "congredi -p 8800 peer", instead of calling python -m congredi')
    run()
