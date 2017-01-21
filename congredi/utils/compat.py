import sys
# CharDet...
if sys.version_info < (3, 0):
    PY2 = True
    PY3 = False
    base_str = (str, unicode)
    text_type = unicode
    bin_type = str
else:
    PY2 = False
    PY3 = True
    base_str = (bytes, str)
    text_type = str
    bin_type = (bytes, bytearray)

# will need to write tests for these
# and in general just avoid not telling what type variables are

def ensureBinary(statement,hexr=False):
    if not isinstance(statement, bin_type):
        print('EnsureBinary: swapping to binary from %s' % type(statement))
        if not hexr:
            statement = statement.encode('utf8')
        else:
            statement = statement.encode('hex')
    return statement
def ensureString(statement,hexr=False):
    if not isinstance(statement, text_type):
        print('EnsureString: swapping to string from %s' % type(statement))
        if not hexr:
            statement = statement.decode('utf8')
        else:
            statement = statement.decode('hex')
    return statement
