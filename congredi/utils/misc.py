from itertools import tee
from six.moves import zip
from os import path


def expand(pathname):
    return path.expanduser(pathname)


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return list(zip(a, b))
