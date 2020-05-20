from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# The purpose of the consumer DAO is to extract the information regarding a consumer that has been requested

class FuelDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, fueltypename, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join fuel natural inner join fuel_type where aviable = true order by fueltypename;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getFuelByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, fueltypename, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join fuel natural inner join fuel_type where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllFuelByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid, userid, firstname, lastname, resourceTypeName, fueltypename, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join fuel natural inner join fuel_type natural inner join supplies where aviable = true order by fueltypename;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllFuelByFuelTypeName(self, name):
        cursor = self.conn.cursor()
        query = "select resourceid, resourceTypeName, fueltypename, purchaseTypeName, ammount, cost from Resources natural inner join resource_type natural inner join purchase_type natural inner join fuel natural inner join fuel_type where aviable = true and fueltypename = %s ;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insert(self, resourceid, fueltypenumber, litro):
        cursor = self.conn.cursor()
        query = "insert into fuel(resourceid, fueltypenumber, litro) values(%s,%s,%s) returning fuelid"
        cursor.execute(query, (resourceid, fueltypenumber, litro))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

