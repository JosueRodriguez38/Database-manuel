from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def getAllSuppliers(self):

        r = []
        r.append(1)
        r.append('Manuel')
        r.append('787-123-4567')
        r.append('manuel.rodriguez7@upr.edu')
        r.append('mayaguez')
        result=[]
        result.append(r)
        return result

    def getSupplierById(self, sid):
        r = []
        if sid==1:
            r.append(1)
            r.append('Manuel')
            r.append('787-123-4567')
            r.append('manuel.rodriguez7@upr.edu')
            r.append('mayaguez')


        return r

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, pmaterial, pcolor, pprice, qty from resources natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByCity(self, city):
        r = []
        result = []
        if city == 'mayaguez':
            r.append(1)
            r.append('Manuel')
            r.append('787-123-4567')
            r.append('manuel.rodriguez7@upr.edu')
            r.append('mayaguez')
            result.append(r)

        return result

    def insert(self, sname, scity, sphone):
        cursor = self.conn.cursor()
        query = "insert into supplier(sname, scity, sphone) values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sname, scity, sphone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid