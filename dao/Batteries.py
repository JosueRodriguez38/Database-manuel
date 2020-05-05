from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class BatteriesDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)


    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries where aviable = true order by baterytype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryById(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries where aviable = true and resourceid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllBatteriesByBatteryType(self, batteryType):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries where aviable = true and baterytype = %s;"
        cursor.execute(query, (batteryType,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllBatteriesByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries natural inner join supplies natural inner join users where aviable = true and userid = %s order by baterytype;"
        cursor.execute(query, (uid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllBatteriesByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries where aviable = true and cost <= %s order by baterytype;"
        cursor.execute(query, (cost,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllBatteriesByUserIDAndBatteryType(self, uid, batteryType):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, baterytype, purchaseTypeName, quantityperpack, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join batteries natural inner join supplies natural inner join users where aviable = true and userid = %s and baterytype= %s;"
        cursor.execute(query, (uid, batteryType,))
        result = []
        for row in cursor:
            result.append(row)
        return result