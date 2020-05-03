
from config.dbconfig import pg_config
import psycopg2

# The purpose of the user DAO is to extract and insert the information regarding a consumer that has been requested

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)


    def getUsernameByUid(self, uid):
        return


    def getPasswordByUid(self, uid):
        return


    def getCredetialsByUid(self, uid):
        return


    def getPasswordByUsername(self, Username):
        return


    def getAllUsersNames(self):
        return