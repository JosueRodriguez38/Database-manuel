from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class DryFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllDryFood(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost, expirationdate from Resources natural inner join resource_type natural inner join purchase_type natural inner join dry_food where aviable = true order by resourceid;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getDryFoodByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost, expirationdate from Resources natural inner join resource_type natural inner join purchase_type natural inner join dry_food where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllDryfoodByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, name, resourceTypeName, purchaseTypeName, ammount, cost, expirationdate from Resources natural inner join resource_type natural inner join purchase_type natural inner join dry_food natural inner join supplies where aviable = true and userid = %s order by name;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllDryfoodByName(self, name):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, purchaseTypeName, ammount, cost, expirationdate from Resources natural inner join resource_type natural inner join purchase_type natural inner join dry_food where aviable = true and name = %s order by resourceid;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result