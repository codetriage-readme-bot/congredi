#import pudb; pu.db
# pylint: disable=unused-import
from .algos.router import router
from .utils.options import MainOptions
from .term.client import CongrediClient as client
from .factory import CongrediPeerFactory as peer
from .term.run import run

if __name__ == '__main__':
    run()
