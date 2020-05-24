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
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, flavor,expirationdate from baby_food natural inner join resources natural inner join purchase_type natural inner join resource_type  ;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodByResourceID(self,resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, flavor,expirationdate,googlemapurl  from baby_food natural inner join resources  natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where resourceid=%s;"
        cursor.execute(query, [resourceid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getBabyFoodByFlavor(self,flavor):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, flavor,expirationdate from baby_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where flavor = %s;"
        cursor.execute(query, (flavor))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodBySize(self,size):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, flavor,expirationdate from baby_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where size = %s;"
        cursor.execute(query, [size])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getBabyFoodByExpirationDate(self, expirationdate):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, flavor,expirationdate from baby_food natural inner join resources natural inner join purchase_type natural inner join resource_type  where expirationdate = %s;"
        cursor.execute(query,(expirationdate))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertBabyFood(self,resourceid, flavor, expirationdate):
        cursor = self.conn.cursor()
        query = "insert into baby_food(resourceid,flavor,expirationdate) values(%s,%s,%s) returning babyfoodid;"
        cursor.execute(query, (resourceid,  flavor, expirationdate))
        babyfoodid = cursor.fetchone()[0]
        self.conn.commit()
        return babyfoodid