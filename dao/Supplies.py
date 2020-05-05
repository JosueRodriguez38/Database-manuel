from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class SuppliesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAlltheResourcesOfuser(self,userid):
        cursor = self.conn.cursor()
        query = "select firstname, name,ammount,cost from users natural inner join supplies natural inner join resources where userid = %i;"
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllResourcesIdOfAUser(self,userid):
        cursor = self.conn.cursor()
        query = "select resourceid from users natural inner join supplies userid = %i;"
        cursor.execute(query,[userid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getUserIdFromResourceId(self,resourceid):
        cursor = self.conn.cursor()
        query = "select userid from users natural inner join supplies resourceif = %i;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertSuppies(self,resourceid,userid):
        cursor = self.conn.cursor()
        query = "insert into supplies(resourceid,userid) values(%i,%i));"
        cursor.execute(query, [resourceid,userid])
        supplieid = cursor.fetchone()[0]
        self.conn.commit()
        return supplieid