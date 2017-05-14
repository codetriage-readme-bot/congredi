from storage.abs import absRedis, absNeo4j, absJWT
from errors import BadIFace
# import redis?
class configplugin(object):
    def setRedis(self,driver,ip,port):
        if not isinstance(storage, absRedis):
            raise BadIFace('Bad Interface!')
        self.redis = driver(ip,port)
    def setNeo4j(self,driver,ip,port):
        if not isinstance(storage, absNeo4j):
            raise BadIFace('Bad Interface!')
        self.neo4j = driver(ip,port)
    def setJWT(self,driver):
        if not isinstance(storage, absJWT):
            raise BadIFace('Bad Interface!')
        self.JWT = driver("None","None")
