from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class WaterDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select name, ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getWaterbyResourceId(self,resourceid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,watertypename, ounces from (water natural inner join water_type)natural inner join resources natural inner join purchase_type natural inner join resource_type where resourceid=%s;"
        cursor.execute(query,[resourceid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllWaterbyType(self,watertypenumber):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources where watertypenumber=%s;"
        cursor.execute(query,[watertypenumber])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result


    def getWaterByOunces(self,ounces):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources where onces=%f;"
        cursor.execute(query,[ounces])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getWaterOrderedByOunceDes(self):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources order by ounces desc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result


    def getWaterOrderedByOunceAsc(self):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources order by ounces Asc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getWaterOrderedByTypeAsc(self):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources order by watertypenumber Asc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getWaterOrderedByTypeDesc(self):
        cursor = self.conn.cursor()
        query = "select ammount,cost,watertypename, ounces from (water natural inner join water_type)natural inner join resources order by watertypenumber desc;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insertWater(self, resourceid, watertypenumber,ounces):
        wcursor = self.conn.cursor()
        query = "insert into water(resourceid, watertypenumber,ounces) values(%s,%s,%s) returning waterid;"
        wcursor.execute(query, (resourceid, watertypenumber,ounces))
        result = wcursor.fetchall()
        for row in wcursor:
            result.append(row)
        self.conn.commit()
        return result
