def whoops(err):  # test
    """
    The default errback (design - set as default errback?)
    can't pull traceback, which is unfortunate.
    """
    logger.critical(err)
