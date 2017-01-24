#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PY3 Compatibility

Will need to look into each of the times this is used.
"""
import sys
# CharDet...
# pylint: disable=redefined-variable-type
if sys.version_info < (3, 0):
    PY3 = False
    # base_str = (str, unicode)
    # pylint: disable=undefined-variable
    text_type = unicode
    # pylint: enable=undefined-variable
    bin_type = str
else:  # not used in py2 coverage
    PY3 = True
    # base_str = (bytes, str)
    text_type = str
    bin_type = (bytes, bytearray)
# pylint: enable=redefined-variable-type

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
