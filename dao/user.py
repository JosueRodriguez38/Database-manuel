from config.dbconfig import pg_config

import psycopg2

# The purpose of the user DAO is to extract and insert the information regarding a consumer that has been requested

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # inserts a new user with given informaiton
    def insertUser(self,accountType, name, lastName, phone, email):
        cursor = self.conn.cursor()
        query = "insert into users(accounttype,firstname,lastname,phone,email,status) values (%s, %s, %s,%s,%s,true) returning userid;"
        cursor.execute(query, (accountType, name, lastName, phone, email))
        uid = cursor.fetchone()[0]
        self.conn.commit()
        return uid

    def updateUserInfo(self,accountType, name, lastName, phone, email):
        return

    def RemoveUserById(self, uid):
        return

    def getUserById(self, userid):
        cursor = self.conn.cursor()
        query = "select userid, accounttypename, firstname, lastname , phone, email,adressline1, adressline2, pueblo, pais, codigopostal,googlemapurl, status from users natural inner join location left join account_type on accounttype=accounttypenumber  where userid= %s;"
        cursor.execute(query, [userid])
        users = cursor.fetchall()
        self.conn.commit()
        return users

    def getAllUsersByStatus(self,status):
        return

    # returns users if they are suppliers or consumers or admins
    def getAllUserByAccountType(self, accountType):
        cursor = self.conn.cursor()
        query = "select userid, accounttypename, firstname, lastname , phone, email,adressline1, adressline2, pueblo, pais, codigopostal,googlemapurl, status from users natural inner join location left join account_type on accounttype=accounttypenumber where accounttype=%s;"
        cursor.execute(query, [accountType])
        users = cursor.fetchall()
        self.conn.commit()
        return users

    def getUsersByAccountTypeAndLocation(self,accountype,location):
        return


    def getAccountTypes(self):
        return





