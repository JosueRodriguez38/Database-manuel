from config.dbconfig import pg_config
from config.tuple_config import user_supp_admin
from config.tuple_config import inserted
import psycopg2

# The purpose of the supplier DAO is to extract the information regarding a supplier that has been requested

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s " % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2.connect(connection_url)

    # The getAll function returns all the suppliers in the database
    def getAllSuppliers(self):

        result=[]
        result.append(user_supp_admin)
        return result

    # This function receives an id and returns the supplier with the same id if it exists
    def getSupplierById(self, sid):
        r = []
        if sid==user_supp_admin[0]:
            r=user_supp_admin

        return r

    # This function receives an id and returns the items that a supplier has, if the input id matches the id of an
    # existing supplier. This is accomplished via a natural join of tables Resources, Supplier, and
    # the relationship Supplies
    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select rid, rname, rmaterial, rcolor, rprice, qty from resources natural inner join supplier natural inner join supplies where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Displays all the suppliers in the city that was received as input
    def getSuppliersByCity(self, city):
        result = []
        if city == user_supp_admin[6]:

            result.append(user_supp_admin)

        return result

    # Allows for the change of the name, city and phone number of the supplier whose id matches the input, if it exists
    def update(self,sid, sname, scity, sphone):
        if sid==user_supp_admin[0]:
            r = []
            r.append(sname)
            r.append(scity)
            r.append(sphone)
            return r
        else:
            return

    # deletes the supplier specified by the input id if the supplier exists
    def deleteSupplier(self,sid):

        if sid == user_supp_admin[0]:
            result = user_supp_admin
            return result
        else:
            return