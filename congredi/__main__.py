#import pudb
#pu.db
import logging
logger = logging.getLogger('delegito')
logger.setLevel(1)
fh = logging.StreamHandler()
fh.setLevel(1)
#if logger.level > logging.WARNING:
fm = logging.Formatter(
	"%(asctime)s[%(name)s:%(levelname)s]%(filename)s(%(lineno)d) %(funcName)s: %(message)s",
	#"%(levelname)s %(filename)s(%(lineno)d) %(funcName)s: %(message)s",
	"%Y-%m-%d %H:%M:%S")
fh.setFormatter(fm)
logger.addHandler(fh)

logger.info('Congredi __main__ in use.')
# pylint: disable=unused-import
from .main.client import CongrediClient as client
from .main.peer import CongrediPeer as peer
