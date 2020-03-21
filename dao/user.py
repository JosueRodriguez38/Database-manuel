from config.dbconfig import pg_config
from config.tuple_config import inserted,admin
import psycopg2


class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                             pg_config['user'],
                                                             pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def insertConsumer(self, sname, scity, sphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (sname, scity, sphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertAdmin(self, sname, scity, sphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (sname, scity, sphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertSupplier(self, sname, scity, sphone):
        #cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        #cursor.execute(query, (sname, scity, sphone))
        #sid = cursor.fetchone()[0]
        #self.conn.commit()

        return inserted[0]

    def insertAdminById(self, aid, sname, scity, sphone):
        if aid==admin[0]:
            return admin[0]
        else:
            return

    def getAdminById(self, aid):
        pass