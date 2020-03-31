from config.dbconfig import pg_config
from config.tuple_config import inserted,admin,user_supp_admin
import psycopg2

# The purpose of the user DAO is to extract and insert the information regarding a consumer that has been requested

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # inserts a user's name, city and phone linked to and account (name, user, password)
    def insertConsumer(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    # inserts an admin user with their name, city and phone
    def insertAdmin(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    # inserts a supplier user and their information
    def insertSupplier(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    # inserts an admin with a specified id if it exists
    def insertAdminById(self, aid, uname, ucity, uphone):
        if aid==admin[0]:
            return admin[0]
        else:
            return

    # returns an admin with the specified admin id if it exists
    def getAdminById(self, aid):
        if aid == admin[0]:
            return user_supp_admin
        else:
            return

    # deletes the admin user if it exists
    def deleteAdmin(self, aid):
        if aid == user_supp_admin[0]:
            result = user_supp_admin
            return result
        else:
            return