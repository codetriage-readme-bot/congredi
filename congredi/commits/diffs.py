def resolveUnifiedDiff(md1, md2, l1, l2):
    """Resolving unified diff instead of using libgit (design/feature - make one of them work #G)"""
    # must use python-patch to use unified diffs...
    md1 = ensureString(md1)
    md2 = ensureString(md2)
    diff = unified_diff(md1.splitlines(
        1), md2.splitlines(1), l1, l2, lineterm='', n=0)
    print(diff)
    result = '\n'.join(list(diff))
    return result


def resolveDiff(md1, md2):
    md1 = ensureString(md1)
    md2 = ensureString(md2)
    """Ndiffs (for right now unless resolveUnifiedDiff #G can be solved)"""
    diff = ndiff(md1.splitlines(1), md2.splitlines(1))  # , lineterm='', n=0)
    result = ''.join(list(diff))
    #result = '\n'.join(list(diff))
    return result


def rebuildFile(diff, option):
    """Restore an Ndiff"""
    result = ''.join(restore(diff, option))
    return result


def tick(md1, md2):
    """Get a storeable object"""
    unified = resolveDiff(md1, md2)
    print(type(unified))
    compressed = compressDiff(unified)
    return compressed


def tock(compressed, direction):
    """Decompress a stored object"""
    uncompressed = uncompressDiff(compressed)
    uncompressed = ensureString(uncompressed)
    original = '\n'.join(list(restore(uncompressed, direction)))
    return original
