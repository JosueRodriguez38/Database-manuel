
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
        cursor = self.conn.cursor()
        query = "select username from user_credentials natural inner join users where userid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def getPasswordByUid(self, uid):
        cursor = self.conn.cursor()
        query = "select password from user_credentials natural inner join users where userid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result



    def getCredetialsByUid(self, uid):
        cursor = self.conn.cursor()
        query = "select username, password from user_credentials natural inner join users where userid = %s"
        cursor.execute(query, (uid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result



    def getPasswordByUsername(self, Username):
        cursor = self.conn.cursor()
        query = "select password from user_credentials where username = %s"
        cursor.execute(query, (Username,))
        result = cursor.fetchone()
        self.conn.commit()
        return result


    def getAllUsersNames(self):
        cursor = self.conn.cursor()
        query = "select * from user_credentials order by username"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result