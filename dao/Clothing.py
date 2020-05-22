from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class ClothingDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothing(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing where aviable = true order by agecategory;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getClothingByresourceID(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllClothingByAgeCategory(self, age):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing where aviable = true and agecategory = %s order by size;"
        cursor.execute(query, (age,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingBySize(self, size):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing where aviable = true and size = %s order by agecategory;"
        cursor.execute(query, (size,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByCost(self, cost):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing where aviable = true and cost <= %s order by agecategory;"
        cursor.execute(query, [cost])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing natural inner join supplies natural inner join users where aviable = true and userid = %s order by agecategory;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllClothingByUserIDAndAgeCategory(self, uid, age):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, name, agecategory, size, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join clothing natural inner join supplies natural inner join users where aviable = true and userid = %s and agecategory = %s order by size;"
        cursor.execute(query, ([uid], age,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertClothing(self, rid, ageCategory, size):
        cursor = self.conn.cursor()
        query = "insert into cards(resourceid,agecategory,size) values(%i,%s,%s) returning clothingid;"
        cursor.execute(query, ([rid], ageCategory,size))
        clothingid = cursor.fetchone()[0]
        self.conn.commit()
        return clothingid