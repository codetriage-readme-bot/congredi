from ..utils.compat import ensureBinary
from ..utils.errors import CensorError
import chardet


def stateEncoding(statement):
    binaryStatement = ensureBinary(statement)
    try:
        return chardet.detect(binaryStatement)['encoding']
    except UnicodeDecodeError:  # needs a test
        raise CensorError('Unicode Decode Failed')


class censor():
    """
    A censor that checks the encoding of a message.
    """
    encodings = ['UTF-8', 'ASCII']

    def __init__(self, encodings=None):
        self.encodings = encodings

    def checkGood(self, statement):
        statementType = stateEncoding(statement)
        return statementType in self.encodings
