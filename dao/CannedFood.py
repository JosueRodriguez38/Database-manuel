from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class CannedFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCannedFood(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true order by primaryingridient;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getCannedFoodByID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getBCannedFoodByResourceID(self,resourceid):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,primaryingidient, ounces, expirationdate from canned_food natural inner join resources where resourceid=%s;"
        cursor.execute(query, [resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByFlavour(self, flavour):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true and primaryingridient = %s order by expirationdate;"
        cursor.execute(query, (flavour,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true and userid = %s order by primaryingridient;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true and cost <= %s order by primaryingridient;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllCannedFoodByUserIDAndPrimaryIngredient(self, uid, ingredient):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, primaryingridient, purchaseTypeName, ounces, expirationdate, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join canned_food where aviable = true and userid = %s and primaryingridient = %s;"
        cursor.execute(query, (uid, ingredient,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result
