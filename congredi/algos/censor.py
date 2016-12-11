#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
censor things objectionable to you, rather than store/query/communicate them
the current library is old and might simply need to include regexes...
"""
import logging, entropy, chardet
import pycld2 as cld2
from profanity import profanity
logger = logging.getLogger('delegito')

class censor():
    def __init__(self, encodings, languages, profanity=False, wordlist=None, listhash=None):
        self.encodings = encodings
        self.languages = languages
        self.profanities = profanity
        if wordlist: profanity.load_words(wordlist)
        elif listhash:
            content = getSHA(listhash).split('\n'); profanity.load_words(wordlist)
    def profanity(self, statement):
        return profanity.contains_profanity(statement)
    def entropy(self, statement):
        return entropy.shannon_entropy(statement)
    def language(self, statement):
        try: return cld2.detect(statement)[2][0][0]
        except: return None
    def encoding(self, statement):
        try: return chardet.detect(statement)['encoding']
        except: return None
    def check(self, content):
        return not self.block(content)[0]
    def block(self, statement):
        res_encode = self.encoding(statement)
        res_encode_ok = res_encode in self.encodings
        res_lang = self.language(statement)
        res_lang_ok = res_lang in self.languages
        res_profanities = self.profanities and self.profanity(statement)
        res = True
        #if res_encode_ok and res_lang_ok and not profanity:
        if res_encode_ok:
            if res_lang_ok:
                if not res_profanities:
                    res = False
        res_human = "SAFE"
        if res: res_human = "BLOCK"
        print(res,res_human, res_encode,res_lang,res_encode_ok,res_lang_ok,res_profanities)
        return res, res_human, res_encode, res_lang, res_encode_ok, res_lang_ok, res_profanities

logger.info('loaded congredi/algos/censor.py')




