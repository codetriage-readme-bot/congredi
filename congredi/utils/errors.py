class CongrediError(Exception):
    """The Root Error Class."""
    pass


class BadIFace(CongrediError):
    """A Bad Interface (Redis, Neo4j, JWT, etc)."""
    pass


class BadVersion(BadIFace):
    """The Version is Wrong"""


class BadConfig(CongrediError):
    """The Config you gave won't work."""
    pass


class ConnectError(CongrediError):
    """A problem with a connection"""
    pass


class NoRoute(ConnectError):
    """No route to host"""
    pass


class DepsError(CongrediError):
    """An error in a dependancy"""
    pass


class CensorError(CongrediError):
    """The Censor Failed"""
    pass
