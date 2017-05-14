from ..storage.abstracts.redis import absRedis
from ..storage.abstracts.neo4j import absNeo4j
from ..storage.abstracts.JWT import absJWT
from ..utils.errors import BadIFace
# import redis?


class configplugin(object):

    def __init__(self):
        self.redis = None
        self.neo4j = None
        self.JWT = None

    def setRedis(self, driver):
        if not isinstance(driver, absRedis):
            raise BadIFace('Bad Interface!')
        # if not storage.version() == '1.0':
        #     raise BadVersion('Non-compatible version!')
        self.redis = driver

    def setNeo4j(self, driver):
        if not isinstance(driver, absNeo4j):
            raise BadIFace('Bad Interface!')
        self.neo4j = driver

    def setJWT(self, driver):
        if not isinstance(driver, absJWT):
            raise BadIFace('Bad Interface!')
        self.JWT = driver
# class Base(metaclass=ABCMeta):
