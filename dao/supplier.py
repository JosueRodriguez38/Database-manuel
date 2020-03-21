from config.dbconfig import pg_config
from config.tuple_config import user_supp_admin
from config.tuple_config import inserted
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    def getAllSuppliers(self):

        result=[]
        result.append(user_supp_admin)
        return result

    def getSupplierById(self, sid):
        r = []
        if sid==user_supp_admin[0]:
            r=user_supp_admin

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
        result = []
        if city == user_supp_admin[6]:

            result.append(user_supp_admin)

        return result

    def update(self,sid, sname, scity, sphone):
        if sid==user_supp_admin[0]:
            r = []
            r.append(sname)
            r.append(scity)
            r.append(sphone)
            return r
        else:
            return

    def deleteSupplier(self,sid):

        if sid == user_supp_admin[0]:
            result = user_supp_admin
            return result
        else:
            return