from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Atributos de Baby Food: (Name, Flavor, Size, Expiration Date, ResourceID)

class BabyFoodDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBabyFood(self):
        cursor = self.conn.cursor()
        query = "select name, ammount, cost, flavor,size,expirationDate from baby_food natural inner join resources ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodByResourceID(self,resourceid):
        cursor = self.conn.cursor()
        query = "select name,ammount,cost,flavor, size, expirationdate from baby_food natural inner join resources where resourceid=%s;"
        cursor.execute(query, [resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodByFlavor(self,flavor):
        cursor = self.conn.cursor()
        query = "select name, ammount, cost,size,expirationDate from baby_food natural inner join resources ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodBySize(self,size):
        cursor = self.conn.cursor()
        query = "select name, ammount, cost, flavor,expirationDate from baby_food natural inner join resources where size = %s;"
        cursor.execute(query, [size])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodByExpirationDate(self, expirationdate):
        cursor = self.conn.cursor()
        query = "select name, ammount, cost, flavor,size from baby_food natural inner join resources where expirationdate = %s;"
        cursor.execute(query,(expirationdate))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertBabyFood(self,resourceid, name, ammount, cost, flavor, size, expirationdate):
        cursor = self.conn.cursor()
        query = "insert into baby_food(resourceid, name,ammount,cost,flavor,expirationdate) values(%i,%i,%f));"
        cursor.execute(query, ([resourceid], name, [ammount], [cost], flavor, expirationdate))
        babyfoodid = cursor.fetchone()[0]
        self.conn.commit()
        return babyfoodid