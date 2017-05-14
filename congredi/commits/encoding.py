def stateEncoding(statement):
    """Return character encoding"""
    statement = ensureBinary(statement)
    try:
        return chardet.detect(statement)['encoding']
    except UnicodeDecodeError:  # needs a test
        return None
