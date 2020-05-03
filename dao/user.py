from config.dbconfig import pg_config

import psycopg2

# The purpose of the user DAO is to extract and insert the information regarding a consumer that has been requested

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insertUser(self,accountType, name, lastName, phone, email):
        cursor = self.conn.cursor()
        query = "insert into users(accounttype,firstname,lastname,phone,email,status) values (%i, %s, %s,%s,%s,true) returning uid;"
        cursor.execute(query, (accountType, name, lastName, phone, email))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def updateUserInfo(self,accountType, name, lastName, phone, email):
        return

    def RemoveUserById(self, uid):
        return

    def getUserById(self, uid):
        return

    def getAllUsersByStatus(self,status):
        return

    def getAllUserByAccountType(self, accountType):
        cursor = self.conn.cursor()
        query = "SELECT * FROM users left join account_type on accounttype = accounttypenumber where accounttype=%s"
        cursor.execute(query, accountType)
        users = cursor.fetchone()[0]
        self.conn.commit()
        return users


    def getAccountTypes(self):
        return





