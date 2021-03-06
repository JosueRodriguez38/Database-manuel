from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Fuel Attributes: FuelID, ResourceID, fuelTypeNumber, litro)

# getAllFuel: extracts the Fuel attributes plus
# the resource id and typename of every tuple in the fuel table

# getFuelByResourceId: obtains the attributes of a specific tuple as specified by a resource id

# getAllFuelByFuelTypeName/UserID: These methods obtain the canned Food tuples
# that have the specified attribute

# insert: inserts a new fuel tuple with the information specified
class FuelDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, fueltypename,litro from fuel natural inner join fuel_type natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by fueltypename;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getFuelByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, fueltypename,litro,googlemapurl  from fuel natural inner join fuel_type natural inner join resources  natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllFuelByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, fueltypename,litro from fuel natural inner join fuel_type natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by fueltypename;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllFuelByFuelTypeName(self, name):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename, fueltypename,litro from fuel natural inner join fuel_type natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and fueltypename = %s ;"
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

