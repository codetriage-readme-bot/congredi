#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
error utilities
Timing objects for UnitTest

    these use Blender's color codes class,

    as well as the setUp/tearDown functions for timing.
pairwise implementation (used in ../storage/Router)

should this be used anywhere else, or moved into Router?
# Pairwise recipe
Log management (could use twisted's log utility, but must have formating ability)

    maintenance: look for usage across codebase, simplify (keep it simple, stupid)
command line options

	a bit frustrating for out-of-order parameters (see below)
design i.e.:
	valid:
		congredi --port 9797 --debug peer
		congredi peer --redis 6999
	invalid:
		congredi --port --debug peer (port required)
	tested:
		python -m congredi
	unimplemented:
		congredi peer --debug (master options can't be reordered??)
		docker run congredi peer (options dependent on arg #'s?)
    progressBars for functions (could use on client side)
These are markdown sources for Diff problems.
randomness function libraries

    extensions need to include lists, dictionaries, and empty objects.

    Possibly rename this into oracle.py

    current tests only use a small amount of hex code, could use base64 for
    wider oracle range of valid ASCII, or even a UTF-8 oracle for some of the
    STR functions.
PY3 Compatibility

Will need to look into each of the times this is used.

    cast to binary:
    ./congredi/storage/test/test_censor.py
    ./congredi/storage/censor.py
    ./congredi/storage/zlibs.py

    cast to string:
    ./congredi/storage/diff.py

    possibly better to just cast diff's output to binary, fewer steps involved


    running an if statement on the required types,
    better to check a global PY3 in areas where PY2/PY3 return STRs differ.

Yaml Config Loading - & default configs

    need to reset the config design for this...

"""
#from twisted.python import log
# log.startLogging(sys.stdout)

from __future__ import absolute_import
from __future__ import unicode_literals
from __future__ import print_function
import logging
logger = logging.getLogger('congredi')
import binascii
import os
import unittest
import math
import time
import yaml
import errno
import argparse
import sys
import random as rand
from six.moves import range
from progressbar import AnimatedMarker, Bar, Counter, ETA, \
    Percentage, Widget, ProgressBar, Timer
from itertools import tee
from six.moves import zip
# CharDet...
if sys.version_info < (3, 0):
    PY3 = False
    # base_str = (str, unicode)
    text_type = unicode  # pylint: disable=undefined-variable
    # pylint: enable=undefined-variable
    bin_type = str
else:  # not used in py2 coverage
    PY3 = True
    # base_str = (bytes, str)
    text_type = str
    bin_type = (bytes, bytearray)

# will need to write tests for these
# and in general just avoid not telling what type variables are

logger = logging.getLogger('congredi')

defaultPath = os.path.expanduser('~') + '/.local/congredi/'
defaultFile = 'congrediSettings.yaml'

class CongrediError(Exception):
    """
        Ability to raise a custom error or family of errors (design - family of errors to raise?)
        pulling other Error classes from other files into here.

        Key/Connection/Command style errors?
    """
    pass

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
    # pylint: disable=undefined-variable
    if any(k not in config for k in ('admins', 'users')):  # need test case
        logger.warning('Config does not contain "admins" or "users"')
        raise CongrediConfigError('Config missing %s' % k)
    # pylint: enable=undefined-variable
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
    'settings': {
        'listen': {
            'api': "0.0.0.0:443",
            'peer': "0.0.0.0:8800"
        },
        'proxy': {
            'allowed': True,
            'preferred': False,
            'available': {
                ".onion": True,
                ".i2p": False
            }
        },
        'private': {
            'router': "abcd",
            'server': "defg"
        },
        'storage': {
            'redis': "localhost:",
            'neo4j': "localhost:"
        }
    },
    'addrbook': {
        'routes': {
            'peers': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            },
            'rendesvous': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            },
            'couriers': {
                'nicname': {
                    'addr': "192.168.2.55:9090",
                    'key': "a4232323"
                }
            }
        },
        'guests': {
            'admins': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            },
            'users': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            },
            'servers': {
                'nicname': {
                    'key': "ab4332",
                    'rendesvous': {
                        'nic': {
                            'addr': "192.168.2.55",
                            'key': "23232323"
                        }
                    }
                }
            }
        }
    }
}


def ensureBinary(statement):
    if not isinstance(statement, bin_type):
        print('EnsureBinary: swapping to binary from %s' % type(statement))
        statement = statement.encode('utf8')
    return statement


def ensureString(statement):
    if not isinstance(statement, text_type):
        print('EnsureString: swapping to string from %s' % type(statement))
        statement = statement.decode('utf8')
    return statement


def passLevel(args):
    """take an args object and set the log level"""
    level = logging.WARNING
    if args.quiet:
        level = logging.CRITICAL
    if args.verbose:
        level = logging.INFO
    if args.debug:
        level = logging.DEBUG
    formatLevel(level)
hexy = {
    # Fix to bypass dictionary as "english"
    "0": b"Zero", "1": b"One", "2": b"Two", "3": b"Three",
    "4": b"Four", "5": b"Five", "6": b"Six", "7": b"Seven",
    "8": b"Eight", "9": b"Nine", "a": b"Apple", "b": b"Boy",
    "c": b"Cat", "d": b"Dog", "e": b"Echo", "f": b"Fox",
    # unused past this
    "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November",
    "O": "Oscar", "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform", "V": "Victor",
    "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
}


def pick_range(num):
    x = []
    for _ in range(0, num):
        x.append(rand.randrange(0, 32))
    return x


def random():
    return os.urandom(15)


def hexify(r):
    return binascii.hexlify(r)


def phony(h):
    return b" ".join(hexy[a] for a in str(h)[2:-1])


class Speed(Widget):
    FORMAT = '%6.2f %s/s'
    PREFIXES = 'okMGTPEZY'

    def update(self, pbar):
        """Updates the widget with the current SI prefixed speed."""

        if pbar.seconds_elapsed < 2e-6 or pbar.currval < 2e-6:  # =~ 0
            scaled = power = 0
        else:
            speed = pbar.currval / pbar.seconds_elapsed
            power = int(math.log(speed, 1000))
            scaled = speed / 1000.**power

        return self.FORMAT % (scaled, self.PREFIXES[power])
# http://www.artima.com/weblogs/viewpost.jsp?thread=240845
# class example(object):
#     # def wrapped(*args):
#     #     f(args)
#     # return wrapped
#     def __init__(self, f):
#         self.f = f
#     def __call__(self, *args):
#         """
#         The __call__ method is not called until the
#         decorated function is called.
#         """
#         print "Inside __call__()"
#         self.f(*args)
# @example
source = b"""
Hello, *world*! This is a ~~good~~marvelous day!
Here is an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk

You can also have fenced code blocks:

```
import this
```
"""

source2 = b"""
Hello, *world*! This is a ~~good~~marvelous day!
Here was an auto link: https://example.org/

Le me introduce you to [task lists] (https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

- [ ] eggs
- [x] milk
- [x] ten


```
import this
```
"""
empty = b""
empty2 = b"""


Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu viverra lacus. Vestibulum a est a felis posuere pellentesque ac sit amet sem. Aliquam erat volutpat. Phasellus eleifend, felis eget lobortis dapibus, ligula purus rhoncus massa, placerat pharetra urna lacus vel ex. Proin finibus pellentesque dui id mollis. Vestibulum id nibh libero. Quisque at odio velit. Morbi ac viverra velit, ut elementum erat. Cras varius, odio sit amet rutrum porta, purus mi sollicitudin sem, vel rutrum nisl augue non arcu. Fusce sagittis sem commodo lorem malesuada, eu vestibulum lacus laoreet. Proin nibh dolor, blandit sed dictum in, imperdiet nec risus. Quisque sem est, ultrices consequat urna id, malesuada vestibulum lacus. Nullam congue lectus sed mollis sagittis. Vestibulum pellentesque vulputate lacus sed consectetur.

Etiam gravida justo vel venenatis convallis. Vestibulum a nunc at justo vestibulum mattis quis eget erat. Sed semper hendrerit orci. In in sapien vitae purus sodales gravida vel et nunc. Fusce porttitor, ante molestie blandit laoreet, massa libero commodo ex, at suscipit lacus dolor a elit. Aenean ut erat non sapien blandit ullamcorper eget sit amet velit. Nullam mattis nulla a urna maximus pellentesque vel in enim. Nullam lorem dui, ullamcorper id velit et, consequat porta justo. Duis lacus ipsum, finibus eget est ut, accumsan interdum augue. Maecenas convallis sed enim non rhoncus. Vestibulum at commodo nisl, id ultricies ex. Morbi nunc est, semper et efficitur ac, porta ut leo. Donec eu facilisis justo.

Maecenas congue suscipit lacus vitae rhoncus. Donec dictum lacinia elementum. Proin fringilla ante elit. Maecenas lacus arcu, eleifend non consectetur non, aliquet tincidunt lectus. Duis a fringilla massa, sed varius neque. Phasellus placerat non risus a finibus. Curabitur ut eros mattis, ornare purus ac, volutpat ante. Mauris at auctor ligula, et lacinia metus. Ut vitae neque mattis, placerat sem et, blandit neque. Donec rutrum, neque non feugiat laoreet, enim nibh pharetra purus, eu tincidunt nisi metus id lacus. Vestibulum efficitur venenatis velit, quis sodales orci laoreet et. Nunc vestibulum non tortor eget tempor. Duis congue nunc eu gravida consectetur. Vivamus sagittis ante nec erat accumsan, nec interdum risus varius. Nullam ac turpis blandit, viverra augue ultrices, pellentesque mauris. Nulla eu faucibus ante.

Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Vivamus molestie nibh vel felis consequat, ut consectetur arcu porta. Duis in tortor ultrices mi malesuada mattis at quis turpis. Morbi enim nunc, accumsan id leo eget, egestas blandit dolor. Aenean id sapien quis quam sollicitudin laoreet in in lacus. Suspendisse potenti. Donec ut erat malesuada, tempus nunc ac, sodales ante. Phasellus ac felis ultricies, ullamcorper ipsum sed, vehicula urna. Nullam ac lacus euismod, fermentum justo a, ornare massa. Vestibulum sed mollis nulla. Nulla turpis tellus, porttitor a sodales ac, lacinia sodales ex. Donec scelerisque magna vel nisi cursus malesuada. Aenean vehicula dictum enim, eu semper nisi dictum nec. Nunc in leo varius, sagittis odio in, rhoncus purus.

Nulla facilisi. Vestibulum aliquet est a ex lobortis vulputate. Curabitur at ultrices orci. Vestibulum varius nulla eu aliquet finibus. Donec id posuere est. Donec sit amet lacus vitae nulla dapibus imperdiet sed id ante. Nullam vitae lorem tristique, lobortis justo sit amet, porta erat. Donec quam lorem, ullamcorper sit amet tortor hendrerit, tempor dapibus magna. Cras viverra consectetur odio, quis iaculis lacus ornare vel. Pellentesque id lorem eu sapien vehicula molestie in vitae purus. Sed ac sapien non purus dapibus lacinia. Integer vel nunc vel tortor tempor accumsan. Integer tempor sit amet dolor in posuere. Etiam maximus odio quis felis blandit scelerisque. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.
"""


def together(interval=10000):
    things = [AnimatedMarker(), " ", Counter(), "/{} ".format(interval),
              Percentage(), ' ', Speed(), ' ', Bar(), ' ', Timer(), ' ', ETA()]
    pbar = ProgressBar(widgets=things, maxval=interval).start()
    for i in range(interval):
        pbar.update(i + 1)
    pbar.finish()
# together(100000000)


def formatLevel(level):
    """set formatting based on a level"""
    formatting = "%(levelname)s %(filename)s(%(lineno)d) %(funcName)s: %(message)s"
    if level == logging.DEBUG:
        formatting = "%(asctime)s[%(name)s:%(levelname)s]%(filename)s(%(lineno)d) %(funcName)s: %(message)s"
    setLog(level, formatting)

# load defaults from config file (we recheck this when passed a new config...)
defaults = configArr(defaultPath)

MainOptions = argparse.ArgumentParser(add_help=False)
# no option ("--help") - (Design -h if -h is used as host.)
MainOptions.add_argument(
    '-u', '--help', help='prints usage/help', action='store_true')

# option required after this ("--port 8000")
MainOptions.add_argument('-p', '--port', default=8800,
                         help='congredi port', type=int)
# no option after this (bool flag "--debug")
MainOptions.add_argument(
    '-c', '--config', type=argparse.FileType('r'),
    help='config file to use', default=defaultPath + defaultFile)

# verbosity options

MainOptions.add_argument(
    '-q', '--quiet', action='store_true', help='set logging to CRITICAL (wordy-)')
MainOptions.add_argument(
    '-v', '--verbose', action='store_true', help='set logging to INFO (wordy+)')
MainOptions.add_argument(
    '-d', '--debug', action='store_true', help='set logging to DEBUG (wordy++)')

subparsers = MainOptions.add_subparsers()

ClientOptions = subparsers.add_parser(
    "client", help="client to interact with congredi", add_help=False)
ClientOptions.add_argument('-h', '--host', default='localhost',
                           help='Host to connect to')  # (see design, above)
ClientOptions.set_defaults(which='client')

PeerOptions = subparsers.add_parser(
    "peer", help="run congredi peer instance", add_help=False)
# redis port on options - int/socket
PeerOptions.add_argument('-r', '--redis', default=6379, help='redis port')
# neo4j port options - int/socket
PeerOptions.add_argument('-n', '--neo4j', default=7474, help='neo4j port')
PeerOptions.set_defaults(which='peer')


def setLog(level, formatting):
    """Set log level"""
    logger.setLevel(level)
    fh = logging.StreamHandler()
    fh.setLevel(level)
    fm = logging.Formatter(
        formatting,
        "%Y-%m-%d %H:%M:%S")
    fh.setFormatter(fm)
    logger.addHandler(fh)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))




class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
warning = bcolors.WARNING + 'Timing Warning' + bcolors.ENDC + \
    ': Test Took ' + bcolors.BOLD + '%.2f' + bcolors.ENDC + \
    's (threshold ' + bcolors.FAIL + '%.2f' + bcolors.ENDC + 's)'


class TimedTestCase(unittest.TestCase):
    threshold = 0
    def setUp(self):
        #print('ran setup for %s' % self.id())
        self.threshold = .5
        self._time_started = time.time()

    def tearDown(self):
        elapsed = time.time() - self._time_started
        if elapsed > self.threshold:
            print((warning % (elapsed, self.threshold)))


def whoops(err):  # test
    """
    The default errback (design - set as default errback?)
    can't pull traceback, which is unfortunate.
    """
    #trace = traceback.format_exc()
    # traceback.print_exc()
    logger.critical(err)
