from config.dbconfig import pg_config
from config.tuple_config import user_cons
import psycopg2

# Heavy Equipment Attributes: name, fuelType

# getAllHeavyEquipment: extracts the Heavy Equipment attributes plus
# the resource id and typename of every tuple in the baby food table

# getHeavyEquipmentById: obtains the attributes of a specific tuple as specified by a resource id

# getAllHeavyEquipmentByName/UserID/FuelType: These methods obtain the heavy equipment tuples
# that have the specified the specified attribute

# insert: inserts a heavy equipment tuple with the information specified

class HeavyEquipmentDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s host=24.54.205.36" % (pg_config['dbname'],
                                                                           pg_config['user'],
                                                                           pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllHeavyEquipment(self):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,fueltype from  heavy_equipment natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true order by name;"
        cursor.execute(query)
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getHeavyEquipmentById(self, rid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,fueltype,googlemapurl  from  heavy_equipment natural inner join resources  natural inner join supplies natural inner join location natural inner join purchase_type natural inner join resource_type  where aviable = true and resourceid = %s;"
        cursor.execute(query, [rid])
        result = cursor.fetchone()
        self.conn.commit()
        return result

    def getAllHeavyEquipmentByUserID(self, uid):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,fueltype from  heavy_equipment natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and userid = %s order by name;"
        cursor.execute(query, [uid])
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllHeavyEquipmentByName(self, name):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,fueltype from  heavy_equipment natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and name like %s;"
        cursor.execute(query, (name,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def getAllHeavyEquipmentByFuelType(self, fuelType):
        cursor = self.conn.cursor()
        query = "select resourceid,name , resourcetypename ,ammount,cost,purchasetypename,fueltype from  heavy_equipment natural inner join resources natural inner join purchase_type natural inner join resource_type  where aviable = true and fueltype like %s;"
        cursor.execute(query, (fuelType,))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result

    def insert(self, resourceid, fueltype):
        cursor = self.conn.cursor()
        query = "insert into heavy_equipment(resourceid,fueltype) values(%s,%s) returning heavyequipmentid"
        cursor.execute(query, (resourceid, fueltype))
        result = cursor.fetchall()
        for row in cursor:
            result.append(row)
        self.conn.commit()
        return result