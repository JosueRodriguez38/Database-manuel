from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Class handles the general resource class (where the resourceID comes from), not specific typed objects

class SuppliesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAlltheResourcesOfuser(self,userid):
        cursor = self.conn.cursor()
        query = "select firstname, name,ammount,cost from users natural inner join supplies natural inner join resources where userid = %s;"
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllResourcesIdOfAUser(self,userid):
        cursor = self.conn.cursor()
        query = "select resourceid from users natural inner join supplies where userid = %s;"
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getUserIdFromResourceId(self,resourceid):
        cursor = self.conn.cursor()
        query = "select userid from users natural inner join supplies where resourceid = %s;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertSupplies(self,resourceid,userid):
        ncursor = self.conn.cursor()
        query = "INSERT INTO supplies(resourceid,userid) values(%s,%s) returning suppliesid;"

        ncursor.execute(query, (resourceid,userid))
        suppliedid = ncursor.fetchone()[0]
        self.conn.commit()
        return suppliedid