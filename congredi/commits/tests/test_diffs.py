class test_zlib(TimedTestCase):
    things = [
        'a',
        'b',
        'c'
    ]
    splits = None
    thing1 = None
    res = None

    def test_split(self):
        """
            Split something into chunks
            passes if it doesn't throw errors
            next design should split into a known number of chunks and assert()
        """
        self.threshold = .2
        self.splits = chunkSplit(source)
        print((len(self.splits)))

    def test_compression(self):
        """Compress, Uncompress, ensure equal"""
        self.threshold = .2
        self.thing1 = compressDiff(source2)
        self.res = uncompressDiff(self.thing1)
        print('New')
        print(self.res)
        print('Original')
        print(source2)
        assert self.res == source2

    # test split error-raising

    # test compression error-raising
class test_diff(TimedTestCase):

    def test_resolve_ndiff(self):
        """NDiff of source, source2, rebuild diff"""
        self.threshold = .2
        print('The Diff:')
        result = resolveDiff(source, source2)
        print((''.join(result)))
        print('The Original:')
        orig = rebuildFile(result, 1)
        print((''.join(orig)))

    def test_compression(self):
        """Full-integrated Tick/Tock compression"""
        self.threshold = .2
        # Direct conversion
        res = tick(source, source2)
        beep = tock(res, 1)
        print('Compression test:')
        print(beep)

    def test_splits(self):
        """Split & recombine, check hashes."""
        self.threshold = .2
        data = {'pieces': {}}
        comp = tick(empty, empty2)
        print(('compressed %d' % len(comp)))
        data['length'] = len(comp)
        data['hash'] = hashlib.sha256(comp).digest()
        splt = chunkSplit(comp)
        for c in splt:
            key = hashlib.sha256(c).hexdigest()
            print(type(c))
            data['pieces'][key] = binascii.hexlify(c)
        for k, v in data['pieces'].items():
            print(k, binascii.hexlify(v))
        jnd = b''.join(splt)
        final = hashlib.sha256(jnd).digest()
        print(('join %d' % len(jnd)))
        print(('hash: %(one)s\nhash: %(two)s' %
               {'one': binascii.hexlify(data['hash']), 'two': binascii.hexlify(final)}))

    def test_uni(self):
        """Unified Diffs."""
        self.threshold = .2
        diff = resolveUnifiedDiff(
            source, source2,
            'congredi/test/core/algos/a.txt',
            'congredi/test/core/algos/b.txt')
        print(type(diff))
        # not python3 compatible
        #patch = fromstring(silenceInsanity(diff))
        # print((patch.errors))
        #patch.revert(0, root='.')
        #patch.apply(0, root=".")
