#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
censor things objectionable to you, rather than store/query/communicate them
the current library is old and might simply need to include regexes...
(Feature: Should add the ability to publish your router's censor settings - #E)
"""
import logging
import entropy
import chardet
import pycld2 as cld2
from profanity import profanity
logger = logging.getLogger('congredi')


def stateProfanity(statement):  # needs a test
    """Profanity checks (Design: should probably be in a class - #A)"""
    return profanity.contains_profanity(statement)


def stateEntropy(statement):  # needs a test
    """Return the entropy of an item (Feature: could use the histogram - #B)"""
    return entropy.shannon_entropy(statement)


def stateLanguage(statement):
    """"Language detection (Design: still a bare except - #C)"""
    try:
        return cld2.detect(statement)[2][0][0]
    except:
        return None


def stateEncoding(statement):
    """Return character encoding"""
    try:
        return chardet.detect(statement)['encoding']
    except UnicodeDecodeError:  # needs a test
        return None


class censor():
    """
    A censor that keeps along the allowed encodings, languages, and profanity.
    Can be used to check (returns false if bad) or block (returns true if bad).
    """

    def __init__(self, encodings, languages, checkProfanity=False, wordlist=None, listhash=None):
        self.encodings = encodings
        self.languages = languages
        self.profanities = checkProfanity
        """loading wordlists (Design: should be part of class - A)"""
        # needs a test
        if wordlist:
            profanity.load_words(wordlist)
        # elif listhash:
        #	content = getSHA(listhash).split('\n'); profanity.load_words(wordlist)

    def check(self, statement):
        """Opposite result (Design: return the rest of the objects? - #D)"""
        return not self.block(statement)[0]

    def block(self, statement):
        res_encode = stateEncoding(statement)
        res_encode_ok = res_encode in self.encodings
        res_lang = stateLanguage(statement)
        res_lang_ok = res_lang in self.languages
        res_profanities = self.profanities and stateProfanity(statement)
        res = True
        # if res_encode_ok and res_lang_ok and not profanity:
        if res_encode_ok:
            if res_lang_ok:
                if not res_profanities:
                    res = False
        res_human = "SAFE"
        if res:
            res_human = "BLOCK"
        """Results objects.... (Design: reorder? - #D)"""
        return res, res_human, res_encode, res_lang, res_encode_ok, res_lang_ok, res_profanities
