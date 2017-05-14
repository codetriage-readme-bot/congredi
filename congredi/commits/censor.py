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
        statement = ensureBinary(statement)
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
