from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllConsumer(self):
        result = []
        result.append(user_cons)
        return result

    def update(self,cid,cname,ccity,cphone):
        if cid==user_cons[0]:
            r = []
            r.append(cname)
            r.append(ccity)
            r.append(cphone)
            return r
        else:
            return

    def deleteConsumer(self,cid):
        if cid == user_cons[0]:
            result = user_cons
            return result
        else:
            return

    def getConsumerById(self,cid):
        if cid == user_cons[0]:
            return user_cons
        else:
            return