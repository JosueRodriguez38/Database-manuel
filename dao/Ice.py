from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class IceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, weight, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join ice where aviable = true order by resourceid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceByID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, weight, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join ice where aviable = true and resourceid = %s order by resourceid;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllIceByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, weight, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join ice natural inner join supplies natural inner join users where aviable = true and userid = %s order by resourceid;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, weight, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join ice where aviable = true and cost = %s order by resourceid;"
        cursor.execute(query, (cost,))
        result = []
        for row in cursor:
            result.append(row)
        return result