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
