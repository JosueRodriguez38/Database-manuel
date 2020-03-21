from config.dbconfig import pg_config
from config.tuple_config import inserted,admin,user_supp_admin
import psycopg2


class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insertConsumer(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertAdmin(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertSupplier(self, uname, ucity, uphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(uname, ucity, uphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (uname, ucity, uphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertAdminById(self, aid, uname, ucity, uphone):
        if aid==admin[0]:
            return admin[0]
        else:
            return

    def getAdminById(self, aid):
        if aid == admin[0]:
            return user_supp_admin
        else:
            return

    def deleteAdmin(self, aid):
        if aid == user_supp_admin[0]:
            result = user_supp_admin
            return result
        else:
            return