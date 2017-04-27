#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
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

"""
import sys
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
# congredi/utils/compat.py                    27      7    74%   12-16, 28, 38
