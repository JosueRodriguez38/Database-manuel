from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class ConsumerDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=127.0.0.1" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # this function allows for the localhost to display all consumers and their information
    def getAllConsumer(self):
        result = []
        result.append(user_cons)
        return result

    # this function allows you to change the information of the consumer tuple
    # whose id matches the input id
    def update(self,cid,sname,scity,sphone):
        if cid==user_cons[0]:
            r = []
            r.append(sname)
            r.append(scity)
            r.append(sphone)
            return r
        else:
            return

    # deletes the consumer data if the id matches the input
    def delete(self,cid):
        if cid == user_cons[0]:
            result = user_cons
            return result
        else:
            return

    # returns consumer information if the input id matches an id in the database
    def getConsumerById(self,cid):
        if cid == user_cons[0]:
            return user_cons
        else:
            return