import sys
import logging
from twisted.internet import reactor
from twisted.internet.error import CannotListenError
from ..packets.factory import BareFactory
from .arguments import MainOptions
#from .defaultpath import normalConfigPath
from ..utils.logs import passLevel
from ..utils.errors import CongrediError
# ChatFactory(RedisVar,)
logger = logging.getLogger('congredi')


def run(GivenConfig):
    f = BareFactory(GivenConfig)
    # better than previous coordination/failover/errback method.
    # will still need to read DB and try to
    # say hello to hosts that aren't localhost.
    try:
        reactor.listenTCP(8123, f)
        print('listening as server')
    except CannotListenError:
        print('Whoops, being a client')
        reactor.connectTCP("localhost", 8123, f)
    try:
        reactor.run()
    except KeyboardInterrupt:
        pass
    except CongrediError as e:
        logger.critical("Congredi failed: %s", e.message)
    finally:
        print('\ngoodbye...')


def runOld():
    """
        pull args (ports, debug level, config location)
        http api, redis addr/port, neo4j addr/port
    """
    args = MainOptions.parse_args()
    if args.help:
        MainOptions.print_help()
        sys.exit(0)
    # pull config location
    #configPath = normalConfigPath()
    # if args.config:
    #    configPath = args.config
    # did I set the right config order in the spec?
    # pylint: disable=unused-variable
    #config = configArr(configPath)

    # setting log level from arguments.
    passLevel(args)

    # try to start on specific port, fail over
